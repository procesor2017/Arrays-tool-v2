"""Unit test for create matrix"""
import unittest
from matrix.create_matrix import create_orto


class TestOrtoMetod(unittest.TestCase):
    def test_two_on_three(self):
        user_payload = [{"0": "a", "1": "aa", "2": "aaa"},
                        {"0": "b", "1": "bb", "2": "bbb"}]
        expect_result = [['a', 'aa', 'aaa'], ['a', 'bb', 'bbb'], [
            'b', 'aa', 'bbb'], ['b', 'bb', 'aaa']]
        self.assertEqual(create_orto(0, 1, user_payload), expect_result)

    def test_two_on_four_and_four_on_one(self):
        user_payload = [{"0": "a", "1": "aa", "2": "aaa", "3": "aaaa", "4": "aaaaa"}, {
            "0": "b", "1": "bb", "2": "bbb", "3": "bbbb", "4": "bbbbb"}, {"4": "ccccc"}, {"4": "ddddd"}]
        expect_result =[["a", "aa", "bbb", "bbbb", "ccccc"], 
                        ["a", "bb", "aaa", "bbbb", "bbbbb"],
                        ["a", "bb", "bbb", "aaaa", "ddddd"],
                        ["b", "aa", "aaa", "bbbb", "ddddd"],
                        ["b", "aa", "bbb", "aaaa", "bbbbb"],
                        ["b", "bb", "aaa", "aaaa", "ccccc"],
                        ["b", "bb", "bbb", "bbbb", "aaaaa"]]
        self.assertEqual(create_orto(0, 8, user_payload), expect_result)


if __name__ == '__main__':
    unittest.main()
