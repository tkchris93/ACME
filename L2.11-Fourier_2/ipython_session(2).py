from scipy.io import wavfile
import scipy as sp
import numpy as np
rate1, piano = wavfile.read("chopinw.wav")
rate2, balloon = wavfile.read("balloon.wav")
mono_piano = piano[:,0]
mono_bal = balloon[:,0]
sig = np.zeros(len(mono_piano)+len(mono_bal))
sig[:len(mono_piano)] = mono_piano
impulse = np.zeros_like(sig)
impulse[:len(mono_bal)] = mono_bal
fsig = sp.fft(sig)
fimp = sp.fft(impulse)
fconv = fsig*fimp
out = sp.ifft(fconv)
out = sp.real(out)
scaled = sp.int16(out/sp.absolute(out).max()*32767)
wavfile.write("mono_conv.wav",rate1,scaled)
