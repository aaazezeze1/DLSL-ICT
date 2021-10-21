if __name__ == "__main__":
    name = "Oh, Sehun"
    age = "27"
    temp = "36.1"
    bp = "120/80"

    if temp <= "37" and bp <= "120/80":
        print("Person is now vaccinated")
    elif temp <= "37" and bp <= "120/80":
        print("Person's temperature and bp will get rechecked")
    else:
        print("Sorry, you won't get vaccinated. Please go home.”")

    result = name + " " + age + " " + temp + " " + bp
    print(result)
