# Document: This python is my 9th application of CS50P Week 0.

# Prompts user to input text
def before():
    text = input("Hello user. \nEnter text: ")
    return text

# Removes whitelines
def process(text):
    processing = text.strip()
    output = processing.lower()
    return output

# Runs entire program
def main():
    text = before()
    output = process(text)
    print(output)
    print(f"\"{output}\"")

main()