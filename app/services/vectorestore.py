import chromadb
from chromadb.config import Settings

client = chromadb.PersistentClient(
    path="app/data/chroma_db"
)

collection = client.get_or_create_collection(
    name="documents"
)

def add_document(
    chunks,
    embeddings,
    filename
):
    ids = []
    documents = []
    vectores = []
    metadatas = []

    for index, chunk in enumerate(chunks):

        ids.append(
            f"{filename}_{index}"
        )

        documents.append(chunk)

        vectores.append(
            embeddings[index]
        )

        metadatas.append(
            {
                "Filename" : filename,
                "chunk_id" : index  
            }
        )

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )

def search_documents(
    query_embedding,
    limit=3
):
    
    results = collection.query(
        query_embeddings=[
            query_embedding
        ],  
        n_results=limit
    )

    return results

def search_documents(
    query_embedding,
    limit=3
):
    
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=limit
    )
    
    return results