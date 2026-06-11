def generate_quiz(certification):

    quizzes = {
        "DP-203": [
            "What is Azure Data Factory?",
            "What is ETL?",
            "What is Databricks?"
        ],
        "AZ-204": [
            "What is an Azure Function?",
            "What is REST API?",
            "What is Azure Storage?"
        ],
        "AZ-400": [
            "What is CI/CD?",
            "What is Docker?",
            "What is Kubernetes?"
        ]
    }

    return quizzes.get(certification, [])