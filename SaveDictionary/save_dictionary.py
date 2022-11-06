from dataclasses import dataclass

@dataclass
class OperationResponse:
    data: object
    status: str
    error: str

def load_dictionary(file_path: str) -> OperationResponse:
    pass

def save_dictionary(dictionary: dict, file_path: str) -> OperationResponse:
    pass

def run_dictionary_save_interactions():
    user_input = eval(input())
    file_path = input()

    if type(user_input) != "dict":
        print("Input is not a valid dictionary!")

    save_response = save_dictionary(dictionary, file_path)
    print(f"Dictionary Save Status: {save_response.status}")

    if save_response.status == "Failure":
        return

    load_response = load_dictionary(file_path)
    if load_response.status == "Success":
        print(f"Loaded Dictionary: {load_response.data}")
    else:
        print(f"Load operation failure: {load_response.error}")

if __name__ == "__main__":
    run_dictionary_save_interactions()