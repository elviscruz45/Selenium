class HelloWorld(): 
    @classmethod
    def tearDownClass(self,a,b):
        print(a+b)

HelloWorld.tearDownClass(2,3)