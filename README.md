🎓 CertifyAI – Multi-Agent Certification Coach
🚀 Overview
CertifyAI is an AI-powered multi-agent certification coaching platform built for the Microsoft Agents League Hackathon (June 2026).

The system helps students and professionals prepare for technical certifications by generating personalized learning paths, assessing readiness levels, forecasting certification success, and providing intelligent study recommendations through a collaborative network of specialized AI agents grounded with Microsoft Foundry IQ.

❗ Problem Statement
Many learners and organizations struggle with certification preparation because:

Scattered Resources: Learning materials, exam objectives, and documentation are fragmented across multiple platforms.

Lack of Personalization: Static study guides do not adapt to an individual's current knowledge base or weekly work schedule.

Manual Tracking: Progress tracking is manual, making it difficult to gauge true exam readiness.

Organizational Blindspots: Management lacks aggregated visibility into team-wide readiness, creating risks for corporate compliance and upskilling goals.

💡 Solution & Microsoft IQ Integration
CertifyAI addresses these challenges by orchestrating a team of intelligent agents. The platform integrates Microsoft Foundry IQ as its core intelligence layer.

┌────────────────────────────────────────────────────────┐
│               Microsoft Foundry IQ Layer               │
│  (Grounded Examination Blueprints & Resource Indices)  │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│                  CertifyAI Core App                    │
│   ┌──────────────────┐        ┌──────────────────┐     │
│   │  Learning Agent  ├───────►│  Planner Agent   │     │
│   └────────┬─────────┘        └────────┬─────────┘     │
│            ▼                           ▼               │
│   ┌──────────────────┐        ┌──────────────────┐     │
│   │ Assessment Agent │        │Team Insights Agt │     │
│   └──────────────────┘        └──────────────────┘     │
└────────────────────────────────────────────────────────┘
By leveraging Foundry IQ, our agents retrieve verified, citation-backed exam objectives and syllabi directly from structured sources. This dramatically minimizes hallucination rates and guarantees that study plans always align with current, official certification standards.

🤖 Multi-Agent Architecture & Reasoning
CertifyAI implements a multi-step reasoning workflow where agents pass context down a cooperative chain:

1. 📘 Learning Agent
Role: Analyzes raw certification requirements from data/certifications.json paired with external Foundry IQ documentation.

Reasoning Pattern: Maps target exam domains against user profiles to recommend hyper-specific study resources and modular milestones.

2. 🗓️ Planner Agent
Role: Contextualizes learning tasks alongside external life factors.

Reasoning Pattern: Cross-references the output of the Learning Agent with data/workload.json (user availability) to calculate dynamic, hour-by-hour weekly preparation calendars.

3. 📝 Assessment Agent
Role: Evaluates knowledge retention and handles certification forecasting.

Reasoning Pattern: Conducts deep skill-gap analysis by tracking mock question performance metrics to project an analytical "Exam Readiness Score %".

4. 📊 Team Insights Agent
Role: Aggregates individual readiness models into high-level metrics.

Reasoning Pattern: Converts personal agent timelines into organizational summaries, flagging team members who are at risk of missing deadlines or needing extra mentoring.

🛠️ Technology Stack
Language: Python

Intelligence Layer: Microsoft Foundry IQ (Grounding & Resource Retrieval)

Application Framework: Streamlit / Python Backend

Data Layer: JSON Data Management (certifications.json, workload.json)

📂 Project Structure
Plaintext

certifyai-multi-agent/
│
├── agents/
│   ├── learning_agent.py      # Core agent logic for path curation
│   ├── planner_agent.py       # Algorithmic scheduler and workload mapper
│   └── [assessment/insights]  # Evaluation and aggregation routines
│
├── data/
│   ├── certifications.json    # Synthetic registry of exam domains
│   └── workload.json          # Synthetic repository tracking student time
│
├── app.py                     # Main execution entry-point and agent broker
├── requirements.txt           # Main project dependencies
├── README.md                  # Comprehensive documentation
└── .gitattributes             # Git configuration
▶️ Installation & Setup
Clone the repository:

Bash

git clone https://github.com/Keerthi8970/certifyai-multi-agent.git
cd certifyai-multi-agent
Install dependencies:

Bash

pip install -r requirements.txt
Configure Environment Variables:
Create a .env file in the root directory and pass your Microsoft Foundry configurations:

Code snippet

FOUNDRY_IQ_ENDPOINT="your-endpoint-here"
FOUNDRY_IQ_API_KEY="your-api-key-here"
Run the application:

Bash

python app.py
🎯 Use Cases
Students: Preparing for structured academic or technical certification exams.

Professionals: Upskilling efficiently for career changes or internal promotions.

Training Teams: Coordinating learning pathways across entire lines of business.

Enterprise Organizations: Mitigating skill gaps by visualizing employee readiness in real time.

🌟 Key Benefits
Personalized Curations: Tailored learning tracks that fit real schedule limits.

Data-Grounded Accuracy: Direct integration with Foundry IQ prevents off-topic or hallucinated study steps.

Data-Driven Foreknowing: Predicts target exam dates based on historical mock score tracking.

Multi-Agent Orchestration: Showcases advanced, enterprise-ready multi-step reasoning capabilities.

🏆 Hackathon Submission
Challenge Track: Reasoning Agents

Hackathon: Microsoft Agents League Hackathon (June 2026)

Project Name: CertifyAI – Multi-Agent Certification Coach

👩‍💻 Author
Keerthi K R

GitHub: @Keerthi8970
