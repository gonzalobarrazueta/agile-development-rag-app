import re


def clean_document(doc):

    clean_doc = re.sub(r'\n\s*\n', '\n', doc)
    return clean_doc
