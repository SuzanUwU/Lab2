def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    # Code to calculate BMI
    BMI = weight / (height * height)

    # Check under, over or normal weight
    if BMI < 18.5:
        user = "Under weight"
    elif 18.5 <= BMI <= 25.0:
        user = "Normal weight"
    else:
        user = "Over weight"

    # Code to display the calculated BMI
    print("BMI is " + str(BMI) + "\nThis person is " + user)

calculate_bmi(weight=57, height=1.73)
