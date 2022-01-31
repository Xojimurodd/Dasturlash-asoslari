num1 = int(input("Sonni kiriting?"))
num2 = int(input("Sonni kiriting2?"))
action = str(input("Choose action: Add(a),Sub(s) Mult(m) Div(d) ->"))

print("The result is",end="")
if action == "a":
    print(num1+num2)
elif action == "s":
    print(num1-num2)
elif action == "m":
    print(num1*num2)
else:
    print(num1/num2) 
