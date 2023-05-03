from unittest import TestCase, main
from whiteboard import solution


class WhiteboardTestCase(TestCase):
    
    def test_1_vowel_on_end(self):
        self.assertEqual(solution("apple"), "ppl")
    
    def test_2_vowel_in_middle(self):
        self.assertEqual(solution("linux"), "lnx")

    def test_3_containing_y(self):
        self.assertEqual(solution("kayak"), "kyk") 

    def test_4_capitalization(self):
        self.assertEqual(solution("XAEioUx"), "Xx")
      

if __name__ == "__main__":
    main()