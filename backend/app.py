from fastapi import FastAPI
import requests
from sqlalchemy import create_engine, text

DATABASE_URL = "mssql+pyodbc://sa:YourStrong!Passw0rd@localhost:1433/InventoryDB?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"

engine = create_engine(DATABASE_URL)
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Inventory AI Backend Running 🚀"}


@app.get("/ask-ai")
def ask_ai(question: str):

    # Detect if question is about inventory/business data
    if any(word in question.lower() for word in ["inventory", "summary", "items", "customers", "vendors", "orders"]):
        
        query = """
        SELECT
            (SELECT COUNT(*) FROM Customers) AS customers,
            (SELECT COUNT(*) FROM Vendors) AS vendors,
            (SELECT COUNT(*) FROM Items) AS items,
            (SELECT COUNT(*) FROM SalesOrders) AS sales_orders
        """

        with engine.connect() as conn:
            result = conn.execute(text(query)).mappings().first()

        context = f"""
        Customers: {result['customers']}
        Vendors: {result['vendors']}
        Items: {result['items']}
        Sales Orders: {result['sales_orders']}
        """

        prompt = f"""
        You are a business analyst.

        Using this real inventory data:
        {context}

        Answer this question clearly:
        {question}
        """

    else:
        # Normal AI question (no DB)
        prompt = question

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()
    return {"answer": data["response"]}



@app.get("/inventory-summary")
def inventory_summary():
    query = """
    SELECT
        (SELECT COUNT(*) FROM Customers) AS customers,
        (SELECT COUNT(*) FROM Vendors) AS vendors,
        (SELECT COUNT(*) FROM Items) AS items,
        (SELECT COUNT(*) FROM SalesOrders) AS sales_orders
    """

    with engine.connect() as conn:
        result = conn.execute(text(query)).mappings().first()

    return result



@app.get("/ai-inventory-overview")
def ai_inventory_overview():
    query = """
    SELECT
        (SELECT COUNT(*) FROM Customers) AS customers,
        (SELECT COUNT(*) FROM Vendors) AS vendors,
        (SELECT COUNT(*) FROM Items) AS items,
        (SELECT COUNT(*) FROM SalesOrders) AS sales_orders
    """

    with engine.connect() as conn:
        result = conn.execute(text(query)).mappings().first()

    summary_text = f"""
    Customers: {result['customers']}
    Vendors: {result['vendors']}
    Items: {result['items']}
    Sales Orders: {result['sales_orders']}
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": f"Explain this inventory summary in simple business language:\n{summary_text}",
            "stream": False
        }
    )

    data = response.json()

    return {
        "data": result,
        "ai_explanation": data["response"]
    }
