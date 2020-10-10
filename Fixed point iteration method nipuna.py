def fixedp(f,x0, tol, max_itr):
    e =1
    itr = 0
    xp = []
    while (e > tol and itr <max_itr):
        x = f(x0) #the fixed point equation
        e = abs(x0-x) #the error of current iteration
        x0 = x
        xp.append(x0) 
        itr =+ 1
    print("Root of the equation = ", x)
    print("No. of Iterations = ",len(xp) )

def f(x):
    f = (3*x + 2)**(1/2)
    return f

x0 =1
tol = 0.001
max_itr = 140
fixedp(f,x0, tol, max_itr)







