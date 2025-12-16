import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

query_embedding = np.random.rand(1024)
doc_embedding = np.random.rand(1024)

score = cosine_similarity(query_embedding, doc_embedding)
print("Similarity score:", score)

