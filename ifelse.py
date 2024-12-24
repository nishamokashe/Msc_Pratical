avg = float(input("Enter your marks : ")) 
if avg >= 90 and avg <= 100:
    print("Congrutulation Your Grade is A")
elif avg >= 80 and avg < 90:
    print("Congrutulation Your Grade is B")
elif avg >= 71 and avg < 80:
    print("Congrutulation Your Grade is C")
elif avg >= 60 and avg < 71:
    print("Congrutulation Your Grade is D")
elif avg >= 50 and avg < 60:
    print("Congrutulation Your Grade is E")
elif avg >= 35 and avg < 50:
    print("Congrutulation Your Grade is F")
else:
    print(" Your Result Fail ")
