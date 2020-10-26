# Simple Ball

Scouting how easy (or hard) it's to game program in Python using [Raylib examples][raylib-eg].

Before proceeding make sure Python 3.8+ is installed.  Check with `where python` or `which python3` on Windows or Linux respectively.

[raylib-eg]: https://www.raylib.com/examples.html

## Raylibpy Initialzie

1. `pip install raylib-py`; [refer][raylibpy]
2. Download [raylib 2.0][] (other versions don't seem to work)
3. Extract downloaded archive here

Once done, verify with a simple snippet

``` python
import os

# set the path before raylib is imported.
os.environ["RAYLIB_BIN_PATH"] = "path/to/the/binary"

import raylibpy
```

## VS Code Setup

Install these extensions:

* _Python_
* _Git History_

# References

* [Learn X in Y minutes: Python](https://learnxinyminutes.com/docs/python/)
* [Markdown Cheatsheet](https://commonmark.org/help/)
* [Git Cheatsheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)
* [Raylib Cheatsheet](https://www.raylib.com/cheatsheet/cheatsheet.html)


[raylibpy]: https://github.com/overdev/raylib-py
[raylib 2.0]: https://github.com/raysan5/raylib/releases/download/2.0.0/raylib-2.0.0-Win64-mingw.zip
