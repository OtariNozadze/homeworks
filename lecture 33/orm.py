from datetime import date
from models import session, Product, CartItems, Order, OrderItem
def main():
    while True:
        print('''1 - see cart
              2 - add to cart
              3 - delete products from cart
              4 - order
              5 - see orders
        ''')
        choice = input("Input Your Choice: ")
        if choice == '1':
            cart = session.query(CartItems).all()
            for i in cart:
                print(i)
        elif choice == '2':
            add_item = input("Input Item Id You Want To Add: ")
            add_quantity = input("Input Quantity You Want To Add: ")
            add_to_cart = CartItems(add_item, add_quantity)
        elif choice == '3':
            item_id = input("Input Item Id You Want To Delete: ")
            delete_cart = session.query(CartItems).filter(CartItems.product_id == item_id)
            if delete_cart:
                session.delete(delete_cart)
                session.commit()
            else:
                print("Item not in cart")

        elif choice == '4':
            order_date = date.today()
            new_order = Order(order_date)
            session.add(new_order)
            session.commit()
            cart_items = session.query(CartItems).all()
            total_amount = 0

            for item in cart_items:
                order_item = OrderItem(new_order.id, item.product_id, item.quantity)
                total_amount += order_item.quantity * order_item.price_per_item
                session.add(order_item)
            new_order.total_amount = total_amount
            session.add(new_order)
            session.commit()

            session.query(CartItems).delete()
            session.commit()
            print("Order placed successfully.")

        elif choice == '5':
            orders = session.query(Order).all()
            for order in orders:
                print(f"Order ID: {order.id}, Date: {order.order_date}, Total Amount: {order.total_amount}")

main()


        