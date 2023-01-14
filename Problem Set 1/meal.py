def main():
    time = input("What time is it?")
    #ct short for check time
    ct = convert(time)
    if ct >= 7 and ct <=8:
        print("breakfast time")
    elif ct >=12 and ct <=13:
        print("lunch time")
    elif ct >=18 and ct <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    min = float(minutes)/60
    return float(hours) + min

if __name__ == "__main__":
    main()
