def generate_study_plan(certification, study_hours):

    if study_hours < 5:
        duration = "8 Weeks"
    elif study_hours < 10:
        duration = "6 Weeks"
    else:
        duration = "4 Weeks"

    return [
        f"Duration: {duration}",
        "Learn Fundamentals",
        "Practice Labs",
        "Mock Tests",
        "Final Revision"
    ]