"""
Message Length Analyzer
This program checks message length and flags long messages.
"""

def analyze_messages():
    messages = ["Hi", "Welcome to the platform", "OK"]

    for message in messages:
        length = len(message)
        print(f"Message: '{message}' | Length: {length}")

        if length > 10:
            print("Status: Long Message")


if __name__ == "__main__":
    analyze_messages()
