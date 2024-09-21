import os

import dotenv
import openai

dotenv.load_dotenv()

AZURE_OPENAI_SERVICE = os.getenv("AZURE_OPENAI_SERVICE")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ADA_DEPLOYMENT = os.getenv("AZURE_OPENAI_ADA_DEPLOYMENT")
AZURE_OPENAI_COMPLETIONS_DEPLOYMENT = os.getenv("AZURE_OPENAI_COMPLETIONS_DEPLOYMENT")
AZURE_OPENAI_ENDPOINT= f"https://{AZURE_OPENAI_SERVICE}.openai.azure.com"


def get_openai_client():

    openai_client = openai.AzureOpenAI(
        api_key=AZURE_OPENAI_API_KEY,
        api_version="2024-07-01-preview",
        azure_endpoint=AZURE_OPENAI_ENDPOINT
    )

    return openai_client


def get_embedding(text):

    openai_client = get_openai_client()

    get_embeddings_response = openai_client.embeddings.create(model=AZURE_OPENAI_ADA_DEPLOYMENT, input=text)
    return get_embeddings_response.data[0].embedding


def get_completions(system_message, user_message):

    openai_client = get_openai_client()

    response = openai_client.chat.completions.create(
        model=AZURE_OPENAI_COMPLETIONS_DEPLOYMENT,
        temperature=0.4,
        messages=[
            {'role': 'system', 'content': system_message },
            {'role': 'user', 'content': user_message }
        ],
        max_tokens=100
    )

    return response.choices[0].message.content
