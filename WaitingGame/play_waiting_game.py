from random import randint
from datetime import datetime
from dataclasses import dataclass

@dataclass
class WaitingGameResponse:
    time_difference: float
    game_message: str

def waiting_game(expected_waiting_time, actual_waiting_time) -> WaitingGameResponse:
    pass

if __name__ == "__main__":
    expected_waiting_time = randint(2,4)
    print(f"Your target time is {expected_waiting_time} seconds.")
    
    starting_time = datetime.now()
    enter_input = input("--- Press Enter to Begin")
    ending_time = datetime.now()
    actual_waiting_time = ending_time - starting_time

    waiting_game(expected_waiting_time, actual_waiting_time)