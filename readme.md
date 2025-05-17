# FastAPI Tutorial Projects 🚀

Welcome to the FastAPI learning hub! This repository contains multiple hands-on mini-projects and examples to help you understand and implement FastAPI with various features such as CRUD operations, WebSocket communication, JWT authentication, rate limiting, and more.

---

##
---

## 📦 Requirements
 🧠 Project Structure

FASTAPI/
│
├── Cache/ # Examples using FastAPI caching
├── ChatApp_with_websocket/ # Real-time chat app using WebSockets
├── CRUD_operation_with_db/ # Basic CRUD operations with a database
├── Handle_CRUD_with_JWT/ # CRUD with JWT-based authentication
├── middleware/ # Custom middlewares in FastAPI
├── ratelimiter/ # Rate limiting implementation
│
├── app.log # Application logs
├── readme.md # Documentation (You're reading it!)
├── Rest_API_FastAPI.py # Basic REST API example with FastAPI
├── Restapi_mysql.py # REST API using FastAPI and MySQL
└── test_Rest_API_with_pytest.py # Pytest-based testing for FastAPI


To get started, install the dependencies:

```bash
pip install -r requirements.txt
If not available, install FastAPI and Uvicorn manually:


pip install fastapi uvicorn python-multipart pymysql python-jose
🚀 Running the Server
Use Uvicorn to run any of the scripts. For example:


uvicorn Rest_API_FastAPI:app --reload
Or for MySQL integration:


uvicorn Restapi_mysql:app --reload
🛠️ Features Covered
✅ Basic REST API

✅ Database integration with SQL (e.g., MySQL)

✅ CRUD operations

✅ JWT Authentication & Authorization

✅ Middleware usage

✅ WebSocket (Real-time communication)

✅ Caching support

✅ Rate Limiting

✅ Testing using Pytest

🧪 Running Tests

pytest test_Rest_API_with_pytest.py
🧑‍💻 Author
Nitesh Upadhyay
📧 upadhyay02nitesh@gmail.com
🔗 GitHub

📜 License
This project is open-source and available under the MIT License.

Happy coding with FastAPI! 🎉
