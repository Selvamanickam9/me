import os
os.environ["RAYLIB_BIN_PATH"] = "raylib-2.0.0-Win64-mingw/lib/"
import raylibpy

raylibpy.init_window(900, 500, "Hello")
ballpos = (raylibpy.get_screen_width, raylibpy.get_screen_height)

raylibpy.set_target_fps(60)