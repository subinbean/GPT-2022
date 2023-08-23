from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import os
from api.utils import pinecone_setup
from dotenv import load_dotenv
import pinecone

load_dotenv()


def generate_message(query):
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
        # question = "What are some highlights for the fourth quarter of 2022?"
        # docs = vectorstore.similarity_search(question)
        # print(docs)

        # template used to prompt the model
        template = """Use the following pieces of context to answer the question at the end. 
        If you don't know the answer, just say that you don't know, don't try to make up an answer.
        Always say "thanks for asking!" at the end of the answer. 
        {context}
        Question: {question}
        Helpful Answer:"""

        qa_chain_prompt = PromptTemplate.from_template(template)

        # retrieves from vector store relevant documents and passes them as context to prompt
        # k is the number of documents retrieved
        qa_chain = RetrievalQA.from_chain_type(
            llm, retriever=vectorstore.as_retriever(search_kwargs={'k': 2}), return_source_documents=True, chain_type_kwargs={"prompt": qa_chain_prompt})

        # print(qa_chain({"query": question}))
        return qa_chain({"query": query})

    except Exception as e:
        print('An error occurred:', e)
