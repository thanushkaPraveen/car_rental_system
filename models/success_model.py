class SuccessModel:
    def __init__(self, code: int, message: str, data=None):
        self.code = code
        self.message = message
        self.data = data

    @classmethod
    def with_data(cls, data, message: str = "Success", code: int = 200):
        return cls(code, message, data)

    def to_dict(self):
        return {"code": self.code, "message": self.message, "data": self.data}
