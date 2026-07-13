weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height: "))
BMI = weight / (height * height)
if BMI <=18.5 :
               print("underweight")
elif 18.5<= BMI <=24.9:
               print("Normal")
elif 25.0<= BMI <= 29.9:
               print("over weight")
elif BMI >= 30.0 :
               print("Obese")
               

