# Spaceship

## Overview
A 2D space-themed arcade game where players control a spaceship to destroy incoming meteors. Survive as long as possible while earning points and progressing through increasingly difficult levels.

## Purpose
To create a space shooter game using Python and Pygame, demonstrating classic arcade game mechanics with modern object-oriented programming. The game showcases player movement, collision detection, scoring system, and level progression.

## Scope

### Technology Stack:
- **Python**: 3.x
- **Pygame**: Game development framework
- **CSV**: Score data storage

### Game Features:
- 8-directional spaceship movement with rotation sprites
- Dual-shot projectile system based on ship direction
- Two types of meteors with different speeds and point values
- Health system with power-ups
- Progressive level difficulty
- CSV-based high score tracking
- Sound effects and background music

## Implementation

### Installation:
```bash
# Clone the repository
git clone https://github.com/mulosbron/Spaceship.git

# Navigate to project directory
cd Spaceship

# Install dependencies
pip install pygame

# Run the game
python py/main.py
```

### Project Structure:
```
Spaceship/
├── py/
│   ├── main.py              # Game entry point
│   ├── game_settings.py     # Main game loop and initialization
│   ├── player.py            # Player spaceship class
│   ├── meteor.py            # Meteor classes (Meteor, Meteor2)
│   ├── player_bullet.py     # Player projectile class
│   ├── health.py            # Health power-up class
│   ├── collision.py         # Explosion effects class
│   ├── scenes.py            # Game scenes (Menu, Game, Scores)
│   └── scene_control.py     # Scene management
├── img/                     # Game sprites and backgrounds
├── audio/                   # Sound effects and music
├── font/                    # Game font
├── score/                   # Score data storage
└── README.md
```

### Controls:
- **Arrow Keys**: Move spaceship in 8 directions
- **SPACE**: Shoot (fires from both sides)
- **ENTER**: Restart game after collision
- **Mouse**: Menu interaction

## Screenshots

![Main Menu](https://zym3lg5yyjfv6n5abuoqznp2kptw4hfvscw5qxq2n65xqtevrenq.arweave.net/zhm1m7jCS183oA0dDLX6U-duHLWQrdheGm-7eEyViRs)
![In-Game](https://cxwdum4j57oratztmm6cdmpwnk4ujrvuyoirar7v35xaaw3justq.arweave.net/Few6M4nv3RBPM2M8IbH2arlExrTDkRBH9d9uAFtppKc)
![Scores](https://zqld65g4b75pqi2h73pdgiryvjpwhzdoqyeubery3e56woyso2aa.arweave.net/zBY_dNwP-vgjR_7eMyI4ql9j5G6GCUCSONk76zsSdoA)
