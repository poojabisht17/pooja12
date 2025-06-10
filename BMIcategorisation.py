weight= float(input("Enter your weight in kg: "))
height=float(input("Enter your height in meters: "))

bmi=weight/(height*2)

if bmi<16:
    print(f"Your BMI s {bmi} and You are underweight (Severe thinness)")
elif bmi<=16.9:
    print(f"Your BMI s {bmi} and You are underweight (moderate thinness)")
elif bmi<=18.4:
    print(f"Your BMI s {bmi} and You are underweight (mild thinness)")
elif bmi<=24.9:
    print(f"Your BMI s {bmi} and Your weight is normal")
elif bmi<=29.9:
    print(f"Your BMI s {bmi} and You are Overweight (Pre-obese)")
elif bmi<=34.9:
    print(f"Your BMI s {bmi} and You are Obese (Class I)")
elif bmi<=39.9:
    print(f"Your BMI s {bmi} and You are Obese (Class II)")

else: print(f"Your BMI s {bmi} and You are Obese (Class III)")