from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Database connection
engine = create_engine('sqlite:///shop.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Table for Users
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    email = Column(String(200), nullable=False)

    orders = relationship("Order", back_populates="user")

# Table for Products
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    price = Column(Integer)

    orders = relationship("Order", back_populates="product")

T# Table for Orders
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)

    user = relationship("User", back_populates="orders")
    product = relationship("Product", back_populates="orders")


# Create tables
Base.metadata.create_all(engine)

# Seed data
user1 = User(name="Isaiah", email="isaiahb@example.com")
user2 = User(name="Dayana", email="day98@example.com")

product1 = Product(name="Laptop", price=1200)
product2 = Product(name="Mouse", price=35)
product3 = Product(name="Notebook", price=12)

session.add(user1)
session.add(user2)
session.add(product1)
session.add(product2)
session.add(product3)
session.commit()

order1 = Order(user_id=user1.id, product_id=product1.id, quantity=2)
order2 = Order(user_id=user1.id, product_id=product2.id, quantity=3)
order3 = Order(user_id=user2.id, product_id=product3.id, quantity=4)
order4 = Order(user_id=user2.id, product_id=product1.id, quantity=1)

session.add(order1)
session.add(order2)
session.add(order3)
session.add(order4)
session.commit()

print("Seed data inserted successfully.")

# Retrieve all users and print their information
print("\nUsers:")
for user in session.query(User).all():
    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")

# Retrieve all products and print their name and price
print("\nProducts:")
for product in session.query(Product).all():
    print(f"Name: {product.name}, Price: ${product.price}")

# Retrieve all orders and show user name, product name, and quantity
print("\nOrders:")
for order in session.query(Order).all():
    user_name = order.user.name if order.user else "Unknown user"
    product_name = order.product.name if order.product else "Unknown product"
    print(f"User: {user_name}, Product: {product_name}, Quantity: {order.quantity}")

# Update a product's price
product_to_update = session.query(Product).filter_by(name="Mouse").first()
if product_to_update:
    product_to_update.price = 45
    session.commit()
    print(f"\nUpdated Mouse price to ${product_to_update.price}")

# Delete a user by ID
user_to_delete = session.get(User, 1)
if user_to_delete:
    session.delete(user_to_delete)
    session.commit()
    print("\nDeleted user with ID 1")

# Print final data after update/delete
print("\nFinal Users:")
for user in session.query(User).all():
    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")

print("\nFinal Products:")
for product in session.query(Product).all():
    print(f"Name: {product.name}, Price: ${product.price}")