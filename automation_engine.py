import re

# Extract numeric ID from ticket
def extract_id(ticket):
    match = re.search(r'\d{4,}', ticket)
    if match:
        return match.group()
    return "UNKNOWN"

# Automation functions
def restart_sync(shipment_id):
    return f"Shipment {shipment_id} sync restarted successfully."

def refund_payment(order_id):
    return f"Refund initiated for order {order_id}."

def retrigger_api(order_id):
    return f"API retriggered for order {order_id}."

def update_eta(order_id):
    return f"ETA updated and driver reassigned for shipment {order_id}."

def resync_inventory(order_id):
    return f"Warehouse inventory re-synced for order {order_id}."

# Main handler
def handle_automation(issue_type, ticket):

    extracted_id = extract_id(ticket)

    if issue_type == "tracking":
        return restart_sync(extracted_id)

    elif issue_type == "payment":
        return refund_payment(extracted_id)

    elif issue_type == "api_failure":
        return retrigger_api(extracted_id)

    elif issue_type == "delivery_delay":
        return update_eta(extracted_id)

    elif issue_type == "warehouse_sync":
        return resync_inventory(extracted_id)

    else:
        return "Escalated to human support."

# import re

# # -----------------------------
# # Extract ID from ticket
# # -----------------------------
# def extract_id(ticket):
#     match = re.search(r'\d{4,}', ticket)
#     if match:
#         return match.group()
#     return "UNKNOWN"

# # -----------------------------
# # Tool Functions
# # -----------------------------
# def restart_sync(shipment_id):
#     return f"Shipment {shipment_id} sync restarted successfully."

# def refund_payment(order_id):
#     return f"Refund initiated for order {order_id}."

# def retrigger_api(order_id):
#     return f"API retriggered for order {order_id}."

# def update_eta(order_id):
#     return f"ETA updated and driver reassigned for shipment {order_id}."

# def resync_inventory(order_id):
#     return f"Warehouse inventory re-synced for order {order_id}."

# # -----------------------------
# # Tool Registry
# # -----------------------------
# TOOLS = {
#     "restart_sync": restart_sync,
#     "refund_payment": refund_payment,
#     "retrigger_api": retrigger_api,
#     "update_eta": update_eta,
#     "resync_inventory": resync_inventory
# }