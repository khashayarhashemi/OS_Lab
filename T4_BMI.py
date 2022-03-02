print("Enter your weight: ") 
weight_in_kg=float(input())
print("Enter your height: ") 
height_in_meters=float(input())
BMI = (weight_in_kg / height_in_meters)**2
print(BMI)