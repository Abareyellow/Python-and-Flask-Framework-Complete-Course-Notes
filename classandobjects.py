class MyComplexNumber:
  # Constructor methods
  def __init__(self, real = 0, imag = 0):
    print("MyComplexNumber constructor executing..")
    self.real_part = real
    self.imag_part = imag

  def displayComplex(self):
    print("{0} + {1}j".format(self.real_part, self.imag_part))

cmplxl = MyComplexNumber(40, 50)
cmplxl.displayComplex()

cmplx2 = MyComplexNumber(10, 20)
cmplx2.displayComplex()
cmplx2.new_attribute = 80

print((cmplx2.real_part, cmplx2.imag_part, cmplx2.new_attribute))