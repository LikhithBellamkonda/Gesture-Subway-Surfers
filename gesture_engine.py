import time
import math
import config

class GestureEngine:
    def __init__(self):
        self.last_shoulder_y = None
        self.last_wrist_y = None
        self.last_action_time = time.time()
        self.action_cooldown = 0.2 # Lowered cooldown for super fast response

    def calculate_distance(self, p1, p2):
        return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

    def detect_gestures(self, results):
        action = None
        current_time = time.time()
        
        if not results or not results.pose_landmarks:
            return action

        landmarks = results.pose_landmarks[0]
        
        # Extract landmarks
        left_shoulder = landmarks[11]
        right_shoulder = landmarks[12]
        left_hip = landmarks[23]
        right_hip = landmarks[24]
        left_knee = landmarks[25]
        right_knee = landmarks[26]
        left_ankle = landmarks[27]
        right_ankle = landmarks[28]
        left_wrist = landmarks[15]
        right_wrist = landmarks[16]

        shoulder_y = (left_shoulder.y + right_shoulder.y) / 2.0
        hip_y = (left_hip.y + right_hip.y) / 2.0
        wrist_y = (left_wrist.y + right_wrist.y) / 2.0

        if current_time - self.last_action_time < self.action_cooldown:
            return action

        if self.last_wrist_y is not None:
            dy = self.last_wrist_y - wrist_y # Positive if moving up
            
            if dy > config.HAND_MOVEMENT_THRESHOLD:
                action = "JUMP"
                self.last_action_time = current_time
            elif dy < -config.HAND_MOVEMENT_THRESHOLD:
                action = "SLIDE"
                self.last_action_time = current_time

        self.last_shoulder_y = shoulder_y
        self.last_wrist_y = wrist_y

        return action
