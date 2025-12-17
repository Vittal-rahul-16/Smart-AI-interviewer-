# ==============================
# Importing Libraries
# ==============================

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
import streamlit as st
from pypdf import PdfReader
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="langchain")

# ==============================
# Initialize Local AI Model
# ==============================

llm = ChatOllama(model="llama3")

# ==============================
# App Title
# ==============================

st.title("Smart AI Interviewer")

# ==============================
# Greeting Test
# ==============================

response = llm.invoke([
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Say Hello to me")
])
st.write(response.content)

# ==============================
# File Upload (TXT + PDF)
# ==============================

st.write("### Upload your resume and job description to begin:")

resume_file = st.file_uploader(
    "Upload your Resume (.txt or .pdf)",
    type=["txt", "pdf"]
)

jd_file = st.file_uploader(
    "Upload Job Description (.txt or .pdf)",
    type=["txt", "pdf"]
)

# ==============================
# File Reader Function
# ==============================

def read_file(file):
    if file.type == "text/plain":
        return file.read().decode("utf-8")

    elif file.type == "application/pdf":
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

# ==============================
# Main Logic
# ==============================

if resume_file and jd_file:

    resume_text = read_file(resume_file)
    jd_text = read_file(jd_file)

    # ==============================
    # AGENT 1: Resume & JD Parser
    # ==============================

    st.subheader("Resume & JD Parsing")
    st.markdown("""
    **Purpose:**
    - Extract key skills
    - Highlight experiences
    - Identify JD requirements
    """)

    parser_prompt = [
        SystemMessage(content="You are a Resume & JD Parsing Agent. Extract structured information."),
        HumanMessage(content=f"""
        Resume:
        {resume_text}

        Job Description:
        {jd_text}

        Tasks:
        1. Extract 5–7 core skills from the resume
        2. Mention 3 key job experiences
        3. Extract 5 required JD competencies
        4. Use bullet points
        """)
    ]

    with st.spinner("Parsing resume and job description..."):
        parse_response = llm.invoke(parser_prompt)

    st.text_area("Parsed Summary", parse_response.content, height=300)

    # ==============================
    # AGENT 2: Interview Question Generator
    # ==============================

    st.subheader("Interview Question Generator")

    question_prompt = [
        SystemMessage(content="You are an Interview Question Generator Agent."),
        HumanMessage(content=f"""
        Generate 10 interview questions using the resume and job description.

        - Mix Technical, Behavioral, Situational
        - Tag each question
        - Make them job-relevant

        Resume:
        {resume_text}

        Job Description:
        {jd_text}
        """)
    ]

    with st.spinner("Generating interview questions..."):
        question_response = llm.invoke(question_prompt)

    st.text_area("Interview Questions", question_response.content, height=300)

    # ==============================
    # AGENT 3: Mock Interview Feedback
    # ==============================

    st.subheader("Mock Interview Feedback")

    user_answer = st.text_area("Type your answer to any one question:")

    if st.button("Get Feedback") and user_answer.strip():
        feedback_prompt = [
            SystemMessage(content="You are an Interview Feedback Agent."),
            HumanMessage(content=f"""
            Candidate Answer:
            {user_answer}

            Tasks:
            1. Score out of 10
            2. Strengths & weaknesses
            3. Rewrite using STAR method
            """)
        ]

        with st.spinner("Analyzing your answer..."):
            feedback_response = llm.invoke(feedback_prompt)

        st.text_area("AI Feedback", feedback_response.content, height=300)

    # ==============================
    # AGENT 4: Job Suitability Score
    # ==============================

    st.subheader("Job Suitability Score")

    if st.button("Check My Job Match Score"):
        match_prompt = [
            SystemMessage(content="You are a Job Match Evaluation Agent."),
            HumanMessage(content=f"""
            Resume:
            {resume_text}

            Job Description:
            {jd_text}

            Tasks:
            1. Match score out of 100%
            2. 2–3 strengths
            3. 2–3 gaps
            4. Final recommendation
            """)
        ]

        with st.spinner("Evaluating job fit..."):
            match_response = llm.invoke(match_prompt)

        st.text_area("Job Fit Report", match_response.content, height=300)

else:
    st.warning("Please upload both Resume and Job Description to continue.")
