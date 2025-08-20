class HelloWorld:
    def printHelloWorld(self):
        print('Hello World')

class HelloPy:
    def printHelloWorld(self):
        print("Hello Java World!") 

    def printHelloPy(self):
        print("Hello Python World!")

    def printHelloJava(self):
        print("Hello Java ITI")        

if __name__ == '__main__':
    hw = HelloWorld()
    hw.printHelloWorld()
    hj = HelloPy()
    hj.printHelloWorld()
    hj.printHelloPy()
    hj.printHelloJava()  