# HandJam –Gesture-Controlled Spotify Player

HandJam lets you control your Spotify music hands-free using your laptop's webcam.  
Pause, play, skip tracks, and adjust volume with simple hand gestures — no mouse, no keyboard, just your vibe.

## ✨ Features
- **Gesture-based controls**:
  - Open palm → Play / Pause
  - Point right → Next track
  - Thumb up → Volume up
  - Thumb down → Volume down
- Real-time **track info & album art** overlay
- **Spotify Web API** integration (works with any active Spotify device)

---

## 📸 How It Works
Using [MediaPipe Hands](https://developers.google.com/mediapipe/solutions/hands) and [OpenCV](https://opencv.org/), AI DJ recognizes your hand gestures in real time and maps them to Spotify playback controls via [Spotipy](https://spotipy.readthedocs.io/).

---

## 🚀 Installation
1. **Clone the repo**
    ```bash
    git clone https://github.com/your-username/AI-DJ.git
    cd AI-DJ
    ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure Spotify API**
    - Create an app at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
    - Add this redirect URI:  
      ```
      http://127.0.0.1:8888/callback
      ```
    - Copy your **Client ID** and **Client Secret** into `music_controls.py`.

4. **Run**
    ```bash
    python main.py
    ```

---

## 🕹 Usage
- Launch the app and allow Spotify authentication (opens in your browser).
- Ensure you have an active Spotify device (desktop, phone, or speaker).
- Show gestures in front of your webcam — AI DJ will do the rest.
- Press `q` to quit.

---

## 📦 Tech Stack
- **Python**
- [OpenCV](https://opencv.org/) – Camera feed & UI
- [MediaPipe Hands](https://developers.google.com/mediapipe/solutions/hands) – Gesture recognition
- [Spotipy](https://spotipy.readthedocs.io/) – Spotify API integration
- [Requests](https://docs.python-requests.org/en/master/) & NumPy – For album art display

---

## 🛠 Future Plans
- Package into a one-click **desktop app** (Windows/macOS)
- Gesture remapping & calibration
- Support for **Spotify Premium** advanced features

---

## 🤝 Contributing
Pull requests and suggestions are welcome! Feel free to fork and improve AI DJ.

---

## 📜 License
MIT License – free to use and modify.
