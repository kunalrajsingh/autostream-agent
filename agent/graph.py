from agent.intent import detect_intent
from agent.rag import retrieve_answer
from agent.tools import mock_lead_capture

# LangChain-style Agent Wrapper
class SimpleAgent:
    def __init__(self, kb):
        self.kb = kb

    def run(self, state, user_input):

        state["messages"].append(user_input)

        # Lead collection flow
        if state["stage"] == "collect_name":
            state["name"] = user_input
            state["stage"] = "collect_email"
            return "Please provide your email."

        if state["stage"] == "collect_email":
            state["email"] = user_input
            state["stage"] = "collect_platform"
            return "Which platform do you create content on?"

        if state["stage"] == "collect_platform":
            state["platform"] = user_input

            mock_lead_capture(
                state["name"],
                state["email"],
                state["platform"]
            )

            state["stage"] = "done"
            return "You're all set! We'll contact you."

        # Intent detection
        intent = detect_intent(user_input)
        state["intent"] = intent

        if intent == "greeting":
            return "Hi! Welcome to AutoStream 🎬"

        if intent == "query":
            return retrieve_answer(user_input, self.kb)

        if intent == "high_intent":
            state["stage"] = "collect_name"
            return "Great! What's your name?"

        return "I can help with AutoStream pricing and features."