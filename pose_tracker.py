import cv2
import mediapipe as mp
import time

class PoseTracker:
    def __init__(self):
        BaseOptions = mp.tasks.BaseOptions
        PoseLandmarker = mp.tasks.vision.PoseLandmarker
        PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
        VisionRunningMode = mp.tasks.vision.RunningMode

        options = PoseLandmarkerOptions(
            base_options=BaseOptions(model_asset_path='pose_landmarker_lite.task'),
            running_mode=VisionRunningMode.VIDEO)
            
        self.landmarker = PoseLandmarker.create_from_options(options)
        self.start_time = int(time.time() * 1000)
        self.last_ts = -1

    def process_frame(self, frame):
        # Convert BGR to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
        
        # Calculate timestamp
        timestamp_ms = int(time.time() * 1000)
        
        ts = timestamp_ms - self.start_time
        if ts <= self.last_ts:
            ts = self.last_ts + 1
        self.last_ts = ts
        
        pose_landmarker_result = self.landmarker.detect_for_video(mp_image, ts)
        
        return pose_landmarker_result

    def draw_landmarks(self, frame, results):
        if results and results.pose_landmarks:
            for pose_landmarks in results.pose_landmarks:
                for landmark in pose_landmarks:
                    x = int(landmark.x * frame.shape[1])
                    y = int(landmark.y * frame.shape[0])
                    cv2.circle(frame, (x, y), 2, (245, 117, 66), -1)
        return frame
