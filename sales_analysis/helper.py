# helper.py

def calculate_total(quantity, price):
    """Calcular el total para un ítem individual"""
    return quantity * price

def format_currency(amount):
    """Formatear el número como divisa en euros"""
    return f"{amount:,.2f} €"