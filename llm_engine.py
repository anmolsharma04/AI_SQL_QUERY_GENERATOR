from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os

def generate_sql(schema_info, user_question):

    llm = ChatGroq(
        model_name="llama-3.1-8b-instant",
        temperature=0.4
    )

    template = """
    You are an expert SQL query generator.

    Table Name: dataset_table

    Available Columns:
    {schema}

    User Question:
    {user_question}

    Rules:
    - Only use the available columns.
    - Return only SQL query.
    - Do not explain.

    Generate SQL:
    """

    prompt = PromptTemplate(
        input_variables=["schema", "user_question"],
        template=template
    )

    formatted_prompt = prompt.format(
        schema=schema_info,
        user_question=user_question
    )

    response = llm.invoke(formatted_prompt)

    return response.content
