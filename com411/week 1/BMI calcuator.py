user_name = input ("what is your name? \n ")
print (f"Hello {user_name}")
user_age = input ("what is your age in years? \n ")

user_weight = float(input ("what is your weight in KG? \n "))

user_hight = float(input ("what is your hight in meters ? \n "))

hight_squared = user_hight * user_hight
BMI = user_weight / hight_squared
print (f"your BMI is {BMI} ")

