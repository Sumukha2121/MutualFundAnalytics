import os
from sqlalchemy import create_engine, text

# Database file
db_file = "bluestock_mf.db"

# Delete old database if it exists
if os.path.exists(db_file):
    os.remove(db_file)
    print("Old database deleted.")

# Create new database
engine = create_engine(f"sqlite:///{db_file}")

# Read schema.sql
with open("schema.sql", "r") as file:
    schema = file.read()

# Execute SQL statements
with engine.connect() as connection:
    for statement in schema.split(";"):
        statement = statement.strip()
        if statement:
            connection.execute(text(statement))
    connection.commit()

print("Database and tables created successfully.")