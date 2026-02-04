fruits = [
    {"name":"Apple","calories":"130"},
    {"name":"Avocado","calories":"50"},
    {"name":"Banana","calories":"110"},
    {"name":"Cantaloupe","calories":"50"},
    {"name":"Grapefruit","calories":"60"},
    {"name":"Grapes","calories":"90"},
    {"name":"Honeydew Melon","calories":"50"},
    {"name":"kiwifruit","calories":"19"},
    {"name":"lemon","calories":"15"},
    {"name":"lime","calories":"20"},
]

item = input("Item: ")
for fruit in fruits:
    if fruit.get("name") == item:
        print("Calories:",fruit.get("calories"))
