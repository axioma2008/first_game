import cx_Freeze

executables = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
    name="cool_game",
    options={"build.exe": {"packages": ["pygame"],
                           "include_files": ["settings.py", "sprites.py", "images/2627196.png",
                                             "images/sky.png", "images/bird.png", "images/first_screen.png",
                                             "images/plane.png", ]}},
    executables=executables
)
