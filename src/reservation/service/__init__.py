class ServiceError(Exception):
    def __init__(self, message: str, code: int = 500):
        self.message = message
        self.code = code

    def __str__(self):
        return f"{self.__class__.__name__}: {self.message}"


class NoUserIDFoundError(ServiceError):
    def __init__(self, message: str):
        super().__init__(message=message, code=404)
