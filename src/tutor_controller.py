import uuid
from src.tutor_service import TutorService


class TutorController:
    def __init__(self):
        self.tutor_service = TutorService()
    
    def ensure_user_session(self, session):
        """Ensure user has a session ID."""
        if 'user_id' not in session:
            session['user_id'] = str(uuid.uuid4())
        return session['user_id']
    
    def create_session(self, session):
        """Handle chat creation request."""
        user_id = session.get('user_id')
        if not user_id:
            return {'error': 'Session expired'}, 401
        
        session_id = self.tutor_service.create_session(user_id)
        return {
            'session_id': session_id,
            'message': 'Chat created successfully'
        }
    
    def send_query(self, data, session):
        """Handle message sending request."""
        user_id = session.get('user_id')
        session_id = data.get('session_id')
        user_message = data.get('query')
        if not user_id:
            return {'error': 'Session expired'}, 401
        
        if not session_id or not user_message:
            return {'error': 'Missing session_id or message'}, 400
            
        try:
            tutor_response = self.tutor_service.process_query(user_id, session_id, user_message)
            return {'response': tutor_response}
        except ValueError as e:
            return {'error': str(e)}, 404
        except RuntimeError as e:
            return {'error': str(e)}, 500