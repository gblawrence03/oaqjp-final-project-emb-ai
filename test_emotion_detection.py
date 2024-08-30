import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        self.run_test("I am glad this happened", "joy")
        self.run_test("I am really mad about this", "anger")
        self.run_test("I feel disgusted just hearing about this", "disgust")
        self.run_test("I am so sad about this", "sadness")
        self.run_test("I am really afraid that this will happen", "fear")

    def run_test(self, text, emotion):
        self.assertEqual(emotion_detector(text)["dominant_emotion"], emotion)

unittest.main()
