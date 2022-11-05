from play_waiting_game import waiting_game, WaitingGameResponse
import unittest

class TestWaitingGame(unittest.TestCase):

    def test_too_slow(self):
        expected_waiting_time = 4
        actual_waiting_time = 4.213
        answer = waiting_game(expected_waiting_time, actual_waiting_time)
        self.assertEqual(answer, WaitingGameResponse(0.213, "too slow"))

    def test_exact(self):
        expected_waiting_time = 4
        actual_waiting_time = 4.213
        answer = waiting_game(expected_waiting_time, actual_waiting_time)
        self.assertEqual(answer, WaitingGameResponse(0, "exact"))

    def test_too_fast(self):
        expected_waiting_time = 4
        actual_waiting_time = 3.213
        answer = waiting_game(expected_waiting_time, actual_waiting_time)
        self.assertEqual(answer, WaitingGameResponse(-0.787, "too fast"))