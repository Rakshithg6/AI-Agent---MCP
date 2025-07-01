from collections import defaultdict
session_memory = defaultdict(list)
def get_session_history(session_id):
    return session_memory[session_id]

def update_session_history(session_id,user_input, bot_response):
    session_memory[session_id].append((user_input,bot_response))