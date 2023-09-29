### generateFallback

Fallback function used to generate content for generateReflect if the original does not provide a good answer

To deploy run

```commandline
gcloud functions deploy generateFallback --gen2 --runtime=python311 --region=asia-east2 --source=. --memory=512MiB --entry-point=generateFallback --trigger-http --allow-unauthenticated --timeout=120 --set-env-vars OPENAI_API_KEY=<PASTE_KEY_HERE>
```


To run locally
```commandline
functions-framework-python --target generateFallback
```