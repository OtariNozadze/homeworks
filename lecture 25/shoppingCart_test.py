import unittest
from shoppingCart import ShoppingCart
class TestShoppingcart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
        self.cart.add_item("Laptop", 1500, 4)
        self.cart.add_item("Mouse", 100, 2)

    def test_is_empty(self):
        self.assertFalse(self.cart.is_empty())
        self.cart.remove_item("Laptop")
        self.cart.remove_item("Mouse")
        self.assertTrue(self.cart.is_empty())
        
    
    def test_add_item(self):
        with self.assertRaises(ValueError) as context:
            self.cart.add_item("Mouse", 100, 0)
        self.assertEqual(str(context.exception), ("Quantity must be greater than 0"))

        with self.assertRaises(ValueError) as context:
            self.cart.add_item("Headphones", 150, -2)
        self.assertEqual(str(context.exception), ("Quantity must be greater than 0"))

        self.cart.add_item("Keyboard", 500, 4)
        expected_item = {
            'name': "Keyboard",
            'price': 500,
            'quantity': 4
        }
        self.assertEqual(self.cart.items[2], expected_item)

    def test_total_price(self):

        self.assertEqual(self.cart.total_price(), 6200)
    
    def test_remove_item(self):
        expected_item = [{'name': "Laptop", 'price': 1500, 'quantity': 4}]
        self.cart.remove_item("Mouse")
        self.assertEqual(self.cart.items, expected_item)

        

        

                
    

    


if __name__ == "__main__":
    unittest.main()

        

        