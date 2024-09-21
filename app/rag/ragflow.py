from azure_open_ai import get_embedding, get_completions
from azure_ai_search import get_matching_documents


def embed_text(question):
    return get_embedding(question)


def get_sources(question):

    question_embedding = embed_text(question)
    sources = get_matching_documents(question, question_embedding)

    return sources


def set_system_message(system_message):
    return system_message


def chat(system_message, user_question):
    SYSTEM_MESSAGE = system_message
    USER_MESSAGE = user_question + "\nSources: " + get_sources(user_question)

    response = get_completions(SYSTEM_MESSAGE, USER_MESSAGE)

    return response
