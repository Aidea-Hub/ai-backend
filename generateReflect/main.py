import os
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_experimental.smart_llm import SmartLLMChain


# Get the OpenAI API key from the environment variable
api_key = os.environ.get("OPENAI_API_KEY")

# Check if the API key is set
if api_key is None:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

def generateReflect(params):
    try:
        # Get the input text from the dictionary
        prompt = params["prompt"]
        format = params["format"]
        title = params["title"]
        description = params["description"]

        template = f"""
        {prompt}
        {format}

        Title: {title}
        Description: {description}
        """

        # Initialize your prompt and ChatOpenAI model
        prompt_template = PromptTemplate.from_template(template)
        print(prompt_template)
        creative_llm = ChatOpenAI(temperature=0.9, model_name="gpt-3.5-turbo")
        base_llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")

        chain = SmartLLMChain(
            ideation_llm=creative_llm,
            llm=base_llm,
            prompt=prompt_template,
            n_ideas=2,
            verbose=True
        )
        # Run the chain
        result = chain.run({})
        print(result)

        return {"result": result}, 200

    except Exception as e:
        return {"error": str(e)}, 500



p = "For the following idea, suggest 10 of the most useful and innovative product capabilities. A common pitfall is failing to consider how the product serves the problem in the process. Consider your product's capabilities - does your product have the capabilities to succeed in your chosen problem space?"
f = "Give your answers in a list, and include a conclusion at the end."
t = "TravelBuddy: Local Experience Curation"
d = "A platform where locals can offer personalized travel experiences or guides to tourists. Unlike generic travel services, each itinerary is tailored to individual preferences and interests."

# Test the function locally
result, status_code = generateReflect(
    {"prompt": p, "format": f, "title": t, "description": d}
)
print("Status Code:", status_code)
print("Result:", result)
