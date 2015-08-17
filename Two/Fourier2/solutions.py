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

#Problem 3. Convolve piano and balloon.
def problem3():
	'''
	If problem 3 stays as it is, this is a CORRECT solution. The current solution
	is totally jacked.
	'''
	# read in files
    rate1,piano = wavfile.read('chopinw.wav')
    rate2,balloon = wavfile.read('balloon.wav')
    
    # pad signal with zeros
    sig = np.zeros((piano.shape[0]+balloon.shape[0],2))
    sig[:len(piano)] = piano
    imp = np.zeros_like(sig)
    imp[:len(balloon)] = balloon
    
    # fourier transforms
    f1 = fftw.fft(sig,axis=0)
    f2 = fftw.fft(imp,axis=0)
    out = sp.ifft((f1*f2),axis=0)
    
    # prepping output and writing file
    out = sp.real(out)
    scaled = sp.int16(out/sp.absolute(out).max() * 32767)
    wavfile.write('test.wav',rate1,scaled)
    
#Problem 4. Let's make the "tada" circular convolution example a problem instead.
def problem4():
	# read in tada.wav
	rate, tada = wavfile.read('tada.wav')
	
	# upon inspection, we find that tada.wav is a stereo audio file. 
	# we create stereo white noise that lasts 10 seconds
	L_white = sp.int16(sp.random.randint(-32767,32767,rate*10))
	R_white = sp.int16(sp.random.randint(-32767,32767,rate*10))
	white = sp.zeros((len(L_white),2))
	white[:,0] = L_white
	white[:,1] = R_white
	
	# pad tada signal with zeros
	padded_tada = sp.zeros_like(white)
	padded_tada[:len(tada)] = tada
	ptada = padded_tada
	
	# fourier transforms
	ftada = sp.fft(ptada,axis=0)
	fwhite = sp.fft(white,axis=0)
	
	# inverse transform of convolution
	out = sp.ifft((ftada*fwhite),axis=0)
	
	# prepping output and writing file
	out = sp.real(out)
	scaled = sp.int16(out / sp.absolute(out).max() * 32767)
	wavfile.write('my_tada_conv.wav',rate,scaled)
