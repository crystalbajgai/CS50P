def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    rmdollar = d.replace("$", "")
    return float(rmdollar)


def percent_to_float(p):
    rmpercentsign = p.replace("%", "")
    # percent in decimal (pid)
    pid = float(rmpercentsign)/100
    return pid


main()
