import cv2
import time
import config
from pose_tracker import PoseTracker
from lane_detector import LaneDetector
from gesture_engine import GestureEngine
from browser_controller import BrowserController
from overlay_ui import OverlayUI

def main():
    cap = cv2.VideoCapture(config.CAMERA_INDEX)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, config.CAMERA_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, config.CAMERA_HEIGHT)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1) # CRITICAL: Removes camera delay/latency

    tracker = PoseTracker()
    lane_detector = LaneDetector()
    gesture_engine = GestureEngine()
    controller = BrowserController()
    ui = OverlayUI()

    prev_time = time.time()
    
    cv2.namedWindow('Subway Surfers Motion Controller', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Subway Surfers Motion Controller', cv2.WND_PROP_TOPMOST, 1)

    print("Starting Ultra-Low Latency AI Motion Controller...")

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Flip the frame horizontally for a selfie-view display
        frame = cv2.flip(frame, 1)

        # FPS Calculation
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time) if (curr_time - prev_time) > 0 else 0
        prev_time = curr_time

        # Pose Tracking
        results = tracker.process_frame(frame)
        
        if results and results.pose_landmarks:
            # Analyze Lane
            current_lane = lane_detector.detect_lane(results)
            if lane_detector.has_lane_changed():
                if current_lane == "LEFT":
                    controller.move_left()
                elif current_lane == "RIGHT":
                    controller.move_right()
                elif current_lane == "CENTER":
                    if lane_detector.last_lane == "LEFT":
                        controller.move_right()
                    elif lane_detector.last_lane == "RIGHT":
                        controller.move_left()

            # Analyze Gestures
            action = gesture_engine.detect_gestures(results)
            
            if action == "JUMP":
                controller.jump()
            elif action == "SLIDE":
                controller.slide()

            # Draw
            frame = tracker.draw_landmarks(frame, results)
        else:
            current_lane = "CENTER"
            action = None

        # Render UI
        frame = ui.draw(frame, current_lane, action, fps)

        # Small window size for playing
        display_frame = cv2.resize(frame, (320, 240))
        cv2.imshow('Subway Surfers Motion Controller', display_frame)
        
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
