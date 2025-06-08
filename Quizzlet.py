def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }

    correct = 0

    print("Spanish Translation Quiz!\n")

    for english, spanish in translations.items():
        print(english)
        print(spanish)
        user_answer = input(f"What is the Spanish translation for {english}? ").strip().lower()

        if user_answer == spanish:
            print("That is correct!\n")
            correct += 1
        else:
            print(f"That is incorrect, the Spanish translation for {english} is {spanish}.\n")

    print(f"You got {correct}/{len(translations)} words correct, come study again soon!")


if __name__ == '__main__':
    main()