# Note: this is just some sample code demonstrating that you can use <= signs
# or what not in python and the program will still work. 

if __name__ == "__main__":
    name = "Oh, Sehun"
    age = "27"
    temp = "36.1"
    bp = "120/80"

    if temp <= "37" and bp <= "120/80":
        result = name + " " + age + " " + temp + " " + bp
        print(result)
    elif temp <= "37" and bp <= "120/80":
        print("Person's temperature and bp will get rechecked")
    else:
        print("Sorry, you won't get vaccinated. Please go home.”")

# Sample Output
# Oh, Sehun 27 36.1 120/80