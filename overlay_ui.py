import cv2
import config

class OverlayUI:
    def __init__(self):
        self.font = cv2.FONT_HERSHEY_SIMPLEX

    def draw(self, frame, lane, action, fps):
        h, w, _ = frame.shape
        
        # Draw Lane boundaries
        left_x = int(config.LANE_LEFT_THRESHOLD * w)
        right_x = int(config.LANE_RIGHT_THRESHOLD * w)
        
        cv2.line(frame, (left_x, 0), (left_x, h), config.COLOR_LANE_LEFT, 2)
        cv2.line(frame, (right_x, 0), (right_x, h), config.COLOR_LANE_RIGHT, 2)

        # Highlight current lane zone
        overlay = frame.copy()
        alpha = 0.2
        if lane == "LEFT":
            cv2.rectangle(overlay, (0, 0), (left_x, h), config.COLOR_LANE_LEFT, -1)
        elif lane == "CENTER":
            cv2.rectangle(overlay, (left_x, 0), (right_x, h), config.COLOR_LANE_CENTER, -1)
        elif lane == "RIGHT":
            cv2.rectangle(overlay, (right_x, 0), (w, h), config.COLOR_LANE_RIGHT, -1)
            
        cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

        # UI Panel
        cv2.rectangle(frame, (10, 10), (350, 150), (0, 0, 0), -1)
        
        # FPS
        cv2.putText(frame, f"FPS: {fps:.1f}", (20, 40), self.font, 0.8, config.COLOR_TEXT, 2)
        
        # Lane
        cv2.putText(frame, f"LANE: {lane}", (20, 80), self.font, 0.8, config.COLOR_TEXT, 2)

        # Action
        action_text = action if action else "NONE"
        cv2.putText(frame, f"ACTION: {action_text}", (20, 110), self.font, 0.8, config.COLOR_TEXT, 2)

        return frame
