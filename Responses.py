from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "wassup", "sup"):
        return "Hey! How's it going?"

    if user_message in ("who are you", "who is you", "who are you?", "who r u"):
        return "I am testbot 1 !!!"

    if user_message in ("time"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M%S")

        return str(date_time)

    return "I don't understand you"