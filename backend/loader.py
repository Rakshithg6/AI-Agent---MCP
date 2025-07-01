from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
import os
import logging
import shutil

def ingest_pdf(path: str):
    loader = PyPDFLoader(path)
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    texts = splitter.split_documents(pages)

    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = FAISS.from_documents(texts, embeddings)

    # SAFELY replace existing vectorstore folder
    if os.path.exists("vectorstore"):
        if os.path.isfile("vectorstore"):
            os.remove("vectorstore")
        else:
            shutil.rmtree("vectorstore")

    vectorstore.save_local("vectorstore")
