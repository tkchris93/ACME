# coding: utf-8
from scipy.io import wavfile
rate, tada = wavfile.read('tada.wav')
import scipy as sp

L_white = sp.int16(sp.random.randint(-32767,32767,rate*10))
R_white = sp.int16(sp.random.randint(-32767,32767,rate*10))
white = sp.zeros((len(L_white),2))
white[:,0] = L_white
white[:,1] = R_white
padded_tada = sp.zeros_like(white)
padded_tada[:len(tada)] = tada
ptada = padded_tada
ftada = sp.fft(ptada,axis=0)
fwhite = sp.fft(white,axis=0)
out = sp.ifft((ftada*fwhite),axis=0)
out = sp.real(out)
scaled = sp.int16(out / sp.absolute(out).max() * 32767)
wavfile.write('my_tada_conv.wav',rate,scaled)
