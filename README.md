# Numerical Integration Calculator

This Python script calculates numerical integration using various methods, such as the Trapezoidal Rule, Simpson's 1/3 Rule, Simpson's 3/8 Rule, and combinations of these rules.

## Features

- Numerical integration using different methods.
- Graphical representation of the function and integration area.

## Prerequisites

- Python 3.x
- Required Python libraries: `matplotlib`, `pandas`, `numpy`, `math`

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/m-essam-s/Numerical_Integration.git
   cd Numerical_Integration
   ```

2. Run the script:

   ```bash
   python main.py
   ```

3. Enter the function, lower bound, and upper bound as prompted.

4. View the results and graphical representation.

## Function Format

The input function should be in the format of a valid Python expression. For example:

```python
"0.2 + (25 * x) - (200 * (x**2)) + (675 * (x**3)) - (900 * (x**4)) + (400 * (x**5))"
```

## Example

```python
if __name__=='__main__':
    Function = input("F(X) = ")
    LowerBound = eval(input("Lower bound = "))
    UpperBound = eval(input("Upper bound = "))
    
    Calc = Numerical_Integration(Function, LowerBound, UpperBound)
    print(Calc)
    Calc.Graph()
```
```bash
$ python main.py
F(X) =  (0.2+(25*x)-(200*(x**2))+(675*(x**3))-(900*(x**4))+(400*(x**5)))
Lower bound = 0.2
Upper bound = 0.8
```

## Results

The results will be displayed in tabular format, including the true value and percentage error for each integration method.

```
                                Result             |εₜ|
True Value                  |  1.2825416666851581                   0 %
Trapezoidal Rule            |  0.9127499999999996  28.832721485058464 %
Simpson's 1/3 Rule          |  0.7948000000000065   43.91758396977672 %
Simpson's 3/8 Rule          |  0.9564000000000059   32.51481795255984 %
Compination 1/3 & 3/8 Rule  |   1.267564117333339  10.558557909825753 %
1/3 & 3/8 & 1/3 & 3/8 Rule  |  1.4910980853333393   5.214372374852828 %
```

## Graphical Representation

A plot of the function and the shaded area representing the integration will be displayed using `matplotlib`.

## License

This project is licensed under the MIT License

## Author✍️

* **[Mohamed Essam](https://twitter.com/m-essam-s)** <[m-essam-s](https://github.com/m-essam-s)>