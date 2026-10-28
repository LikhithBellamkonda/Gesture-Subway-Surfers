import time
import config
from gesture_engine import GestureEngine

class MockLandmark:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class MockPoseLandmarks:
    def __init__(self, landmarks):
        self.pose_landmarks = [landmarks]

def create_mock_landmarks(shoulder_y, hip_y, wrist_y, left_wrist_x=0.6, right_wrist_x=0.4):
    landmarks = [MockLandmark(0, 0) for _ in range(33)]
    landmarks[11] = MockLandmark(0.5, shoulder_y) # left shoulder
    landmarks[12] = MockLandmark(0.5, shoulder_y) # right shoulder
    landmarks[23] = MockLandmark(0.5, hip_y) # left hip
    landmarks[24] = MockLandmark(0.5, hip_y) # right hip
    landmarks[15] = MockLandmark(left_wrist_x, wrist_y) # left wrist (normally higher x when mirrored)
    landmarks[16] = MockLandmark(right_wrist_x, wrist_y) # right wrist
    return MockPoseLandmarks(landmarks)

def run_tests():
    print("Testing GestureEngine...")
    engine = GestureEngine()

    # Initial state
    initial_results = create_mock_landmarks(shoulder_y=0.3, hip_y=0.7, wrist_y=0.7)
    action = engine.detect_gestures(initial_results)
    print(f"Initial state action: {action}")
    assert action is None

    # Wait for cooldown
    time.sleep(0.3)

    # Move hands up slightly from 0.7 to 0.65 (Threshold is 0.06, so 0.05 is not enough)
    results_move_up_small = create_mock_landmarks(shoulder_y=0.3, hip_y=0.7, wrist_y=0.65)
    action = engine.detect_gestures(results_move_up_small)
    print(f"Move hands up small action: {action}")
    assert action is None

    # Wait for cooldown
    time.sleep(0.3)

    # Move hands up large from 0.65 to 0.55 (0.1 difference, > 0.06)
    results_move_up_large = create_mock_landmarks(shoulder_y=0.3, hip_y=0.7, wrist_y=0.55)
    action = engine.detect_gestures(results_move_up_large)
    print(f"Move hands up large action: {action}")
    assert action == "JUMP"

    # Wait for cooldown
    time.sleep(0.3)

    # Cross hands
    results_crossed_arms = create_mock_landmarks(shoulder_y=0.3, hip_y=0.7, wrist_y=0.55, left_wrist_x=0.3, right_wrist_x=0.7)
    action = engine.detect_gestures(results_crossed_arms)
    print(f"Cross arms action: {action}")
    assert action == "SLIDE"

    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
