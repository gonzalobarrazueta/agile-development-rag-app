import os

import dotenv
from azure.search.documents.indexes import SearchIndexClient
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import ResourceNotFoundError
from azure.search.documents.models import VectorizedQuery
from azure.search.documents import SearchClient
from app.utils.documents import clean_document

from azure.search.documents.indexes.models import (
    HnswAlgorithmConfiguration,
    SearchField,
    SearchFieldDataType,
    SearchIndex,
    SimpleField,
    VectorSearch,
    VectorSearchProfile,
)

dotenv.load_dotenv()

AZURE_SEARCH_SERVICE = os.getenv("AZURE_SEARCH_SERVICE")
AZURE_SEARCH_ENDPOINT = f"https://{AZURE_SEARCH_SERVICE}.search.windows.net"
AZURE_SEARCH_API_KEY = os.getenv("AZURE_SEARCH_API_KEY")
AZURE_SEARCH_INDEX = os.getenv("AZURE_SEARCH_INDEX")

azure_credential = AzureKeyCredential(AZURE_SEARCH_API_KEY)


def get_azure_search_client():

    return SearchIndexClient(endpoint=AZURE_SEARCH_ENDPOINT, credential=azure_credential)


def create_index():

    index_client = get_azure_search_client()

    index = SearchIndex(
        name=AZURE_SEARCH_INDEX,
        fields=[
            SimpleField(name="id", type=SearchFieldDataType.String, key=True),
            SearchField(name="content_vector", type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
                        searchable=True, vector_search_dimensions=1536, vector_search_profile_name="my-vector-config"),
        ],
        vector_search=VectorSearch(
            profiles=[
                VectorSearchProfile(name="my-vector-config", algorithm_configuration_name="my-algorithms-config")],
            algorithms=[HnswAlgorithmConfiguration(name="my-algorithms-config")],
        )
    )

    index_client.create_index(index)


def get_search_index(index_name=AZURE_SEARCH_INDEX):

    return SearchClient(endpoint=AZURE_SEARCH_ENDPOINT, index_name=index_name, credential=azure_credential)


def get_matching_documents(question, question_vector):
    search_client = get_search_index(AZURE_SEARCH_INDEX)
    results = search_client.search(
        question,
        top=2,
        vector_queries=[
            VectorizedQuery(vector=question_vector, k_nearest_neighbors=2, fields="text_vector")
        ]
    )

    sources = "\n\n".join([f"[Documento {index}]: {clean_document(doc['chunk'])}\n" for index, doc in enumerate(results)])

    return sources
