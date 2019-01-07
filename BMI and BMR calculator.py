weight = float(input("Enter your weight in kg:  "))
height = float(input("Enter yout hight in m "))

BMI = weight/(height)**2

print(BMI)

user_q = input("I'll show you a primary BMR, are you man or woman? m/w")
mass_weight = int(input("Enter your weight in kg "))
height_bmr = int(input("Enter your height in cm "))
age = int(input("Enter your age "))

BMR_male = 66+(13.7*mass_weight)+(5*height_bmr)-(6.76*age)
BMR_woman = 655+(9.6*mass_weight)+(1.8*height_bmr)-(4.7*age)

if user_q == 'm':
    print(BMR_male)
elif user_q == 'w':
    print(BMR_woman)
