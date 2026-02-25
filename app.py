import streamlit as st
import joblib
import ollama
from rag_engine import retrieve_solution
from automation_engine import handle_automation
import numpy as np
from logger import log_ticket
import pandas as pd
import os
# -----------------------------
# Load ML Model & Vectorizer
# -----------------------------
@st.cache_resource
def load_models():
    model = joblib.load("models/classifier.pkl")
    vectorizer = joblib.load("models/vectorizer.pkl")
    return model, vectorizer

model, vectorizer = load_models()

st.set_page_config(page_title="AutoResolveAI", layout="wide")

st.title("AutoResolveAI - Support Automation Agent")

st.markdown("Simulating AI-powered enterprise ticket automation.")

ticket = st.text_area("Enter Support Ticket")

# -----------------------------
# Analyze Button
# -----------------------------
if st.button("Analyze"):

    if ticket.strip() == "":
        st.warning("Please enter a support ticket.")
        st.stop()

    # -----------------------------
    # Step 1: Classification
    # -----------------------------
    vec = vectorizer.transform([ticket])
    prediction = model.predict(vec)[0]
    probabilities = model.predict_proba(vec)
    confidence = np.max(probabilities)

    st.subheader("Predicted Issue Type:")
    st.write(f"**{prediction}**")
    st.write(f"Confidence: {round(confidence * 100, 2)}%")

    # -----------------------------
    # Step 2: RAG Retrieval
    # -----------------------------
    solution = retrieve_solution(ticket)

    st.subheader("Retrieved Solution:")
    st.write(solution)

    # -----------------------------
    # Step 3: LLM Explanation
    # -----------------------------
    st.subheader("AI Explanation:")

    with st.spinner("Generating AI explanation using phi3..."):
        try:
            response = ollama.chat(
                model='phi3',
                messages=[
                    {
                        "role": "system",
                        "content": "You are an enterprise logistics AI support assistant."
                    },
                    {
    "role": "user",
    "content": f"""
Ticket:
{ticket}

Predicted Issue:
{prediction}

Suggested Fix:
{solution}

Write a professional customer response email.
Sign off with:

Sincerely,
Dhanasree Gidijala
Applied AI Support Engineer
"""
}
                ]
            )

            explanation = response['message']['content']
            st.write(explanation)

        except Exception as e:
            st.error(f"LLM Error: {e}")
            st.stop()

    # -----------------------------
    # Step 4: Automation / Escalation
    # -----------------------------
    st.subheader("Automation Result:")

    if confidence > 0.60:
        action_result = handle_automation(prediction, ticket)
        st.success(action_result)

        log_ticket(
            ticket,
            prediction,
            confidence,
            action_result,
            status="Automated"
        )
    else:
        st.warning("Low confidence prediction. Escalated to human support.")

        log_ticket(
            ticket,
            prediction,
            confidence,
            result="Escalated to human support",
            status="Escalated"
        )

# -----------------------------
# Logs Dashboard
# -----------------------------
st.subheader("Active Ticket Logs")

log_path = "data/active_log.csv"

if os.path.exists(log_path):
    logs = pd.read_csv(log_path)
    st.dataframe(logs.tail(10))
else:
    st.write("No logs available yet.")