
from . import common

from .repl_panda import Repl

from ursina import *

import __main__

class Engine3D(Ursina, Repl):
    def __init__(self):
        
        Ursina.__init__(self)

        window.windowed_size = Vec2(500,500)
        window.title = '模擬3D'
        window.borderless = False
        window.fullscreen = False
        window.fps_counter.enabled = False
        window.exit_button.visible = False
        window.cog_button.enabled = False
        
        self.start_repl()