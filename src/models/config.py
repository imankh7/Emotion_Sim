
from dataclasses import dataclass

@dataclass
class ModelConfig:
    # Default small models suitable for CPU/GPU (Colab-friendly)
    embedding_model_name: str = "sentence-transformers/all-MiniLM-L6-v2"
    emotion_model_name: str = "joeddav/distilbert-base-uncased-go-emotions-student"
    vector_store_path: str = "data/processed/chroma_index"
    artifacts_dir: str = "artifacts"
