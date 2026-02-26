SpashtaAI – System Architecture Overview
1. High-Level Architecture

SpashtaAI follows a multi-agent, explainability-first architecture designed for safe and transparent clinical reasoning visualization.

The system consists of the following layers:

User Interface Layer (Streamlit Web App)

Orchestration Layer (AWS Lambda)

Reasoning & RAG Layer (Amazon Bedrock + Embeddings)

Knowledge Storage Layer (Amazon S3)

Metadata & Governance Layer (Amazon DynamoDB + CloudWatch)

2. Component Breakdown
User Interface Layer

Streamlit-based web application

Accepts synthetic clinical input

Displays structured Reason Graphs

Shows confidence bands and traceability

Enforces educational-only disclaimer

Orchestration Layer

AWS Lambda functions coordinate:

Concept extraction

RAG retrieval

Model invocation

Safety validation

Confidence calibration

RAG & Explainability Layer

Clinical text input is received.

Relevant public guideline documents are retrieved from S3.

Amazon Titan Embeddings generate vector representations.

Similar documents are retrieved via similarity search.

Claude 3 Sonnet (via Amazon Bedrock) generates a grounded explanation.

A structured Reason Graph is constructed.

Confidence bands are assigned based on retrieval strength.

Safety Monitor Layer

Before output is displayed:

The response is scanned for prohibited medical advisory content.

If diagnostic or treatment advice is detected:

Output is blocked.

Disclaimer is displayed.

Event is logged in CloudWatch.

Data Storage

Public medical guidelines → Amazon S3

Embedding index → Generated dynamically via Bedrock

Explanation metadata & traceability → Amazon DynamoDB

Audit logs & safety events → Amazon CloudWatch

No patient-identifiable information is used.

3. Deployment Architecture (AWS)

SpashtaAI prototype will be deployed using:

Amazon EC2 (Streamlit hosting)

AWS Lambda (orchestration)

Amazon Bedrock (Claude 3 Sonnet + Titan Embeddings)

Amazon S3 (knowledge base)

Amazon DynamoDB (metadata & confidence tracking)

Amazon CloudWatch (audit & monitoring)

This architecture ensures scalability, security, and responsible AI governance.

4. Architectural Principles

Explainability-First Design

Retrieval-Grounded Generation (RAG)

Safety Boundary Enforcement

Confidence Calibration (qualitative bands)

Synthetic/Public Data Only

Cloud-Native and Scalable

5. Innovation Highlights

Structured Reason Graph generation instead of simple text output

Confidence band mapping instead of raw probabilities

Mandatory safety validation gate

Governance-ready architecture for healthcare AI
