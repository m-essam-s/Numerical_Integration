import unittest
from main import Numerical_Integration

class TestNumericalIntegration(unittest.TestCase):
  """
  to create a unit test you must create a method that starts with test_
  and to evaluate the result you must use the assertEqual method
  you can use any style you want to write your tests, see test_intergation_solution, 
    test_trapezoidal_rule, test_simpson_rule for examples
  you can find about assert in: https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual
  """

  def test_integration_solution(self):
    calc = Numerical_Integration("0.2+(25*x)-(200*(x**2))+(675*(x**3))-(900*(x**4))+(400*(x**5))", 0.2, 0.8)
    result = round(calc.IntergrationSolution(),3)
    self.assertEqual(result, 1.417)

    calc = Numerical_Integration("x**2", 0, 1)
    result = round(calc.IntergrationSolution(),3)
    self.assertEqual(result, 0.333)

    calc = Numerical_Integration("x**3*(x**2+25)", 0.2, 5)
    result = round(calc.IntergrationSolution(),3)
    self.assertEqual(result, 6510.407)
  
  def test_trapezoidal_rule(self):
    #Or you can write tests like the following
    self.assertEqual(
      round(Numerical_Integration("0.2+(25*x)-(200*(x**2))+(675*(x**3))-(900*(x**4))+(400*(x**5))", 0.2, 0.8)
            .TrapeziodalRule(), 3),
      0.456
    )

    self.assertEqual(
      round(Numerical_Integration("x**2", 0, 1)
            .TrapeziodalRule(), 3),
      0.5
    )

    self.assertEqual(
      round(Numerical_Integration("x**3*(x**2+25)", 0.2, 5)
            .TrapeziodalRule(), 3),
      15000.481
    )
  
  def test_simpson_rule(self):
    #Or you can write tests like the following
    calc1 = Numerical_Integration("0.2+(25*x)-(200*(x**2))+(675*(x**3))-(900*(x**4))+(400*(x**5))", 0.2, 0.8)
    calc2 = Numerical_Integration("x**2", 0, 1)
    calc3 = Numerical_Integration("x**3*(x**2+25)", 0.2, 5)

    result1 = round(calc1.SimpsonRule(),3)
    result2 = round(calc2.SimpsonRule(),3)
    result3 = round(calc3.SimpsonRule(),3)

    self.assertEqual(result1, 0.795)
    self.assertEqual(result2, 0.333)
    self.assertEqual(result3, 6360.884)
  
  def test_simpson_second_rule(self):
    calc = Numerical_Integration("0.2+(25*x)-(200*(x**2))+(675*(x**3))-(900*(x**4))+(400*(x**5))", 0.2, 0.8)
    result = round(calc.SimpsonSecondRule(),3)
    self.assertEqual(result, 0.956)

    calc = Numerical_Integration("x**2", 0, 1)
    result = round(calc.SimpsonSecondRule(),3)
    self.assertEqual(result, 0.333)

    calc = Numerical_Integration("x**3*(x**2+25)", 0.2, 5)
    result = round(calc.SimpsonSecondRule(),3)
    self.assertEqual(result, 6031.854)
  
  def test_composite_simpson_rule(self):
    calc = Numerical_Integration("0.2+(25*x)-(200*(x**2))+(675*(x**3))-(900*(x**4))+(400*(x**5))", 0.2, 0.8)
    result = round(calc.CompositeSimpsonRule(),3)
    self.assertEqual(result, 1.268)

    calc = Numerical_Integration("x**2", 0, 1)
    result = round(calc.CompositeSimpsonRule(),3)
    self.assertEqual(result, 0.333)

    calc = Numerical_Integration("x**3*(x**2+25)", 0.2, 5)
    result = round(calc.CompositeSimpsonRule(),3)
    self.assertEqual(result, 6086.938)
  
  def test_double_composite_simpson_rule(self):
    calc = Numerical_Integration("0.2+(25*x)-(200*(x**2))+(675*(x**3))-(900*(x**4))+(400*(x**5))", 0.2, 0.8)
    result = round(calc.DoubleCompositeSimpsonRule(),3)
    self.assertEqual(result, 1.491)

    calc = Numerical_Integration("x**2", 0, 1)
    result = round(calc.DoubleCompositeSimpsonRule(),3)
    self.assertEqual(result, 0.333)

    calc = Numerical_Integration("x**3*(x**2+25)", 0.2, 5)
    result = round(calc.DoubleCompositeSimpsonRule(),3)
    self.assertEqual(result, 6148.007)

if __name__ == '__main__':
  unittest.main()
