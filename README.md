# ai-backend

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
