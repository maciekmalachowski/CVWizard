from llama_index.core import VectorStoreIndex
from llama_index.core.node_parser import MarkdownNodeParser
from llama_index.readers.docling import DoclingReader
from llama_index.embeddings.openai import OpenAIEmbedding
from dotenv import load_dotenv
import json

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
    
    try:
        return json.loads(response.response)  # Convert string response to dictionary
    except json.JSONDecodeError:
        print("Error: AI response is not valid JSON. Check the query formatting.")
        return None  # Handle potential formatting issues



# insights_query = """
# Extract key skills, spoken languages, and a summary from the given CV.

# 1. For each job listed in the CV, extract the relevant skills mentioned in the job title, description, and responsibilities.
# 2. For each project listed in the CV, identify the skills and technologies used, including any specific tools, languages, or methods mentioned.
# 3. List all spoken languages explicitly mentioned in the CV, whether in the personal details, education, or language sections.
# 4. Generate a brief summary of the candidate's experience, highlighting key industries, expertise areas, years of experience, and any notable achievements. The summary should be a well-structured text paragraph.
# 5. Return the output **strictly** as a valid JSON object with the following structure:

# {
#     "summary": "John Doe is a software engineer with 5 years of experience in the finance and healthcare industries. He specializes in machine learning, full-stack development, and cloud computing. Notable achievements include developing an AI-powered chatbot that reduced customer support response time by 40% and leading a team of 5 engineers to build a scalable data pipeline for financial analytics.",
#     "skills": ["Python", "HTML", "Numpy", "Pandas", "Docker", "Java", "Jupyter Notebook", "LLMs", "Langchain", "LlamaIndex", "AutoML", "Scikit-learn", "Hugging Face"],
#     "languages": ["English", "Spanish"]
# }

# Ensure the AI carefully considers each job and project and accurately identifies skills and languages. The summary should be **concise yet informative**, capturing the candidate’s key strengths and accomplishments in natural language. Do not include any additional text, explanations, or formatting outside of this JSON structure.
# """



# insights = retrieve_relevant_info(read_cv("C:/Users/Maciek/Downloads/Resume-EN.pdf"), insights_query)
# print(insights)