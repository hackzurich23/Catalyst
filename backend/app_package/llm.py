import os
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from app_package.prompts import BOT_SYSTEM_PROMPT
from app_package.faiss_db import FAISS_DB


class LLM:
    """Langchain wrapper."""
    def __init__(self):
        self.llm = ChatOpenAI(temperature=0, model=os.getenv('MODEL_OLD'))
        self.prompt = PromptTemplate(
            input_variables=["message", "best_practice"],
            template=BOT_SYSTEM_PROMPT
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)


    def get_educated_response(self, db: FAISS_DB, message: str, top_k: int = 5, security_level: int = 2):
        """Query the database and answer the question based on the top k answers."""
        # Query the DB for similar questions.
        page_contents, metadata, scores = db.similarity_search(
            message, 
            top_k=top_k,
            security_level=security_level,
        )
        # Build the answer
        response = self.chain.run(message=message, best_practice=page_contents)
        return response, page_contents, metadata, scores
    
