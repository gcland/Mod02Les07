while True:
    try: 
        user_input = int(input("Enter the outside temperature in Fahrenheit: "))
    except ValueError:
        print("Input is not a number. ")
    else:
        # if user_input < -130 or user_input > 140:
        #     print("Temperature values outside reasonable limits.")
        # else:
            break
def FtoC (temperature):
    try: 
        C_temp = (temperature - 32)*(5/9)
    except TypeError:
        print("An unexpected error occured.")
    except OverflowError:
        print("Math range error.")
    print(f"Converted {user_input} degrees F to {C_temp} degrees C.")

FtoC(user_input)