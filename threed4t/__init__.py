
from ursina import *


from . import common
from .engine import Engine3D
from .mouse4t import Mouse4T
模擬3D引擎 = Engine3D
__all__ = [ 
            '模擬3D引擎', 'Entity', 'EditorCamera',
            '模擬進行中','模擬主迴圈', 'color','Vec3','Vec4','Vec2',
            '按住的鍵', '滑鼠','天空', '新增立方體', '新增6面貼圖方塊',
            '新增內面貼圖球體','新增球體', '新增物體', '新增平面',
            '預約執行',
            ]

按住的鍵 = held_keys
滑鼠 = Mouse4T()
天空 = Sky
######## top level function
# import __main__
# __main__.按住的鍵 = held_keys


def simulate():
    if not common.is_engine_created:
        Engine3D()

    common.stage.simulate()


模擬主迴圈 = simulate
模擬進行中 = simulate

######## top level function

def add_cube(*args, **kwargs):
    if not common.is_engine_created:
        Engine3D()
    return common.stage.add_cube(*args, **kwargs)
新增立方體 = add_cube
新增物體 = add_cube

def add_sphere(*args, **kwargs):
    if not common.is_engine_created:
        Engine3D()
    return common.stage.add_sphere(*args, **kwargs)
新增球體 = add_sphere

def add_quad(*args, **kwargs):
    if not common.is_engine_created:
        Engine3D()
    return common.stage.add_quad(*args, **kwargs)
新增平面 = add_quad


def add_cubic6(*args, **kwargs):
    if not common.is_engine_created:
        Engine3D()
    return common.stage.add_cubic6(*args, **kwargs)
新增6面貼圖方塊 = add_cubic6

def add_sphere_inward(*args, **kwargs):
    if not common.is_engine_created:
        Engine3D()
    return common.stage.add_sphere_inward(*args, **kwargs)
新增內面貼圖球體 = add_sphere_inward


def 預約執行(函式, *args, 時間=1, **kwargs):
    kwargs['delay'] = 時間
    invoke(函式, *args, **kwargs)



if __name__ == '__main__' :
    pass
    
