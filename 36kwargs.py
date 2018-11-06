def fave_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favorite color ir {color}")

fave_colors(colt="purple", ruby="red", ethel="teal")