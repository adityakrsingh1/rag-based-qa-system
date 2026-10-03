import os

class Config:
    def __init__(self):
        self.load_env_variables()

    def load_env_variables(self):
        self.api_key = os.getenv("API_KEY")
        self.database_url = os.getenv("DATABASE_URL")
        self.embedding_model = os.getenv("EMBEDDING_MODEL", "default_model")
        self.vector_store_path = os.getenv("VECTOR_STORE_PATH", "data/vector_store")
        self.chunk_size = int(os.getenv("CHUNK_SIZE", 512))
        self.chunk_overlap = int(os.getenv("CHUNK_OVERLAP", 50))

config = Config()