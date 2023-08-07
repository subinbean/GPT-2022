from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader('assets/Apple-10k-2022.pdf')
pages = loader.load_and_split()
print(pages[0])
