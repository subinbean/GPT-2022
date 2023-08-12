from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings

# load the pdf
loader = PyPDFLoader('assets/Apple-10k-2022.pdf')
raw_file = loader.load()

# split up the raw text of pdf
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
split_text = text_splitter.split_documents(raw_file)
for s in split_text:
    print(s.metadata)

# # sanity check
# with open('sample.txt', 'w') as file:
#     for s in split_text:
#         file.write(s.page_content)
#         file.write('\n --section--\n')

# create embeddings
embeddings_model = OpenAIEmbeddings()

"""
First, load the pdf. Then, split it using some sort of mechanism. Turn it into embeddings then store it in Pinecone. (Ingestion step)

Then, have it such that I develop a chain to answer questions by fetching from Pinecone DB.

Then, create a frontend that can interact via chat (or honestly just Q&A)

Possible extensions: Using agents, chat memory, attributions, model fine-tuning, fetching multiple documents
"""
