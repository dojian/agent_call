# Personal Tutor API

A FastAPI-based personal tutoring service powered by DeepSeek AI, designed to provide interactive educational assistance through conversational AI.

## Overview

This project implements a RESTful API for a personal tutor service that:
- Manages user sessions and conversation history
- Integrates with DeepSeek AI for intelligent tutoring responses
- Provides personalized learning experiences
- Supports multiple tutoring sessions per user

## Project Structure

```
src/
├── main.py              # FastAPI application entry point
├── tutor_controller.py  # Request handling and session management
├── tutor_service.py     # AI integration and business logic
├── session.py           # Session management utilities
└── README.md           # This file
```

### File Descriptions

- **main.py**: The main FastAPI application with route definitions and server configuration
- **tutor_controller.py**: Handles HTTP requests, manages user sessions, and coordinates with the tutor service
- **tutor_service.py**: Contains the core tutoring logic, AI client integration, and session processing
- **session.py**: Manages conversation history and session state for users

## Dependencies

- `fastapi` - Web framework for building APIs
- `uvicorn` - ASGI server for running FastAPI
- `openai` - Client for interacting with DeepSeek AI
- `python-dotenv` - Environment variable management
- `starlette` - ASGI toolkit (used for session middleware)

## Environment Setup

1. Create a `.env` file in the project root with the following variables:
   ```
   DEEPSEEK_API_KEY=your_deepseek_api_key_here
   DEEPSEEK_URL=your_deepseek_base_url_here
   ```

2. Ensure the `data/system_prompt.txt` file exists with the tutor persona configuration.

## Installation

1. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

2. Activate the virtual environment:
   ```bash
   poetry shell
   ```

## Running the Application

Start the development server:
```bash
python src/main.py
```

The API will be available at `http://localhost:3000`

## API Endpoints

### GET /
Returns a welcome message and ensures user session exists.

**Response:**
```json
"Welcome to the Personal Tutor Service!"
```

### POST /api/create_session
Creates a new tutoring session for the authenticated user.

**Response:**
```json
{
  "session_id": "uuid-string",
  "message": "Chat created successfully"
}
```

### POST /api/send_query
Sends a query to the tutor in an existing session.

**Request Body:**
```json
{
  "session_id": "uuid-string",
  "query": "What is machine learning?"
}
```

**Response:**
```json
{
  "response": "Machine learning is a subset of artificial intelligence..."
}
```

## Usage Examples

### Creating a Session
```bash
curl -X POST http://localhost:3000/api/create_session
```

### Sending a Query
```bash
curl -X POST http://localhost:3000/api/send_query \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "your-session-id",
    "query": "Explain quantum physics"
  }'
```

## Session Management

- User sessions are managed automatically using cookies
- Each user can have multiple tutoring sessions
- Conversation history is maintained per session
- Sessions persist conversation context for coherent tutoring

## AI Integration

The service integrates with DeepSeek AI using:
- Model: `deepseek-chat`
- Temperature: 0.7 (balanced creativity and coherence)
- Max tokens: 500 per response
- System prompt loaded from `data/system_prompt.txt`

## Error Handling

The API includes comprehensive error handling for:
- Session expiration (401)
- Missing parameters (400)
- Session not found (404)
- AI service failures (500)

## Development

### Code Structure
- **Controller Layer**: `TutorController` handles HTTP requests and responses
- **Service Layer**: `TutorService` manages business logic and AI integration
- **Data Layer**: `SessionManager` handles session storage and conversation history

### Testing
Run the application and test endpoints using tools like:
- curl
- Postman
- FastAPI's interactive documentation at `/docs`

## Configuration

Key configuration options in `main.py`:
- Server host: `0.0.0.0`
- Server port: `3000`
- Session secret key: Configure in production
- AI model parameters: Adjustable in `tutor_service.py`

## Security Notes

- Session management uses secure cookies
- API keys are loaded from environment variables
- Input validation is implemented for all endpoints
- Error messages avoid exposing sensitive information

## Future Enhancements

- User authentication and authorization
- Database integration for persistent sessions
- Rate limiting and API throttling
- Advanced tutoring features (quizzes, progress tracking)
- Multi-language support
