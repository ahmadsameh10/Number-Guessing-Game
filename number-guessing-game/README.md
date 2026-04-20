# 🎯 Number Guessing Game

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-Free-lightgrey)

---

## 📌 Overview

The **Number Guessing Game** is a simple command-line Python application.
The system randomly selects a number between **1 and 100**, and the player must guess it.

After each attempt, the program gives feedback:

* Too high 🔺
* Too low 🔻

Until the correct number is guessed 🎉

---

## 🎮 Features

* Random number generation (1–100)
* User input handling
* Helpful hints (Too high / Too low)
* Attempt counter
* Error handling for invalid input

---

## 👥 Team Members

| Name                         | ID       |
| ---------------------------- | -------- |
| Ahmed Mohamed Khater         | 24040818 |
| Eyad Mohamed Hamed Gebril    | 24040825 |
| Ahmad Sameh Talaat Abdelhadi | 24040320 |
| Ahmed Osama Mahmoud Mohamed  | 24040529 |
| Islam Mahmoud Abdelrafea     | 24040895 |

---

## 🛠 Tech Stack

* **Language:** Python
* **Library:** random (built-in)

---

## ▶️ Getting Started

### 📥 Installation

```bash
git clone https://github.com/iia7mxd/number-guessing-game.git
cd number-guessing-game
```

---

### ▶️ Run the Game

```bash
python game.py
```

---

## 📸 Screenshots

### Game Start

![Game Start](screenshots/start.png.jpeg)

### Winning Moment

![Winning](screenshots/win.png.jpeg)

---

## 🧪 Testing

### ✔️ Test Cases

| Scenario          | Expected Result         |
| ----------------- | ----------------------- |
| Correct guess     | Winning message appears |
| Lower guess       | "Too low" message       |
| Higher guess      | "Too high" message      |
| Invalid input     | Error message shown     |
| Multiple attempts | Counter increases       |

---

## ⚠️ Limitations

* Terminal only (no GUI)
* Fixed range (1–100)
* No difficulty levels
* No player profiles

---

## 🚀 Future Improvements

* Add GUI
* Add difficulty levels
* Add scoring system
* Add multiplayer mode
* Save player progress

---

## 📂 Project Structure

```bash
number-guessing-game/
│── game.py
│── README.md
│── screenshots/
    ├── start.png.jpeg
    └── win.png.jpeg
```

---

## 📄 License

This project is for educational purposes and is free to use.
