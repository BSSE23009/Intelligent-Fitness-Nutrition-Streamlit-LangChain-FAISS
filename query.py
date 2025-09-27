from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from dotenv import load_dotenv
from langchain.tools import tool
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    openai_api_key=OPENAI_API_KEY
)

faiss_store = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = faiss_store.as_retriever(search_kwargs={"k": 3})

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    openai_api_key=OPENAI_API_KEY
)

prompt = ChatPromptTemplate.from_template(
    """Use the provided context to answer the question. 
If the answer is not in the context, say "I don't know."

Context:
{context}

Question: {question}

Answer:"""
)

def combine_docs(docs):
    return "\n\n".join([d.page_content for d in docs])

retrieve_runnable = RunnableLambda(lambda x: retriever.invoke(x["question"]))
combine_runnable = RunnableLambda(combine_docs)

rag_chain = (
    {
        "context": retrieve_runnable | combine_runnable,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
)





@tool
def answer_question(question: str) -> str:
    """Answers a question using the RAG chain."""
    return rag_chain.invoke({"question": question})
