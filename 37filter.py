users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]
#extraer los usuarios inactivos:
inactive_users = list(filter(lambda u: not u['tweets'], users))
#inactive_users = list(filter(lambda u: len(u['tweets']) == 0, users))

#extraer los usuarios inactivos usando list comprehension:
inactive_users2= [user for user in users if not user["tweets"]]

# extraer el username de los usuarios inactivos combinando map y filter: 
usernames = list(map(lambda user: user["username"].upper(), 
	filter(lambda u: not u['tweets'], users)))

# extraer el username de los usuarios inactivos w/ list comprehension
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]



 