def is_palindrome(string):
    test_string = [char.lower() for char in string if char.isalpha()]

    start = 0
    end = len(test_string) - 1
    while start < end:
        if (test_string[start] != test_string[end]):
            return False
        start += 1
        end -= 1

    return True


if __name__ == "__main__":
    string = input("Enter string (A-z, a-z): ")
    answer = is_palindrome(string)
    if answer:
        print(f"The string {string} is palindrome")
    else:
        print(f"The string {string} is not a palindrome")
