import sys
import math


class QuadraticEquationSolver:
    def __init__(self):
        self.a = self.get_coef(1, 'Enter real A:')
        self.b = self.get_coef(2, 'Enter real B:')
        self.c = self.get_coef(3, 'Enter real C:')
        self.roots = []

    def get_coef(self, index, prompt):
        try:
            coef_input = sys.argv[index]
        except IndexError:
            try:
                coef_input = float(input(prompt))
            except ValueError:
                print("Not a valid value")
                return self.get_coef(index, prompt)
        return float(coef_input)

    def get_sqRoots(self, root):
        if root >= 0:
            root = math.sqrt(root)
            if root > 0:
                self.roots.append(-root)
            self.roots.append(root)

    def get_roots(self):
        d = self.b * self.b - 4 * self.a * self.c
        print("Discriminant =", d)
        if d == 0.0:
            root = -self.b / (2.0 * self.a)
            self.get_sqRoots(root)
        elif d > 0.0:
            sqd = math.sqrt(d)
            root1 = (-self.b + sqd) / (2.0 * self.a)
            root2 = (-self.b - sqd) / (2.0 * self.a)
            self.get_sqRoots(root1)
            self.get_sqRoots(root2)

    def show_equation(self):
        print('You entered: {}x^4 + {}x^2 + {} = 0'.format(self.a, self.b, self.c))

    def show_solution(self):
        len_roots = len(self.roots)
        if len_roots == 0:
            print('There are no real roots')
        elif len_roots == 1:
            print('There is one real root:\n', *self.roots)
        else:
            print('There are {} real roots:'.format(len_roots))
            list(map(print, self.roots))


def main():
    equation_solver = QuadraticEquationSolver()
    equation_solver.show_equation()
    equation_solver.get_roots()
    equation_solver.show_solution()


if __name__ == "__main__":
    main()
