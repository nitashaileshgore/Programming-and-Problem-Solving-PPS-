class even_odd:
    even = 0

    def check(self, num):
        if num % 2 == 0:
            self.even = 1


    def odd_even(self, num):
        self.check(num)   #method
        if self.even == 1:
            print("number is even")
        else:
            print("number is odd")

n = even_odd()
num = int(input("enter number"))
n.odd_even(num)
