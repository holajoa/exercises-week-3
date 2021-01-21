class Circle:

    def __init__(self, centre, radius):
        self.c = centre
        self.r = radius

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.c) + ", " \
                                                + repr(self.r) + ")"

    def __contains__(self, p):
        if len(p) == 2:
            dsq = (self.c[0]-p[0])**2 + (self.c[1]-p[1])**2
            return True if dsq < self.r**2 else False
        else:
            raise IndexError
    

        