from save_dictionary import save_dictionary, load_dictionary, save_dictionary_best_way, load_dictionary_best_way
from models import OperationResponse, OperationStatus


def run_dictionary_save_interactions():
    user_input = eval(input("Enter dictionary data: "))

    if type(user_input) != dict:
        print("Input is not a valid dictionary!")
        return

    file_path = input("Enter file name: ")

    # save_response = save_dictionary(user_input, file_path)
    save_response = save_dictionary_best_way(user_input, file_path)
    print(f"Dictionary Save Status: {save_response.status}")

    if save_response.status == OperationStatus.FAILURE:
        print(f"Reason: {save_response.error}")
        return

    # load_response = load_dictionary(file_path)
    load_response = load_dictionary_best_way(file_path)
    if load_response.status == OperationStatus.SUCCESS:
        print(f"Loaded Dictionary: {load_response.data}")
    else:
        print(f"Load operation failure: {load_response.error}")


if __name__ == "__main__":
    run_dictionary_save_interactions()
