# Job-Match-Platform
This is the backend API service for an AI-driven job recommendation platform. Built with FastAPI, it handles user authentication, profile management, job listing storage, and integrates with OpenRouter’s LLaMA 3.3 8B model to generate personalized job recommendations.

⚙️ Tech Stack
FastAPI – High-performance web framework

PostgreSQL – Relational database

SQLAlchemy / Tortoise ORM – Database ORM

JWT (PyJWT) – Secure token-based authentication

OpenRouter API (LLaMA 3.3 8B) – AI recommendation engine

🚀 Features
🔐 Authentication

Register, login, and logout

JWT-based auth

👤 User Profile Management

Create, retrieve, update, delete profiles

💼 Job Listings

Add, retrieve, and browse job data

🤖 AI-Powered Recommendations

Fetch job recommendations tailored to the user using OpenRouter’s LLaMA 3.3

📁 Project Structure
bash
Copy
Edit
backend/
├── main.py               # FastAPI entry point
├── models/               # ORM models (users, jobs, profiles)
├── schemas/              # Pydantic request/response schemas
├── routes/               # Route handlers
│   ├── auth.py
│   ├── users.py
│   └── ai.py
├── services/             # Business logic and database helpers
├── ai/
│   └── recommender.py    # AI integration via OpenRouter
├── utils/
│   └── security.py       # JWT handling and password hashing
├── tests/                # Backend unit and integration tests
└── requirements.txt
🔌 AI Integration with OpenRouter
Located in ai/recommender.py

Uses httpx or requests to send prompts to OpenRouter API

Constructs a prompt from user profile and job descriptions

Returns ranked job matches

🔐 Environment Variables
Create a .env file in the backend root:

env
Copy
Edit
DATABASE_URL=postgresql://user:password@localhost:5432/jobmatch
JWT_SECRET=your_jwt_secret_key
OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_MODEL=meta-llama-3-8b-instruct
🧪 Running Locally
1. Clone & Install
bash
Copy
Edit
git clone https://github.com/yourusername/jobmatch-backend.git
cd jobmatch-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
2. Run FastAPI Server
bash
Copy
Edit
uvicorn main:app --reload
3. Access API Docs
Visit http://localhost:8000/docs for Swagger UI.

🧪 Testing
bash
Copy
Edit
pytest tests/
Use mocks for OpenRouter responses during testing (unittest.mock or pytest-mock).

🛰️ Deployment Notes
Use Render, Railway, or Docker for backend deployment.

Ensure all secrets are set as environment variables in production.

Set CORS settings appropriately for frontend domain access.

📎 Example API Usage
POST /recommend
json
Copy
Edit
{
  "user_id": "123",
  "job_ids": ["job1", "job2", "job3"]
}
Returns:

json
Copy
Edit
{
  "recommended_jobs": ["job2", "job3", "job1"]
}
📚 License
MIT License – Feel free to use and modify.

Let me know if you’d like this as a downloadable README.md file or adapted for Docker support or database migrations (e.g., with Alembic).








