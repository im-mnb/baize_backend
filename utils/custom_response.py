from rest_framework.response import Response
from utils.response_code import ResponseCode

class BaseResponse(Response):
    def __init__(self, code, count, message, data, content_type="application/json"):
        super().__init__(data={
            "code": code,
            "count": count,
            "message": message,
            "data": data
        }, content_type=content_type)

class SuccessResponse(BaseResponse):
    def __init__(self, code=ResponseCode.SUCCESS.value, count=1, message="success", data=""):
        super().__init__(code, count, message, data)

class ErrorResponse(BaseResponse):
    def __init__(self, code=ResponseCode.UNKNOE.value, count=0, message="error", data=""):
        super().__init__(code, count, message, data)