import json

def get_learning_path(certification):

    data = {
        "DP-203": {
            "role": "Data Engineer",
            "skills": ["Python", "SQL", "Azure Data Factory", "Databricks"]
        },
        "AZ-204": {
            "role": "Cloud Engineer",
            "skills": ["Azure Functions", "APIs", "Storage", "Security"]
        },
        "AZ-400": {
            "role": "DevOps Engineer",
            "skills": ["Git", "CI/CD", "Docker", "Kubernetes"]
        }
    }

    return data[certification]