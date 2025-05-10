# Flappy Bird Comes to UJ!

Welcome to **Flappy Bird Comes to UJ!** – a fun, university-themed twist on the classic Flappy Bird game. In this game, Flappy is trying to get to class at the University of Jos. Help him navigate pipes, travel the distance, and avoid carryovers!

## Features

* Classic flappy bird gameplay with a University of Jos twist
* Score meter that tracks how far Flappy travels
* Restart button unfortunately themed as a "Carry Over"
* Animated welcome screen and themed background
* Two versions available: the improved UJ-themed game and the original base version

---

## Getting Started

### 1. Install Python

First, ensure Python is installed on your system:

* Download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
* Run the installer and make sure to check **"Add Python to PATH"**

To confirm installation, open a terminal or command prompt and run:

```bash
python --version
```

### 2. (Optional) Set Up a Virtual Environment

To isolate dependencies, you can create a virtual environment:

```bash
python -m venv venv
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate
```

### 3. Install Required Library

Install Pygame using pip:

```bash
pip install pygame
```

---

## How to Run the Game

### To Play the UJ Version:

```bash
python final.py
```

This runs the full version of **Flappy Bird Comes to UJ!**, including scoring, animations, and the University of Jos theme.

### To Play the Original Base Version:

```bash
python old.py
```

This runs the simple, base version of Flappy Bird — great for learning the basics.

---

## Project Structure

```
Flappy-Bird-in-UJ/
├── final.py         # Main UJ-themed game
├── old.py           # Basic original version
├── assets/          # Game assets for UJ-themed game (images, font)
│   ├── bg.png
│   ├── bird1.png
│   ├── bird2.png
│   ├── bird3.png
│   ├── bubble.png
│   ├── ground.png
│   ├── logo.png
│   ├── pipe.png
│   ├── restart.png
│   ├── welcome.png
│   └── PressStart2P.ttf
├── assets/old/       # Game assets for original version (images, font)
│   ├── bg.png
│   ├── bird1.png
│   ├── bird2.png
│   ├── bird3.png
│   ├── ground.png
│   ├── pipe.png
│   ├── restart.png
│   └── PressStart2P.ttf
```

Make sure all asset files inside the `public` folder are in place before running the game.

---

## Credits

* **Developed by**: Student team from the University of Jos
* **Inspired by**: Flappy Bird (original game)
* **Built with**: [Pygame](https://www.pygame.org/)
* **Assets**: Custom and open-source graphics and fonts

---

Enjoy the game — and don’t let Flappy miss his class!
