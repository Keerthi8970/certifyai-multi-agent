def get_manager_insights(certification):

    insights = {
        "DP-203": {
            "readiness": "78%",
            "risk": "Medium",
            "recommendation": "Focus on Databricks and Data Pipelines"
        },
        "AZ-204": {
            "readiness": "82%",
            "risk": "Low",
            "recommendation": "Practice Azure Functions and Authentication"
        },
        "AZ-400": {
            "readiness": "75%",
            "risk": "Medium",
            "recommendation": "Improve Kubernetes knowledge"
        }
    }

    return insights.get(certification, {})