from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from pypdf import PdfReader  
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

book = PdfReader("/Users/apple/Desktop/Workout_Recommender/Starting Strength PDF.pdf")
text = ""
for page in book.pages:
    text += page.extract_text()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_text(text)
print(f"Number of chunks: {len(chunks)}")

docs = [
    Document(
        page_content=chunk,
        metadata={
            "book": "Starting Strength",
            "chunk": i,
            "source": "Starting Strength By Mark Rippetoe"
        }
    )
    for i, chunk in enumerate(chunks)
]

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    openai_api_key=OPENAI_API_KEY
)

faiss_store = FAISS.from_documents(docs, embeddings)
faiss_store.save_local("faiss_index")
print("✅ FAISS index saved to disk.")
