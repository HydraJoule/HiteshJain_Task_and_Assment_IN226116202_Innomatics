"""
Pass / Fail Analyzer
This program counts pass and fail students.
"""

def analyze_results():
    marks = [45, 78, 90, 33, 60]

    pass_count = 0
    fail_count = 0

    for mark in marks:
        if mark >= 50:
            pass_count += 1
        else:
            fail_count += 1

    print("Total Students:", len(marks))
    print("Pass Students:", pass_count)
    print("Fail Students:", fail_count)


if __name__ == "__main__":
    analyze_results()
