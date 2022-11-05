from random import randint
from datetime import datetime
from dataclasses import dataclass
import time

@dataclass
class WaitingGameResponse:
    time_difference: float
    time_taken: float
    game_message: str

    def __eq__(self, other):
        if isinstance(other, WaitingGameResponse):
            return self.time_difference == other.time_difference and self.time_taken == other.time_taken
        return False

def waiting_game(expected_waiting_time, actual_waiting_time) -> WaitingGameResponse:
    elasped_time = actual_waiting_time - expected_waiting_time
    game_response = ""

    if elasped_time > 0:    
        game_response = "too slow"
    elif elasped_time < 0:
        game_response = "too fast"
    else:
        game_response = "exact"

    return WaitingGameResponse(elasped_time, actual_waiting_time ,game_response)

def waiting_game_personal():
    expected_waiting_time = randint(2,4)
    print(f"Your target time is {expected_waiting_time} seconds.")
    
    starting_time = datetime.now()
    enter_input = input("--- Press Enter to Begin")
    ending_time = datetime.now()
    actual_waiting_time = (ending_time - starting_time).total_seconds()
    actual_waiting_time = round(actual_waiting_time, 3)
    
    answer = waiting_game(expected_waiting_time, actual_waiting_time)
    print(f"You are {answer.game_message}. \
            \n Waiting Time: {abs(answer.time_taken)} seconds \
             \n Elasped Time: {answer.time_difference} seconds")

def waiting_game_official_solution():
    expected_waiting_time = randint(2,4)
    print(f"Your target time is {expected_waiting_time} seconds.")
    
    starting_time = time.perf_counter()
    enter_input = input("--- Press Enter to Begin")
    ending_time = time.perf_counter()
    actual_waiting_time = ending_time - starting_time
    
    answer = waiting_game(expected_waiting_time, actual_waiting_time)
    print(f"You are {answer.game_message}. \
            \n Waiting Time: {abs(answer.time_taken)} seconds \
             \n Elasped Time: {answer.time_difference} seconds")

if __name__ == "__main__":
    waiting_game_official_solution()