# 🤖 Inventory AI Assistant

An AI-powered inventory analytics dashboard that combines **FastAPI**, **SQL Server**, and a local **LLM (Llama via Ollama)** to provide intelligent insights and conversational access to business data.

---

#  Project Overview

Inventory AI Assistant is a full-stack data application designed to demonstrate how modern AI can integrate with enterprise data systems.

It allows users to:

* Query inventory data using natural language
* View business KPIs in a modern dashboard
* Generate AI explanations of database metrics
* Connect a backend API with a local LLM

The project simulates a real-world scenario where AI augments decision-making in inventory and operations management.

---

#  Key Features

✅ FastAPI backend with REST endpoints
✅ SQL Server database integration
✅ AI question answering using local LLM (Ollama + Llama)
✅ Automated inventory summaries
✅ Streamlit analytics dashboard
✅ Docker environment support
✅ Clean modular project structure

---

#  Architecture

User → Streamlit UI → FastAPI Backend → SQL Server
↘
AI Model (Ollama)

---

#  Tech Stack

**Backend**

* FastAPI
* SQLAlchemy
* PyODBC

**AI**

* Ollama
* Llama 3

**Frontend**

* Streamlit
* Plotly

**Database**

* Microsoft SQL Server

**DevOps**

* Docker
* GitHub

---

# 📂 Project Structure

```
inventory-ai-assistant/
│
├── backend/
│   └── app.py              # FastAPI application
│
├── docker/
│   └── docker-compose.yml  # Services setup
│
├── ui.py                   # Streamlit dashboard
├── db.py                   # Database connection logic
├── test_ollama.py          # AI connectivity test
├── .gitignore
└── README.md
```

---

# ⚙️ Setup Instructions

## 1️ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/inventory-ai-assistant.git
cd inventory-ai-assistant
```

---

## 2️ Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
# venv\Scripts\activate    # Windows
```

---

## 3️ Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy pyodbc requests streamlit plotly pandas
```

---

## 4️ Start the database

Make sure SQL Server is running locally and create:

Database name:

```
InventoryDB
```

Tables expected:

* Customers
* Vendors
* Items
* SalesOrders

---

## 5️ Run the AI model (Ollama)

```bash
ollama run llama3
```

---

## 6️ Start backend API

```bash
cd backend
uvicorn app:app --reload
```

API docs will be available at:

👉 http://localhost:8000/docs

---

## 7️ Run the dashboard

```bash
streamlit run ui.py
```

Dashboard will open at:

👉 http://localhost:8501

---

# Example Questions You Can Ask the AI

* “Explain the current inventory overview”
* “How many customers are in the system?”
* “Give me a business summary of the data”
* “What does this inventory snapshot mean?”

---

# 📸 Screenshots

## Dashboard

*Add screenshot here*

## AI Chat

*Add screenshot here*

## API Docs

*Add screenshot here*

## Architecture Diagram

*Add screenshot here*

---

# 🧪 How It Works

1️⃣ Streamlit sends user question
2️⃣ FastAPI receives request
3️⃣ API queries SQL database
4️⃣ Data sent to LLM
5️⃣ AI generates explanation
6️⃣ Response returned to UI

---

# 📈 Future Improvements

* Role-based authentication
* Real-time data streaming
* Cloud deployment (AWS / Azure)
* Vector database for semantic search
* Advanced analytics & forecasting
* CI/CD pipeline

---

# 🔐 Security Notes

This project uses local credentials and is intended for demonstration purposes.

For production:

* Use environment variables
* Implement secrets management
* Add authentication

---

# 🌍 Scalability Vision

The system can evolve into a production-grade platform by:

* Migrating to cloud databases
* Container orchestration (Kubernetes)
* API gateway integration
* Monitoring with Prometheus/Grafana

---

# 🎯 Portfolio Value

This project demonstrates:

✔ Full-stack development
✔ AI integration with business data
✔ API design
✔ Data engineering fundamentals
✔ System architecture thinking

---

# 🙌 Credits

Developed by **Sohila Ahmed**

Built as an end-to-end AI + Data Engineering portfolio project.

---

# 📜 License

This project is licensed under the MIT License.

---

⭐ If you found this project interesting, consider starring the repo!
