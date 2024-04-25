while True:
    try:
        recipe_servings = float(input("How many servings does the original recipe call for? "))
    except ValueError:
        print("Input is not a number.")
    else:
        if recipe_servings <= 0:
            print("Servings amount cannot be less than or equal to 0.")
        else:
            break
while True:    
    try:
        desired_servings = float(input("How many servings do you wish to make? "))
    except ValueError:
        print("Input is not a number.")
    else:
        if desired_servings <= 0:
            print("Servings amount cannot be less than or equal to 0.")
        else:
            break