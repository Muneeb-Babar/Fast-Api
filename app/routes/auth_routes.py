from fastapi import APIRouter, HTTPException, status, Depends
from ..schemas.user_schema import UserRegister, UserLogin
from ..models.user_model import user_collection
from ..utils.hash_password import hash_password, verify_password
from ..utils.jwt_handler import create_access_token
from bson import ObjectId

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register")
async def register_user(user: UserRegister):
    existing_user = await user_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
    
    hashed_pw = hash_password(user.password)
    new_user = {"name": user.name, "email": user.email, "password": hashed_pw}
    result = await user_collection.insert_one(new_user)
    return {"message": "User registered successfully", "user_id": str(result.inserted_id)}

@router.post("/login")
async def login_user(user: UserLogin):
    db_user = await user_collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    token = create_access_token({"user_id": str(db_user["_id"]), "email": db_user["email"]})
    return {"access_token": token, "token_type": "bearer"}
