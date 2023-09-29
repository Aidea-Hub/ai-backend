### generateIdea1

Used to generate ideas for a problem that requires reflection

It performs the following 3 steps:

1. Ideation: Pass the user prompt n times through the LLM to get n output proposals (called "ideas"), where n is a parameter you can set
2. Critique: The LLM critiques all ideas to find possible flaws and picks the best one
3. Resolve: The LLM tries to improve upon the best idea (as chosen in the critique step) and outputs it. This is then the final output.

To deploy run

```
gcloud functions deploy generateIdea3 \
--runtime python310 \
--trigger-http \
--allow-unauthenticated
```
