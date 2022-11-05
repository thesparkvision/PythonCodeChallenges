def sort_string(text):
    strings = text.split(" ")
    sorted_strings = list(sorted(strings, key = lambda x: x.lower()))
    return " ".join(sorted_strings)

if __name__ == "__main__":
    string = input("Enter string of words: ")
    answer = sort_string(string)
    print(f"The sorted string is: {answer}")