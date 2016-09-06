
def tset():
    print 'yyy'
    # try{
    # print 'hello'
    # }catch(Exception e){
    # print 'no'
    #
    # }
    # print 'yes'
try:
    # tset() #hj
    x = 2
    x = x/0
except ArithmeticError:
    print ArithmeticError.mro
print 'uuuuuuu'
