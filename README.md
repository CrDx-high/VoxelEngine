# VoxelEngine

A voxel engine built from scratch in Python using ModernGL, Pygame, PyGLM, and Numba.

The project explores modern voxel rendering techniques including chunk-based terrain generation, frustum culling, ambient occlusion, packed vertex formats, texture arrays, procedural cave systems, and real-time voxel interaction.


---

## Features

### Procedural Terrain Generation

The terrain is generated entirely at runtime using layered noise functions.

Current terrain generation includes:

* Multi-octave terrain noise
* Island-shaped world generation
* Height-based biome distribution
* Snow, stone, dirt, grass and sand layers
* Cave generation using 3D noise
* Procedural tree placement

### Chunk-Based World System

The world is divided into chunks for efficient storage and rendering.

Current world dimensions:

* Chunk Size: 48 × 48 × 48
* World Size: 20 × 2 × 20 chunks
* Total Voxels: Over 17 million voxels

Each chunk:

* Stores its own voxel data
* Generates terrain independently
* Builds optimized meshes
* Performs frustum visibility testing

---

## Rendering Pipeline

The renderer uses Modern OpenGL (Core Profile 3.3).

### Vertex Packing

Every rendered vertex is compressed into a single 32-bit integer.

Packed data contains:

| Field    | Bits |
| -------- | ---- |
| X        | 6    |
| Y        | 6    |
| Z        | 6    |
| Voxel ID | 8    |
| Face ID  | 3    |
| AO ID    | 2    |
| Flip ID  | 1    |

Benefits:

* Smaller vertex buffers
* Reduced memory bandwidth
* Faster mesh uploads
* Lower VRAM consumption

---

### Texture Arrays

The engine uses OpenGL texture arrays.

Advantages:

* Multiple block textures in a single texture object
* No texture switching during rendering
* Reduced draw-call overhead
* Better GPU utilization

---

### Ambient Occlusion

Ambient Occlusion is generated during mesh construction.

For every visible face:

1. Neighboring voxels are sampled.
2. AO values are calculated.
3. AO information is packed into vertex data.
4. Shaders apply smooth corner shading.

This creates depth and visual separation between blocks without expensive lighting calculations.

---

## Optimization Techniques

### Face Culling

Only visible voxel faces are generated.

Hidden faces between solid blocks are discarded before reaching the GPU.

### Frustum Culling

Chunks outside the player's field of view are skipped entirely.

The frustum system performs:

* Near plane checks
* Far plane checks
* Horizontal FOV tests
* Vertical FOV tests

This dramatically reduces rendering cost in large worlds.

### Numba JIT Compilation

Performance-critical systems are accelerated using Numba.

Compiled systems include:

* Terrain generation
* Cave generation
* Ambient Occlusion calculations
* Vertex packing
* Mesh construction
* Voxel lookup

This provides near-native execution speed while remaining entirely in Python.

---

## Voxel Interaction

The engine supports real-time voxel manipulation.

### Ray Casting

A voxel DDA traversal algorithm is used to determine which voxel the player is targeting.

Current functionality:

* Remove blocks
* Place blocks
* Face normal detection
* Adjacent chunk rebuilding

---

## Controls

| Key         | Action                |
| ----------- | --------------------- |
| W           | Move Forward          |
| S           | Move Backward         |
| A           | Move Left             |
| D           | Move Right            |
| Q           | Move Up               |
| E           | Move Down             |
| Mouse       | Look Around           |
| Left Click  | Remove Voxel          |
| Right Click | Toggle Placement Mode |
| ESC         | Exit                  |

---

## Project Structure

```text
VoxelEngine/
│
├── assets/
│   ├── textures
│   └── UI assets
│
├── meshes/
│   ├── base_mesh.py
│   ├── chunk_mesh.py
│   ├── chunk_mesh_builder.py
│   ├── cube_mesh.py
│   └── quad_mesh.py
│
├── shaders/
│   ├── chunk.vert
│   ├── chunk.frag
│   ├── voxel_marker.vert
│   ├── voxel_marker.frag
│   ├── quad.vert
│   └── quad.frag
│
└── world_objects/
    ├── camera.py
    ├── player.py
    ├── frustum.py
    ├── chunk.py
    ├── world.py
    ├── scene.py
    ├── voxel_handler.py
    ├── voxel_marker.py
    ├── terrain_gen.py
    ├── textures.py
    ├── shader_program.py
    ├── settings.py
    └── main.py
```

---

## Dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install pygame
pip install moderngl
pip install numpy
pip install numba
pip install PyGLM
```

---

## Running

```bash
python world_objects/main.py
```

---

## Current Roadmap

### World

* Infinite terrain generation
* Chunk streaming
* Biome system
* Rivers and lakes
* Better cave generation

### Rendering

* Dynamic lighting
* Shadow mapping
* Water shaders
* Volumetric clouds
* Post-processing pipeline
* PBR experimentation

### Gameplay

* Collision detection
* Inventory system
* Block selection
* Entity system
* Mob AI
* Survival mechanics

### Engine

* Save/load system
* Multi-threaded chunk generation
* LOD system
* GPU-driven meshing
* Networking experiments

---

## Why This Project Exists

VoxelEngine is a personal graphics programming project built to better understand:

* OpenGL
* GPU pipelines
* Real-time rendering
* Procedural generation
* Engine architecture
* Data-oriented design
* Performance optimization in Python

The long-term goal is to evolve the project into a fully featured sandbox voxel engine while exploring low-level graphics and engine development concepts.

---

## Author

**Prajanya Chauhan**

Built from scratch as a graphics programming and engine architecture learning project.
