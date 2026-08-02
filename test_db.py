from utils.db import get_data

query = "SELECT * FROM employee"

result = get_data(query)

for row in result:
    print(row)