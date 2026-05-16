import config

class LaneDetector:
    def __init__(self):
        self.current_lane = "CENTER"
        self.last_lane = "CENTER"

    def detect_lane(self, results):
        if not results or not results.pose_landmarks:
            return self.current_lane

        landmarks = results.pose_landmarks[0]
        # Use shoulders to calculate center of torso
        left_shoulder = landmarks[11]
        right_shoulder = landmarks[12]
        
        if left_shoulder.visibility < 0.5 or right_shoulder.visibility < 0.5:
            return self.current_lane

        center_x = (left_shoulder.x + right_shoulder.x) / 2.0

        self.last_lane = self.current_lane

        if center_x < config.LANE_LEFT_THRESHOLD:
            self.current_lane = "LEFT"
        elif center_x > config.LANE_RIGHT_THRESHOLD:
            self.current_lane = "RIGHT"
        else:
            self.current_lane = "CENTER"

        return self.current_lane

    def has_lane_changed(self):
        return self.current_lane != self.last_lane
