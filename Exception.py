from typing_extensions import Self

class FileExtensionException(Exception):
    """Exception raised for errors in the file extension

    Attributes:
        file_type (str, optional): 
        message (str, optional): 
    """
    def __init__(self: Self, file_type: str|None = None, message: str = "File must be a .wav") -> None:
        self.message = message + ' (Current file extension:' + file_type + ')' if file_type else message
        super().__init__(self.message)