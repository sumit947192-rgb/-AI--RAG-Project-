import google.generativeai as genai
from dotenv import load_dotenv
import os 

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-3-flash-preview")


def generate_answers(query, docs):
    context = "\n\n".join([doc.page_content for doc in docs[:5]])
    prompt = f"""
    Answer the question based only on context below.
    Cite the source. 
    Context:
    {context}
    Question:
    {query}
    """

    response = model.generate_content(prompt)
    return response.text


