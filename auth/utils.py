from jose import jwt, JWTError
from datetime import datetime, timedelta

ALGORITHM="HS256"

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

def create_access_token(subject:str,expire:timedelta):
    expire_at=datetime.utcnow()+expire
    to_encode={"exp":expire_at,"sub":str(subject)}
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

def to_decode(my_token:str):
    decoded_token=jwt.decode(my_token,SECRET_KEY,algorithms=[ALGORITHM])
    return decoded_token
