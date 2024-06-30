# EquationGenerator

EquationGenerator is a tool to generate LaTeX formatted equations based on user input descriptions. The project uses Python to parse the descriptions and generate the LaTeX code.

## Features

- Parse user input descriptions of mathematical expressions
- Generate LaTeX formatted equations
- Append generated equations to a LaTeX document

## Directory Structure

```plaintext
.
├── src/
│   ├── main.tex
│   ├── equations/
│   │   ├── arithmetic.tex
│   │   ├── algebra.tex
│   │   ├── trigonometry.tex
│   │   ├── calculus.tex
│   │   ├── linear_algebra.tex
│   │   ├── statistics.tex
│   ├── generate_equation.py
├── data/
│   ├── equations_arithmetic.txt
│   ├── equations_algebra.txt
│   ├── equations_trigonometry.txt
│   ├── equations_calculus.txt
│   ├── equations_linear_algebra.txt
│   ├── equations_statistics.txt
├── README.md
```
## Getting Started
### Prerequisites
Python 3.6+

TeX distribution (e.g., TeX Live, MiKTeX)

### Installation
Clone the repository:


git clone https://github.com/your_username/EquationGenerator.git

cd EquationGenerator

### Install dependencies:


pip install -r requirements.txt

## Usage
Run the equation generator script:


python src/generate_equation.py

Enter a mathematical description:

Enter descriptions of mathematical equations in plain English, and the script will generate corresponding LaTeX formatted equations. For example:

Input: "five plus three equals eight"
Output: 
5
+
3
=
8
5+3=8
### Compile the LaTeX document:

cd src

pdflatex main.tex
