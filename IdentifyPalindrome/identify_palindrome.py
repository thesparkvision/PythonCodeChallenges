def is_palindrome(string):
    if not string.isalpha():
        raise Exception("Invalid String entered. Use A-z, a-z")

    lowercase_string = string.lower()

    start = 0
    end = len(lowercase_string) - 1
    while start < end:
        if(lowercase_string[start] != lowercase_string[end]):
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