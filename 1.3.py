while True:
    try: 
        user_input = int(input("Enter the outside temperature in Fahrenheit: "))
    except ValueError:
        print("Input is not a number. ")
    else:
        if user_input < -130 or user_input > 140:
            print("Temperature values outside reasonable limits.")
        else:
            break
def FtoC (temperature):
    try: 
        C_temp = (temperature - 32)*(5/9)
    except TypeError:
        print("An unexpected error occured.")
    except OverflowError:
        print("Math range error.")
    else: 
        print(f"Converted {user_input} degrees F to {C_temp} degrees C.")
    finally:
        print("Thank you for using weather forecast application!")

FtoC(user_input)