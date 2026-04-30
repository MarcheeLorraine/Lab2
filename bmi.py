def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi=(weight)/(height*height)
    print(f"Your BMI is: {bmi:.2f}")
    if bmi >= 18.5 :
        if bmi <= 25.0 :
            print("You are Normal Weight!")
        else: print("You are Overweight!")
    else: print("You are Underweight!")
calculate_bmi(weight=57, height=1.73)



