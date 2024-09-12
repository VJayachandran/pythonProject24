class Television:  # all python3 classes inherit from object
    def __init__(self, volume=0, channel=0):
    #def __init__(self, Brand, price, inches, volume=0, channel=0):
        #self.Brand = Brand
        #self.__price = price
        #self.inches = inches
        self.volume = volume
        self.channel = channel

    #def TVBrand(self, Brand):  # reference to instance as first arg
     #  print('Panasonic Television')
      # return
       #self.Brand = Brand  # setting member
    #def TVprice(self, __price):  # reference to instance as first arg
     #   print('50000')
      #  return  self.__price # return without setting member
    #def TVInches(self, inches):  # reference to instance as first arg
     #   print('48')
      #  self.inches = inches  # setting member

    def setVolume(self, volume):  # reference to instance as first arg
        if not 0 <= volume <= 100:
            print('Volume 75')
            return  # return without setting member
        self.volume = volume  # setting member

    def setChannel(self, channel):
        if not 0 <= channel <= 100:
            print('Panasonic at channel 8')

            return
        self.channel = channel

    def __str__(self):  # for printing it
        return ' Volume is {} and channel is {}.'.format(self.volume, self.channel)

tv = Television()  # calling init

while True:
    choice = input('''Panasonic TV

0 - Turn off TV
1 - TV status
2 - Change channel
3 - Change volume



''')
    if choice == '0': break
    if choice == '1':
        print(tv)  # calling __str__
        continue
    if choice == '2':
        tv.setChannel(int(input('New channel: ')))
        continue
    if choice == '3':
        tv.setVolume(int(input('New volume: ')))
        continue
    #if choice == '4':
     #   tv.Brand(int(input('Panasonic')))
        #continue
    #if choice == '5':
     #   tv.price(int(input('50000')))
      #  continue
    #if choice == '6':
     #   tv.inches(int(input('48')))
      #  continue
    print("Unknown command.")