class Polynomial:

    def __init__(self, *args):
        self._coefs = []
        for arg in args:
            self._coefs.append(arg)

    def __call__(self, x):
        buf = 0
        cur = 1
        for i, coef in enumerate(self._coefs):
            buf += coef * cur
            cur *= x
        return buf

    @property  # устанавливает getter
    def coefs(self):
        return self._coefs

    @coefs.setter  # устанавливает setter
    def coefs(self, new_coefs):
        # print('вызван сетер')
        if isinstance(new_coefs, (tuple, list)):
            self._coefs = list(new_coefs)
        else:
            raise TypeError

    def __setitem__(self, key, v):
        self._coefs[key] = v

    def __getitem__(self, key):
        return self._coefs[key]


class IntegerPolynomial(Polynomial):

    def __init__(self, *args):
        # for arg in args:
        #     round(arg)
        super().__init__(*args)
        self.to_int()

    def to_int(self):
        for i, coef in enumerate(self._coefs):
            self._coefs[i] = round(coef)

    @Polynomial.coefs.setter  # устанавливает setter
    def coefs(self, new_coefs):
        Polynomial.coefs.fset(self, new_coefs)
        # super().coefs = new_coefs
        self.to_int()

    def __setitem__(self, key, v):
        self._coefs[key] = v
        self.to_int()


# p = Polynomial(1.5, 2, 3, 4, 5, 7, 8, 9)
# print(p[0])
#
# polynom = Polynomial(2, 3, 1)
# print(polynom.coefs)
# polynom.coefs = [1, 2]
# print(polynom.coefs)
#
# polynom = Polynomial(2, 3, 1)
# print(polynom(4))
#
# polynom = Polynomial(2, 3, 1, 4, 5)
# polynom[0] = 10
# polynom[1::2] = [-1, -2]
# print(polynom.coefs)

integer_polynom = IntegerPolynomial(2, 3.5, 1)
# print(integer_polynom(1))
#
# integer_polynom[2] = -1.2
# print(integer_polynom.coefs)

integer_polynom.coefs = 3.4
