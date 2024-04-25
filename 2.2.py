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
try: 
    adjustment_factor = (desired_servings/recipe_servings)
except ZeroDivisionError: # this should not happen because input cannot be <= 0
    print("Desired servings cannot be 0. ")
except NameError:
    print("Variable is not defined.")
else:
    if adjustment_factor == 1:
        print("Recipe servings and desired servings are equal.")
    else:
        print(f"You should multiply your serving amounts by {adjustment_factor}. ")
    
    