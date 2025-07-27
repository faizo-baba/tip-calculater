print ("welcome to tip calculater!")
bill = (float (input ("how much is the actual bill ?: ")))
tip = (int(input ("how much tip you like to give? 10%,12% or 15%: ")))
people = (int(input("how many people have to pay: ")))
tip_as_percent = tip / 100
total_tip_amount = tip_as_percent * bill
total_bill = bill + total_tip_amount
each_pay = total_bill / people 

print (f"each person should pay: {each_pay}")
