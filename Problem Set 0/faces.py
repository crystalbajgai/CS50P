def main():
    eicons = input("")
    print(convert(eicons))


def convert(eicons):
    emoji = eicons.replace(":)", "🙂").replace(":(", "🙁")
    return emoji


main()
