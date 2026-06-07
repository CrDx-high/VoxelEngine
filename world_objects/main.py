import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import moderngl as mgl
import pygame as pg

from world_objects.settings import *
from world_objects.shader_program import ShaderProgram
from world_objects.scene import Scene
from world_objects.player import Player
from world_objects.textures import Textures




class VoxelEngine:
    def __init__(self): # class constructor 
        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION,3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)

        pg.display.set_mode(WIN_RES, flags = pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()# Creating access to the pg display through mgl
        # Keep back faces visible so the chunk shell can be seen from inside.
        self.ctx.enable(flags = mgl.DEPTH_TEST | mgl.BLEND)
        self.ctx.gc_mode = 'auto' # setting the garbage collector to automatic, so that the unused openGL objects are not manually deleted 



        # setting up time and clock 
        self.clock = pg.time.Clock() 
        self.delta_time  = 0
        self.time = 0 

        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        
        self.is_running = True
        self.on_init()

    def on_init(self):
        self.textures = Textures(self)
        self.player = Player(self)
        self.shader_program = ShaderProgram(self)
        self.scene = Scene(self )






    def update(self): # for updating the state of objects 

        self.player.update()
        self.shader_program.update()
        self.scene.update()
        self.delta_time = self.clock.tick()
        self.time = pg.time.get_ticks()*0.001
        pg.display.set_caption(f'{self.clock.get_fps():.0f}')







    def render(self):


        self.ctx.clear(color=BG_COLOR)
        self.scene.render()
        pg.display.flip()






    def handle_events(self): # methods for handling events and calling the amin application loop 

        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False
            self.player.handle_event(event=event)



    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
        pg.quit()
        sys.exit()

if __name__ == '__main__':
    app = VoxelEngine()
    app.run() 
