from starlette.responses import JSONResponse


class MessagesOk:
    @classmethod
    def protected(cls):
        return JSONResponse(status_code=200, content={"message": "Access allowed!"})

    @classmethod
    def get_token(cls, access_token):
        return JSONResponse(status_code=201,
                            content={"status": "Access allowed!", "type": "Bearer", "key": access_token})
