from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import os
from dotenv import load_dotenv
import pinecone_setup
import re

load_dotenv()


def ingest_file(pdf_path):
    try:
        # extract title of pdf
        title = re.search(r'([A-Za-z]+)-', pdf_path).group(1).lower()
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
        # with open(f'{title}.txt', 'w') as file:
        #     for d in documents:
        #         file.write(str(d))
        #         file.write('\n --section--\n')

        # initialize embeddings model
        embeddings = OpenAIEmbeddings()

        # pinecone
        pinecone_setup.pinecone_setup()
        index_name = os.environ.get("PINECONE_INDEX_NAME")
        print('creating embeddings and storing in pinecone')

        # upserting by chunks to try and avoid pinecone errors
        for i in range(0, len(documents), 50):
            Pinecone.from_documents(documents[i:i + 50], embeddings,
                                    index_name=index_name)
        print('Done!')

    except Exception as e:
        print('An error occurred:', e)


def main():
    folder_path = 'assets'
    for root, _, files in os.walk(folder_path):
        for file in files:
            ingest_file(os.path.join(root, file))


if __name__ == '__main__':
    main()
