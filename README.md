# 🐍 FastAPI + MongoDB CRUD API with Authentication
A modern **FastAPI** project built using Python, following clean architecture principles similar to **MERN structure**. This project includes **JWT Authentication** for users and **CRUD operations** for e-commerce products using **MongoDB**.

##  Features
✅ User Authentication (Register & Login) using JWT  
✅ Secure Password Hashing (Bcrypt)  
✅ MongoDB Database Connection  
✅ CRUD APIs for Products (Create, Read, Update, Delete)  
✅ Modular Folder Structure  
✅ Follows Modern Best Practices  
✅ Fast, Lightweight, and Easy to Extend  

## 🧩 Project Structure
FastApi/  
│  
├── app/  
│   ├── main.py — Entry point of the app  
│   ├── core/database.py — MongoDB connection setup  
│   ├── models/user_model.py — User schema  
│   ├── models/product_model.py — Product schema  
│   ├── routes/auth_routes.py — Register & Login routes  
│   ├── routes/product_routes.py — CRUD operations for products  
│   ├── schemas/user_schema.py — Pydantic user validation schema  
│   ├── schemas/product_schema.py — Pydantic product validation schema  
│   ├── utils/jwt_handler.py — JWT encode/decode helper  
│   └── __init__.py  
│  
├── .env — Environment variables  
├── .gitignore — Ignore files for git  
├── requirements.txt — Python dependencies  
└── README.md — Project documentation  

## ⚙️ Installation
**1️⃣ Clone the Repository**

**2️⃣ Create a Virtual Environment**

**3️⃣ Install Dependencies**

**4️⃣ Setup Environment Variables**  
Create a `.env` file in the root directory:

**5️⃣ Run the Server**

Your API will run on 👉 http://127.0.0.1:8000  

## 🧠 API Endpoints
### 🔐 Authentication
| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | /auth/register | Register new user |
| POST | /auth/login | Login existing user |

**Example JSON for Register**


{
"username": "muneeb",
"email": "muneeb@example.com
",
"password": "123456"
}



## 🧰 Tech Stack
- FastAPI — Web Framework  
- MongoDB — NoSQL Database  
- Pydantic — Data Validation  
- PyJWT — JSON Web Tokens  
- Bcrypt — Password Hashing  
- Uvicorn — ASGI Server  

## 🧑‍💻 Author
**Muneeb Babar**  
📍 Pakistan  
💼 [GitHub](https://github.com/Muneeb-Babar)

## 📝 License
This project is licensed under the **MIT License** — feel free to use and modify it.

### 🌟 Show your support
If you found this helpful, give it a ⭐ on GitHub!



