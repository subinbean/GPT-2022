from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
import os
from api.utils import pinecone_setup
from dotenv import load_dotenv
import pinecone
import re

load_dotenv()


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
            index, embedding=embeddings, text_key="text")

        # sanity check for retrieval
        # question = "What are some highlights for the fourth quarter of 2022?"
        # docs = vectorstore.similarity_search(question)
        # print(docs)

        # template used to prompt the model
        template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question, in its original language. At the end of standalone question add this: 'Always say "thanks for asking!" at the end of the answer.'

        Chat History:
        {chat_history}
        Follow Up Input: {question}
        Standalone question:"""

        custom_prompt = PromptTemplate.from_template(template)

        # retrieves from vector store relevant documents and passes them as context to prompt
        # k is the number of documents retrieved
        qa_chain = ConversationalRetrievalChain.from_llm(
            llm, retriever=vectorstore.as_retriever(search_kwargs={'k': 2}), condense_question_prompt=custom_prompt, return_source_documents=True)

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
