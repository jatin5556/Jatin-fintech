income = int(input("100000:"))
expenses = int(input("20000: "))
loan = input("No ")
age = int (input("23 "))
employment = input("imployment")

score = 0
if income > 10000:
    score += 30
if expenses < 20000:
    score += 20
 if loan.lower() == "No":
     score += 30
if 25 <= age <= 40:
    score += 20
    
  if score >= 80:
      print("High - Credit worthy ")
  elif score >= 50:
      print("Medium - caution ")
  else:
      print("Low - Not Eligible")