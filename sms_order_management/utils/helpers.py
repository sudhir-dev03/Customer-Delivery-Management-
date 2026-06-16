import uuid

def generate_order_id():

    return "ORD-" + str(uuid.uuid4())[:8]