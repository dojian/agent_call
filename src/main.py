from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware
from src.tutor_controller import TutorController
import uvicorn

# Initialize the FastAPI application
app = FastAPI(title="Personal Tutor API")

# Add session middleware
app.add_middleware(
    SessionMiddleware,
    secret_key="your_secret_key_here"
)

# Create controller instance
tutor_controller = TutorController()


# Define a route for the index page that ensures a user session
@app.get("/")
async def index(request: Request):
    # Ensure user has a session
    tutor_controller.ensure_user_session(request.session)
    return "Welcome to the Personal Tutor Service!"


# Define a route for creating a new tutoring session
@app.post("/api/create_session")
async def create_session(request: Request):
    tutor_controller.ensure_user_session(request.session)
    # Handle tutoring session creation request
    return tutor_controller.create_session(request.session)


# TODO: Define a route for sending a query in an existing tutoring session
# - Create a POST endpoint at '/api/send_query'
# - Parse the JSON request body using 'await request.json()'
# - Pass the session and parsed data to tutor_controller.send_query
# - Return the response from the controller
@app.post("/api/send_query")
async def send_query(request: Request):
    tutor_controller.ensure_user_session(request.session)
    data = await request.json()
    return tutor_controller.send_query(data,request.session)

# Run the server
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=3000,
        reload=True
    )