#Day 6 practice
'''
Profile = {
            "Name": "Dhruv",
            "Role": "Data Engineer",
            "Experience": 4.5,
            "Age": 27,
            "City": "Chennai"
        
}

print(Profile)

print(Profile["Age"])


key = ["Name", "Role", "Experience", "Age", "City"]
value = ["Dhruv", "Data Engineer", 4.5, 27, "Chennai"]

result = dict(zip(key, value))
print(result)
'''
#Assignment


merged = {}

Candidate = {
    "Name": "Dhruva",
    "Age": 28,
    "City": "Chennai"
}

Experience1 = {
    "Company1": "Access Healthcare",
    "Role1": "SQL Developer",
    "Experience1": "1.2 years"
}

Experience2 = {
    "Company2": "Coronis Ajuba",
    "Role2": "Snowflake Developer",
    "Experience2": "10 months"
}

Experience3 = {
    "Company3": "AGS Health",
    "Role3": "Snowflake Developer",
    "Experience3": "10 months"
}

Experience4 = {
    "Company4": "Guidehouse",
    "Role4": "Senior Snowflake Developer",
    "Experience4": "6 months"
}

Experience5 = {
    "Company5": "RBD Billing",
    "Role5": "Snowflake Data Engineer",
    "Experience5": "7 months"
}

print("Candidate Details")
print("-" * 30)

for key, value in Candidate.items():
    print(f"{key:<12}: {value}")

print("\nExperience 1")
print("-" * 30)
for key, value in Experience1.items():
    print(f"{key:<12}: {value}")

print("\nExperience 2")
print("-" * 30)
for key, value in Experience2.items():
    print(f"{key:<12}: {value}")

print("\nExperience 3")
print("-" * 30)
for key, value in Experience3.items():
    print(f"{key:<12}: {value}")

print("\nExperience 4")
print("-" * 30)
for key, value in Experience4.items():
    print(f"{key:<12}: {value}")

print("\nExperience 5")
print("-" * 30)
for key, value in Experience5.items():
    print(f"{key:<12}: {value}")    
