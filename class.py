class Equation():
    """docstring for ."""

    def __init__(this, a, b, c):
        super(Equation, this).__init__()
        this.a = a
        this.b = b
        this.c = c
        this.nature = ""
        this.d = 0

    def determinant(this):
        """
        Compute the determinant
        """
        b = this.pow()
        product = this.mult()
        this.d = b - product
        this.nature = "identical" if this.d == 0 else "distinct" if this.d > 0 else "complex"

    def compute(this):
        this.determinant()
        x1 = x2 = 0
        if this.nature == "distinct":
            x1 = ((-1 * this.b) + this.sqrt()) / (2 * this.a)
            x2 = ((-1 * this.b) - this.sqrt()) / (2 * this.a)
        elif this.nature == "complex":
            this.d = this.d * -1
            x1 = ((-1 * this.b) + this.sqrt()) / (2 * this.a)
            x2 = ((-1 * this.b) - this.sqrt()) / (2 * this.a)
            return (complex(x1), complex(x2))
        else:
            x1 = (-1 * this.b) / (2 * this.a)
            x2 = x1
        # Display results
        return (x1, x2)

    def pow(this):
        return this.b**2

    def mult(this):
        return 4 * this.a * this.c

    def sqrt(this):
        return this.d**0.5

# arguments
a = 1
b = -4
c = 4
# Instantiate object of equation class
equation = Equation(a, b, c)
# Compute Quadratic Equation
x1, x2 = equation.compute()
# Display the solutions
result = "The solutions of {0}x^2 + {1}x + {2} = 0 are {3} and {4}"
print(result.format(a, b, c, x1, x2))
