import random

products = {
    "1": {"name": "T-shirt", "price": 15},
    "2": {"name": "Jeans", "price": 30},
    "3": {"name": "Sneakers", "price": 50},
    "4": {"name": "Backpack", "price": 40},
    "5": {"name": "Watch", "price": 100}
}

orders = {
    "1": {"product_id": "1", "quantity": 2},
    "2": {"product_id": "3", "quantity": 1},
}

def respond_to_query(query):
    query = query.lower()
    
    if "hello" in query or "hi" in query:
        return "Hi there! How can I assist you today?"
    
    elif "product" in query:
        return "Sure, we have a variety of products available. What are you looking for?"
    
    elif "order" in query:
        return "Sure, what product would you like to order and how many?"
    
    elif "status" in query:
        order_id = input("Please provide your order ID: ")
        if order_id in orders:
            order = orders[order_id]
            product_id = order["product_id"]
            product_name = products[product_id]["name"]
            quantity = order["quantity"]
            total_price = quantity * products[product_id]["price"]
            return f"Your order for {quantity} {product_name}(s) is on its way! Total: ${total_price}"
        else:
            return "Sorry, I couldn't find any order with that ID."
    
    elif "thanks" in query or "thank you" in query:
        return "You're welcome! If you need further assistance, feel free to ask."
    
    elif "bye" in query or "exit" in query:
        return "Thank you for using our chatbot. Have a great day!"
    
    elif any(word.isdigit() for word in query.split()) and any(word in query.lower() for word in products.values()):
        quantity = [int(word) for word in query.split() if word.isdigit()][0]
        product_name = next((product["name"] for product in products.values() if product["name"].lower() in query), None)
        product_id = next((key for key, value in products.items() if value["name"].lower() == product_name.lower()), None)
        if product_id and quantity > 0:
            order_id = str(len(orders) + 1)
            orders[order_id] = {"product_id": product_id, "quantity": quantity}
            total_price = quantity * products[product_id]["price"]
            return f"Your order for {quantity} {product_name}(s) has been placed! Total: ${total_price}"
        else:
            return "I'm sorry, I couldn't understand your order. Please try again."
    
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase your question?"

def main():
    print("Welcome to our e-commerce chatbot!")
    print("How can I assist you today?")
    
    while True:
        user_query = input("You: ")
        response = respond_to_query(user_query)
        print("Bot:", response)
        if "bye" in user_query or "exit" in user_query:
            break

if __name__ == "__main__":
    main()
