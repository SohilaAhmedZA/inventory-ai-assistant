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

 *FastAPI backend with REST endpoints
 *SQL Server database integration
 *AI question answering using local LLM (Ollama + Llama)
 *Automated inventory summaries
 *Streamlit analytics dashboard
 *Docker environment support
 *Clean modular project structure

---

#  Architecture

<img width="1749" height="326" alt="mermaid-diagram (1)" src="https://github.com/user-attachments/assets/b791e08d-fb64-4322-9020-b8ff7612a4ea" />


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

#  Project Structure

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

#  Setup Instructions

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

#  Screenshots




https://github.com/user-attachments/assets/aa09be6d-51f4-4e54-8e33-d0ff7d6cd32d





## Dashboard

<img width="1792" height="1120" alt="Screenshot 2026-02-27 at 7 23 08 AM" src="https://github.com/user-attachments/assets/615071d7-1ca8-4f46-8dc6-266a7582fce8" />


## AI Chat

<img width="1792" height="1120" alt="Screenshot 2026-02-27 at 7 23 26 AM" src="https://github.com/user-attachments/assets/4b9194b3-20bf-4f96-9d03-f475fb176db6" />
<img width="1792" height="1120" alt="Screenshot 2026-02-27 at 6 29 49 AM" src="https://github.com/user-attachments/assets/4dd0bb43-516f-423d-86ed-2be227a1015b" />
<img width="1792" height="1120" alt="Screenshot 2026-02-27 at 6 32 38 AM" src="https://github.com/user-attachments/assets/e03c0757-e70a-4cfa-a899-5446b36c4548" />
<img width="1792" height="1120" alt="Screenshot 2026-02-27 at 7 26 44 AM" src="https://github.com/user-attachments/assets/c93a1e94-6adf-4f88-804d-20aba8c0ee26" />







# 🧪 How It Works

1️) Streamlit sends user question
2️) FastAPI receives request
3️) API queries SQL database
4️) Data sent to LLM
5️) AI generates explanation
6️) Response returned to UI

---

#  Future Improvements

* Role-based authentication
* Real-time data streaming
* Cloud deployment (AWS / Azure)
* Vector database for semantic search
* Advanced analytics & forecasting
* CI/CD pipeline

---

#  Security Notes

This project uses local credentials and is intended for demonstration purposes.

For production:

* Use environment variables
* Implement secrets management
* Add authentication

---

#  Scalability Vision

The system can evolve into a production-grade platform by:

* Migrating to cloud databases
* Container orchestration (Kubernetes)
* API gateway integration
* Monitoring with Prometheus/Grafana

---

#  Portfolio Value

This project demonstrates:

✔ Full-stack development
✔ AI integration with business data
✔ API design
✔ Data engineering fundamentals
✔ System architecture thinking

---

#  Credits

Developed by **Sohila Ahmed**

Built as an end-to-end AI + Data Engineering portfolio project.

---

#  License

This project is licensed under the MIT License.

---

⭐ If you found this project interesting, consider starring the repo!
