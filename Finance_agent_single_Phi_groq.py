import os
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools

# Load environment variables
def initialize_environment():
    load_dotenv()
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("GROQ_API_KEY is not set in the environment variables.")
    return groq_api_key

# Create a finance agent using the Groq model
def create_finance_agent(api_key):
    return Agent(
        name="Finance Agent",
        model=Groq(id="llama-3.2-11b-vision-preview", api_key=api_key),
        tools=[YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True
        )],
        instructions=["Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )

# Main function
def main():
    try:
        # Initialize environment variables and get the API key
        groq_api_key = initialize_environment()

        # Create the agent
        finance_agent = create_finance_agent(groq_api_key)

        # Perform a task using the agent
        finance_agent.print_response(
            "Summarize analyst recommendations for NVDA",
            stream=True,
        )
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
