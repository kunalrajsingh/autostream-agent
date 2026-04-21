def detect_intent(text):
    text = text.lower()

    if any(x in text for x in ["hi", "hello", "hey"]):
        return "greeting"

    elif any(x in text for x in ["buy", "subscribe", "sign up", "try", "start", "i want"]):
        return "high_intent"

    elif any(x in text for x in ["price", "cost", "plan", "feature"]):
        return "query"

    return "query"