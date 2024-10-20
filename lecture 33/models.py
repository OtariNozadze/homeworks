from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

host = 'localhost'
port = 5432
database = 'lectures'
user = 'postgres'
password = 'otari321'

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')
Base = declarative_base()

class Product(Base):
    __tablename__ = 'product'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(20))
    price = Column('price', Float)
    quantity_in_stock = Column('quantity_in_stock', Integer)

    def __init__(self, name, price, quantity_in_stock):
        self.name = name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

class CartItems(Base):
    __tablename__ = 'cartitems'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    product_id = Column('product_id', Integer, ForeignKey('product.id'))
    quantity = Column('quantity', Integer)

    def __init__(self, product_id, quantity):
        product = session.query(Product).filter(Product.id == product_id).first()

        if not product:
            raise ValueError("Product not found")
        
        if quantity > product.quantity_in_stock or quantity <= 0:
            raise ValueError("Quantity cant be negative or quantity cannot exceed stock available")

        self.product_id = product_id
        self.quantity = quantity

class Order(Base):
    __tablename__ = 'order'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    order_date = Column('order_date', Date)
    total_amount = Column('total_amount', Float)

    def __init__(self, order_date):
        self.order_date = order_date
        self.total_amount = 0.0


class OrderItem(Base):
    __tablename__ = 'orderitem'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    order_id = Column('order_id', Integer, ForeignKey('order.id'))
    product_id = Column('product_id', Integer, ForeignKey('product.id'))
    quantity = Column('quantity', Integer)
    price_per_item = Column('price_per_item', Float)

    def __init__(self, order_id, product_id, quantity):
        
        product = session.query(Product).filter(Product.id == product_id).first()
        
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price_per_item = product.price


product1 = Product(name='Laptop', price=999.99, quantity_in_stock=50)
product2 = Product(name='Smartphone', price=599.99, quantity_in_stock=150)
product3 = Product(name='Headphones', price=199.99, quantity_in_stock=200)
product4 = Product(name='Smartwatch', price=299.99, quantity_in_stock=75)
product5 = Product(name='Tablet', price=399.99, quantity_in_stock=100)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
session.add(product1)
session.add(product2)
session.add(product3)
session.add(product4)
session.add(product5)
session.commit()


