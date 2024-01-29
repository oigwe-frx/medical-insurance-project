# create the initial variables below
age = 28 # age of the individual in years
sex = 0 # 0 for female, 1 for male*
bmi = 26.2 # individual’s body mass index
num_of_children = 3 # number of children the individual ha
smoker = 0 # 0 for a non-smoker, 1 for a smoker

# Add insurance estimate formula below
insurance_cost = 250 * age -128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

print(f"This person\'s insurance cost is {insurance_cost} dollars")
# Age Factor
age += 4

new_insurance_cost = 250 * age -128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print(f"The change in cost of insurance after increasing the age by 4 years is {change_in_insurance_cost} dollars.")

# BMI Factor
age = 28

bmi += 3.1

new_insurance_cost = 250 * age -128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print(f"The change in estimated insurance after increasing the BMI by 3.1 is {change_in_insurance_cost} dollars.")

# Male vs. Female Factor
bmi = 26.2

sex = 1 # 1 identifies male individuals and 0 identifies female individuals

new_insurance_cost = 250 * age -128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print(f"The change in estimated cost for being male instead of female is {change_in_insurance_cost} dollars.")

# Extra Practice
