import unittest
from Calculator import Calculator
from CsvReader import CsvReader



class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.test_data = CsvReader('/src/Addition.csv').data
        for row in self.test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), (row['Result']))
            self.assertEqual(self.calculator.result, row['Result'])
            print(self.calculator.result)

    def test_subtract_method_calculator(self):
        self.test_data = CsvReader('/src/Subtraction.csv').data
        for row in self.test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), (['Result']))
            self.assertEqual(self.calculator.result, row['Result'])
            print(self.calculator.result)

    def test_divide_method_calculator(self):
        self.test_data = CsvReader('/src/Division.csv').data
        for row in self.test_data:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), (['Result']))
            self.assertEqual(self.calculator.result, row['Result'])
            print(self.calculator.result)

    def test_multiply_method_calculator(self):
        self.test_data = CsvReader('/src/Multiplication.csv').data
        for row in self.test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), (['Result']))
            self.assertEqual(self.calculator.result, row['Result'])
            print(self.calculator.result)

    def test_square_method_calculator(self):
        self.test_data = CsvReader('/src/Square.csv').data
        for row in self.test_data:
            self.assertAlmostEqual(self.calculator.square(int(row['Value 1'])))
            self.assertEqual(self.calculator.result, int(row['Result'])),
            print(self.calculator.result)

    def test_squareroot_method_calculator(self):
        self.test_data = CsvReader('/src/Square Root.csv').data
        for row in self.test_data:
            self.assertAlmostEqual(self.calculator.squareroot(int(row['Value 1'])))
            self.assertEqual(self.calculator.result, int(row['Result']))
            print(self.calculator.result)



if __name__ == '__main__':
    unittest.main()
