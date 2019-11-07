import numpy as np
import matplotlib.pyplot as plt




eps = 1.5
sqlam = 1
beta = 2000
x = np.linspace(0.0, 1.0, 101)



#########  Closed form solutions
coeff_denom = 2.0 * ( 1 + np.cos(sqlam)*np.cosh(sqlam) + ( 1j * beta * sqlam * eps) / (1 + 1j * beta * sqlam * sqlam ) * ( np.sin(sqlam)*np.cosh(sqlam) + np.cos(sqlam)*np.sinh(sqlam) )  )
Ae = ( 1 + np.cos(sqlam)*np.cosh(sqlam) - np.sin(sqlam)*np.sinh(sqlam) + ( 2 * 1j * beta * sqlam * eps) / (1 + 1j * beta * sqlam * sqlam ) * np.cos(sqlam)*np.sinh(sqlam) ) / coeff_denom
Be = ( np.sin(sqlam)*np.cosh(sqlam) + np.cos(sqlam)*np.sinh(sqlam) + ( 2 * 1j * beta * sqlam * eps) / (1 + 1j * beta * sqlam * sqlam ) * np.sin(sqlam)*np.sinh(sqlam) ) / coeff_denom
Ce = - Ae
De = - Be







#########  Zeroth order expansion
A0 = ( 1.0 + np.cos(sqlam) * np.cosh(sqlam) - np.sin(sqlam) * np.sinh(sqlam) )/( 2.0 + 2.0 * np.cos(sqlam) * np.cosh(sqlam) )
B0 = ( np.cos(sqlam) * np.sinh(sqlam) + np.sin(sqlam) * np.cosh(sqlam) )/( 2.0 + 2.0 * np.cos(sqlam) * np.cosh(sqlam) )
C0 = - A0
D0 = - B0

ue = Ae * np.cos(sqlam*x) + Be * np.sin(sqlam*x) + Ce * np.cosh(sqlam*x) + De * np.sinh(sqlam*x)

#########  First order expansion
A1 = (1j * beta * sqlam / (1.0 + 1j * beta * sqlam * sqlam )) * ( (np.sinh(sqlam) - np.sin(sqlam))/(1.0 + np.cos(sqlam)*np.cosh(sqlam)) ) * ( (np.cos(sqlam) + np.cosh(sqlam))/(2.0 + 2.0*np.cos(sqlam)*np.cosh(sqlam)) )
B1 = (1j * beta * sqlam / (1.0 + 1j * beta * sqlam * sqlam )) * ( (np.sinh(sqlam) - np.sin(sqlam))/(1.0 + np.cos(sqlam)*np.cosh(sqlam)) ) * ( (-np.sinh(sqlam) + np.sin(sqlam))/(2.0 + 2.0*np.cos(sqlam)*np.cosh(sqlam)) )
C1 = - A1
D1 = - B1

#########  Second order expansion
A2 = A1 * (1j * beta * sqlam / (1.0 + 1j * beta * sqlam * sqlam )) * ( (-np.sinh(sqlam) * np.cos(sqlam) - np.sin(sqlam) * np.cosh(sqlam))/(1.0 + np.cos(sqlam)*np.cosh(sqlam)) ) 
B2 = B1 * (1j * beta * sqlam / (1.0 + 1j * beta * sqlam * sqlam )) * ( (-np.sinh(sqlam) * np.cos(sqlam) - np.sin(sqlam) * np.cosh(sqlam))/(1.0 + np.cos(sqlam)*np.cosh(sqlam)) ) 
C2 = - A2
D2 = - B2


#########  Third order expansion
A3 = A2 * (1j * beta * sqlam / (1.0 + 1j * beta * sqlam * sqlam )) * ( (-np.sinh(sqlam) * np.cos(sqlam) - np.sin(sqlam) * np.cosh(sqlam))/(1.0 + np.cos(sqlam)*np.cosh(sqlam)) ) 
B3 = B2 * (1j * beta * sqlam / (1.0 + 1j * beta * sqlam * sqlam )) * ( (-np.sinh(sqlam) * np.cos(sqlam) - np.sin(sqlam) * np.cosh(sqlam))/(1.0 + np.cos(sqlam)*np.cosh(sqlam)) ) 
C3 = - A3
D3 = - B3

#########  Expansion for the function
u0 = A0 * np.cos(sqlam*x) + B0 * np.sin(sqlam*x) + C0 * np.cosh(sqlam*x) + D0 * np.sinh(sqlam*x)
u1 = A1 * np.cos(sqlam*x) + B1 * np.sin(sqlam*x) + C1 * np.cosh(sqlam*x) + D1 * np.sinh(sqlam*x)
u2 = A2 * np.cos(sqlam*x) + B2 * np.sin(sqlam*x) + C2 * np.cosh(sqlam*x) + D2 * np.sinh(sqlam*x)
u3 = A3 * np.cos(sqlam*x) + B3 * np.sin(sqlam*x) + C3 * np.cosh(sqlam*x) + D3 * np.sinh(sqlam*x)


plt.figure()
plt.plot(x,np.abs(ue),'m--', label = 'ue')
plt.plot(x,np.abs(u0),'r-', label = 'u0')
plt.plot(x,np.abs(u0 + u1*eps),'b-', label = 'u0+e u1')
plt.plot(x,np.abs(u0 + u1*eps + u2*eps*eps),'k-', label = 'u0+e u1 + e2 u2')
plt.plot(x,np.abs(u0 + u1*eps + u2*eps*eps + + u3*eps*eps*eps),'c-', label = 'u0+e u1 + e2 u2 + e3 u3')
plt.legend()
plt.show()