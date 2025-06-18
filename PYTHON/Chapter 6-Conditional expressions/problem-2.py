m1 = int(input("enter marks : "))
m2 = int(input("enter marks : "))
m3 = int(input("enter marks : "))

# Check for total percentage

total_percentage = (m1 + m2 + m3)/3

if(total_percentage>=40 and m1>=33 and m2>=33 and m3>=33):
  print("You are pass :" , total_percentage)

else:
  print("You failed ,Try again next year:", total_percentage)