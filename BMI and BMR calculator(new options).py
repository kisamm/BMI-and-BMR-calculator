print("This will be a result of BMI")
weight = int(input("Enter your weight in kg:  "))
height = float(input("Enter yout hight in m "))

BMI = weight/(height)**2
print("This is yout BMI: ",BMI)

user_q = input("I'll show you a primary BMR, are you man or woman? m/w")
mass_weight = int(input("Enter your weight in kg "))
height_bmr = int(input("Enter your height in cm "))
age = int(input("Enter your age "))

BMR_male = 66+(13.7*mass_weight)+(5*height_bmr)-(6.76*age)
BMR_woman = 655+(9.6*mass_weight)+(1.8*height_bmr)-(4.7*age)

if user_q == 'm':
    print("Primary BMR for male is: ",BMR_male,"kcal")
elif user_q == 'w':
    print("Primary BMR for women is: ",BMR_woman,"kcal")


user_q2 = input("What activity are you doing? [FOR MALE]if you are not(skip):  without activity(wa), low activity(la) 1-2 trenings, medium activity(ma) 3-4 treinings, high activity(ha)3-4 treinings and physically work, very high activity(vah)")

wa = float(BMR_male*1.2)
la = float(BMR_male*1.3)
ma = float(BMR_male*1.5)
ha = float(BMR_male*1.7)
vah = float(BMR_male*1.9)

if user_q2 == "wa":
    print("Your activity: ",wa,"kcal")
elif user_q2 == "la":
    print("Your activity: ",la,"kcal")
elif user_q2 == "ma":
    print("Your activity: ",ma,"kcal")
elif user_q2 == "ha":
    print(ha)
elif user_q2 == "vah":
    print("Your activity: ",vah,"kcal")

women = input("So you'are women, choose your activities: without activity(wa), low activity(la) 1-2 trenings, medium activity(ma) 3-4 treinings, high activity(ha)3-4 treinings and physically work, very high activity(vah) ")

if user_q2 == "skip":
    print(women)


wa_women = float(BMR_woman*1.2)
la_women = float(BMR_woman*1.3)
ma_women = float(BMR_woman*1.5)
ha_women = float(BMR_woman*1.7)
vah_women = float(BMR_woman*1.9)


if women == "wa":
    print("Your activity: ",wa_women,"kcal")
elif women == "la":
    print("Your activity: ",la_women,"kcal")
elif women == "ma":
    print("Your activity: ",ma_women,"kcal")
elif women == "ha":
    print("Your activity: ",ha_women,"kcal")
elif women == "vah":
    print("Your activity: ",vah_women,"kcal")