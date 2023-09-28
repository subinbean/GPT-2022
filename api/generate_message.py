from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
# from langchain.chains import RetrievalQA
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
import os
from api.utils import pinecone_setup
from dotenv import load_dotenv
import pinecone

load_dotenv()


def get_list_names():
    for root, _, files in os.walk(folder_path):
        for file in files:
            ingest_file(os.path.join(root, file))


def generate_message(query, past_messages):
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
            index, embedding=embeddings, namespace="Apple-10k-2022", text_key="text")

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
        qa_chain = ConversationalRetrievalChain.from_llm(
            llm, retriever=vectorstore.as_retriever(search_kwargs={'k': 2}), return_source_documents=True)

        # data transform for past messages (list of messages -> tuple of)
        if past_messages:
            temp = []
            for i in range(0, len(past_messages), 2):
                # print(i, flush=True)
                temp.append((past_messages[i], past_messages[i + 1]))
            past_messages = temp

        # return qa_chain({"query": query})
        # print(past_messages, flush=True)
        # print(
        #     qa_chain({"question": query, "chat_history": past_messages}), flush=True)
        return qa_chain({"question": query, "chat_history": past_messages})
        # return qa_chain({"question": query, "chat_history": past_messages})

    except Exception as e:
        print('An error occurred:', e, flush=True)
