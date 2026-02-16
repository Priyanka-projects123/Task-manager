from datetime import datetime


VALID_PRIORITIES = ["High", "Medium", "Low"]
VALID_CATEGORIES = ["Work", "Personal", "Study", "General"]


def validate_required(value, field_name):
    if not value.strip():
        print(f"{field_name} is required.")
        return False
    return True


def validate_priority(priority):
    if priority not in VALID_PRIORITIES:
        print("Invalid priority! Choose High, Medium, or Low.")
        return False
    return True


def validate_category(category):
    if category not in VALID_CATEGORIES:
        print("Invalid category! Choose from:", ", ".join(VALID_CATEGORIES))
        return False
    return True


def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        print("Invalid date format! Use YYYY-MM-DD.")
        return False


def validate_index(index, tasks):
    if index < 0 or index >= len(tasks):
        print("Invalid task number!")
        return False
    return True
