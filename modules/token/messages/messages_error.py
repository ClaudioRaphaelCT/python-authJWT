from starlette.responses import JSONResponse


class MessagesError:
    @classmethod
    def protected(cls):
        return JSONResponse(status_code=400, content={"message": "Access denied!"})

    @classmethod
    def get_token(cls):
        return JSONResponse(status_code=401, content={"message": "User does not have permission!"})
