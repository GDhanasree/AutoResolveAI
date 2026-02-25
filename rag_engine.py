import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Knowledge base
knowledge_base = [
    "Tracking issue: Restart shipment sync and refresh webhook.",
    "Payment issue: Verify transaction ID and initiate refund.",
    "API failure: Check authentication token and retrigger API.",
    "Delivery delay: Check driver allocation and update ETA.",
    "Warehouse sync: Re-sync inventory and validate stock mapping."
]

# Create embeddings
embeddings = embed_model.encode(knowledge_base)
dimension = embeddings.shape[1]

# Create FAISS index
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

def retrieve_solution(query):
    query_embedding = embed_model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k=1)
    return knowledge_base[indices[0][0]]


# import faiss
# import numpy as np
# from sentence_transformers import SentenceTransformer

# # Load embedding model
# embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# # Structured Knowledge Base
# knowledge_base = {
#     "tracking": "Restart shipment sync and refresh webhook logs.",
#     "payment": "Verify transaction ID and initiate refund process.",
#     "api_failure": "Check authentication token and retrigger API request.",
#     "delivery_delay": "Check driver allocation and update ETA in system.",
#     "warehouse_sync": "Re-sync inventory and validate stock mapping."
# }

# labels = list(knowledge_base.keys())
# solutions = list(knowledge_base.values())

# # Create embeddings
# embeddings = embed_model.encode(solutions)
# dimension = embeddings.shape[1]

# index = faiss.IndexFlatL2(dimension)
# index.add(np.array(embeddings))

# def retrieve_solution(query):
#     query_embedding = embed_model.encode([query])
#     distances, indices = index.search(np.array(query_embedding), k=1)

#     matched_label = labels[indices[0][0]]
#     matched_solution = solutions[indices[0][0]]

#     return matched_label, matched_solution