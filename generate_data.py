import pandas as pd
import random
import datetime

# ------------------------------------
# Helper Data
# ------------------------------------

clients = ["Flipkart", "Amazon", "Reliance", "DTDC", "Aramex", "BlueDart"]
locations = ["Dubai", "Mumbai", "Bangalore", "Riyadh", "Delhi", "London"]

def random_id():
    return random.randint(1000, 9999)

def random_time():
    hours = random.randint(1, 12)
    return f"{hours} hours"

# ------------------------------------
# Category Templates (More Realistic)
# ------------------------------------

categories = {
    "tracking": [
        "Client {client} reporting shipment ID {id} not updated in dashboard since {time}.",
        "Tracking page for order {id} shows stale information from {time} ago.",
        "Shipment {id} status stuck in transit. No webhook activity detected.",
        "Unable to refresh tracking details for shipment {id}.",
        "Delivery status not reflecting latest scan for order {id}."
    ],
    "payment": [
        "Customer charged twice for order {id}. Please verify invoice.",
        "Refund for shipment {id} not processed even after {time}.",
        "Invoice mismatch detected for order {id} from {client}.",
        "Billing amount incorrect for transaction {id}.",
        "Payment failed but amount debited for order {id}."
    ],
    "api_failure": [
        "API returning 500 error while updating shipment {id}.",
        "Webhook not triggered for client {client} order {id}.",
        "Authentication failed for API call from {client}.",
        "Timeout error observed during data sync for shipment {id}.",
        "Data sync failed between systems for order {id}."
    ],
    "delivery_delay": [
        "Shipment {id} delayed beyond SLA by {time}.",
        "Order {id} not delivered on time in {location}.",
        "Driver assigned late for delivery {id}.",
        "Delivery rescheduled for shipment {id}.",
        "Dispatch delay reported for order {id}."
    ],
    "warehouse_sync": [
        "Inventory not updated in WMS for SKU linked to order {id}.",
        "Warehouse sync issue between OMS and WMS for shipment {id}.",
        "Stock mismatch detected for product in order {id}.",
        "Order {id} not reflecting in warehouse system.",
        "Sync failure between systems affecting shipment {id}."
    ]
}

# ------------------------------------
# Generate Dataset
# ------------------------------------

data = []

for label, templates in categories.items():
    for _ in range(80):  # 80 each → 400 total
        template = random.choice(templates)
        ticket = template.format(
            client=random.choice(clients),
            id=random_id(),
            time=random_time(),
            location=random.choice(locations)
        )
        data.append([ticket, label])

# Shuffle for realism
random.shuffle(data)

df = pd.DataFrame(data, columns=["ticket_text", "label"])
df.to_csv("data/tickets.csv", index=False)

print("Improved enterprise-style dataset created with 400 tickets.")