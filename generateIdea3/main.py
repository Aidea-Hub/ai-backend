import os
import logging
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from llmChain import SmartLLMChain
import functions_framework

# Get the OpenAI API key from the environment variable
# api_key = os.environ.get("OPENAI_API_KEY")

# # Check if the API key is set
# if api_key is None:
#     raise ValueError("OPENAI_API_KEY environment variable is not set")

@functions_framework.http
def generateIdea3(request):
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
        problem = request_data.get("problem", "")

        template = f"""
        Suggest 3 innovative ideas to solve the following problem, making sure to consider the root causes of the problem.
        
        ###
        Problem: {problem}
        ###
        
        ###
        Desired format:
        Give me the ideas to solve the problem in a list format.

        For each idea, I want it in the following format:
        <Idea Name>:<One liner describing the idea>   
        ###
        """

        logging.info(template)

        prompt_template = PromptTemplate.from_template(template)
        logging.info(prompt_template)

        creative_llm = ChatOpenAI(temperature=0.9, model_name="gpt-3.5-turbo")
        base_llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

        chain = SmartLLMChain(
            ideation_llm=creative_llm,
            llm=base_llm,
            prompt=prompt_template,
            n_ideas=2,
            verbose=True
        )
        # Run the chain
        response = chain.run({})

        return {"response": response}, 200

    except Exception as e:
        return {"error": str(e)}, 500


# p = """Suggest 3 innovative ideas to solve the following problem, making sure to consider the root causes of the problem."""
# f = """
# Give me the ideas to solve the problem in a list format.

# For each idea, I want it in the following format:
# <Idea Name>:<One liner describing the idea>
# """
# problem = "I hate it when I have to wait at a hospital."
# i = 1

# # Test the function locally
# result, status_code = generateIdea1(
#     {"prompt": p, "format": f, "problem": problem, "num_ideas": i}
# )
# print("Status Code:", status_code)
# print("Result:", result)
