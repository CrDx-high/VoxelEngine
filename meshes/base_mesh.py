import numpy as np 

class Basemesh:
    def __init__(self):
        #OpenGL context 
        self.ctx = None
        # shader program 
        self.program = None
        # Here we will define the vertex array for object formation 
        # Vertex buffer data type : '3f 3f'
        self.vbo_format = None
        # attribute names according to the format 
        self.attrs: tuple[str,...] = None
        # vertex array object
        self.vao = None 
        # we are using a vertex array object as they store the state required to read and feed it to the graphics pipeline, it eliminates the need to repeateadly rebind buffers and configure vertex attributes, they are used becase they help in optimizing performance and keep the code clean, it is a standard procedure to them 

    def get_vertex_data(self) -> np.array:...

    def get_vao(self):
        vertex_data = self.get_vertex_data()
        if vertex_data.size == 0:
            return None
        vbo = self.ctx.buffer(vertex_data)
        vao = self.ctx.vertex_array(
            self.program,[(vbo,self.vbo_format, *self.attrs)], skip_errors = True
        )
        return vao
    def render(self):
        if self.vao is not None:
            self.vao.render()
