import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")


def generate_python_code(user_input, extracted_keywords):
    genai.configure(api_key=api_key)

    prompt = f"""
        You are a Python code generator. Strictly follow these rules when generating Python code:

        1. Use only the variable names from the provided keyword list.
        2. Do not modify, rename, or merge any keywords. Use them exactly as they appear.
        3. Map the correct variable names from the list to match their intended functionality in Python code.
        4. If a necessary variable name is missing from the keyword list, do not create a new one—instead, return an error message.
        5. Generate only Python code as output—no explanations, comments, or extra text.

         Keyword List:
        {extracted_keywords}  

         User Request:
        {user_input}  

        Now generate the correct Python script while strictly following these rules.

    """

    response = genai.GenerativeModel("gemini-2.0-flash").generate_content(prompt)

    return response.text

