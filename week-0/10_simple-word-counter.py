# Document: This python is my 10th application of CS50P Week 0.

# Replace space with ...
def process():
    text = input("Enter text: ").strip()
    output = text.replace(" ", "...")
    return output

# Runs entire program
def main():
    output = process()
    print(output)
    print(f"Length: {len(output)}")

main()
