# service/search.py

from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from config import AZURE_SEARCH_API_KEY, AZURE_SEARCH_ENDPOINT, AZURE_SEARCH_INDEX

def search_chunks_from_azure(query: str) -> str:
    client = SearchClient(
        endpoint=AZURE_SEARCH_ENDPOINT,
        index_name=AZURE_SEARCH_INDEX,
        credential=AzureKeyCredential(AZURE_SEARCH_API_KEY)
    )

    results = client.search(search_text=query, top=3)
    chunks = [doc.get("chunk", "") for doc in results]
    return "\n".join(chunks)

