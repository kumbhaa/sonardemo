import os


def insecure_command_execution(user_input):
    # Security Issue: Command injection vulnerability
    os.system(f"echo {user_input}")

# Example usage
insecure_command_execution("hello; rm -rf /")


import sqlite3

def insecure_sql_query(user_input):
    # Security Issue: SQL Injection vulnerability
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    cursor.execute(query)
    conn.close()

# Example usage
insecure_sql_query("admin' OR '1'='1")


# Security Issue: Hardcoded credentials
def get_api_key():
    api_key = "12345-ABCDE-SECRET"
    return api_key


import hashlib

def insecure_hashing(data):
    # Security Issue: Using a weak hashing algorithm (MD5)
    return hashlib.md5(data.encode()).hexdigest()

# Example usage
print(insecure_hashing("password"))
