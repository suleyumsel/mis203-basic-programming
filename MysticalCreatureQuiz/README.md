# 🔮 Mystical World – Which Mystical Creature Are You?

## Project Description
Mystical World is an interactive personality quiz developed using Python. The player answers 9 questions to discover which mystical creature matches their personality.

## Mystical Creatures
- 🧛 Vampire
- 🐺 Werewolf
- 🧝 Elf
- 👻 Ghost
- 🐉 Dragon
- 🧙 Witch

## Features
- 9 multiple-choice personality questions
- Input validation for answers
- Score-based personality matching
- Random selection when characters have equal highest scores
- Compatibility percentage calculation
- Colorful terminal interface
- Progress bars and loading animations
- Play Again option

## Libraries Used
- **math:** Calculates and rounds up the compatibility percentage.
- **random:** Selects a random character when scores are tied.
- **time:** Adds delays between questions and animations.
- **rich:** Creates colorful text, panels, progress bars, and loading animations.

## How to Run
1. Install Python.
2. Install the Rich library:

   `pip install rich`

3. Run the game:

   `python mystical_quiz.py`

4. Answer the 9 questions and discover your mystical identity.

## How It Works
Each answer adds points to specific mystical creatures. After all 9 questions, the program finds the highest score and selects the matching creature. If multiple creatures have the same highest score, one is selected randomly.

The game then displays the creature's special power, personality, mystical home, and compatibility percentage.

## Programming Concepts
- Variables
- Conditional statements (`if`, `elif`, `else`)
- Loops (`while`, `for`)
- Functions (`def`)
- Lists and dictionaries
- User input validation
- Imported modules and libraries

## Developer
Şule Yümsel
Developed as a Python programming project.