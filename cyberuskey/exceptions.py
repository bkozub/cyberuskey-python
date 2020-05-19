class InvalidValueError(ValueError):
    def __init__(self, value: str):
        self.value = value
        super().__init__(value)

    def __str__(self):
        return f"Provided {self.value} is invalid"


class InvalidAuthenticateValueError(ValueError):
    def __str__(self):
        return "Value isn't initialized. You need to authenticate."


class MissingAuthorizationCode(ValueError):
    def __str__(self):
        return "Missing authorization code value"


class AuthenticateBaseException(Exception):
    def __init__(self, error: str, error_description: str):
        self.error = error
        self.error_description = error_description
        super().__init__(error)

    def __str__(self):
        return self.error_description


class AuthenticateException(AuthenticateBaseException):
    pass
