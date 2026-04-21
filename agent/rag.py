import json

def load_kb():
    with open("data/knowledge.json", "r") as f:
        return json.load(f)


def retrieve_answer(query, kb):
    query = query.lower()

    if any(x in query for x in ["price", "pricing", "plan", "cost"]):
        basic = kb["pricing"]["basic"]
        pro = kb["pricing"]["pro"]

        return f"""
🎬 AutoStream Pricing:

🔹 Basic Plan
- Price: {basic["price"]}
- Videos: {basic["videos"]}
- Resolution: {basic["resolution"]}

🔹 Pro Plan
- Price: {pro["price"]}
- Videos: {pro["videos"]}
- Resolution: {pro["resolution"]}
- Features: {", ".join(pro["features"])}

👉 Pro plan is best for serious creators and YouTubers.
"""

    elif "basic" in query:
        return str(kb["pricing"]["basic"])

    elif "pro" in query:
        return str(kb["pricing"]["pro"])

    elif "refund" in query:
        return kb["policies"]["refund"]

    elif "support" in query:
        return kb["policies"]["support"]

    elif "autostream" in query:
        return kb["product"]

    return "AutoStream helps creators edit videos using AI."