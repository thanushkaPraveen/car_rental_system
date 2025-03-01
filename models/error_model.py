class ErrorModel:
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

    @classmethod
    def from_message(cls, message: str, code: int = 400):
        return cls(code, message)

    def to_dict(self):
        return {"code": self.code, "message": self.message}
