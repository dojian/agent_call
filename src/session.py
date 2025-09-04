class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self,user_id,session_id,system_prompt):
        """create a new session for a user with a system prompt."""
        if user_id not in self.sessions:
            self.sessions[user_id] = {}
        self.sessions[user_id][session_id] = {
            'system_prompt': system_prompt,
            'messages':[]
        }
        
    def get_session(self,user_id,session_id):
        """Retrieve a session by user_id and session_id."""
        return self.sessions.get(user_id,{}).get(session_id,None)
    
    def add_message(self, user_id, session_id, role, content):
        """Add a message to a session."""
        if session := self.get_session(user_id, session_id):
            session['messages'].append({"role": role, "content": content})
            
    def get_conversation(self, user_id, session_id):
        """Get the full conversation history for a session."""
        
        if session := self.get_session(user_id, session_id):
            return [ 
                {'role':'system','content':session['system_prompt']}
            ] + session['messages']
        return []