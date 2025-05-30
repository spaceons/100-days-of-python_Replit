print("Tip Calculator")
print()
expense = float(input("""Ile wydaliście? > """))
tip_proc = float(input("""Jaki procent chcesz napiwkować (XD)? > """))

tip_number = tip_proc / 100 * expense + expense

ppl = int(input("""Ilu Was jest? > """))
naGlowe = tip_number / ppl
naGlowe = round(naGlowe, 2)

print("Suma wynosi: ", tip_number)
print("Każdy musi dać: ", naGlowe)

# były małe problemy, ale ogarnąłem temat
