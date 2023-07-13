from datetime import datetime

class GreetUser:
    def greet_user():
        time = datetime.now()
        current_hour = time.hour

        if 5 <= current_hour < 12:
            return "Good morning...\nWelcome to linkify, a program that shortens your URLs making them easier to share."
        elif 12 <= current_hour < 18:
            return "Good afternoon...\nWelcome to linkify, a program that shortens your URLs making them easier to share."
        else:
            return "Good evening...\nWelcome to linkify, a program that shortens your URLs making them easier to share."
        