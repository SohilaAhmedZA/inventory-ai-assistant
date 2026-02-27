from sqlalchemy import create_engine, text

DATABASE_URL = "mssql+pyodbc://sa:YourStrong!Passw0rd@localhost:1433/InventoryDB?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"

engine = create_engine(DATABASE_URL)

def test_connection():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("✅ Connected to SQL Server:", result.scalar())

if __name__ == "__main__":
    test_connection()