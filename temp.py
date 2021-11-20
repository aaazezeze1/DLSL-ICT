# Note: this is just some SAMPLE CODE DEMONSTRATING WHY I USED and ON MY FLOWCHART
# and = returns True if both statements are true
# https://www.w3schools.com/python/trypython.asp?filename=demo_oper_logical2

if __name__ == "__main__":
    temp = input()

    # i used "and" because if temp >= 35 and temp <= 37, its still considered normal
    # https://www.mayoclinic.org/diseases-conditions/hypothermia/symptoms-causes/syc-20352682

    if temp >= "35" and temp <= "37":
        # if temp is >= 35 and is also <= 37 then it returns True
        # if both conditions return True then Normal Temperature will be printed
        print("Normal Temperature")
    else:
        # if temp is not >= 35 and is also not <= 37 then it returns False
        # if both conditions return False then Not Normal will be printed
        print("Not Normal")

# Example output
# 36 
# Normal Temperature

# 38.1 
# Not Normal
