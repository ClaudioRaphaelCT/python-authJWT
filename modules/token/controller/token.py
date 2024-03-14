import jwt
from datetime import datetime, timedelta
from modules.token.messages.messages_ok import MessagesOk
from modules.token.messages.messages_error import MessagesError

SECRET_KEY = "my_key"
ALGORITHM = "HS256"


class Token:
    @classmethod
    def create(cls, username: str, expires_delta: timedelta):
        to_encode = {"sub": username, "exp": datetime.now() + expires_delta}
        key_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return key_token

    @classmethod
    def validate(cls, token: str, access: str):
        if token == "Bearer " + access:
            return MessagesOk.protected()
        else:
            return MessagesError.protected()

    @classmethod
    def get(cls, username: str, password: str, access_token):
        if username == "Top" and password == "2024":
            return MessagesOk.get_token(access_token)
        return MessagesError.get_token()
