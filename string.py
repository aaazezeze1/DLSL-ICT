# Note: this is just some SAMPLE CODE DEMONSTRATING THAT YOU CAN USE <= SIGNS IN
# STRINGS IN PYTHON and the program will still work AND TO SHOW YOU WHY I HAVE
# EMPTY STRINGS IN MY FLOWCHART. This DOES NOT INCLUDE MOST PARTS OF MY
# FLOWCHART and IS JUST A SAMPLE FOR YOU TO UNDERSTAND MY ANSWER BETTER.
# IF YOU ARE STILL UNSURE ABOUT MY ANSWER THEN RUN THIS CODE IN
# https://www.programiz.com/python-programming/online-compiler/
# OR IN YOUR LOCAL MACHINE TO BETTER UNDERSTAND MY ANSWER.

if __name__ == "__main__":
    name = input()
    age = input()
    gender = input()
    temp = input()
    bp = input()

    # YOU CAN USE <= SIGNS IN STRINGS
    if temp <= "37" and bp <= "120/80":
        # EMPTY STRINGS ARE HERE FOR SPACING
        result = name + " " + age + " " + gender + " " + temp + " " + bp
        print(result)
        print("Person is now vaccinated")
    else:
        print("Person's temperature and bp will get rechecked")

# Example Output
# Oh, Sehun 27 M 36.1 120/80
# Person is now vaccinated

# Kim, Jong-in 27 M 38.3 130/80
# Person's temperature and bp will get rechecked
