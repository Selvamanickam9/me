
import os
os.environ["RAYLIB_BIN_PATH"] = "raylib-2.0.0-Win64-mingw/lib/"
import raylibpy

class Ball:
    def __init__(self, x, y, Color):
        self.pos = raylibpy.Vector2(x, y)
        self.Color = Color

balls = []
balls.append(Ball(20, 20, raylibpy.BLACK))
balls.append(Ball(30, 30, raylibpy.RED))
balls.append(Ball(40, 40, raylibpy.WHITE))

raylibpy.init_window(900, 500, "Hello")
raylibpy.set_target_fps(60)

while not raylibpy.window_should_close():
    for b in balls:
        if raylibpy.is_mouse_button_pressed(raylibpy.MOUSE_LEFT_BUTTON):
            b.pos =  raylibpy.get_mouse_position()

    raylibpy.begin_drawing()
    raylibpy.clear_background(raylibpy.Color(0, 0, 255, 255))
    for b in balls:
        raylibpy.draw_circle(b.pos.x, b.pos.y, 6.0, b.Color)
    raylibpy.end_drawing()

raylibpy.close_window()
