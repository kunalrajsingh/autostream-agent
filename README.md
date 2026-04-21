# Social-to-Lead Agentic Workflow (AutoStream)

---
 ▶️ How to Run the Project Locally

1. Clone the repository:

```bash
git clone https://github.com/kunalrajsingh/autostream-agent.git
cd autostream-agent
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate it:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the application:

```bash
python app.py
```

---

🧠 Architecture Explanation

This system is designed using a LangGraph-inspired agentic workflow, where the conversation is structured into distinct steps such as intent detection, retrieval (RAG), and tool execution. LangGraph-style design was chosen because it enables modular and controlled flow management, allowing the agent to make decisions based on user intent rather than responding statically like a traditional chatbot.

The workflow begins with intent detection, which classifies user input into greeting, query, or high intent. For informational queries, the system uses a JSON-based knowledge base to retrieve accurate responses (RAG). When high intent is detected, the agent transitions into a lead collection stage.

State is managed using a centralized dictionary that persists across multiple turns. This state stores conversation history, detected intent, and user-provided details such as name, email, and platform. This enables multi-turn interaction and ensures that the lead capture tool is executed only after all required information is collected, maintaining a structured and reliable workflow.

📲 WhatsApp Integration (Using Webhooks)

To integrate this agent with WhatsApp, the WhatsApp Business API can be used along with a backend server (Flask or FastAPI) that acts as a webhook endpoint.

When a user sends a message on WhatsApp, the message is forwarded to the webhook. The backend receives this request, extracts the user message, and passes it to the agent for processing. The agent performs intent detection, retrieves relevant information, or executes actions such as lead capture.

The generated response is then sent back to the user via the WhatsApp API. User state can be maintained using the phone number as a unique identifier, allowing the system to handle multi-turn conversations seamlessly and convert interactions into qualified leads in real time.
