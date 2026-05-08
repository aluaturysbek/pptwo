import re
import json

with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()


# Prices
prices = re.findall(r"\d+\s?\d*,\d{2}", text)

clean_prices = []

for price in prices:
    value = price.replace(" ", "").replace(",", ".")
    clean_prices.append(float(value))


# Product names
products = re.findall(
    r"\d+\.\s*\n([^\n]+)",
    text
)

products = [product.strip() for product in products]


# Total amount
total_match = re.search(r"ИТОГО:\s*\n?([\d\s]+,\d{2})", text)

total = None

if total_match:
    total = total_match.group(1)
    total = total.replace(" ", "").replace(",", ".")


# Date and time
datetime_match = re.search(
    r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s*(\d{2}:\d{2}:\d{2})",
    text
)

date = None
time = None

if datetime_match:
    date = datetime_match.group(1)
    time = datetime_match.group(2)


# Payment method
payment_match = re.search(
    r"(Банковская карта|Наличные)",
    text
)

payment_method = None

if payment_match:
    payment_method = payment_match.group(1)


# Structured output
data = {
    "products": products,
    "prices": clean_prices,
    "total": total,
    "date": date,
    "time": time,
    "payment_method": payment_method
}


print(json.dumps(data, indent=4, ensure_ascii=False))