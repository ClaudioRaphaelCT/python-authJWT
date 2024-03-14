from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import timedelta
from modules.token.controller.token import Token
from modules.home.messages.Message import Message


app = FastAPI(title="Faculty")
security = HTTPBearer()

access_token = Token.create("user123", timedelta(minutes=15))


@app.get("/")
def home():
    return Message.tip()


@app.get("/token")
def login(username: str, password: str):
    return Token.get(username, password, access_token)


@app.get("/protected")
def protected_route(credentials: HTTPAuthorizationCredentials = Depends(security)):
    return Token.validate(credentials.credentials, str(access_token))

