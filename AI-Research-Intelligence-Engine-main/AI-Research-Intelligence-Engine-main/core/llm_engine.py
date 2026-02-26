import requests
from config.settings import OLLAMA_URL, MODEL_NAME, DEFAULT_TEMPERATURE, MAX_CONTEXT

def query_llm(prompt, temperature=DEFAULT_TEMPERATURE):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
                "top_p": 0.9,
                "num_ctx": MAX_CONTEXT
            }
        }
    )

    return response.json().get("response", "No response received.")