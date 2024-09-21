import os

import dotenv
import openai

dotenv.load_dotenv()

AZURE_OPENAI_SERVICE = os.getenv("AZURE_OPENAI_SERVICE")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ADA_DEPLOYMENT = os.getenv("AZURE_OPENAI_ADA_DEPLOYMENT")
AZURE_OPENAI_ENDPOINT= f"https://{AZURE_OPENAI_SERVICE}.openai.azure.com"


def get_openai_client():

    openai_client = openai.AzureOpenAI(
        api_key=AZURE_OPENAI_API_KEY,
        api_version="2024-07-01-preview",
        azure_endpoint=AZURE_OPENAI_ENDPOINT
    )

    return openai_client


def get_embedding(text="this is a text to embed. only for testing"):

    openai_client = get_openai_client()

    get_embeddings_response = openai_client.embeddings.create(model=AZURE_OPENAI_ADA_DEPLOYMENT, input=text)
    return get_embeddings_response.data[0].embedding


print(get_embedding())
