import logging
import os
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from llmChain import SmartLLMChain
import functions_framework


# Set your OpenAI API key as an environment variable (you'll set it in the Cloud Console)
# api_key = os.environ.get("OPENAI_API_KEY")

@functions_framework.http
def generateReflect(request):
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
        # Get the input data from the HTTP request
        request_data = request.get_json()
        prompt = request_data.get("prompt", "")
        format = request_data.get("format", "")
        title = request_data.get("title", "")
        description = request_data.get("description", "")
        model = request_data.get("model", "gpt-3.5-turbo")

        template = f"""
        {prompt}

        Desired format:
        {format}

        Idea: \"\"\"
        {title}
        {description}
        \"\"\"
        """

        logging.info(template)

        # Initialize your prompt and ChatOpenAI model
        prompt_template = PromptTemplate.from_template(template)
        logging.info(prompt_template)

        creative_llm = ChatOpenAI(temperature=0.9, model_name=model)
        base_llm = ChatOpenAI(temperature=0.5, model_name=model)

        chain = SmartLLMChain(
            ideation_llm=creative_llm,
            llm=base_llm,
            prompt=prompt_template,
            n_ideas=1,
            verbose=True
        )

        # Run the chain
        response = chain.run({})
        return {"response": response}, 200, headers

    except Exception as e:
        logging.error(str(e))
        return {"error": str(e)}, 500, headers
