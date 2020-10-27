import raylibpy
import os
os.environ["RAYLIB_BIN_PATH"] = "raylib-2.0.0-Win64-mingw/lib/"

raylibpy.init_window(900, 500, "Hello")
ball = raylibpy.Vector2(100, 100)

raylibpy.set_target_fps(60)

while not raylibpy.window_should_close():
    if raylibpy.is_key_down(raylibpy.KEY_RIGHT):
        ball.x += 5
    if raylibpy.is_key_down(raylibpy.KEY_DOWN):
        ball.y += 5

    raylibpy.begin_drawing()
    raylibpy.clear_background(raylibpy.Color(0, 0, 255, 255))
    raylibpy.draw_circle(ball.x, ball.y, 10.0, raylibpy.BLACK)
    raylibpy.end_drawing()

raylibpy.close_window()
