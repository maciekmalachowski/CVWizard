from llama_index.core import VectorStoreIndex
from llama_index.core.node_parser import MarkdownNodeParser
from llama_index.readers.docling import DoclingReader
from llama_index.embeddings.openai import OpenAIEmbedding
from dotenv import load_dotenv

def read_cv(source):
    # load_dotenv()
    # reader = DoclingReader()
    # node_parser = MarkdownNodeParser()
    # embed_model = OpenAIEmbedding(model="text-embedding-3-small")

    # index = VectorStoreIndex.from_documents(
    #     documents=reader.load_data(source),
    #     transformations=[node_parser],
    #     embed_model = embed_model
    # )

    # pdf_engine = index.as_query_engine()

    # return pdf_engine
    print("cv reader")