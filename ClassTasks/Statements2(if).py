score = int(input("Enter Score:"))

if score >100:
	print ("Invalid Score")
elif score >= 75 and score <= 100:
	print("You Got An A")
elif score >= 60 and score <=74:
	print("You Got An B")
elif score >= 40 and score <=59:
	print("You Got An C")
else:
	print("You failed")

