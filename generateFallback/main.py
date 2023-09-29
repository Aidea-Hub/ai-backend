import os
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.utilities import GoogleSerperAPIWrapper
from langchain.llms.openai import OpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.agents import AgentType
from langchain.tools import DuckDuckGoSearchRun
from langchain.utilities import WikipediaAPIWrapper
from langchain.agents import initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
import functions_framework

@functions_framework.http
def generateFallback(request):
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
        prompt = request_data.get("prompt", "")
        format = request_data.get("format", "")
        title = request_data.get("title", "")
        description = request_data.get("description", "")
        model = request_data.get("model", "gpt-3.5-turbo")

        llm = ChatOpenAI(temperature=0.5, model_name=model)
        template = f"""
        {prompt}

        Desired format:
        {format}

        Idea: \"\"\"
        {title}
        {description}
        \"\"\"
        """
        # Initialize your prompt and ChatOpenAI model
        prompt_template = PromptTemplate.from_template(template)
        llm_chain = LLMChain(prompt=prompt_template, llm=llm)

        # Run the chain
        response = llm_chain.run({})
        return {"response": response}, 200, headers

    except Exception as e:
        return {"error": str(e)}, 500, headers
