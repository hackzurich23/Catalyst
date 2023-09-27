import os
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.schema.document import Document
from dotenv import load_dotenv


class FAISS_DB:
    def __init__(self):
        # Create the vector database
        embeddings = OpenAIEmbeddings()
        if os.path.exists("faiss_index"):
            self.db = FAISS.load_local("faiss_index", embeddings)
        else:
            # self.db = FAISS.from_documents([], embeddings)
            list_of_documents = [
                Document(page_content="test", metadata=dict(page=1)),
            ]
            db = FAISS.from_documents(list_of_documents, embeddings)
            self.db = db

    def save_to_disk(self):
        self.db.save_local("faiss_index")
    
    def new_from_documents(self, documents):
        embeddings = OpenAIEmbeddings()
        self.db = FAISS.from_documents(documents, embeddings)
        
    def _add(self, docs):
        embeddings = OpenAIEmbeddings()
        # Add to the DB if it exists.
        if self.db:
            temp_db = FAISS.from_documents(docs, embeddings)
            self.db.merge_from(temp_db)
        # Create a new DB if it doesn't exist.
        else:
            self.new_from_documents(docs)
            

    def _build_security_level_dict(self, security_level: int) -> dict[str, bool]:
        """Build a dictionary of security levels."""
        return {
            "security_level_0": security_level >= 0,
            "security_level_1": security_level >= 1,
            "security_level_2": security_level >= 2,
        }
        
        
    def append_fact_as_document(self, facts: list[str], metadata: dict=None):
        """Encode a fact as a document and add it to the DB."""
        documents = [
            Document(
                page_content=fact, 
                metadata=metadata if metadata else None
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
            
            
    def similarity_search(self, query: str, top_k: int=3, security_level: int=2):
        """General similarity search function. Returns a list of documents with metadata and scores."""
        if self.db:
            docs_and_scores = self.db.similarity_search_with_score(
                query, 
                k=top_k,
                filter={k: v for k, v in self._build_security_level_dict(security_level).items() if v}
            )
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
