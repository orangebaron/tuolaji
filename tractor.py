class tractor:
  def __init__(self):
    self.position = 0
  def honk(self):
    print("doot doot")
  def drive(self):
    self.position+=1
  def GPS(self):
    print("in",500-self.position,"turn left")

a = tractor()
a.honk()
a.drive()
a.drive()
a.drive()
a.drive()
a.drive()
a.drive()
a.GPS()
a.honk()
a.drive()
a.drive()
