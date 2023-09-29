### generateResearch

Used to research competitive analysis and moat.
Uses SerpApi to get the latest data from Google

To deploy run

```commandline
gcloud functions deploy generateResearch --gen2 --runtime=python311 --region=asia-east2 --source=. --memory=512MiB --entry-point=generateResearch --trigger-http --allow-unauthenticated --timeout=120 --set-env-vars OPENAI_API_KEY=<PASTE_KEY_HERE>
```


To run locally
```commandline
functions-framework-python --target generateResearch
```