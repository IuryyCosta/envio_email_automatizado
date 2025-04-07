from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

class SendEmailSchema(BaseModel):
   
    PORT : int = Field(default=300)
    MODE_ENV: str = Field(default="production", pattern="^(development|production)$")
    RESEND_API_KEY: str
    EMAIL_FROM: str
    EMAIL_TO: str
    ORACLE_HOST: str
    ORACLE_USER: str
    ORACLE_PASSWORD: str
    ORACLE_DATABASE: str
    ORACLE_LIB_DIR: str
    ORACLE_CONNECT_STRING: str
    EXECUTION_HOUR: int = Field(..., ge=0, le=23)  # Restrição entre 0 e 23
    EXECUTION_MINUTE: int = Field(..., ge=0, le=59)  # Restrição entre 0 e 59

    @classmethod
    def load_from_env(cls):
          return cls(**{field: os.getenv(field) for field in cls.model_fields.keys()})
          

try:
     env = SendEmailSchema.load_from_env()
except Exception as e:
     print(f"Error loading environment variables: {e}")
     raise e