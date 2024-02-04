import matplotlib.pyplot as plt
import numpy as np


class Polynomial:
    
    def __init__(self, *coefficients):
        self.coefficients = coefficients
        
    def __call__(self, x):
        res = 0
        for index, coeff in enumerate(self.coefficients):
            res += coeff * x ** index
        return res


def main():
    x = np.linspace(-10., 10., 100)

    p0 = Polynomial(0.75)
    p1 = Polynomial(0.75, 2.)
    p2 = Polynomial(0.75, 2., 1.)
    p3 = Polynomial(0.75, 2., 1., 0.25)

    _, axes = plt.subplots(1,4,figsize=(12,3))

    for i, (p, ax) in enumerate(zip([p0,p1,p2,p3], axes)):
        y = p(x)
        ax.plot(x,y)
        ax.set_title(f"poly with degree {i}")
        ax.axis("off")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()