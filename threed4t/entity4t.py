from ursina import *

class Entity4t(Entity):
    def __init__(self, *args, **kwargs):
        # if not 'model' in kwargs:
        #     kwargs['model'] = 'cube'
        #     kwargs['texture'] = 'white_cube.png' 
        super().__init__(*args, **kwargs)

    @property
    def 模型(self):
        return self.model 

    @模型.setter
    def 模型(self, value):
        self.model = value 

    @property
    def 紋理(self):
        return self.texture 

    @模型.setter
    def 紋理(self, value):
        self.texture = value

    @property
    def 位置(self):
        return self.position 

    @位置.setter
    def 位置(self, value):
        self.position = value  

