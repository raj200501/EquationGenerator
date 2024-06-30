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
    Main function to take user input, parse it, generate LaTeX, and append to the appropriate output file.
    """
    categories = {
        'arithmetic': '../data/equations_arithmetic.txt',
        'algebra': '../data/equations_algebra.txt',
        'trigonometry': '../data/equations_trigonometry.txt',
        'calculus': '../data/equations_calculus.txt',
        'linear algebra': '../data/equations_linear_algebra.txt',
        'statistics': '../data/equations_statistics.txt',
        'geometry': '../data/equations_geometry.txt',
        'complex numbers': '../data/equations_complex_numbers.txt'
    }

    while True:
        user_input = input("Enter a mathematical description (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        
        category = input(f"Enter the category ({', '.join(categories.keys())}): ").lower()
        if category not in categories:
            print("Invalid category. Please try again.")
            continue
        
        parsed_equation = parse_input(user_input)
        latex_equation = generate_latex(parsed_equation)
        
        with open(categories[category], 'a') as f:
            f.write(latex_equation + '\n')
        
        print(f"Generated LaTeX: {latex_equation}")

if __name__ == "__main__":
    main()
