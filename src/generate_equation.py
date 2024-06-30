import re

def parse_input(description):
    """
    Parse a description of a mathematical equation and convert it to a LaTeX-friendly format.
    """
    description = description.lower()
    description = description.replace("plus", "+")
    description = description.replace("minus", "-")
    description = description.replace("times", "*")
    description = description.replace("divided by", "/")
    description = description.replace("to the power of", "^")
    description = description.replace("equals", "=")
    description = description.replace("open parenthesis", "(")
    description = description.replace("close parenthesis", ")")
    
    # Ensure there are no unsupported characters
    description = re.sub(r'[^0-9+\-*/^().=]', ' ', description)
    return description

def generate_latex(equation):
    """
    Wrap the parsed equation in LaTeX math delimiters.
    """
    return f"\\[{equation}\\]"

def main():
    """
    Main function to take user input, parse it, generate LaTeX, and append to the output file.
    """
    while True:
        user_input = input("Enter a mathematical description (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        
        parsed_equation = parse_input(user_input)
        latex_equation = generate_latex(parsed_equation)
        
        with open('../data/equations.txt', 'a') as f:
            f.write(latex_equation + '\n')
        
        print(f"Generated LaTeX: {latex_equation}")

if __name__ == "__main__":
    main()
