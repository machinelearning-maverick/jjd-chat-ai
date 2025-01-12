import os.path

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI


def chunk_data(data, chunk_size=256, chunk_overlap=20):
    print(f"chunk_data()")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = text_splitter.split_documents(data)
    print("Chunks created")
    return chunks

def create_embeddings(chunks, persist_directory="./chroma_db"):
    print(f"create_embeddings()")
    if os.path.exists(persist_directory) and os.listdir(persist_directory):
        print("Persist directory is not empty. Loading existing vector store.")
        vector_store = Chroma(persist_directory=persist_directory)
    else:
        print("Persist directory is empty. Creating new vector store.")
        embeddings = OpenAIEmbeddings()
        vector_store = Chroma.from_documents(chunks, embeddings, persist_directory=persist_directory)
    print("Embeddings created")
    return vector_store

def ask_and_get_answer(vector_store, q, k=3):
    print(f"ask_and_get_answer()")
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5)
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": k})
    chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    answer = chain.invoke(q)
    print("Answer received")
    return answer
