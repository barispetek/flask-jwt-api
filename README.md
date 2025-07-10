# Flask JWT REST API

This is a simple RESTful API built with Flask, PostgreSQL, and JWT authentication.  
It supports user registration, login, and CRUD operations for blog posts.

---

## 🚀 Features

- User registration & login (JWT based)
- Token authentication (access control)
- PostgreSQL integration
- RESTful endpoints
- Dockerized setup (Docker + docker-compose)
- Tested with Postman

---

## 📦 Technologies Used

- Python 3.11
- Flask
- Flask-JWT-Extended
- SQLAlchemy
- PostgreSQL
- Docker & Docker Compose

---

## ⚙️ Installation

### Clone the repo
```bash
git clone https://github.com/barisdev/flask-jwt-api.git
cd flask-jwt-api
```

```env
#Environment variables
#Create a .env file in the root directory
POSTGRES_DB=jwt_api
POSTGRES_USER=youruser
POSTGRES_PASSWORD=yourpassword
POSTGRES_HOST=db
POSTGRES_PORT=5432
JWT_SECRET_KEY=your-secret-key
```

```bash
#Build & Run with Docker
docker-compose up --build
```

## 📮 API Endpoints

```text

Method   Endpoint             Description
------   -------------------  -------------------------
POST     /api/auth/register   Register a new user
POST     /api/auth/login      Login and get token
GET      /api/posts/          Get all posts
GET      /api/posts/<id>      Get post by ID
POST     /api/posts/          Create new post (auth required)
PUT      /api/posts/<id>      Update post (auth required)
DELETE   /api/posts/<id>      Delete post (auth required)
```
 
🧪 Testing
Use Postman to test the API.

Set Authorization header as Bearer <access_token> for protected routes.





