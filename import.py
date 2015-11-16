__author__ = 'kkdaadhi'
PI=3.14159265358979 # global constant -- only place the value of PI is set
import config
#app=input("Enter name")
#print(app)
def test(x,y,z):
    print("From Test",int(x+y+z))
    print("PI value is",PI)
    return x*y*z
ret=test(config.a,config.b,config.c)
print("Return is:",ret)