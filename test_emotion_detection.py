from EmotionDetection import emotion_detector as ed
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        response = ed("I am glad this happened")
        testing = response["dominant_emotion"]
        self.assertEqual(testing, "joy")
    
    def test_anger(self):
        response = ed("I am really mad about this")
        testing = response["dominant_emotion"]
        self.assertEqual(testing, "anger")

    def test_disgust(self):
        response = ed("I feel disgusted just hearing about this")
        testing = response["dominant_emotion"]
        self.assertEqual(testing, "disgust")

    def test_sadness(self):
        response = ed("I am so sad about this")
        testing = response["dominant_emotion"]
        self.assertEqual(testing, "sadness")

    def test_fear(self):
        response = ed("I am really afraid that this will happen")
        testing = response["dominant_emotion"]
        self.assertEqual(testing, "fear")

if __name__ == '__main__':
    unittest.main()
