"""
Error Message Detector
This program counts ERROR entries in logs.
"""

def detect_errors():
    logs = ["INFO", "ERROR", "WARNING", "ERROR"]

    error_count = 0

    for log in logs:
        if log == "ERROR":
            error_count += 1

    print("Total ERROR entries:", error_count)


if __name__ == "__main__":
    detect_errors()
