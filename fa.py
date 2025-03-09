from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from openai import OpenAI

wesearch_agent=Agent(
    name="web agent",
    role="search the web for the information",
    model=Groq( id="llama-3.3-70b-versatile",api_key=''),
    tools=[DuckDuckGo()],
    instructions=["always include sources"],
    show_tool_calls=True,
    markdown=True,

)

finance_agent=Agent(
    name="finance agent",
    model=Groq( id="llama-3.3-70b-versatile",api_key=''),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions=("use table to display the information"),
    show_tool_calls=True,
    markdown=True,
)
# multi agent application
multi_ai_agent = Agent(
    team=[wesearch_agent, finance_agent],
    model=Groq( id="llama-3.3-70b-versatile",api_key=''),
    instructions=["Use the web search agent to find information about the company and the financial agent to find information about the stock.",
                  "Use table to display the data"],
    show_tool_calls=True,
    markdown=True,
)
multi_ai_agent.print_response("summarize the analyst recommendation and share the latest news for pgel",stream=True)
