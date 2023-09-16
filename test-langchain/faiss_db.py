import os
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.schema.document import Document
import typing as Dict
from dotenv import load_dotenv



class FAISS_DB:
    def __init__(self):
        # Create the vector database
        if os.path.exists("faiss_index"):
            embeddings = OpenAIEmbeddings()
            self.db = FAISS.load_local("faiss_index", embeddings)
        else:
            self.db = None
        
    def save_to_disk(self):
        self.db.save_local("faiss_index")
    
    def new_from_documents(self, documents):
        embeddings = OpenAIEmbeddings()
        self.db = FAISS.from_documents(documents, embeddings)
        
    def _add(self, docs):
        # Add to the DB if it exists.
        if self.db:
            self.db.aadd_documents(docs)
        # Create a new DB if it doesn't exist.
        else:
            self.new_from_documents(docs)
        
    def append_fact_as_document(self, facts: list[str], meeting_id=-1, meeting_participants=""):
        """Encode a fact as a document and add it to the DB."""
        documents = [
            Document(
                page_content=fact, 
                metadata={'source': 'test-langchain/generated_q_and_a_correct.csv', 'id': 5}
            )
            for fact in facts
        ]
        self._add(documents)

    def append_q_and_a_as_document(self, q_and_a: dict[str, str], metadata: dict=None):
        """Encode {"question": "answer"} like dict into the DB."""
        documents = [
            Document(
                page_content=f"""question: {question}\n\"answer\": \"{answer}\"""", 
                metadata=metadata if metadata else None
            )
            for question, answer in q_and_a.items()
        ]
        self._add(documents)
            
            
    def similarity_search(self, query: str, top_k: int=3):
        """General similarity search function. Returns a list of documents with metadata and scores."""
        if self.db:
            docs_and_scores = self.db.similarity_search_with_score(query, k=top_k)
            page_contents = [doc.page_content for doc, score in docs_and_scores]
            metadatas = [doc.metadata for doc, score in docs_and_scores]
            scores = [score for doc, score in docs_and_scores]
            return page_contents, metadatas, scores
        raise ModuleNotFoundError("DB is not initialized.")


# For testing. 
if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    assert load_dotenv(dotenv_path=dir_path + "/../.env", override=True), "Could not load .env file"
    faiss_db = FAISS_DB()
    documents = {"Who am i": "Philipp", "who sits next to me": "Natalia"}
    faiss_db.append_q_and_a_as_document(documents)
    faiss_db.similarity_search("Who am i?")
    
    pass
