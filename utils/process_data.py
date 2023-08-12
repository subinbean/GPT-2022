from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import os
from dotenv import load_dotenv
import pinecone

try:
    # load the pdf
    loader = PyPDFLoader('assets/Apple-10k-2022.pdf')
    raw_file = loader.load()

    # split up the raw text of pdf
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    documents = text_splitter.split_documents(raw_file)

    # # sanity check
    # with open('sample.txt', 'w') as file:
    #     for s in split_text:
    #         file.write(s.page_content)
    #         file.write('\n --section--\n')

    # initialize embeddings model
    embeddings = OpenAIEmbeddings()

    # pinecone
    load_dotenv()
    index_name = os.environ.get("PINECONE_INDEX_NAME")
    index = pinecone.Index(os.environ.get("PINECONE_INDEX_NAME"))
    Pinecone.from_documents(documents, embeddings, index_name=index_name)

except Exception as e:
    print('An error occurred:', e)


"""
First, load the pdf. Then, split it using some sort of mechanism. Turn it into embeddings then store it in Pinecone. (Ingestion step)

Then, have it such that I develop a chain to answer questions by fetching from Pinecone DB.

Then, create a frontend that can interact via chat (or honestly just Q&A)

Possible extensions: Using agents, chat memory, attributions, model fine-tuning, fetching multiple documents
"""
