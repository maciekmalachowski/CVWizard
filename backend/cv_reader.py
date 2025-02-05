from llama_index.core import VectorStoreIndex
from llama_index.core.node_parser import MarkdownNodeParser
from llama_index.readers.docling import DoclingReader
from llama_index.embeddings.openai import OpenAIEmbedding
from dotenv import load_dotenv

def read_cv(source):
    load_dotenv()
    reader = DoclingReader()
    node_parser = MarkdownNodeParser()
    embed_model = OpenAIEmbedding(model="text-embedding-3-large")

    index = VectorStoreIndex.from_documents(
        documents=reader.load_data(source),
        transformations=[node_parser],
        embed_model=embed_model
    )

    return index

def retrieve_relevant_info(index, query):
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    return response.response



# insights_query = "Summarize this CV and highlight key skills."
# insights = retrieve_relevant_info(read_cv("C:/Users/Maciek/Downloads/Resume-EN.pdf"), insights_query)
# print(insights)