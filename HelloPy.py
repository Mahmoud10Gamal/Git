class HelloWorld:
    def printHelloWorld(self):
        print('Hello World')

class HelloPy:
    def printHelloWorld(self):
        print("Hello Java World!")     

if __name__ == '__main__':
    hw = HelloWorld()
    hw.printHelloWorld()
    hj = HelloPy()
    hj.printHelloWorld()  