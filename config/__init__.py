from dataclasses import dataclass

@dataclass
class Setting:
    host = "192.168.30.144"
    port = 6688
    SQLALCHEMY_DATABASE_URL = "postgresql://postgres:shiyue@localhost:5432/LLMDB"