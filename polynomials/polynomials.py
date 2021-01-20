from numbers import Number


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a - b for a, b in zip(self.coefficients, other.coefficients))
            coefs += self.coefficients[common:] + tuple([-c for c in other.coefficients[common:]])
            return Polynomial(coefs)
        
        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other, ) + self.coefficients[1:])
        
        else: 
            return NotImplemented

    def __rsub__(self, other):
        return Polynomial(tuple([-c for c in (self - other).coefficients]))

    def __mul__(self, other):
        if isinstance(other, Number):
            return Polynomial(tuple([other * c for c in self.coefficients]))
        elif isinstance(other, Polynomial):
            _s = self.coefficients
            _o = other.coefficients
            prod = [0] * (len(_s)+len(_o)-1)
            for selfpow, selfco in enumerate(_s):
                for otherpow, otherco in enumerate(_o):
                    prod[selfpow+otherpow] += selfco * otherco
            return Polynomial(tuple(prod))
        else:
            return NotImplemented
    
    def __rmul__(self, other):
        return self * other


    