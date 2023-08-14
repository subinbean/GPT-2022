from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import pinecone_setup
import os
from dotenv import load_dotenv
import pinecone

load_dotenv()

try:
    # creates open AI chat model using gpt 3.5 turbo (which is what chat gpt uses)
    # set temperature to whatever you want depending on how random / creative you want answers to be
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    # set up pinecone vectorestore for retrieval
    pinecone_setup.pinecone_setup()
    index_name = os.environ.get("PINECONE_INDEX_NAME")
    index = pinecone.Index(index_name)
    embeddings = OpenAIEmbeddings()
    vectorstore = Pinecone(
        index, embedding_function=embeddings.embed_query, text_key="text")

    # sanity check for retrieval
    question = "What are some highlights for the fourth quarter of 2022?"
    # docs = vectorstore.similarity_search(question)
    # print(docs)

    template = """Use the following pieces of context to answer the question at the end. 
    If you don't know the answer, just say that you don't know, don't try to make up an answer. 
    Use three sentences maximum and keep the answer as concise as possible. 
    Always say "thanks for asking!" at the end of the answer. 
    {context}
    Question: {question}
    Helpful Answer:"""

    qa_chain_prompt = PromptTemplate.from_template(template)
    qa_chain = RetrievalQA.from_chain_type(
        llm, retriever=vectorstore.as_retriever(), chain_type_kwargs={"prompt": qa_chain_prompt})

    print(qa_chain({"query": question}))


except Exception as e:
    print('An error occurred:', e)
