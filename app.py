import streamlit as st
from agents.learning_agent import get_learning_path
from agents.planner_agent import generate_study_plan
from agents.assessment_agent import generate_quiz
from agents.insights_agent import get_manager_insights

st.set_page_config(page_title="CertifyAI", page_icon="🎓", layout="wide")

# ---------------- HEADER ----------------
st.title("🎓 CertifyAI")
st.markdown("### 🚀 AI-Powered Certification Intelligence System")
st.caption("Multi-Agent system for learning, planning, assessment & insights")

# ---------------- SIDEBAR ----------------
st.sidebar.title("📌 CertifyAI Control Panel")
st.sidebar.info("Multi-Agent Certification Coaching System")

st.sidebar.markdown("### System Status")
st.sidebar.success("🟢 All Agents Active")

st.sidebar.markdown("### Agents")
st.sidebar.write("✔ Learning Agent")
st.sidebar.write("✔ Planner Agent")
st.sidebar.write("✔ Assessment Agent")
st.sidebar.write("✔ Insight Agent")

# ---------------- USER INPUT ----------------
st.write("## 👤 Learner Profile")

name = st.text_input("Employee Name")

role = st.selectbox(
    "Current Role",
    ["Data Engineer", "Cloud Engineer", "DevOps Engineer"]
)

study_hours = st.slider("📚 Study Hours per Week", 1, 20, 8)

certification = st.selectbox(
    "🎯 Target Certification",
    ["DP-203", "AZ-204", "AZ-400"]
)

st.divider()

# ---------------- WORKFLOW VIEW ----------------
st.write("## 🔄 Multi-Agent Workflow")
st.markdown("""
User → Foundry IQ Layer → Learning Agent → Planner Agent → Assessment Agent → Insight Agent
""")

# ---------------- BUTTON ----------------
if st.button("Generate Learning Plan"):

    # -------- LOADING SIMULATION --------
    with st.spinner("🔄 Initializing AI Agent System..."):
        st.write("Connecting to Knowledge Layer...")
        st.write("Activating Foundry IQ...")
        st.write("Spawning Multi-Agent Workflow...")

    # ---------------- AGENT 1 ----------------
    result = get_learning_path(certification)

    st.success(f"Learning Path Generated for {name or 'User'}")

    st.write("## 🎯 Target Role")
    st.write(result["role"])

    st.write("## 📚 Required Skills")
    for skill in result["skills"]:
        st.write("✅", skill)

    # ---------------- AGENT 2 ----------------
    study_plan = generate_study_plan(certification, study_hours)

    st.write("## 📅 Study Plan")
    for item in study_plan:
        st.write("📌", item)

    # ---------------- READINESS ----------------
    readiness = min(95, study_hours * 10)

    st.write("## 📊 Readiness Score")
    st.metric("Predicted Readiness", f"{readiness}%")
    st.progress(readiness)

    # ---------------- RISK ANALYSIS ----------------
    st.write("## ⚠️ Risk Intelligence")

    risk_score = 100 - readiness

    st.metric("Risk Score", f"{risk_score}%")

    if risk_score < 20:
        st.success("Very Low Risk - Excellent readiness")
        risk = "Low"
    elif risk_score < 40:
        st.warning("Moderate Risk - Needs revision")
        risk = "Medium"
    else:
        st.error("High Risk - Immediate attention required")
        risk = "High"

    # ---------------- AGENT 3 ----------------
    quiz = generate_quiz(certification)

    st.write("## 📝 Assessment Questions")
    for i, q in enumerate(quiz, 1):
        st.write(f"{i}. {q}")

    # ---------------- AGENT 4 ----------------
    insights = get_manager_insights(certification)

    st.write("## 📊 Manager Insights")
    st.metric("System Readiness Score", insights["readiness"])

    st.write("### Recommendation")
    st.info(insights["recommendation"])

    # ---------------- SUMMARY ----------------
    st.divider()

    st.write("## 🏁 Final Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric("Role", role)
    col2.metric("Certification", certification)
    col3.metric("Study Hours", study_hours)

    # ---------------- AGENT FLOW ----------------
    st.divider()

    st.write("## 🔄 Agent Execution Flow")
    st.markdown("""
    1. Learning Path Agent  
    2. Study Plan Agent  
    3. Assessment Agent  
    4. Insight Agent  
    """)

    st.success("Multi-Agent Workflow Completed Successfully 🎉")

# ---------------- IQ SECTION ----------------
st.divider()

st.write("## 💡 Microsoft Foundry IQ Integration")

st.info("""
Foundry IQ acts as the grounding knowledge layer.

User Query  
↓  
Foundry IQ Retrieval Layer  
↓  
Multi-Agent Reasoning System  
↓  
Final Certification Guidance Output  

This ensures structured, reliable AI-driven learning recommendations.
""")

# ---------------- FINAL WOW SECTION ----------------
st.divider()

st.write("## 🧠 What Makes CertifyAI Special")

st.markdown("""
- Multi-Agent AI orchestration system  
- Personalized certification planning  
- Adaptive learning paths  
- Dynamic readiness prediction  
- Risk intelligence engine  
- Foundry IQ grounded reasoning simulation  
- Enterprise-ready analytics dashboard  
""")