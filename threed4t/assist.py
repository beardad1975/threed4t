from panda3d.core import PerspectiveLens, OrthographicLens, LensNode, NodePath

from ursina import *


# class CompassCube(Entity):
#     def __init__(self):
#         Entity.__init__(self, parent=camera.ui, model='cube', texture='white_cube',scale=0.1)
#         self.x = .4 * window.aspect_ratio
#         self.y = -.4

#     def update(self):
#         print('camara world position', camera.world_rotation)
#         self.rotation = camera.world_rotation * Vec3(-1,-1,-1)


class CorAssist:
    def __init__(self):

        self._enabled = False
        self.grid = Entity(model=Grid(10, 10), scale=10, color=color.rgb(180,180,180))

        # line mesh 
        verts = (Vec3(5,0,0), Vec3(-5,0,0))
        tris = ((0,1), )
        self.line_x = Entity(model=Mesh(vertices=verts, triangles=tris, mode='line', thickness=2),
                             color=color.orange)

        verts = (Vec3(0,5,0), Vec3(0,-5,0))
        tris = ((0,1), )
        self.line_y = Entity(model=Mesh(vertices=verts, triangles=tris, mode='line', thickness=2),
                             color=color.green)

        verts = (Vec3(0,0,5), Vec3(0,0,-5))
        tris = ((0,1), )
        self.line_z = Entity(model=Mesh(vertices=verts, triangles=tris, mode='line', thickness=2),
                             color=color.rgb(180,0,0))



        self.dots = []
        for i in range(-5, 6):
            e = Entity(model='cube', scale=0.1, color=color.rgb(180,0,0),position=(0,0,i))
            self.dots.append(e)

        # self.compass_cube = CompassCube()

        #cone
        self.cone_x = Entity(model=Cone(4, direction=(1,0,0)), color=color.orange,position=(5,0,0),scale=0.5)
        self.cone_y = Entity(model=Cone(4, direction=(0,1,0)), color=color.green,position=(0,5,0),scale=0.5)
        self.cone_z = Entity(model=Cone(4, direction=(0,0,1)), color=color.rgb(180,0,0),position=(0,0,5),scale=0.5)


        self.disable_gizmo()

    def enable_gizmo(self):
        self.grid.enabled = True
        self.line_x.enabled = True
        self.line_y.enabled = True
        self.line_z.enabled = True
        for d in self.dots:
            d.enabled = True
        # self.compass_cube.enabled = True
        self.cone_x.enabled = True
        self.cone_y.enabled = True
        self.cone_z.enabled = True


    def disable_gizmo(self):
        self.grid.enabled = False
        self.line_x.enabled = False
        self.line_y.enabled = False
        self.line_z.enabled = False
        for d in self.dots:
            d.enabled = False
        # self.compass_cube.enabled = False
        self.cone_x.enabled = False
        self.cone_y.enabled = False
        self.cone_z.enabled = False



    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value :
            self._enabled = True
            self.enable_gizmo()
        else:
            self._enabled = False
            self.disable_gizmo()

            
               