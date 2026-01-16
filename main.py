from app.agent import create_agent

agent = create_agent()

print("ReAct Agent Ready (type 'exit' to quit)")

while True:
    query = input("User: ")
    if query.lower() == "exit":
        break

    result = agent.invoke({"input": query})
    print("\nAgent:", result["output"], "\n")
