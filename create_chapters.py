import os

chapter_dirs = [
    "Chapter-01-Procedural-Python-Examples",
    "Chapter-02-Modeling-Physical-Objects-With-Object-Oriented-Programming",
    "Chapter-03-Mental-Models-Of-Objects-And-The-Meaning-Of-Self",
    "Chapter-04-Managing-Multiple-Objects",
    "Chapter-05-Introduction-To-Pygame",
    "Chapter-06-Object-Oriented-Pygame",
    "Chapter-07-Pygame-GUI-Widgets",
    "Chapter-08-Encapsulation",
    "Chapter-09-Polymorphism",
    "Chapter-10-Inheritance",
    "Chapter-11-Managing-Memory-Used-By-Objects",
    "Chapter-12-Card-Games",
    "Chapter-13-Timers",
    "Chapter-14-Animation",
    "Chapter-15-Scenes",
    "Chapter-16-Full-Game-Dodger",
    "Chapter-17-Design-Patterns-And-Wrap-Up",
]

print("Creating chapter directories...")

for dir_name in chapter_dirs:
    try:
        os.makedirs(dir_name, exist_ok=True)
        print(f"Created: {dir_name}")
    except Exception as e:
        print(f"Error creating {dir_name}: {e}")

print("")
print("Chapter directory creation complete!")
