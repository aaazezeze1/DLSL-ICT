# Note: this is just some SAMPLE CODE DEMONSTRATING THAT YOU CAN USE <= SIGNS IN 
# STRINGS IN PYTHON and the program will still work AND TO SHOW YOU HOW FORMATTING
# STRINGS IS DONE. This DOES NOT INCLUDE THE LOOPING PART OF MY FLOWCHART and IS JUST
# A SAMPLE FOR YOU TO UNDERSTAND MY ANSWER BETTER. IF YOU ARE STILL UNSURE ABOUT MY 
# ANSWER THEN RUN THIS CODE IN https://www.programiz.com/python-programming/online-compiler/
# OR IN YOUR LOCAL MACHINE TO BETTER UNDERSTAND MY ANSWER.

if __name__ == "__main__":
    name = input()
    age = input()
    temp = input()
    bp = input()

    # YOU CAN USE <= SIGNS IN STRINGS
    if temp <= "37" and bp <= "120/80":
        # FORMATTING STRINGS
        result = name + " " + age + " " + temp + " " + bp
        print(result)
        print("Person is now vaccinated")
    else:
        print("Person's temperature and bp will get rechecked")

# Sample Output
# Oh, Sehun 27 36.1 120/80
# Person is now vaccinated

# Kim, Jong-in 27 38.3 130/80
# Person's temperature and bp will get rechecked
