from sqlalchemy import create_engine

#engine = create_engine('mssql+pyodbc://<username>:<password>@<server>/<database>?driver=ODBC+Driver+18+for+SQL+Server')
# The original connection string:
# Driver={ODBC Driver 18 for SQL Server};Server=tcp:animals-jh-db-server.database.windows.net,1433;Database=animals-db;Uid=adminuser;Pwd={your_password_here};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;

# Transformed to SQLAlchemy URI:
# mssql+pyodbc://adminuser:your_password_here@animals-jh-db-server.database.windows.net:1433/animals-db?driver=ODBC+Driver+18+for+SQL+Server&Encrypt=yes&TrustServerCertificate=no&ConnectionTimeout=30

engine = create_engine('mssql+pyodbc://adminuser:<password>@animals-jh-db-server.database.windows.net:1433/animals-db?driver=ODBC+Driver+18+for+SQL+Server&Encrypt=yes&TrustServerCertificate=no&ConnectionTimeout=30')
connection = engine.connect()
print("Connection successful!")
connection.close()
