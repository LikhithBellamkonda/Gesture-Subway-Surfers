# 🏃‍♂️🛹 AI Gesture Controller for Subway Surfers

Welcome to the **AI Gesture Controller**! This project transforms your webcam into a motion controller, allowing you to play the web version of *Subway Surfers* using only your body movements.

Powered by **Google's MediaPipe Tasks API**, this application tracks your pose in real-time and translates physical gestures into ultra-low-latency keyboard inputs.

---

## 🚀 Key Features

- ⚡ **Ultra-low Latency:** Utilizes a lightweight pose model and minimizes the camera buffer to a single frame for zero-delay responsiveness.
- 📺 **Always-on-top UI:** A discreet 320x240 heads-up display sits in the corner of your screen, showing live tracking without obstructing your gameplay.
- 🎮 **Zero Keyboard Interaction:** No need to touch your keyboard while playing. Just run the script, step back, and enjoy!

---

## 🕺 Gesture Mapping

Control your character completely hands-free with these intuitive movements:

| Action | Physical Gesture |
| :--- | :--- |
| **Move Left/Right** | Step your body into the left or right third of the camera frame. |
| **Jump** | Raise both of your hands upwards. |
| **Slide / Roll** | Cross your arms over your chest (forming an "X"). |

---

## 🛠️ Installation & Setup

Follow these simple steps to get your motion controller running:

1. **Clone the repository** to your local machine:
   ```bash
   git clone <your-repo-url>
   cd Gesture-Subway-Surfers
   ```

2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🎮 How to Play

1. Open the [web version of Subway Surfers](https://poki.com/en/g/subway-surfers) in your favorite browser.
2. Run the application from your terminal:
   ```bash
   python main.py
   ```
3. **Important:** Click on your browser window to make sure the game is the **active window**.
4. Step back from your webcam until your upper body (shoulders, hips, and hands) is visible.
5. Start moving and set a new high score!
