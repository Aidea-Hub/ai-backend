### generateReflect

Used to generate content that requires reflection

It performs the following 3 steps:

1. Ideation: Pass the user prompt n times through the LLM to get n output proposals (called "ideas"), where n is a parameter you can set
2. Critique: The LLM critiques all ideas to find possible flaws and picks the best one
3. Resolve: The LLM tries to improve upon the best idea (as chosen in the critique step) and outputs it. This is then the final output.

To deploy run

```commandline
gcloud functions deploy generateReflect --gen2 --runtime=python311 --region=asia-east2 --source=. --entry-point=generateReflect --trigger-http --allow-unauthenticated --timeout=120 --set-env-vars OPENAI_API_KEY=<PASTE_KEY_HERE>
```


To run locally
```commandline
functions-framework-python --target generateReflect
```

