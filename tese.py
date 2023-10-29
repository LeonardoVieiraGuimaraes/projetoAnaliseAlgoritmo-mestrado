# -*- coding: latin1 -*-
from numpy import arange, cos, sin
# Duas fun��es do SciPy para processamento de sinais
from scipy.signal import cspline1d, cspline1d_eval
# Duas fun��es do Matplotlib para gerar um gr�fico
from pylab import*
x0 = arange(20) # X original
y0 = cos(x0) * sin(x0 / 2) # Y a partir de X
dx = x0[1]-x0[0] # Diferen�a original
x1 = arange(-1, 21, 0.1)
# Coeficientes para arranjo de 1 dimens�o
cj = cspline1d(y0)
# Avalia o Spline para um novo conjunto de pontos
y1 = cspline1d_eval(cj, x1, dx=dx,x0=x0[0])
plot(x1, y1, '-g', x0, y0, '^y') # Desenha
show() # Mostra o gr�fico
