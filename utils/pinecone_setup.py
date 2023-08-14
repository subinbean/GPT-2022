import pinecone
import os
from dotenv import load_dotenv


def pinecone_setup():
    load_dotenv()
    try:
        # initialize pinecone
        pinecone.init(
            api_key=os.environ.get('PINECONE_API_KEY'),
            environment=os.environ.get('PINECONE_ENV')
        )

        print('pinecone initialized')

        index_name = os.environ.get("PINECONE_INDEX_NAME")

        # First, check if our index already exists. If it doesn't, we create it
        if index_name not in pinecone.list_indexes():
            # we create a new index
            print('creating index')
            pinecone.create_index(
                name=index_name,
                metric='cosine',
                dimension=1536
            )
            print('index created!')

    except Exception as e:
        print('An error occurred:', e)
