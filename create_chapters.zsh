#!/bin/zsh

chapter_dirs=(
"Chapter-1 Procedural Python Examples"
"Chapter-2 Modeling Physical Objects With Object-Oriented Programming"
"Chapter-3 Mental Models Of Objects And The Meaning Of Self"
"Chapter-4 Managing Multiple Objects"
"Chapter-5 Introduction To Pygame"
"Chapter-6 Object-Oriented Pygame"
"Chapter-7 Pygame GUI Widgets"
"Chapter-8 Encapsulation"
"Chapter-9 Polymorphism"
"Chapter-10 Inheritance"
"Chapter-11 Managing Memory Used By Objects"
"Chapter-12 Card Games"
"Chapter-13 Timers"
"Chapter-14 Animation"
"Chapter-15 Scenes"
"Chapter-16 Full Game Dodger"
"Chapter-17 Design Patterns And Wrap-Up"
)

echo "Creating chapter directories..."

for dir_name in "${chapter_dirs[@]}"; do
  mkdir -p "$dir_name"
  echo "Created: $dir_name"
done

echo ""
echo "Chapter directory creation complete!"
