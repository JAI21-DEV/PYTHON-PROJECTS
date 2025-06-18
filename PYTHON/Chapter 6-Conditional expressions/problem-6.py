marks = int(input("Enter your marks (0–100): "))

if 0 <= marks <= 100:
    
    if 90 <= marks <= 100:
        print("Your Grade is Ex")

    elif 80 <= marks < 90:
        print("Your Grade is A")

    elif 70 <= marks < 80:
        print("Your Grade is B")

    elif 60 <= marks < 70:
        print("Your Grade is C")

    elif 50 <= marks < 60:
        print("Your Grade is D")

    else:
        print("Your Grade is F")

else:
    print("❌ Invalid input. Marks should be between 0 and 100.")