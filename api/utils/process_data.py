from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import os
from dotenv import load_dotenv
import pinecone
import pinecone_setup
import re

load_dotenv()


def ingest_file(pdf_path):
    try:
        # extract title of pdf
        title = re.findall(r'/([^/]+)\.pdf$', pdf_path)[0]
        print(title)
        loader = PyPDFLoader(pdf_path)
        raw_file = loader.load()

        # split up the raw text of pdf
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        documents = text_splitter.split_documents(raw_file)
        print('docs loaded and split')

        # sanity check
        with open(f'{title}.txt', 'w') as file:
            for d in documents:
                file.write(str(d))
                file.write('\n --section--\n')

        # initialize embeddings model
        embeddings = OpenAIEmbeddings()

        # pinecone
        # pinecone_setup.pinecone_setup()
        # index_name = os.environ.get("PINECONE_INDEX_NAME")
        # index = pinecone.Index(index_name)
        # print('creating embeddings and storing in pinecone')
        # Pinecone.from_documents(documents, embeddings,
        #                         index_name=index_name, namespace=title)
        # print('Done!')

    except Exception as e:
        print('An error occurred:', e)


def main():
    folder_path = 'assets'
    for root, _, files in os.walk(folder_path):
        for file in files:
            ingest_file(os.path.join(root, file))


if __name__ == '__main__':
    main()
