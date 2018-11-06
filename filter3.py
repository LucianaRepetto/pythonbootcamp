names= ["Colt", "Luciana", "Magda"]

#Return a new list with the string "Yout instructor is"+ each value un the array, but only if the value
# is less than 5 char.

combine = list(map(lambda name: f"Tu instrunctor es {name}",
                filter(lambda value: len(value) < 5, names)))

# En list comprehension seria:
[f"Tu instructor es {name}" for name in names if len(name) > 5]