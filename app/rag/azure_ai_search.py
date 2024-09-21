import os

import azure.identity
import dotenv
from azure.search.documents.indexes import SearchIndexClient

dotenv.load_dotenv()


def get_azure_search_client():

    AZURE_SEARCH_SERVICE = os.getenv("AZURE_SEARCH_SERVICE")
    AZURE_SEARCH_ENDPOINT = f"https://{AZURE_SEARCH_SERVICE}.search.windows.net"

    azure_credential = azure.identity.DefaultAzureCredential()
    index_client = SearchIndexClient(endpoint=AZURE_SEARCH_ENDPOINT, credential=azure_credential)

    return index_client
