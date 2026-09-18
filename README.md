# SQL_Alchemy

### Introduction

The purpose of this project is to show how SQL Alchemy works with Python. Within this project I showcased how to create and manage a relational database using both Python and SQL Alchemy. This project also showcases how to define/create tables, set up relationships, inseart/delete data and perform basic Python queries to print the information.

## Breakdown

1) Defining/Creating Tables and Using Relationships

<img width="1220" height="1362" alt="image" src="https://github.com/user-attachments/assets/af99c3db-6040-42dc-a7f7-b855bfd81c33" />

Here we created (3) tables (User, Product, Order). We created an id, also known as a primary key for each table to identify what is being referenced in the table. The rest of the table are column labels for the information you want to store in the table. Under each table we use a relationship function that connects there tables. We finalize creating the tables by using Base.metadata.create_all(engine).

2) Inserting Data

<img width="1472" height="1157" alt="image" src="https://github.com/user-attachments/assets/3cd32525-3ccc-4213-9e0b-c1b76ba6941b" />

Using session.add() we were able to insert 2 users, 3 products and 4 orders to the table. Once added we use session.commit() to process the data we added and I created a print to let me know the data was inserted successfully.

3) Queries

<img width="1481" height="1474" alt="image" src="https://github.com/user-attachments/assets/35c731d2-69cd-46d9-a02f-c6d6b367795e" />

  - Query 1: Retrieve all users and print information - For all Users in the query, referencing the User table we pulled the ID, name and email of the users I uploaded.
  - Query 2: Retrieve all products and print their name and price - For all Products in the query, referencing the Product table we pulled the product name and price of the products I created.
  - Query 3: Retrieve all orders, showing the user's name, product name and quantity - Here is where the relationship function shows that allows the User to have many orders and allows the products to show in many orders.
  - Query 4: Update a product's price - I chose to update the mouse price to $45 by creating product_to_update function 
  - Query 5: Delete a user by ID - I chose to delete user 1 by creating user_to_delete function.


