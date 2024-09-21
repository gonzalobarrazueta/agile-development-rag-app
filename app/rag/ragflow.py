from app.rag.azure_open_ai import get_embedding, get_completions
from app.rag.azure_ai_search import get_matching_documents


def embed_text(question):
    return get_embedding(question)


def get_sources(question):

    question_embedding = embed_text(question)
    sources = get_matching_documents(question, question_embedding)

    return sources


def set_system_message(system_message):
    return system_message


def chat(system_message, user_question):

    sources = get_sources(user_question)
    user_message = user_question + "\nSources: " + sources

    response = get_completions(system_message, user_message)

    return sources, response
