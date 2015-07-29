# fft_outline.py
"""
    Volume II Lab 9: Fourier I, Fast Fourier Transform
    Written by Tanner Christensen, Summer 2015
"""

import numpy as np
import scipy as sp
from scipy.io import wavfile

# Problem 1: Generate a chord
def generate_chord(freqs, filename="chord.wav", samplerate=44100, length=2):
    '''
    Combines sinusoids of provided frequencies into one signal.
    
    Parameters
    ----------
    freqs : array_like
        list of frequencies to be added together into a chord
    filename : string
        name of the output file
    samplerate : int
        samples per second
    length : int
        length of audio in seconds

    Returns
    -------
    samplerate : int
        The number of samples per second used to make the 
    chord : ndarray
        Output array, the sum of the sinusoids created from the provided frequencies.
    
    Example
    -------
    generate_chord([262,330,392,523]) : will output the resulting signal combining frequencies 
        of 262,330,392, and 523 Hz.  This is a C chord with the root on middle C.  For a list
        of frequencies, see https://en.wikipedia.org/wiki/Piano_key_frequencies
    
    create sinuoids using the frequencies passed to the function.  Add them
    together to create a chord.  Write the resulting array to a .wav file and 
    return the samplerate and array.  A C chord starting on middle C as its root has frequencies
    262,330,392, and 523.  Have a picture that that says, "When plotting the first 2000 terms, 
    your output should look like this..."
    '''
    
    chord = np.zeros(samplerate*length)    #initialize array of proper size
    for i in xrange(len(freqs)):
        #create sinusoids and add them to the chord
        stepsize = freqs[i] * 2 * sp.pi/samplerate
        sig = sp.sin(sp.arange(0, stepsize*length*samplerate, stepsize))
        chord += sig
    chord *= (32767/float(max(chord)))    #scale after the sinusoids have been added together
    chord = np.int16(chord)    #cast result to int16
    wavfile.write(filename, samplerate, chord)   #write resulting chord to .wav file
    return samplerate, chord
        
# Problem 2: Write your own DFT
def DFT(func):
    '''
    Parameters
    ----------
    func : array-like
        array of samples
    
    Returns
    -------
    DFT : array-like
        Output array, array of Discrete Fourier Transform of array, func.
    
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
        if count % 100 == 0:  #implemented just for convenience to track progress of algorithm.
            print count
        count += 1
    return DFT

# Problem 3: Find frequency of greatest amplitude
def dominant_frequency(filename):
    '''
    Calculates and returns the frequency of greatest amplitude from provided .wav file 
    
    Parameters
    ----------
    filename : string
        input .wav file
    
    Returns
    -------
    frequency : int
        The frequency of greatest amplitude in 
    '''
    
    rate, sig = wavfile.read(filename)
    fsig = sp.fft(sig)
    length = len(sig)/float(rate)
    frequency = sp.argmax(sp.absolute(fsig[1:len(fsig)/2]))/length
    return frequency
    
# Problem 4: Down-sample .wav file
def down_sample(filename, new_rate, outputfile=None):
    '''
    Create a down-sampled copy of the provided .wav file.  Unless overridden, the output
        file will be of the form "down_<orginalname>.wav"
        
    Parameters
    ----------
    filename : string
        input .wav file
    new_rate : int
        sample rate of output file
    outputfile : string
        name of output file
    '''
    
    if outputfile is None:
        outputfile = "down_" + filename

    old_rate, in_sig = wavfile.read(filename)
    in_sig = sp.float32(in_sig)
    fin = sp.fft(in_sig)
    nsiz = sp.floor(in_sig.size * new_rate / old_rate)
    nsizh = sp.floor(nsiz / 2)
    fout = sp.zeros(nsiz)
    fout = fout + 0j
    fout[0:nsizh] = fin[0:nsizh]
    fout[nsiz-nsizh+1:] = sp.conj(sp.flipud(fout[1:nsizh]))
    out = sp.ifft(fout)
    out = sp.real(out) # Take the real component of the signal
    out = sp.int16(out/sp.absolute(out).max() * 32767)
    wavfile.write(outputfile, new_rate, out)

'''
Possible Outline:

    How speakers work (shorten what is there)

    How to write a sinusoid to a .wav file. (keep basically what is there already)

    I dont know if it is necessary to include the pulseramp stuff
 Problem 1: Generate a chord.  Add sinusoids together to make a chord.  Scale to the int16 range 
    after adding them together 

    e**(2pi*ikx/N) significance.  Talk about Fourier series a tiny bit.
    
    DFT and the equations for DFT  (make sure the variables used are the same as the textbook.  
        We could even reference the textbook here on this part and dont have any of the explanation, 
        just the equations. Recall from the textbook that the equations
        ******It would be cool to mention that the DFT is the foundation of the Shazam algorithm.
        
    Brief introduction to sp.fft().  Talk about big 0 values of our DFT and scipy's DFT

 Problem 2: Write your own DFT.  Check your function by comparing the outputs from your DFT and sp.fft() 
    when performed on the result from Problem 1.  Only do this for the first 3000 terms so your DFT 
    does not take forever to execute.  Use np.allclose() to check your answers.
    
    Explain significance of peaks in DFT.  Talk about dividing by the length of the audio clip.  
        Demonstrate to the students using their result from Problem 2 that the spikes correspond 
        to the frequencies of the chord.

    Introduce FFTW briefly.  Maybe worth mentioning how much faster fftw.fft() is than sp.fft()    
        
 Problem 3: Write a function that returns the frequency of highest amplitude of a given .wav file.  
    Have the students check their function using pianoclip.wav.  Output should be about 742.28 Hz.

    (Decide whether or not to include overtone stuff. We dont use it at all for the problems and it is a 
        little confusing.)

    Down-sampling a signal and aliasing. (we give them way too much code.  Problem 4 will just be copy 
        and paste in its current state.  Would it be too difficult to not give them any code? Maybe just 
        give them a little pseudocode?)
        
    Details about the equations behind the inverse DFT.  (As of now, its just mentioned briefly then we 
        use the scipy version without understanding anything out it)
        
*  Problem 4: Write a function that down-samples a file to a new provided sample rate.  
'''
