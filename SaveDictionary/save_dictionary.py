from models import OperationResponse, OperationStatus

def load_dictionary(file_path: str) -> OperationResponse:
    try:
        with open(file_path, "r") as file:
            dictionary = eval(file.read())
            return OperationResponse(status=OperationStatus.SUCCESS, data = dictionary)
    except Exception as e:
        print(e,"check")
        return OperationResponse(status=OperationStatus.ERROR, error = str(e))

def save_dictionary(dictionary: dict, file_path: str) -> OperationResponse:
    try:
        with open(file_path, "w") as file:
            file.write(str(dictionary))
            return OperationResponse(status=OperationStatus.SUCCESS)
    except Exception as e:
        return OperationResponse(status=OperationStatus.FAILURE, error=str(e))