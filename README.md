# 🐍 Classic Snake Game in Python

A lightweight, beginner-friendly Snake game built entirely with Python's built-in **`turtle`** graphics library.

**No third-party packages or `pip install` required!** It runs directly on standard Python.

---

## 🎮 Features

- **Zero Installations**: Runs instantly using Python's standard library.
- **Dual Controls**: Play using either the **Arrow keys** or **WASD**.
- **Pause & Resume**: Press `Spacebar` anytime to pause.
- **Score & High Score**: Displays current score and retains the session high score.
- **Smooth & Responsive**: Includes input buffering to prevent accidental 180° self-collisions.
- **Clear Boundaries**: Visible arena border with safe random food spawning.
- **Modern Dark Palette**: Easy on the eyes with vibrant neon accents.

---

## 🚀 How to Run

1. Open your terminal or Command Prompt in this folder:
   ```bash
   cd "C:\Users\angelo\Desktop\Anti-Gravity Course"
   ```

2. Run the game:
   ```bash
   python snake.py
   ```

3. Press any movement key (**Arrow Keys** or **WASD**) to start moving!

---

## 🕹️ Controls

| Action | Primary Key | Alternative Key |
|---|---|---|
| **Move Up** | `↑` (Up Arrow) | `W` |
| **Move Down** | `↓` (Down Arrow) | `S` |
| **Move Left** | `←` (Left Arrow) | `A` |
| **Move Right** | `→` (Right Arrow) | `D` |
| **Pause / Resume** | `Spacebar` | `Spacebar` |
| **Exit** | Close the window (`X`) | Close the window (`X`) |

---

## ⚙️ Easy Customization

All game settings are clearly defined at the top of [`snake.py`](file:///C:/Users/angelo/Desktop/Anti-Gravity%20Course/snake.py#L14-L40). You can tweak them directly:

### 1. Change Difficulty / Speed
```python
# Initial delay per frame in seconds (lower number = faster snake)
INITIAL_DELAY = 0.14   # 0.16 = Very Easy | 0.12 = Normal | 0.08 = Hard
MIN_DELAY = 0.06       # Maximum speed limit
SPEED_RAMP = 0.0015    # How much speed increases per apple eaten
```

### 2. Customize Colors
```python
COLOR_BG = "#1e1e2e"       # Dark background
COLOR_BORDER = "#475569"   # Arena border
COLOR_HEAD = "#4ade80"     # Snake head
COLOR_BODY = "#22c55e"     # Snake body segments
COLOR_FOOD = "#f87171"     # Food apple
```

### 3. Change Window Size
```python
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
```

---

## 📖 How It Works

- **Grid System**: The arena operates on a 20x20 pixel step grid.
- **Game Loop**: Every frame (`window.update()`), the snake advances 20 pixels in its current direction.
- **Body Tracking**: Each segment moves to the previous position of the segment in front of it.
- **Collision Detection**: 
  - Eating food: checks if the head is within 18 pixels of the food.
  - Hitting walls: checks if coordinates exceed the bounding border.
  - Self-collision: checks if the head coordinates overlap any body segment.

Enjoy playing!
