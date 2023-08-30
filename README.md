# GPT 2022

## Project Description

GPT 2022 is a GPT 3.5-turbo Chatbot with knowledge of 2022 events. It uses retrieval-augmented generation on relevant documents (e.g 2022 annual reports) to fetch top-k similar chunks as context for user queries. Features include QA (question-answering), chat memory (remembering conversations), multi-doc fetching (fetching from multiple sources), and citations. Citations provide page number and excerpt!

## Tech Stack

The stack used for this project is: for the frontend, Next.js, TailwindCSS, and React are used. For the backend, Flask is used along with the langchain library for AI-related logic. Finally, Pinecone is used as a vector database storing embeddings of documents.

## Helpful Resources

-   https://python.langchain.com/docs/use_cases/question_answering/
-   https://python.langchain.com/docs/integrations/vectorstores/pinecone
-   https://docs.pinecone.io/docs/quickstart
-   https://github.com/mayooear/gpt4-pdf-chatbot-langchain
-   https://codevoweb.com/how-to-integrate-flask-framework-with-nextjs/
