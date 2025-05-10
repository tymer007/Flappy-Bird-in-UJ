# Flappy Bird Comes to UJ!

Welcome to **Flappy Bird Comes to UJ!** – a fun, university of jos themed twist on the classic Flappy Bird game. In this game, Flappy is trying to get to class at the University of Jos. Help navigate pipes and get to his 8am class, travel the campus, and avoid carryovers!

---

## 🎮 For Non-Developers

If you're not a developer and just want to play the game, simply **open `flappybird-in-uj.exe`** — no setup needed!

---

## Features

* Classic Flappy Bird gameplay with a University of Jos twist
* Score meter that tracks how far Flappy travels
* Restart button humorously themed as a "Carry Over"
* Animated welcome screen and UJ-themed background
* Two playable versions: the improved UJ version and the original base version

---

## 🛠 Getting Started (For Developers)

### 1. Install Python

Ensure Python is installed on your machine:

* Download it from [python.org](https://www.python.org/downloads/)
* During installation, check **"Add Python to PATH"**

Check installation:

```bash
python --version
```

---

### 2. (Optional) Create a Virtual Environment

For isolating project dependencies:

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

---

### 3. Install Pygame

Install the required library:

```bash
pip install pygame
```

---

## ▶️ Running the Game

### UJ-Themed Version

```bash
python final.py
```

This runs the full **Flappy Bird Comes to UJ!** with themes, scoring, and animations.

---

### Original Base Version

```bash
python old.py
```

This runs a simple, original-style version great for beginners.

---

## 📁 Project Structure

```
Flappy-Bird-in-UJ/
├── .gitignore              # Click-and-play executable
├── final.ico               # Logo
├── final.py                # Main UJ-themed game
├── flappybird-in-uj.exe    # Click-and-play executable, run the game here
├── old.ico                 # Original Logo
├── old.py                  # Original version
├── assets/                 # UJ game assets
│   ├── bg.png
│   ├── bird1.png
│   ├── bird2.png
│   ├── bird3.png
│   ├── bubble.png
│   ├── ground.png
│   ├── nav_pole.png
│   ├── pipe.png
│   ├── restart.png
│   ├── welcome.png
│   └── PressStart2P.ttf    # Game font
├── assets/old/             # Assets for original version
│   ├── bg.png
│   ├── bird1.png
│   ├── bird2.png
│   ├── bird3.png
│   ├── ground.png
│   ├── pipe.png
│   └── restart.png
```

Make sure the `assets/` folder stays alongside your `.py` files or `.exe`.

---

## 🙌 Credits

* **Developed by**: Student group at the University of Jos
* **Inspired by**: The original Flappy Bird game
* **Built with**: [Pygame](https://www.pygame.org/)
* **Assets**: Custom designs and open-source visuals & fonts

---

Enjoy the game — and don’t let Flappy miss his class! 🐦🎓
