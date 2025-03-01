class ResponseModel:
    def __init__(self, code: int, message: str, data=None):
        self.code = code
        self.message = message
        self.data = data

    @classmethod
    def create(cls, data=None, message: str = "Success", code: int = 200, is_error=False):
        if is_error:
            return cls(code=400, message=message, data=None)
        return cls(code=code, message=message, data=data)

    def to_dict(self):
        response = {"code": self.code, "message": self.message}
        if self.data is not None:
            response["data"] = self.data
        return response