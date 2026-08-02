from prompts.sql_prompt import PROMPT
from utils.groq_helper import ask_llm
from utils.db_helper import run_query

question = "Show employees whose salary is greater than 50000."

prompt = PROMPT.format(question=question)

sql_query = ask_llm(prompt)

print("\nGenerated SQL query:\n")
print(sql_query)

result = run_query(sql_query)

print("\nResult:\n")
print(result)
