from main import Numerical_Integration

class TestNumericalIntegration():
  """
  Unit test is a piece of code that tests a unit of work. 
  that unit of work can be a function, class, or a module.
  """
  # These are ANSI escape codes that produce colored output in the terminal
  PASS = '\033[96m'
  FAIL = '\033[91m'
  END = '\033[0m'

  def test_integration_solution(self):

    calc = Numerical_Integration("0.2+(25*x)-(200*(x**2))+(675*(x**3))-(900*(x**4))+(400*(x**5))", 0.2, 0.8)
    result = round(calc.IntergrationSolution(),3)
    if(result == 1.417):
      print(f"{self.PASS}Integration Solution Test Passed{self.END}")
    else:
      print(f"{self.FAIL}Integration Solution Test Failed{self.END}")

    calc = Numerical_Integration("x**2", 0, 1)
    result = round(calc.IntergrationSolution(),3)
    if(result == 0.333):
      print(f"{self.PASS}Integration Solution Test Passed{self.END}")
    else:
      print(f"{self.FAIL}Integration Solution Test Failed{self.END}")

    calc = Numerical_Integration("x**3*(x**2+25)", 0.2, 5)
    result = round(calc.IntergrationSolution(),3)
    if(result == 6510.407):
      print(f"{self.PASS}Integration Solution Test Passed{self.END}")
    else:
      print(f"{self.FAIL}Integration Solution Test Failed{self.END}")

    calc = False
    if(calc):
      print(f"{self.PASS}Integration Solution Test Passed{self.END}")
    else:
      print(f"{self.FAIL}Integration Solution Test Failed{self.END}")
  
  @classmethod
  def RunTest(self):
    _test = TestNumericalIntegration()
    _test.test_integration_solution()

if __name__ == '__main__':
  TestNumericalIntegration.RunTest()
