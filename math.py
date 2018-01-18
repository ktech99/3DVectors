class point(object):

    def __init__(self,p1,p2,p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def dot_product(self,other):
        dot_p1 = self.p1 * other.p1
        dot_p2 = self.p2 * other.p2
        dot_p3 = self.p3 * other.p3
        return dot_p1 + dot_p2 + dot_p3

    def cross_product(self,other):
        i = (self.p2 * other.p3)-(self.p3 * other.p2)
        j = (self.p1 * other.p3)-(self.p3 * other.p1)
        j = -j
        k = (self.p1 * other.p2)-(self.p2 * other.p1)
        s = ("(%s)i + (%s)j + (%s)k")%(str(i), str(j), str(k))
        return s

choice = int(input("Enter 1 for dot product & enter 2 for cross product: "))
i1 = int(input("Enter i1: "))
j1 = int(input("Enter j1: "))
k1 = int(input("Enter k1: "))
i2 = int(input("Enter i2: "))
j2 = int(input("Enter j2: "))
k2 = int(input("Enter k2: "))
point1 = point(i1,j1,k1)
point2 = point(i2,j2,k2)
if choice == 1:
    print "Dot product is: %s"%(point1.dot_product(point2))
elif choice == 2:
        print "cross product is: %s" % (point1.cross_product(point2))
else:
    print "Illegal choice."
raw_input()
