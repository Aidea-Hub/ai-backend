import os
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_experimental.smart_llm.base import SmartLLMChain
from langchain.utilities import GoogleSerperAPIWrapper
from langchain.llms.openai import OpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.agents import AgentType
from langchain.tools import DuckDuckGoSearchRun
from langchain.utilities import WikipediaAPIWrapper
from langchain.agents import initialize_agent
from langchain.memory import ConversationBufferMemory

# # Get the OpenAI API key from the environment variable
# api_key = os.environ.get("OPENAI_API_KEY")
#
#
# # Check if the API key is set
# if api_key is None:
#     raise ValueError("OPENAI_API_KEY environment variable is not set")

def generateResearch(params):
#     try:
        os.environ[
            "OPENAI_API_KEY"
        ] = "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"
#         wikipedia = WikipediaAPIWrapper()
#         wikipedia_tool = Tool(
#             name='wikipedia',
#             func= wikipedia.run,
#             description="Useful for when you need to look up a topic, country or person on wikipedia"
#         )
        search = DuckDuckGoSearchRun()
        duckduckgo_tool = Tool(
            name='Search',
            func= search.run,
            description="Useful for when you need to do a search on the internet to find information that another tool can't find. be specific with your input."
        )
        tools = [duckduckgo_tool]
        memory = ConversationBufferMemory(memory_key="chat_history")
        llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

        research_agent = initialize_agent(
            agent= AgentType.OPENAI_FUNCTIONS,
            tools=tools,
            llm=llm,
            verbose=True,
            max_iterations=5,
        )
        # Get the input text from the dictionary
        prompt = params["prompt"]
        format = params["format"]
        title = params["title"]
        description = params["description"]

        prompts =

        template = f"""
        Here is a description of our product idea: {description}

        How much market share does each competitor of our idea have? Please provide an explanation of how you came to your conclusion of at least 100 words. If you cannot find an answer, provide your best guess.

        ### Answer:
        According to research,
        """


        # Initialize your prompt and ChatOpenAI model
        prompt_template = PromptTemplate.from_template(template)
        print(prompt_template)


        response = research_agent.run(prompt_template)
#         print(wikipedia.run('Competitive Analysis'))
#         print(search.run('Competitors for ' + title))
        return {"response": response}, 200,

#     except Exception as e:
#         return {"error": str(e)}, 500



p = """
Perform a competitive landscape analysis of competitors of the following idea, providing critical insights into existing market players, their offerings, strengths, and weaknesses.
"""
f = """
1. Problem Space and Market Competition: <In the problem space that you are trying to "enter", is the market competitive?>
2. Market Share Estimation: <How much market share does each competitor have?>
3. Competitors' Competitive Advantages: <Will you be able to capture meaningful market share?>
4. Potential for Market Share Capture: <What are the competitive advantages of your competitors?>

Conclusion: <Conclusion of competitive landscape analysis>
"""
t = "TravelBuddy: Local Experience Curation"
d = "A platform where locals can offer personalized travel experiences or guides to tourists. Unlike generic travel services, each itinerary is tailored to individual preferences and interests."

# Test the function locally
result, status_code = generateResearch(
    {"prompt": p, "format": f, "title": t, "description": d}
)
print("Status Code:", status_code)
print("Result:", result)