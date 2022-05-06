import numpy as np
import matplotlib.pyplot as plt

h = 6.626e-34
c = 3.0e+8
k = 1.38e-23
pi = 4*np.arctan(1.0)

def planck(W,T): #planck's Law
    a = 8.0*pi*h*c
    b = h*c/(W*k*T)
    ret = a/((W**5)*(np.exp(b)-1.0))
    return ret

def ray(W,T): #rayleigh-Jeans Law
    return (8*pi*k*T)/(W**4)

def wein(W,T): #weins Law
    a = 8.0*pi*h*c
    b = h*c/(W*k*T)
    ret = a*np.exp(-b)/(W**5)
    return ret

w = np.arange(0.1e-6,30e-6,0.005e-6)

p0 = planck(w,500)
p1 = planck(w,600)
p2 = planck(w,700)
p3 = planck(w,800)
p4 = planck(w,900)
p5 = planck(w,1000)

plt.title('PLANCKs radiation Law')
plt.plot(w*1e6,p0)
plt.plot(w*1e6,p1)
plt.plot(w*1e6,p2)
plt.plot(w*1e6,p3)
plt.plot(w*1e6,p4)
plt.plot(w*1e6,p5)
plt.legend(["500k","600k","700k","800k","900k","1000k"])
plt.show()

p5 = planck(w,1000)
r = ray(w,1000)
we = wein(w,1000)

plt.title('T =1000k')
plt.xlim(0,20)
plt.ylim(0,200)
plt.plot(w*1e6,p5)
plt.plot(w*1e6,r)
plt.plot(w*1e6,we)
plt.legend(["Planck's law","rayleigh-Jeans Law","weins law"])
plt.show()