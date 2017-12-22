class tractor:
  position = 0
  def honk():
    print("doot doot")
  def drive():
    position+=1
  def GPS():
    print("in",500-position,"turn left")

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
