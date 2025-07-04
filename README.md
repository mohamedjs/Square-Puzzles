# Square Puzzles – 15 Puzzle Game (Pygame)

A classic sliding puzzle game (15-puzzle) implemented in Python using Pygame. The game features a 4x4 grid of numbered tiles, where the goal is to arrange the tiles in order by sliding them into the empty space. The project includes an A* solver and a graphical interface.

---

## 🧩 Features

- **Classic 15-Puzzle Gameplay:** 4x4 grid with one empty space, slide tiles to solve.
- **A* Solver:** Automatically finds and animates the solution to the puzzle.
- **Pygame GUI:** Visualizes the puzzle, tiles, and solution steps.
- **Customizable Colors:** All colors are defined in `colors.py` for easy theming.
- **Random Shuffle:** Puzzle is shuffled at the start for a new challenge each time.

---

## 📁 Files

- `squarepuzzles (2).py` – Main game logic, GUI, puzzle shuffling, and A* solver.
- `colors.py` – Color definitions for the game (background, tiles, text, etc).

---

## 🚀 How to Run

1. **Install dependencies:**
   - Python 3.x
   - Pygame (`pip install pygame`)
2. **Run the game:**
   ```bash
   python "squarepuzzles (2).py"
   ```
3. **Gameplay:**
   - The puzzle will shuffle and then automatically solve itself, animating each step.
   - The GUI window displays the puzzle and a "solve" button (not interactive in this version).

---

## 🛠️ Code Overview

### Main Components
- **Desk class:** Represents the puzzle grid, supports shuffling, copying, and neighbor generation.
- **Puzzle15 class:** Encapsulates the puzzle logic and A* search for solving.
- **puzzle_GUI class:** Handles Pygame window, drawing tiles, and animating the solution.
- **colors.py:** Contains named RGB color tuples for easy color management.

### How the Solver Works
- Uses A* search with a Manhattan distance heuristic to find the shortest solution path.
- Animates each step of the solution in the GUI.

---

## 🎨 Customization
- Change colors in `colors.py` to update the look and feel of the game.
- Adjust `SHUFFLE_NUMBER` in `Desk` for more/less shuffling.

---

## 👤 Author
- Original code adapted for educational/demo purposes.

---

Enjoy solving the classic 15-puzzle! 