import zoneinfo 
from datetime import datetime

from fastapi import FastAPI
from models import Customer, Transaction, Invoice, CustomerCreate
from db import SessionDep

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hola, Mundo"}


country_timezones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City"
}

@app.get("/time/{iso_code}")
async def time(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    tz = zoneinfo.ZoneInfo(timezone_str)
    return {"time": datetime.now(tz)}


db_customers: list[Customer] = []

@app.post("/customers", response_model = Customer)
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    customer = Customer.model_validate(customer_data.model_dump())
    customer.id = len(db_customers)
    db_customers.append(customer)
    return customer

@app.post("/transactions")
async def create_transactions(transactions_data: Transaction):
    return transactions_data

@app.post("/invoice")
async def create_invoices(invoices_data: Invoice):
    return invoices_data
