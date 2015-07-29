import numpy as np
import scipy as sp
from pyfftw.interfaces import scipy_fftpack as fftw
from scipy.io import wavfile
from matplotlib import pyplot as plt

def problem2(func):
    '''
    N - len(func)
    n - index of func
    f(n) - vector[n]
    k - index of coefficients (output) for loop of length N
    '''

    N = len(func)
    DFT = []
    count = 0
    for k in xrange(N):
        DFT.append(1./N*np.sum([np.exp(-2j*np.pi*k*n/N)*func[n] for n in xrange(N)]))
        if count % 100 == 0:
            print count
        count += 1
    return DFT

def equal(mine, theirs):
    mine = np.array(mine,dtype=np.complex128)
    theirs /= len(theirs)
    return np.allclose(mine,theirs)

def problem3(filename):    
    rate, sig = wavfile.read(filename)
    sig = sp.float32(sig)
    fsig = fftw.fft(sig,axis=0)
    fsig = fsig[1:len(fsig)/2]
    #return sp.argmax(fsig)/2
    plt.plot(sp.absolute(fsig))
    plt.show()

def gen_sinusoid(freq, length):
    samplerate = 44100 # 44100 samples per second
    stepsize = freq * 2 * sp.pi/samplerate
    sig = sp.sin(sp.arange(0, stepsize*length*samplerate, stepsize))
    scaled = sp.int16(sig/sp.absolute(sig).max() * 32767)
    return samplerate, scaled

def write_sinusoid(freq, length, filename=None):
    if filename is None:
        filename = str(freq) + ".wav"
    
    rate, sig = gen_sinusoid(freq, length)
    wavfile.write(filename, rate, sig)
