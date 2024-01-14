import sqlite3
import random
from faker import Faker

conn = sqlite3.connect(r'C:\Users\Valet\Desktop\Shop-laba\shop.db')


c = conn.cursor()

faker = Faker()

#####################################!Provider##########################################

# for i in range(1, 101):
#     name = f"provider{i}_" + faker.user_name()
#     email = f"{i}_" + faker.email()
#     values = (
#         i, 
#         name,
#         faker.address(), 
#         email
#         )
#     c.execute("INSERT INTO Provider VALUES (?, ?, ?, ?)", values)



#####################################!Products##########################################

# for i in range(1, 1000001):
#     values = (
#         i,                                    #id
#         f'Product_name{i}',                   #product_name
#         f'Description{i}',                    #product_description
#         random.randint(1, 30),                #product_category
#         random.randint(1, 300),               #product_brand
#         random.randint(1, 100),               #product_provider
#         random.randint(1, 10),                #product_material
#         random.randint(1, 13),                #product_size
#         random.randint(1, 15),                #product_color
#         round(random.uniform(1000, 10000), 2) #product_price
#         )   
#     c.execute("INSERT INTO Products VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", values)


#####################################!Clients##########################################

# for i in range(1, 100001):
#     print(i)
#     username = f"user{i}_" + faker.user_name()
#     email = f"{i}_" + faker.email()
#     fio = faker.first_name() +' ' + faker.last_name()
#     values = (
#         i, 
#         username,
#         faker.password(), 
#         faker.phone_number(),
#         email, 
#         fio,
#         faker.address()
#         )
#     c.execute("INSERT INTO Clients VALUES (?, ?, ?, ?, ?, ?, ?)", values)


#####################################!Item_in_carts##########################################

# for i in range(1, 100001):
#     print(i)
#     values = (
#         i,                                   
#         random.randint(1, 100000),                #client_id
#         random.randint(1, 1000000),               #product_id
#         random.randint(1, 100),                   #item_count
#         )   
#     c.execute("INSERT INTO Item_in_carts VALUES (?, ?, ?, ?)", values)



#####################################!Orders##########################################

# for i in range(1, 100001):
#     print(i)
#     values = (
#         i,                                        #order_id
#         random.randint(1, 100000),                #client_id
#         faker.date(),              
#         round(random.uniform(1000, 10000), 2)
#         )   
#     c.execute("INSERT INTO Orders VALUES (?, ?, ?, ?)", values)



#####################################!Item_in_order##########################################

# for i in range(1, 100001):
#     print(i)
#     values = (
#         i,                                   
#         random.randint(1, 100000),                #client_id
#         random.randint(1, 1000000),               #order_id
#         random.randint(1, 10),                   #item_count
#         )   
#     c.execute("INSERT INTO Item_in_order VALUES (?, ?, ?, ?)", values)


conn.commit()
conn.close()
