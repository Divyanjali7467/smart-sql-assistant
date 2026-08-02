PROMPT = """
Convert the following question into an SQL query.

Table name: employee

Columns:
id
name
department
salary
city

Question:
{question}

Return only the SQL query.
"""