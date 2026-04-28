from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm
from jose import JWTError, jwt

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "your-secret-key"

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/secure-data")
async def secure_data(user=Depends(verify_token)):
    return {"data": "Secure Information"}


from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "your-secret-key"

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/secure-data")
async def secure_data(user=Depends(verify_token)):
    return {"data": "Secure Information"}


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Por enquanto, aceitamos qualquer user/pass para teste
    payload = {"sub": form_data.username}
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    
    # O Swagger precisa que você retorne 'token_type' como 'bearer'
    return {"access_token": token, "token_type": "bearer"}





