from agent.graph import SimpleAgent
from agent.state import init_state
from agent.rag import load_kb

print("STARTING APP...")

state = init_state()
kb = load_kb()

agent = SimpleAgent(kb)

print("Ready...")

while True:
    user_input = input("You: ")
    response = agent.run(state, user_input)
    print("Bot:", response)