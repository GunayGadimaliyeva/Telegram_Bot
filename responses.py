from datetime import datetime

def sample_responses(text):
    user_message = str(text).lower()

    if user_message in ('hello', 'hi', 'sup',):
        return "Hey! How's it going?"

    if user_message in ('who are you', 'who are you?'):
        return "I am TECHNEST BOT!"

    if user_message in ('', 'who are you?'):
        return "I am TECHNEST BOT!"
    
    return "I dont't understand you"
            