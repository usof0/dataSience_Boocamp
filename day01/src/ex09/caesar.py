import sys

def contains_cyrillic(text):
    for char in text:
        if '\u0400' <= char <= '\u04FF':
            return True
    return False

def caesar_cipher(text, shift, operation):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            base = ord('a')
        elif 'A' <= char <= 'Z':
            base = ord('A')
        else:
            result.append(char)

        if operation == 'encode':
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(shifted_char)
        else:
            shifted_char = chr((ord(char) - base - shift) % 26 + base)
            result.append(shifted_char)

    return ''.join(result)
    
def main():
    if len(sys.argv) != 4:
        raise ValueError("Usage: python3 caesar.py <encode|decode> <text> <shift>")
    operation = sys.argv[1]
    text = sys.argv[2]
    shift = int(sys.argv[3])

    if operation not in ['encode', 'decode']:
        raise ValueError("Invalid operation. Use 'encode' or 'decode'")
    
    if contains_cyrillic(text):
        raise ValueError("The script does not support this language.")
    
    result = caesar_cipher(text, shift, operation)
    print(result)

if __name__ == "__main__":
    main()
