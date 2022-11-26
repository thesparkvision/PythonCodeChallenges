from models import OperationResponse, OperationStatus
import pickle


def load_dictionary(file_path: str) -> OperationResponse:
    try:
        with open(file_path, "r") as file:
            dictionary = eval(file.read())
            return OperationResponse(
                status=OperationStatus.SUCCESS, data=dictionary)
    except Exception as e:
        return OperationResponse(status=OperationStatus.ERROR, error=str(e))


def save_dictionary(dictionary: dict, file_path: str) -> OperationResponse:
    try:
        with open(file_path, "w") as file:
            file.write(str(dictionary))
            return OperationResponse(status=OperationStatus.SUCCESS)
    except Exception as e:
        return OperationResponse(status=OperationStatus.FAILURE, error=str(e))


def save_dictionary_best_way(
        dictionary: dict,
        file_path: str) -> OperationResponse:
    try:
        with open(file_path, "wb") as file:
            pickle.dump(dictionary, file)
            return OperationResponse(status=OperationStatus.SUCCESS)
    except Exception as e:
        return OperationResponse(status=OperationStatus.FAILURE, error=str(e))


def load_dictionary_best_way(file_path: str) -> OperationResponse:
    try:
        with open(file_path, "rb") as file:
            dictionary = pickle.load(file)
            return OperationResponse(
                status=OperationStatus.SUCCESS, data=dictionary)
    except Exception as e:
        return OperationResponse(status=OperationStatus.ERROR, error=str(e))
