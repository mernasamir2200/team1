import unittest
from unittest.mock import patch
from io import StringIO

def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    operation = input("Enter the number of the operation you want to perform (1/2/3/4): ")
    if operation == ['1', '2', '3', '4']:  # Intentional logic error
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if operation == '1':
                print(f"The result is: {num1 + num2}")  # Correct
            elif operation == '2':
                print(f"The result is: {num1 - num2")  # Syntax error
            elif operation == '3':
                print(f"The result is: {num1 + num2}")  # Logic error
            elif operation == '4':
                print(f"The result is: {num1 // num2}")  # Runtime error
        except ValueError:
            print("Erro: Invalid input. Please enter numeric values.")
    else:
        print("Error: Please restart.")  # Poor UX

class TestCalculator(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '5', '3'])  # Simulate addition: 5 + 3
    @patch('sys.stdout', new_callable=StringIO)
    def test_addition(self, mock_stdout, mock_input):
        calculator()
        self.assertIn("The result is: 8.0", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['2', '5', '3'])  # Simulate subtraction: 5 - 3
    @patch('sys.stdout', new_callable=StringIO)
    def test_subtraction(self, mock_stdout, mock_input):
        calculator()
        self.assertIn("Erro", mock_stdout.getvalue())  # Expecting error due to syntax issue

    @patch('builtins.input', side_effect=['3', '5', '3'])  # Simulate multiplication: 5 * 3
    @patch('sys.stdout', new_callable=StringIO)
    def test_multiplication(self, mock_stdout, mock_input):
        calculator()
        self.assertIn("The result is: 15.0", mock_stdout.getvalue())  # This would fail due to the logic error

    @patch('builtins.input', side_effect=['4', '5', '0'])  # Simulate division by zero
    @patch('sys.stdout', new_callable=StringIO)
    def test_division_by_zero(self, mock_stdout, mock_input):
        calculator()
        self.assertIn("division by zero", mock_stdout.getvalue())  # Would expect runtime error

    @patch('builtins.input', side_effect=['5'])  # Invalid operation
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_operation(self, mock_stdout, mock_input):
        calculator()
        self.assertIn("Error: Please restart", mock_stdout.getvalue())  # Poor UX error message

if __name__ == '__main__':
    unittest.main()
