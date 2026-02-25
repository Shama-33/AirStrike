# AirStrike Game

A Battleship-style combat game built with Python and Pygame.

## 📋 Description

AirStrike is a turn-based strategy game where players place ships on a grid and attempt to sink their opponent's fleet. The game features a graphical interface built with Pygame and includes ship placement, collision detection, and visual feedback. This includes Game Theory concepts such as Min-Max Algorithm, Alpha-Beta Pruning, Fuzzy Logic, and other search techniques - each corresponds to different modes of the game.

## 🎮 Features

- **Automatic Ship Placement**: Ships are randomly placed on a 10x10 grid with collision detection
- **Multiple Ship Types**: Fleet includes ships of varying sizes (5, 4, 3, 3, 2 units)
- **Dual Grid Display**: Each player has two grids:
  - Position grid (shows your ships)
  - Search grid (tracks attacks and results)
- **Visual Feedback**: Color-coded display with rounded ship graphics
- **Smart Placement Algorithm**: Prevents ships from overlapping or going out of bounds

## 🚀 Installation

### Prerequisites

- Python 3.x
- Pygame library

### Setup

1. Clone or download the project files
2. Install Pygame:
```bash
pip install pygame
```

3. Ensure you have both files in the same directory:
   - `AirStrike_Engine.py`
   - `AirStrike_GUI.py`

## 🎯 How to Run

Run the GUI file to start the game:

```bash
python AirStrike_GUI.py
```

## 🕹️ Controls

- **ESC**: Close the game
- **SPACEBAR**: Pause/Unpause animation
- **Close Window**: Click the X button to quit

## 📁 Project Structure

```
AirStrike/
├── main/
│   ├── AirStrike_Engine.py    # Game logic and ship placement
│   └── AirStrike_GUI.py        # Pygame graphical interface
├── Report.pdf                  # Detailed Report
└── README.md                   # This file
```

## 🏗️ Architecture

### AirStrike_Engine.py

**Classes:**

1. **Ship Class**
   - Attributes:
     - `row`: Starting row position (0-9)
     - `col`: Starting column position (0-9)
     - `size`: Length of the ship
     - `orientation`: Horizontal ('h') or Vertical ('v')
     - `indexes`: List of grid positions occupied by the ship
   
   - Methods:
     - `compute_indexes()`: Calculates all grid positions the ship occupies

2. **Player Class**
   - Attributes:
     - `ships`: List of Ship objects
     - `search`: 100-element list tracking search/attack results
     - `indexes`: Flattened list of all positions occupied by ships
   
   - Methods:
     - `place_ships(sizes)`: Automatically places ships with collision detection
     - `show_ships()`: Console display of ship positions (for debugging)

### AirStrike_GUI.py

**Key Components:**

- **Display Settings:**
  - Grid size: 10x10 cells
  - Cell size: 30x30 pixels
  - Four grids total (2 per player)
  - Color scheme: Grey background, white grid lines, green ships

- **Functions:**
  - `draw_grid(left, top)`: Renders a 10x10 grid at specified position
  - `draw_ships(player, left, top)`: Draws ships on the position grid

- **Grid Layout:**
  ```
  [Player 1 Search]    [Player 1 Position]
  [Player 2 Position]  [Player 2 Search]
  ```

## 🎨 Game Constants

| Constant | Value | Description |
|----------|-------|-------------|
| SQ_SIZE | 30 | Size of each grid cell in pixels |
| H_MARGIN | 120 | Horizontal margin between grids |
| V_MARGIN | 30 | Vertical margin between grids |
| WIDTH | 720 | Total window width |
| HEIGHT | 660 | Total window height |
| INDENT | 10 | Ship padding within cells |

## 🎯 Ship Placement Algorithm

The game ensures valid ship placement through:

1. **Boundary Check**: Ships cannot extend beyond the 100-cell grid
2. **Orientation Validation**: Horizontal ships stay in their row; vertical ships stay in their column
3. **Collision Detection**: Ships cannot overlap with existing ships
4. **Retry Mechanism**: Invalid placements trigger automatic repositioning


Current code provides the foundation for:
- Attack functionality
- Hit/miss tracking on search grids
- Turn-based gameplay
- AI opponent
- Score tracking
- Game over detection

