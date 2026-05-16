# Constants and configurations

# Camera
CAMERA_INDEX = 0
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480
FPS_TARGET = 30

# Lane zones (x-coordinates mapped to [0.0, 1.0])
LANE_LEFT_THRESHOLD = 0.333
LANE_RIGHT_THRESHOLD = 0.666

# Gesture Thresholds
JUMP_THRESHOLD_Y = 0.03 # Torso movement between frames for jump (lowered for faster response)
BEND_THRESHOLD = 0.18 # Distance between shoulders and hips when bent over
CLAP_THRESHOLD = 0.1 # Distance between wrists to trigger a slide

# Jogging thresholds
JOG_VELOCITY_THRESHOLD = 0.02
JOG_TIMEOUT = 1.5 # seconds before pausing if no jogging

# Colors for UI (BGR)
COLOR_LANE_LEFT = (200, 50, 50)
COLOR_LANE_CENTER = (50, 200, 50)
COLOR_LANE_RIGHT = (50, 50, 200)
COLOR_TEXT = (255, 255, 255)
COLOR_STATUS_RUNNING = (0, 255, 0)
COLOR_STATUS_PAUSED = (0, 0, 255)
