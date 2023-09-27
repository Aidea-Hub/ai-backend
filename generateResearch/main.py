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
import functions_framework

@functions_framework.http
def generateResearch(params):
    # Set CORS headers for the preflight request
    if request.method == "OPTIONS":
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Max-Age": "3600",
        }

        return ("", 204, headers)

    # Set CORS headers for the main request
    headers = {"Access-Control-Allow-Origin": "*"}

    try:
        # Get the input text from the dictionary
        request_data = request.get_json()
        description = request_data.get("description", "")
        model = request_data.get("model", "gpt-3.5-turbo")

        wikipedia = WikipediaAPIWrapper()
        wikipedia_tool = Tool(
            name='wikipedia',
            func= wikipedia.run,
            description="Useful for when you need to look up a specific company"
        )
        search = DuckDuckGoSearchRun()
        duckduckgo_tool = Tool(
            name='Search',
            func= search.run,
            description="Useful for when you need to do a search on the internet to find information that another tool can't find. be specific with your input."
        )
        tools = [wikipedia_tool, duckduckgo_tool]
        llm = ChatOpenAI(temperature=0, model_name=model)

        research_agent = initialize_agent(
            agent= AgentType.OPENAI_FUNCTIONS,
            tools=tools,
            llm=llm,
            verbose=True,
            max_iterations=5,
        )


        prompts = [
        # 1. Problem Space and Market Competition
        f"""Here is a description of our product idea: {description}

        In the problem space that we are trying to "enter", is the market competitive? Please provide an explanation of how you came to your conclusion of at least 100 words. If you cannot find an answer, provide your best guess.

        ### Answer:
        According to research,""",
        # 2. Market Share Estimation
        f"""Here is a description of our product idea: {description}

        How much market share does each competitor of our idea have? Please provide an explanation of how you came to your conclusion of at least 100 words. If you cannot find an answer, provide your best guess.

        ### Answer:
        According to research,""",
        # 3. Potential for Market Share Capture
        f"""Here is a description of our product idea: {description}

        Will you be able to capture meaningful market share? Please provide an explanation of how you came to your conclusion of at least 100 words. If you cannot find an answer, provide your best guess.

        ### Answer:
        According to research,""",
        # 4. Competitors' Competitive Advantages
        f"""Here is a description of our product idea: {description}

        What are the competitive advantages of your competitors? Please provide an explanation of how you came to your conclusion of at least 100 words. If you cannot find an answer, provide your best guess.

        ### Answer:
        According to research,""",
        ]
        headers = [
            "1. Problem Space and Market Competition\n",
            "\n\n\n2. Market Share Estimation\n",
            "\n\n\n3. Potential for Market Share Capture\n",
            "\n\n\n4. Competitors' Competitive Advantages\n"
        ]
        output = ""
        for i in range(len(prompts)):
            prompt_template = PromptTemplate.from_template(prompts[i])
            response = research_agent.run(prompt_template)
            output += headers[i] + response

        return {"response": output}, 200, headers

    except Exception as e:
        return {"error": str(e)}, 500, headers
