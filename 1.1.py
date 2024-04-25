while True:
    try: 
        user_input = int(input("Enter the outside temperature in Fahrenheit: "))
        if user_input < -130 or user_input > 140:
            print("Temperature values outside reasonable limits.")
    except ValueError:
        print("Input is not a number. ")

        