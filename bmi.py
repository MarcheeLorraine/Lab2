def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi=(weight)/(height*height)
    print(f"Your BMI is: {bmi:.2f}")
    if bmi >= 18.5 :
        if bmi <= 25.0 :
            print("You are Normal Weight!")
            return 0
        else: print("You are Overweight!")
        return 1
    else: print("You are Underweight!")
    return -1
calculate_bmi(weight=57, height=1.73)



