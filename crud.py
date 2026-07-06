from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
from typing import List

app = FastAPI()

# Database Connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="MySql123",
        database="userdb"
    )

# Models
class User(BaseModel):
    name: str
    email: str
    role: str

class UserResponse(User):
    id: int

# Home
@app.get("/")
def home():
    return {"message": "FastAPI CRUD API"}

# Create User
@app.post("/users/", response_model=UserResponse)
def create_user(user: User):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users(name,email,role) VALUES(%s,%s,%s)",
        (user.name, user.email, user.role)
    )

    conn.commit()
    user_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return {"id": user_id, **user.dict()}

# Get All Users
@app.get("/users/", response_model=List[UserResponse])
def get_users():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return users

# Get User By ID
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM users WHERE id=%s",
        (user_id,)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user

# Update User
@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: User):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE users
        SET name=%s,email=%s,role=%s
        WHERE id=%s
        """,
        (user.name, user.email, user.role, user_id)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"id": user_id, **user.dict()}

# Delete User
@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM users WHERE id=%s",
        (user_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "User deleted successfully"}