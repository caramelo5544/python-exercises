text = input("Text (small letters): ")
shift = int(input("Shift: "))
result = ""
for letter in text:
    new = chr((ord(letter) - 97 + shift) % 26 + 97)
    result = result + new
print("Encrypted:", result)
input("Press Enter to exit")