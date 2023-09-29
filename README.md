# ai-backend
* Contains google cloud functions that use langchain to interact with OpenAI api calls

## Setup
1. Git clone ai-backend repository
```
https://github.com/Aidea-Hub/ai-backend.git
```
2. Generate your API key from Open AI and set it in your env (`OPENAI_API_KEY`). Follow the guide from Open AI [here](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety#h_a1ab3ba7b2).

### Running locally
1. cd into each functions's folder and install the requirements 
```
pip install -r requirements.txt
```
2. Run each function locally. Follow the respective function's README instructions. It should look something like:
```
functions-framework-python --target <function_name>
```


## Project Strcuture

```
ai-backend/
├── function_1/
│   ├── README.md
│   ├── main.py
│   └── requirements.txt
├── function_2/
│   ├── README.md
│   ├── main.py
│   └── requirements.txt
└── README.md
```

## Deployment guide

```
cd path/to/function_directory

gcloud functions deploy function_name \
--runtime python310 \
--trigger-http \
--allow-unauthenticated
```
