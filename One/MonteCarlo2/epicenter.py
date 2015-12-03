# coding: utf-8

get_ipython().magic(u'pinfo rnorm')
get_ipython().magic(u'pinfo norm')
get_ipython().magic(u'clear ')
randn
randn(20) + 3.
y = _
get_ipython().magic(u'clear ')
y
hist(y)
hist(rnorm(10000) + 3.)
hist(randn(10000) + 3.)
get_ipython().magic(u'clear ')
get_ipython().magic(u'pinfo normpdf')
normpdf(y, 0)
from scipy.stats.distributions import norm
get_ipython().magic(u'clear ')
norm(0).pdf(y)
get_ipython().magic(u'clear ')
xx = linspace(0,6,1000)
plot(xx, norm(0).pdf(xx))
plot(xx, norm(1).pdf(xx))
plot(xx, norm(2).pdf(xx))
close()
prod(norm(m).pdf(y))
prod(norm(0.).pdf(y))
prod(norm(1.).pdf(y))
prod(norm(2.).pdf(y))
mm = linspace(0,6,1000)
plot(mm, [prod(norm(m).pdf(y)) for m in mm])
y.mean()
close()
get_ipython().magic(u'clear ')
yy = linspace(-6,6,1000)
plot(yy, norm().pdf(yy))
plot(yy, norm().pdf(yy)*norm(1).pdf(yy))
close()
plot(yy, norm().pdf(yy)*norm(3).pdf(yy))
plot(yy, norm().pdf(yy)*(sin(yy) + 1))
clsoe()
close()
clsoe()
plot(yy, norm().pdf(yy)*(sin(yy) + 1))
ff = norm().pdf(yy)*(sin(yy) + 1)
ff
sum(norm().pdf(yy))
dy = yy[1] - yy[0]
dy
sum(norm().pdf(yy))*dy
sum(ff)*dy
plot(yy, ff)
ff = norm().pdf(yy)*(sin(yy*10) + 1)
plot(yy, ff)
ff = norm().pdf(yy)*(sin(yy*2) + 1)
plot(yy, ff)
close()
plot(yy, ff)
sum(ff)*dy
ff = norm().pdf(yy)*(sin(yy**2) + 1)
plot(yy, ff)
close()
ff = norm().pdf(yy)*(sin(yy**2) + 1)
plot(yy, ff)
sum(ff) * dy
ll = norm().pdf(yy)
qq = sin(yy**2) + 1
close(
)
plot(yy, ll)
plot(yy, qq)
plot(yy, ll*qq)
close()
plot(yy, ll*qq)
close()
f = norm(rand()*1000000).pdf
xx = linspace(-2000000,2000000,1000)
f(xx)
any(_)
get_ipython().magic(u'clear ')
f(xx)
get_ipython().magic(u'clear ')
sum(linspace(-2000000,2000000,1000))
sum(linspace(-2000000,2000000,10000))
sum(f(linspace(-2000000,2000000,10000)))
sum(f(linspace(-2000000,2000000,1000)))
sum(f(linspace(-2000000,2000000,10000)))
sum(f(linspace(-2000000,2000000,100000)))
f(rand(100)*4000000 - 2000000)
sum(f(rand(100)*4000000 - 2000000))
sum(f(rand(100)*4000000 - 2000000))/100.
g = lambda n: sum(f(rand(n)*4000000 - 2000000))/float(n)
g(100)
g(1000)
g(10000)
g(100000)
g(1000000)
g(10000000)
g(100000000)
m rand()*1000000
m = rand()*1000000
m
hint = 965430
f = norm(m).pdf
g = lambda n: sum(f(rand(n)*4000000 - 2000000))/float(n)
g(1000)
f(norm(hint,5).rvs(1000))
sum(f(norm(hint,5).rvs(1000)))/1000.
sum(f(norm(hint,5).rvs(10000)))/10000.
sum(f(norm(hint,10).rvs(10000)))/10000.
sum(f(norm(hint,20).rvs(10000)))/10000.
sum(f(norm(m).rvs(10000)))/10000.
sum(f(norm(m,10).rvs(10000)))/10000.
sum(f(norm(m,100).rvs(10000)))/10000.
sum(f(norm(m,0.1).rvs(10000)))/10000.
sum(f(norm(m,0.).rvs(10000)))/10000.
get_ipython().magic(u'clear ')
people = zeros(1000000)
people
center = 333000
people = zeros(1000,1000)
people = zeros((1000,1000))
get_ipython().magic(u'clear ')
people
epicenter = array([321,657])
for i in xrange(1000):
    for j in xrange(1000):
        you = array([i,j])
        prob = 4./norm(you - epicenter)
        if rand() < prob:
            people[i,j] = 1.
            
