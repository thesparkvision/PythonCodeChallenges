from dataclasses import dataclass

@dataclass
class OperationResponse:
    status: str
    data: object = None
    error: str = ""

def load_dictionary(file_path: str) -> OperationResponse:
    pass

def save_dictionary(dictionary: dict, file_path: str) -> OperationResponse:
    try:
        with open(file_path, "w") as file:
            file.write(str(dictionary))
            return OperationResponse(status="Success")
    except Exception as e:
        return OperationResponse(status="Failure", error=str(e))    

def run_dictionary_save_interactions():
    user_input = eval(input())

    if type(user_input) != dict:
        print("Input is not a valid dictionary!")
        return
    
    file_path = input()

    save_response = save_dictionary(user_input, file_path)
    print(f"Dictionary Save Status: {save_response.status}")

    if save_response.status == "Failure":
        print(f"Reason: {save_response.error}")
        return

    load_response = load_dictionary(file_path)
    if load_response.status == "Success":
        print(f"Loaded Dictionary: {load_response.data}")
    else:
        print(f"Load operation failure: {load_response.error}")

if __name__ == "__main__":
    run_dictionary_save_interactions()