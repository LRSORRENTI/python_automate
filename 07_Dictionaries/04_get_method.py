# You can use the .get method to check if a key 
# exists in a dictionary as an easier way to check 

cats = {
    'Rufus': 'Scottish Fold',
    'Lex': "Tabby",
    "Veni": 'British Shorthair'
}

# use the .get method by padding in the desired
# key as a first argument, and the second argument
# will default to 0 if isn't found
print(cats.get('Veni', 0)) 
print(cats.get('Ven', 0)) 
# British Shorthair
# 0

# The second arguemt doesn't need to be 0,
# it could be: 
print(cats.get('Oreo', 'Not in cats dictionary'))
# Not in cats dictionary