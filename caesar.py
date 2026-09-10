text = input("Text (small letters): ")
shift = int(input("Shift: "))
mode = input("e or d: ")

if mode == "d":
    shift = -shift

result = ""
for letter in text:
    new = chr((ord(letter) - 97 + shift) % 26 + 97)
    result = result + new

print("Result:", result)
input("Press Enter to exit")