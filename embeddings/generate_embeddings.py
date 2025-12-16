import oci
import numpy as np

config = oci.config.from_file("config/oci_config_example.txt")

client = oci.generative_ai_inference.GenerativeAiInferenceClient(config)

def generate_embedding(text):
    response = client.embed_text(
        model_id="cohere.embed-english-v3.0",
        texts=[text]
    )
    return response.data.embeddings[0]

with open("data/sample_docs.txt") as f:
    documents = f.readlines()

for doc in documents:
    embedding = generate_embedding(doc.strip())
    print(f"Generated embedding of length {len(embedding)}")

