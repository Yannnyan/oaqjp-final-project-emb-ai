""" This module tests the emotion detection module """
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotiondetector(self):
        """
        Performs the tests written in task 5
        """
        cases = [
            {"statement": "I am glad this happened","dominant_emotion": "joy"},
            {"statement": "I am really mad about this", "dominant_emotion": "anger"},
            {"statement": "I feel disgusted just hearing about this", "dominant_emotion": "disgust"},
            {"statement": "I am so sad about this", "dominant_emotion": "sadness"},
            {"statement": "I am really afraid that this will happen", "dominant_emotion": "fear"}
        ]
        for case in cases:
            self.assertEqual(emotion_detector(case['statement'])['dominant_emotion'],
                                case['dominant_emotion'])
if __name__ == '__main__':
    unittest.main()