def addcheck(num, num2, awn):
    if int(awn) == int(num) + int(num2):
        return f"EQ {num} + {num2} = {awn} is ✅"
    else: 
        return f"EQ {num} + {num2} = {awn} is ❌"
    
def subcheck(num, num2, awn):
    if int(awn) == int(num) - int(num2):
        return f"EQ {num} - {num2} = {awn} is ✅"
    else: 
        return f"EQ {num} - {num2} = {awn} is ❌"