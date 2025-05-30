from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

# Create and saves a vector store
def create_vector_store(file):
    dir_name = os.path.dirname(__file__)
    
    file_path = file
    persistant_directory = os.path.join(dir_name, 'db_store', 'chroma_db_romeo_juliet')

    # Load data from document - (Single Chunk)
    loader = TextLoader(file_path)
    document_data = loader.load()

    # Split text in chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(document_data)

    # Create embeddings function
    embeddings = GoogleGenerativeAIEmbeddings(
        model='models/embedding-001',
    )

    # Create and save a vector store
    db = Chroma.from_documents(docs, embeddings, persist_directory=persistant_directory)
    print("Vector store created successfully")


# Returns a combined string of similar docs
def get_similar_docs(query):
    current_dir = os.path.dirname(__file__)
    persistant_directory = os.path.join(current_dir, "db_store", "chroma_db_romeo_juliet")

    # Get the embeddings function
    embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001')

    # Get the stored Vector db
    db = Chroma(
        persist_directory=persistant_directory,
        embedding_function=embeddings
    )

    # Set up the retriever
    retriever = db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3},
    )
    relevant_docs = retriever.invoke(query)

    doc_content = []

    for i, doc in enumerate(relevant_docs, 1):
        doc_content.append(f"\n{doc.page_content}\n")
    return '\n'.join(doc_content)