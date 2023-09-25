### generateResearch

Used to research competitive analysis and moat.
Uses SerpApi to get the latest data from Google

To deploy run

```
gcloud functions deploy generateSearch \
--runtime python310 \
--trigger-http \
--allow-unauthenticated
```
