#My answear:

print("Jaką dostaniesz ocenę? Sprawdź!")
print()
test = input("Jak nazywał się TEST? > ")
maxpoint = float(input("Jaką maksymalną ilość pkt mogłeś uzyskać? > "))
score = float(input("Ile punktów uzyskałeś? > "))

grade = float(score / maxpoint * 100)
perc = round(grade, 2)

if grade >= 90:
  print("A+ 😍! ", perc,"%")
elif grade >= 80 and grade <= 89:
  print("A 🥰! ", perc ,"%")
elif grade >= 70 and grade <= 79:
   print("B 😏 ", perc,"%")
elif grade >= 60 and grade <= 69:
   print("C 🫢 ", perc,"%")
elif grade >= 50 and grade <= 59:
   print("D 😣 ", perc,"%")
elif grade <50:
  print("U 😥 ", perc, "%")

# Replit Answear:

print("Exam Grade Calculator")
print()
name_of_exam = input("Name of exam: ")
print()
total_score = int(input("Max. Possible Score:"))
your_score = int(input("Your score: "))
print()



number_score = float(your_score / total_score)
final_number = round(number_score, 2)
final_perc = round(float(your_score / total_score)*100, 2)

print("You got",final_perc,"%")

if final_number >= .90:
  print("Your letter score is an A+")
elif final_number >= .80 and final_number <= .89:
  print("Your letter grade is an A-.")
elif final_number >= .70 and final_number <= .79:
  print("Your letter score is a B.")
elif final_number >= .60 and final_number <= .69:
  print("Your letter grade is a C.")
elif final_number >= .50 and final_number <= .59:
  print("Your letter grade is a D.")
elif final_number <= .49:
  print("Your letter grade is a U.")
else: 
  print("Try again!")
