from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv


load_dotenv()

@tool
def calculator(a: float, b: float) -> str:
    """Useful for performing basic additions with numbers"""
    print("Tool has been called")
    return f"The sum of {a} and {b} is {a + b}"

def main():
    model = ChatOpenAI(temperature = 0.1) ## lower the temp, the less random the bot

    tools = [calculator]

    agent_executor = create_react_agent(model, tools)

    print("Hi, I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to do some calculations, or just have a chat with me")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            break

        print("\nAssistant: ", end = "") # this end part overrides the automatic \n that python puts in, so it goes straight after assis
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content = user_input)]}
            ):
            if "agent" in chunk and "messages" in chunk["agent"]: #chunks are the parts of response from agent, this is checking whether it is an agent response, and whether there are any messages
                for message in chunk["agent"]["messages"]:
                    print(message.content, end = "")
        print()

if __name__ == "__main__":
    main()
