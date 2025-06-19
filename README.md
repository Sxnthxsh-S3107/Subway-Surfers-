# 🖐️ Subway Surfers Hand‑Gesture Controller

Control **Subway Surfers** with just your hand using your webcam.  
This project uses **Python**, **OpenCV**, **MediaPipe**, and **PyAutoGUI** to detect hand gestures and convert them into game controls.

![Demo](https://www.icegif.com/wp-content/uploads/2024/09/subway-surfers-icegif-5.gif)

---

## 💻 What It Does

| Gesture           | Fingers Up | Action in Game |
|------------------|------------|----------------|
| ☝🏼 One finger     | Jump       | `Up Arrow`     |
| ✌🏼 Two fingers    | Slide      | `Down Arrow`   |
| 🤟 Three fingers  | Move Left  | `Left Arrow`   |
| 🖖 Four fingers   | Move Right | `Right Arrow`  |

---

## ⚙️ Setup & Run

```bash
# Clone the repo
git clone https://github.com/your-username/subway-gesture.git
cd subway-gesture

# Create virtual environment
python -m venv subway_env

# Activate the environment
# For CMD:
subway_env\Scripts\activate
# For PowerShell:
.\subway_env\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the controller
python gesture_controller.py
