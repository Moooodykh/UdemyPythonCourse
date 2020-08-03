import cap
import unittest

class CapTest(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap.cap_func(text)
        self.assertEqual(result,'Python')
    
    def test_two_words(self):
        text = 'hello habibi'
        result= cap.cap_each_ord(text)
        self.assertEquals(result,'Hello Habibi')
if __name__ == "__main__":
    unittest.main()
