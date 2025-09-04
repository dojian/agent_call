import uuid
from openai import OpenAI
from src.session import SessionManager
from dotenv import load_dotenv
import os

load_dotenv()
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
deepseek_base_url = os.getenv("DEEPSEEK_URL")

class TutorService:
    def __init__(self):
        self.session_manager = SessionManager()
        # TODO: Initialize the client to interact with the AI model
        self.client = OpenAI(api_key= deepseek_api_key, base_url= deepseek_base_url)
        self.system_prompt = self.load_system_prompt('data/system_prompt.txt')

    def load_system_prompt(self, file_path: str) -> str:
        """Load the system prompt from file."""
        try:
            with open(file_path, 'r') as f:
                return f.read()
        except Exception as e:
            print(f"Error loading system prompt: {e}")
            return "You are a helpful tutor."

    def create_session(self, student_id: str) -> str:
        """Create a new tutoring session."""
        session_id = str(uuid.uuid4())
        self.session_manager.create_session(student_id, session_id, self.system_prompt)
        return session_id
        
    def process_query(self, student_id: str, session_id: str, query: str) -> str:
        """Process a student query and get AI response."""
        session = self.session_manager.get_session(student_id, session_id)
        if not session:
            raise ValueError("Session not found")

        # Add student query
        self.session_manager.add_message(student_id, session_id, "user", query)

        try:
            # TODO: Retrieve the conversation using the SessionManager
            history = self.session_manager.get_conversation(student_id, session_id)
            # TODO: Use the DeepSeek client to generate a response based on the conversation
            # - Set the model to "deepseek-ai/deepseek-V3"
            # - Pass the conversation as the messages parameter to provide context
            # - Use a temperature of 0.7 to balance creativity and coherence in responses
            # - Limit the response length to 500 tokens
            response = self.client.chat.completions.create(
                model = "deepseek-chat",
                messages = history,
                temperature = 0.7,
                max_tokens = 500
            )
            
            # TODO: Extract the AI's response from the DeepSeek client response
            answer = response.choices[0].message.content.strip()
            # TODO: Add the AI's response to the session history
            self.session_manager.add_message(student_id, session_id,"assistant",answer)
            # TODO: Return the AI's response
            return answer
        except Exception as e:
            # TODO: Handle exceptions and raise a RuntimeError with an appropriate message
            raise RuntimeError(f"AI's response failed：{str(e)}")