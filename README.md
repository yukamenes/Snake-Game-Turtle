# 🐍 Snake Game (Python Turtle)

A classic **Snake Game** implemented in **Python** using the built-in `turtle` graphics module.

The player controls the snake, eats food, grows longer, and tries to avoid collisions with the walls or its own tail.

This version includes a **high score system with file saving**, so your best result is stored between game sessions.

---

## 🎓 About This Project

This project was created while completing the **"100 Days of Code: The Complete Python Pro Bootcamp"** course.

The goal of the project was to practice:

- object-oriented programming in Python  
- working with multiple modules  
- game logic and collision detection  
- keyboard event handling  
- file handling (reading/writing high score)  
- building a simple interactive game  

---

## 🎮 Gameplay

- Control the snake using the **arrow keys**  
- Eat randomly appearing food to **gain points**  
- Different **food colors give different points**  
- The snake **grows longer** after eating  
- The game automatically **resets** if the snake:
  - hits the **wall**
  - hits **its own tail**

---

## 🧩 Game Features

- ✨ Smooth snake movement  
- 🎨 Random food colors  
- 📈 Score tracking system  
- 💾 High score saving (stored in file)  
- 🐍 Snake grows after eating food  
- 💥 Collision detection (walls and tail)  
- 🔁 Automatic game reset instead of game over screen  
- 🧱 Object-oriented structure with multiple modules  

---

## 🍎 Food & Points

Different food colors give different amounts of points:

| Color     | Points |
|----------|--------|
| 🔴 Red    | 1      |
| 🟢 Green  | 2      |
| 🟡 Yellow | 3      |
| 🟠 Orange | 4      |

---

## 🕹 Controls

| Key           | Action     |
|--------------|------------|
| ⬆ Up Arrow    | Move Up    |
| ⬇ Down Arrow  | Move Down  |
| ⬅ Left Arrow  | Move Left  |
| ➡ Right Arrow | Move Right |

---

## 📂 Project Structure

```
Snake-Game-Turtle/
│
├── main.py          # Main game loop and event handling
├── snake.py         # Snake class and movement logic
├── food.py          # Food generation and random position
├── scoreboard.py    # Score tracking and high score system (file-based)
├── data.txt         # Stores high score
├── .gitignore
└── README.md
```

---

## 🚀 How to Run the Game

1. Make sure you have **Python installed** (Python 3 recommended)

2. Clone the repository:

```
git clone https://github.com/yukamenes/Snake-Game-Turtle.git
```

3. Navigate to the project folder:

```
cd Snake-Game-Turtle
```

4. Run the game:

```
python main.py
```

---

## 🛠 Technologies Used

- Python  
- Turtle Graphics  
- Object-Oriented Programming (OOP)  
- File Handling (read/write)  

---

## 📚 What I Practiced in This Project

- Python classes and objects  
- Working with multiple modules  
- Game loops  
- Collision detection  
- Event handling with keyboard input  
- File handling (saving/loading high score)  
- Simple game design  

---

## 🎯 Future Improvements

Some ideas for future improvements:

- ⚡ Increasing snake speed over time  
- 🍏 More food types  
- 🎵 Sound effects  
- 🎨 Improved graphics  
- 🖥 Game over screen with restart button  

---

## 👩‍💻 Author

Created by **Yuliia Menes** while practicing **Python and game development fundamentals**.

---

⭐ If you like this project, feel free to star the repository!
