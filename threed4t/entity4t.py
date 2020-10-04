from ursina import *

class Entity4t(Entity):
    def __init__(self, *args, **kwargs):
        # handle default model and texture
        if not 'model' in kwargs:
            kwargs['model'] = 'cube'
            kwargs['texture'] = 'white_cube.png'
        super().__init__(*args, **kwargs)

    @property
    def 模型(self):
        return self.model 

    @模型.setter
    def 模型(self, value):
        self.model = value 
        # remove previous texture
        self._texture = None
        self.setTextureOff(True)

    @property
    def 紋理(self):
        return self.texture 

    @模型.setter
    def 紋理(self, value):
        self.texture = value

    @property
    def 上層物件(self):
        return self.parent

    @模型.setter
    def 上層物件(self, value):
        self.parent = value

    @property
    def 位置(self):
        return self.position 

    @位置.setter
    def 位置(self, value):
        self.position = value  

    @property
    def 全域位置(self):
        return self.world_position 

    @全域位置.setter
    def 全域位置(self, value):
        self.world_position = value 

    @property
    def 全域位置x(self):
        return self.wrold_position_x 

    @全域位置x.setter
    def 全域位置x(self, value):
        self.wrold_position_x = value 

    @property
    def 全域位置y(self):
        return self.wrold_position_y 

    @全域位置y.setter
    def 全域位置y(self, value):
        self.wrold_position_y = value 

    @property
    def 全域位置z(self):
        return self.wrold_position_z 

    @全域位置z.setter
    def 全域位置z(self, value):
        self.wrold_position_z = value 