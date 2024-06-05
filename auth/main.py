from datetime import datetime, timedelta
from fastapi import Depends,FastAPI,HTTPException
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from typing import Annotated
from jose import jwt,JWTError
from auth.utils import create_access_token,to_decode

app=FastAPI()





# @app.get("/login")
# def login(form_data:Annotated[OAuth2PasswordRequestForm,Depends:OAuth2PasswordRequestForm]):
#     username=form_data.username
#     password=form_data.password
    




auth_scheme=OAuth2PasswordBearer(tokenUrl="/logindb")

fakedata:dict[str, dict[str, str]]={
   "ahmed": {"name":"ahmed",
     "password":"ahmed123",
      "email":"ahmed@gmail.com"       
    }
    }



# def login(username:str,password:str):
#     fake_user_data=fakedata.get(username)

#     if not fake_user_data:
#         raise HTTPException(status_code=400,detail="user not found")
#     if fake_user_data["password"]!= password:
#         raise HTTPException(status_code=400,detail="incorrect password")
    
#     return "correct password"
 
    



@app.post("/token")
def login_db(formdata:Annotated[OAuth2PasswordRequestForm,Depends(OAuth2PasswordRequestForm)]):
    fake_user_data=fakedata.get(formdata.username)

    if not fake_user_data:
        raise HTTPException(status_code=400,detail="user not found")
    if fake_user_data["password"]!= formdata.password:
        raise HTTPException(status_code=400,detail="incorrect password")
    

    expire_at=timedelta(minutes=15)
    access_token=create_access_token(subject=formdata.username,expire=expire_at)
    
    
    return {"access_token":access_token,"access_token_type":"bearer","expires_in":expire_at.total_seconds()}








@app.get("/")
def get():
    return {"Hello":"World"}

@app.get("/locked")
def lock(token:Annotated[str, Depends(auth_scheme)]):
    return {"data":"123"}

@app.get("/new_token")
def new_token(username:str):
    access_token_expires=timedelta(minutes=5)
    create_access_token(subject=username, expire=access_token_expires)
    return {"access_token":create_access_token(subject=username, expire=access_token_expires)}









@app.get("/decodetoken")
def decoded_token(token:str):
    try:
        my_token=to_decode(my_token=str(token))
        return {"decoded_token":my_token}
    except JWTError as e:
        return{"error":str(e)}