for i in xrange(1000):
    for j in xrange(1000):
        you = array([i,j])
        prob = 4./sqrt((you - epicenter)**2)
        if rand() < prob:
            people[i,j] = 1.
            
for i in xrange(1000):
    for j in xrange(1000):
        you = array([i,j])
        prob = 4./sqrt(sum((you - epicenter)**2))
        if rand() < prob:
            people[i,j] = 1.
            
for i in xrange(1000):
    for j in xrange(1000):
        you = array([i,j])
        prob = 4./(1. + sqrt(sum((you - epicenter)**2)))
        if rand() < prob:
            people[i,j] = 1.
            
people
sum(people)_
sum(people)
for i in xrange(1000):
    for j in xrange(1000):
        you = array([i,j])
        prob = 1./(1. + sqrt(sum((you - epicenter)**2)))
        if rand() < prob:
            people[i,j] = 1.
            
sum(peopel)
sum(people)
for i in xrange(1000):
    for j in xrange(1000):
        you = array([i,j])
        prob = .1/(1. + sqrt(sum((you - epicenter)**2)))
        if rand() < prob:
            people[i,j] = 1.
            
sum(people)
.1/(1. + sqrt(sum((array([10,10]) - epicenter)**2)))
pcolor(people)
pcolor(people[::10,::10])
for i in xrange(1000):
    for j in xrange(1000):
        you = array([i,j])
        prob = 1./(1. + sqrt(sum((you - epicenter)**2)))
        if rand() < prob:
            people[i,j] = 1.
            
pcolor(people[::10,::10])
close()
people = zeros((1000,1000))
for i in xrange(1000):
    for j in xrange(1000):
        you = array([i,j])
        prob = 1./(1. + sqrt(sum((you - epicenter)**2)))
        if rand() < prob:
            people[i,j] = 1.
            
sum(people)
pcolor(people[::10,::10])
pcolor(people)
pcolor(people[:100,:100])
pcolor(people[:100,100:200])
pcolor(people[:100,200:300])
epicenter
pcolor(people[300:400,600:700])
people
sum(people)
random.randint(0,100)
people[random.randint(0,1000),random.randint(0,1000)]
people[random.randint(0,1000),random.randint(0,1000)]
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(300)])
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(300)])
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(300)])
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(300)])
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(300)])
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(300)])
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(300)])
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(300)])
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(300)])
epicenter
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(300)]) * 1000000/300.
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(300)]) * 1000000/300.
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(300)]) * 1000000/300.
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(300)]) * 1000000/300.
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(300)]) * 1000000/300.
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(300)]) * 1000000/300.
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(300)]) * 1000000/300.
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(300)]) * 1000000/300.
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(300)]) * 1000000/300.
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(300)]) * 1000000/300.
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(300)])
epicenter
ii = randn(300)*30 + 321
jj = randn(300)*30 + 657
sum([person[i,j] for i,j in zip(ii,jj)])
sum([people[i,j] for i,j in zip(ii,jj)])
w1 = array([norm(321,30).pdf(i) * norm(657,30).pdf(j) for i,j in ii,jj])
w1 = array([norm(321,30).pdf(i) * norm(657,30).pdf(j) for i,j in zip(ii,jj)])
w1
w1 = array([people[i,j]/norm(321,30).pdf(i)/norm(657,30).pdf(j) for i,j in zip(ii,jj)])
w1
sum(_)
sum(_)/300.
sum(people)
jj = randn(300)*10 + 657
ii = randn(300)*10 + 321
w1 = array([people[i,j]/norm(321,10).pdf(i)/norm(657,10).pdf(j) for i,j in zip(ii,jj)])
sum(w1)/300.
ii = randn(3000)*30 + 321
jj = randn(3000)*10 + 657
w1 = array([people[i,j]/norm(321,10).pdf(i)/norm(657,10).pdf(j) for i,j in zip(ii,jj)])
sum(w1)/3000.
ii = randn(3000)*30 + 321
jj = randn(3000)*30 + 657
w1 = array([people[i,j]/norm(321,30).pdf(i)/norm(657,30).pdf(j) for i,j in zip(ii,jj)])
sum(w1)/3000.
sum(people)
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(3000)])*1000000/3000.
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(3000)])*1000000/3000.
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(3000)])*1000000/3000.
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(3000)])*1000000/3000.
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(3000)])*1000000/3000.
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(3000)])*1000000/3000.
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(3000)])*1000000/3000.
sum([people[random.randint(0,1000),random.randint(0,1000)] for i in xrange(3000)])*1000000/3000.
sum(people)
epicenter
ii = randn(3000)*50 + 321
jj = randn(3000)*50 + 657
w1 = array([people[i,j]/norm(321,50).pdf(i)/norm(657,50).pdf(j) for i,j in zip(ii,jj)])
sum(w1)/3000.
jj = randn(3000)*500 + 657
ii = randn(3000)*500 + 321
w1 = array([people[i,j]/norm(321,50).pdf(i)/norm(657,50).pdf(j) for i,j in zip(ii,jj)])
w1 = array([people[i,j]/norm(321,500).pdf(i)/norm(657,500).pdf(j) for i,j in zip(ii,jj)])
ii = randn(3000)*100 + 321
jj = randn(3000)*100 + 657
w1 = array([people[i,j]/norm(321,500).pdf(i)/norm(657,500).pdf(j) for i,j in zip(ii,jj)])
ii = randn(3000)*70 + 321
jj = randn(3000)*70 + 657
people[ii[0],jj[0]]
ii[0]
people[417.1, 435.6]
people[417, 435]
where(peopl)
where(people)
people[0, 344]
people[0.4, 344.4]
ii = randn(3000)*70 + 321
jj = randn(3000)*70 + 657
w1 = array([people[i,j]/norm(321,500).pdf(i)/norm(657,500).pdf(j) for i,j in zip(ii,jj)])
sum(w1)/3000.
sum(w1)/3000.
ii = randn(300)*10 + 321
jj = randn(300)*10 + 657
weights = zeros((1000,1000))
for i in xrange(1000):
    for j in xrange(1000):
        weights = norm(321,10).pdf(i)*norm(657,10).pdf(j)
        
