import time
import math
import config

class GestureEngine:
    def __init__(self):
        self.last_shoulder_y = None
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

        if current_time - self.last_action_time < self.action_cooldown:
            return action

        # 2. Detect Jump (Sudden vertical movement up)
        if self.last_shoulder_y is not None:
            dy = self.last_shoulder_y - shoulder_y # Positive if moving up
            
            if dy > config.JUMP_THRESHOLD_Y:
                action = "JUMP"
                self.last_action_time = current_time

        # 3. Detect Slide (Bending down OR X Gesture)
        # Bending down/forward causes the 2D vertical distance between your shoulders and hips to shrink
        torso_length = hip_y - shoulder_y
        
        # X Gesture: Since the camera is mirrored like a selfie, your left wrist is normally on the right side (higher X).
        # When you cross your arms, they swap sides, so left_wrist.x becomes smaller than right_wrist.x
        arms_crossed = left_wrist.x < right_wrist.x
        
        if torso_length < config.BEND_THRESHOLD or arms_crossed:
            action = "SLIDE"
            self.last_action_time = current_time
        
        # Check hands up for alternative jump
        if left_wrist.y < left_shoulder.y and right_wrist.y < right_shoulder.y:
            action = "JUMP"
            self.last_action_time = current_time

        self.last_shoulder_y = shoulder_y

        return action
