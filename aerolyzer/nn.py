import numpy as np
def nonlin(x,deriv=False):
	if(deriv == True):
		return x*(1-x)
	return 1 / (1 + np.exp(-x))
def network(X,y):	
	#X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
	#y = np.array([[0,1,1,0]]).T
	syn0 = 2*np.random.random((6,(X.size/6))) - 1
	syn1 = 2*np.random.random((y.size,1)) - 1
	for j in xrange(80000):
		l1 = 1/(1+np.exp(-(np.dot(X,syn0))))
		l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))
		l2_delta = (y - l2)*(l2*(1-l2))
		l1_delta = l2_delta.dot(syn1.T) * (l1 * (1-l1))
		syn1 += l1.T.dot(l2_delta)#synapse 1 (in between hidden layer and output)
		syn0 += X.T.dot(l1_delta)#synapse 0 (in between input and hidden layer)

	print l2

X = np.array([[.2745,.2,.3647,.2392,.2392,.3804],
	      [.0823,.1059,.1294,.0667,.0941,.1176],
	      [.4470,.0,.0078,.2353,.2039,0.],
	      [.0039,.0,.0,.2549,.4902,.7451],
	      [.698,.5412,.6902,.6274,.6902,.8431],
	      [.4706,.6078,.6157,.3804,.5882,.6157],
	      [.6667,.5804,.5765,.4745,.5686,.5569],
	      [.9529,.9529,.9176,.949,.9294,.8941],
	      [.7098,.7098,.7255,.4784,.4470,.5137],
	      [.2745,.2392,.2510,.0,.0823,.2039]])
y = np.array([[1],[0],[1],[1],[1],[0],[0],[0],[0],[1]])
network(X,y)
