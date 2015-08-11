import scipy as sp
import numpy as np
from scipy.io import wavfile
from matplotlib import pyplot as plt
from pyfftw.interfaces import scipy_fftpack as fftw


def problem1():
    #clean up noisy signal "The only thing to fear is fear itself"
    rate,data = wavfile.read("Noisysignal2.wav")
    fsig = sp.fft(data,axis=0)
    for j in xrange(14999,50000):
        fsig[j] = 0
        fsig[-j] = 0
    newsig = sp.ifft(fsig)
    newsig = sp.real(newsig)
    newsig = sp.int16(newsig/sp.absolute(newsig).max() * 32767)
    wavfile.write("output.wav", rate, newsig)
    return newsig

'''
Other than figuring out what range of numbers you need to cut out, this
problem is essentially copy-paste at the moment. I guess that's okay for a 
first problem.
'''

#Problem 2. Create your own balloon pop.  I think that's pretty cool

'''
Idea for problem 3.  Write your own convolution function then pass the 
two arrays to it?  We will definitely need to find a way to make the grading
easy.
'''

def problem3():

    rate1,piano = wavfile.read('chopinw.wav')
    rate2,balloon = wavfile.read('balloon.wav')
    sig = np.zeros((piano.shape[0]+balloon.shape[0],2))
    sig[:len(piano)] = piano
    imp = np.zeros_like(sig)
    imp[:len(balloon)] = balloon
    f1 = fftw.fft(sig,axis=0)
    print 'first dft done'
    f2 = fftw.fft(imp,axis=0)
    print 'second dft done'
    out = sp.ifft((f1*f2),axis=0)
    print 'idft done'
    out = sp.real(out)
    scaled = sp.int16(out/sp.absolute(out).max() * 32767)
    wavfile.write('test.wav',rate1,scaled)
    
    '''
    rate1,piano = wavfile.read("chopinw.wav")
    rate2,balloon = wavfile.read("balloon.wav")
    impulse = np.zeros_like(piano)
    impulse[:balloon.shape[0]] = balloon
    fpiano = sp.fft(piano,axis=0)
    fimp = sp.fft(impulse,axis=0)
    fconv = fpiano*fimp
    out = sp.ifft(fconv)
    out = sp.real(out)
    scaled = sp.int16(out/sp.absolute(out).max()*32767)
    wavfile.write("chopin_conv.wav",rate1,scaled)
    '''
def mono_problem3():
    rate1, piano = wavfile.read("chopinw.wav")
    rate2, balloon = wavfile.read("balloon.wav")
    mono_piano = piano[:,0]
    mono_bal = balloon[:,0]
    sig = np.zeros(len(mono_piano)+len(mono_bal))
    sig[:len(mono_piano)] = mono_piano
    impulse = np.zeros_like(sig)
    impulse[:len(mono_bal)] = mono_bal
    fsig = fftw.fft(sig)
    print "piano dft done"
    fimp = fftw.fft(impulse)
    print "balloon dft done"
    fconv = fsig*fimp
    out = fftw.ifft(fconv)
    print "idft done"
    out = sp.real(out)
    scaled = sp.int16(out/sp.absolute(out).max()*32767)
    wavfile.write("mono_conv.wav",rate1,scaled)

#mono_problem3()
