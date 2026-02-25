--> AutoResolveAI – AI-Powered Support Automation Agent

          An applied AI system that simulates enterprise-grade customer support automation for logistics platforms.
          
          This project demonstrates how traditional ML, Retrieval-Augmented Generation (RAG), and LLM-based response generation can be combined to automate customer ticket resolution while maintaining                  reliability and explainability.

--> Problem Statement

Enterprise logistics companies receive thousands of support tickets daily related to:

     Shipment tracking
     
     Payment disputes
     
     API failures
     
     Delivery delays

     Warehouse synchronization issues

Manual handling of these tickets:

     Increases SLA risk
     
     Slows resolution time
     
     Reduces customer satisfaction
     
     Increases operational costs

AutoResolveAI simulates how AI can:

     Classify tickets
     
     Suggest resolutions
     
     Generate professional responses
     
     Execute automated actions
     
     Log all activities for monitoring

--> System Architecture
     User Ticket
          ↓
     ML Classification (Logistic Regression)
          ↓
     RAG-based Suggested Resolution
          ↓
     LLM (Phi-3 via Ollama) → Customer Email Generation
          ↓
     Deterministic Automation Execution
          ↓
     Structured Logging (CSV-based)
          ↓
     Dashboard Display
--> Key Components
1️. Ticket Classification

     File: 
     
     ticket_classifier
     
     TF-IDF Vectorization
     
     Logistic Regression
     
     Confidence-based automation threshold
     
     Synthetic enterprise dataset

2️. Synthetic Data Generator

     File: 
     
     generate_data
     
     Generates realistic enterprise-style tickets with:
     
     Client names
     
     Shipment IDs
     
     Locations
     
     SLA delays
     
     API failures

3️. RAG Engine (Knowledge Retrieval)

     File: 
     
     rag_engine
     
     Uses sentence-transformers
     
     FAISS similarity search
     
     Retrieves best-matching resolution template

4️. Automation Engine

     File: 
     
     automation_engine
     
     Maps issue type → automated action:
     
     restart_sync()
     
     refund_payment()
     
     retrigger_api()
     
     update_eta()
     
     resync_inventory()
     
     Includes dynamic ID extraction from ticket text.

5️. LLM-Powered Response Generation

     Inside: 
     
     app
     
     Uses:
     
     Ollama
     
     Phi-3 model
     
     Generates professional customer-facing email responses signed as:
     
     Dhanasree Gidijala

6️. Structured Logging System

     File: 
     
     logger
     
     Logs every ticket into:
     
     data/active_log.csv

Captures:

     Timestamp
     
     Ticket text
     
     Predicted issue
     
     Confidence
     
     Automation result
     
     Status (Automated / Escalated)
     
     Displayed in dashboard for monitoring.

--> Web Interface

     File: 
     
     app

Built with:

     Streamlit
     
     Interactive dashboard
     
     Live automation logs table
     
     Confidence-based escalation

--> Installation & Setup
     1️. Clone Repository
     git clone https://github.com/GDhanasree/AutoResolveAI.git
     cd AutoResolveAI
     2️. Create Virtual Environment
     python -m venv venv
     venv\Scripts\activate
     3️. Install Dependencies
     pip install -r requirements.txt

Requirements file: 

     requirements

4️. Install Ollama

Download from:

https://ollama.com

Pull lightweight model:

ollama pull phi3
5️. Generate Dataset
python generate_data.py
6️. Train Classifier
python ticket_classifier.py
7️. Run Application
streamlit run app.py

--> Features

     ML-based ticket classification
     Confidence-based automation threshold
     RAG-powered solution suggestion
     LLM-generated professional email responses
     Deterministic automation execution
     Structured logging for audit & analytics
     Interactive Streamlit dashboard

--> Design Philosophy

     This system intentionally uses a hybrid deterministic architecture:
     
     ML decides issue type
     
     Automation mapping is controlled
     
     LLM generates explanation only
     
     Logging ensures auditability

This improves:

     Reliability
     
     Explainability
     
     Production stability
     
     Enterprise readiness

--> Future Improvements

     SLA breach risk prediction
     
     Automation success rate metrics dashboard
     
     Escalation analytics
     
     Multi-agent routing
     
     FastAPI backend separation
     
     Real database (PostgreSQL) instead of CSV
     
     Real API integration

--> What This Project Demonstrates

     Applied ML in production workflows
     
     Hybrid AI system design
     
     LLM integration using local models
     
     Automation reliability trade-offs
     
     Enterprise CX engineering thinking

     Observability via logging