i
epicenter
d1 = norm(321,10)
d2 = norm(657,10)
for i in xrange(1000):
    for j in xrange(1000):
        weights = d1.pdf(i)*d2.pdf(j)
        
outer(d1.pdf(arange(1000)), d2.pdf(arange(1000))
)
weights = _
weights.sum()
pcolor(weights[300:400,600:700])
weights outer(norm(321,100).pdf(arange(1000)), norm(657,100).pdf(arange(1000))
)
weights = outer(norm(321,100).pdf(arange(1000)), norm(657,100).pdf(arange(1000))
)
weights
pcolor(weights[300:400,600:700])
get_ipython().magic(u'clear ')
sum(weights)
get_ipython().magic(u'clear ')
weights
get_ipython().magic(u'clear ')
multinomial(3000, weights.flatten())
multinomial(1, weights.flatten()).argmax)
multinomial(1, weights.flatten()).argmax()
multinomial(1, weights.flatten()).argmax()
tests = array([multinomial(1, weights.flatten()).argmax() for i in xrange(3000)])
tests = array([multinomial(1, weights.flatten()).argmax() for i in xrange(30)])
tests
testsii = tests/1000
testsjj = tests%1000
testsii
testsjj
[people[i,j] for i,j in zip(testsii,testsjj)]
[people[i,j]/weights[i,j] for i,j in zip(testsii,testsjj)]
sum([people[i,j]/weights[i,j] for i,j in zip(testsii,testsjj)])
sum([people[i,j]/weights[i,j] for i,j in zip(testsii,testsjj)])/30.
tests = array([multinomial(1, weights.flatten()).argmax() for i in xrange(30)])
sum([people[i,j]/weights[i,j] for i,j in zip(testsii,testsjj)])/30.
tests = array([multinomial(1, weights.flatten()).argmax() for i in xrange(300)])
sum([people[i,j]/weights[i,j] for i,j in zip(testsii,testsjj)])/300.
testsii = tests/1000
testsjj = tests%1000
sum([people[i,j]/weights[i,j] for i,j in zip(testsii,testsjj)])/300.
sum(people)
get_ipython().magic(u'save epicenter')
get_ipython().run_cell_magic(u'save', u'epicenter', u'')
get_ipython().magic(u'save')
get_ipython().magic(u'save epicenter.py')
get_ipython().magic(u'save epicenter 0-288')
