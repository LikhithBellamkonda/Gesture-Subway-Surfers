# AI Gesture Controller for Subway Surfers 🏃‍♂️🛹

Play the web version of Subway Surfers using only your body! This project uses Google's MediaPipe Tasks API to track your movements in real-time through your webcam and translates them into ultra-low-latency keyboard inputs.

## 🎮 How to Play
1. Open the [web version of Subway Surfers](https://poki.com/en/g/subway-surfers) in your browser.
2. Start the Python script.
3. Make sure your browser window is **active** (click on it).
4. Step back so the camera can see your shoulders and hips!

## 🕺 Gestures
- **Move Left/Right:** Simply step into the left or right third of your camera frame.
- **Jump:** Thrust your shoulders upward, OR raise your hands above your shoulders.
- **Slide / Roll:** Bend down/forward toward the camera, OR cross your arms over your chest (the "X" gesture).

## 🚀 Features
- **Ultra-low Latency:** Uses the new MediaPipe Tasks API with a lightweight pose model. The camera buffer is minimized to 1 frame to ensure absolute zero delay.
- **Always-on-top UI:** A small 320x240 heads-up display sits in the corner of your screen showing your live tracking and detected gestures without blocking the game.
- **Zero Keyboard Interaction:** No keyboard touching required. Just run the script and play!

## 🛠️ Setup
1. Clone the repository.
2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```
