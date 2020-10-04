
from ursina import *


from . import common
from .engine import Engine3D
模擬3D引擎 = Engine3D
__all__ = [ 
            '模擬3D引擎', 'Entity', 'EditorCamera',
            '模擬進行中', '新增3D物件', 'color',
            ]

######## top level function


def simulate():
    if not common.is_engine_created:
        Engine3D()

    common.stage.simulate()


模擬主迴圈 = simulate
模擬進行中 = simulate

######## top level function

def add_entity(*args, **kwargs):
    if not common.is_engine_created:
        Engine3D()
    return common.stage.add_entity(*args, **kwargs)

新增3D物件 = add_entity





if __name__ == '__main__' :
    pass
    
