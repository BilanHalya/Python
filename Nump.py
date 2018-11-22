from numpy import*
print(__version__)
show_config()
Z1 = zeros(10)
print(Z1)
Z2 = ones(10)
print(Z2)
Z3 = full(10, 2.5)
print(Z3)
Z4 = zero(10)
Z4[4] = 1
print(Z4)
Z5 = arange(10,50)
print(Z5)
Z6 = arange(50)
Z6 = Z6[::-1]
print(Z6)
Z7 = arange(9).reshape(3,3)
print(Z7)
nz = nonzero([1,2,0,0,4,0])
print(nz)
Z8 = eye(3)
print(Z8)
Z9 = random.random((3,3,3))
print(Z9)
Z10 = random.random((10,10))
Zmin, Zmax = Z10.min(), Z10.max()
print(Zmin, Zmax)
Z11 = random.random(30)
m = Z11.mean()
print(m)
Z12 = ones((10,10))
Z12[1:-1,1:-1]= 0

0 * nan
nan == nan
inf > nan
nan - nan
0.3 == 3*0.1

Z13 = diag(arange(1,5), k=-1)
print(Z13)

Z14 = zeros((8,8), dtype=int)
Z14[1::2,::2] = 1
Z14[::2,1::2]=1
print(Z14)

print(unravel_index(100,(6,7,8)))

Z15 = tile(array([[0,1],[1,0]]), (4,4))
print(Z15)

Z16 =  dot(ones((5,3)), ones((3,2)))
print(Z16)

Z17 = arange(11)
Z17[(3<Z17) & (Z<=8)]* =-1

Z18 = zeros((5,5))
Z18 += arange(5)
print(Z18)

def generate():
    for x in xrange(10):
        yield x
Z19 = fromiter(generate(),dtype = float,count = -1)
print(Z19)

Z20 = linspace(0,1,12)[1:-1]
print(Z20)

K = random.random(10)
K.sort()
print(K)

A = random.randint(0,2,5)
B = random.randint(0,2,5)
equal = allclose(A,B)
print(equal)

K1 = zeros(10)
#K1.flags.writetable = False
K1[0] = 1

K2 = random.random((10,2))
X,Y = K2[:,0],K2[:,1]
R = hypot(X, Y)
T = arctan2(Y, X)
print(R)
print(T)

K3 =  random.random(10)
K3[K3.argmax()] = 0
print(K3)

K4 = zeros((10,10),[('x',float),('y', float)])
K4['x'], K4['y'] = meshgrid(linspace(0,1,10),linspace(0,1,10))
print(K4)

X1 = arange(8)
Y1 = X1 + 0.5
C = 1.0 / subtract.outer(X1, Y1)
print(linalg.det(C))

for dtype in [int8, int32, int64]:
    print(iinfo(dtype).min)
    print(iinfo(dtype).max)
for dtype in [float32, float64]:
    print(finfo(dtype).min)
    print(finfo(dtype).max)
    print(finfo(dtype).eps)

set_printtoptions(threshold=nan)
K5 = zeros((25,25))
print(K5)

K6 = arange(100)
v = random.uniform(0,100)
index = (abs(Z-v)).argmin()
print(K6[index])

K7 = zeros (10,[('position',[('x',float,1),('y',float,1)]),
                ('color',[('r',float,1),('g',float,1), ('b',float,1)]) ])
print(K7)
import scipy.spatial

K8=random.random((10,2))
D = scipy.spatial.distance.cdist(K8,K8)
print(D)

K9 = arange(10, dtype = int32)
K9 = K9.astype(float32,  copy = False)

K10 = arange(9).reshape(3,3)
for index1, value in ndenumerate(Z):
    print(index1, value)
for index1 in ndindex(K10.shape):
    print(index1, K10[index1])

X2, Y2 = meshgrid(linspace(-1,1,10), linspace(-1,1,10))
D1 = hypot(X2, Y2)
sigma, mu = 1.0, 1.0
G = exp(-((D1-mu)**2/(2.0*sigma**2)))
print(G)

n = 10
p = 3
K11 = zeros((n,n))
put(K11, random.choice(range(n*n),p,replace=False),1)

X3 = random.rand(5,10)
Y3 = X3 -X3.mean(axis=1,keepims = True)

K11 = random.randint(0,10,(3,3))
n1 = 1
print(K11)
print(K11[K11[:,n].argsort()])

K12 = random.randint(0,3,(3,10))
print((~Z.any(axis=0)).any())

K13 = ones(10)
I = random.randint(0,len(K13),20)
K13 += bincount(I, minlength=len(K13))
print(K13)

w,h = 16, 16
I1 = random.randint(0,2,(h,w,3)).astype(ubyte)
F = I1[...,0]*256*256+I1[...,1]*256+I1[...,2]
n2 = len(unique(F))
print(unique(I1))

A3 = random.randint (0,10, (3,4,3,4))
sum = A.reshape(A.shape[:2]+(-1,)).sum(axis=-1)
print(sum)

diag(dot(A,B))
sum(A*B.T,axis=1)
eisum("ij,ji->",A,B)

K14 = array([1,2,3,4,5])
nz = 3
K0 = zeros(len(K14)+(len(K14)-1)*(nz))
K0[::nz+1]=K14
print(K0)

A4 = arange(25).reshape(5,5)
A4[[0,1]]=A4[[1,0]]
print(A4)

faces = random.randint(0,10,(10,3))
F = roll(facs.repeat(2,axis=1),-1,axis=1)
F = F.reshape(len(F)*3,2)
F = sort(F,axis=1)
G1 = F.view(dtype = [('p0',F.dtype),('p1',F.dtype)])
G1 = unique(G1)
print(G1)

C1 = bincount([1,1,2,3,4,4,6])
A5 = repeat(arabge(len(C1)),C1)
print(A5)

def moving_average(a, n=3):
    ret = cumsum(a, dtype =  float)
    ret[n:] = ret[n:]-ret[:-n]
    return ret [n-1:]/n
print(moving_average(20),3)

from numpy.lib import stride_tricks

def rolling(a,window):
    shape = (a.size - window +1, window)
    strides = (a.itemsize, a.itemsize)
    return stride_tricks.as_strided(a, shape=shape, strides=strides)
K15 = rolling(arange(10),3)
print(K15)

K16 = random.randint(0,2,10)
logical_not(arr, out =arr)

K16 = random.uniform(-1.0,1.0,100)
negative(arro, out=arr)

def distance(P0, P1, p):
    T = P1-P0
    L = (T**2).sum(axis=1)
    U = -((P0[:,0]-p[...,0])*T[:,0]+(P0[:,1]-p[...,1])*T[:,1])/L
    U = U.reshape(len(U),1)
    D = P0 + U*T-p
    return sqrt((D**2).sum(axis=1))
P0= random.uniform(-10,10,(10,2))
P1= random.uniform(-10,10,(10,2))
p= random.uniform(-10,10,(1,2))
print(distance(P0,P1, p))


K17 = random.randint(0,10,(10,10))
shape = (5,5)
fill = 0
position = (1,1)

R = ones(shape, dtype = K17.dtype)*fill
P2 = array(list(position)).astype(int)
Rs = array(list(R.shape)).astype(int)
Ks = array(list(K17.shape)).astype(int)

R_start = zeros((len(shape),)).astype(int)
R_stop = array(list(shape)).astype(int)
K17_start = (P2-Rs//2)
K17_stop = (P2+Rs//2)+Rs%2

R_start = (R_start - minimum(K17_start)).tolist()
K17_start = (maximum(K17_start,0)).tolist()
R_stop = maximum(R_start,(R_stop - maximum(K17_stop-Ks,0)).tolist()
K17_stop =(minimum(K17_stop,Ks)).tolist()



r = [slice(start,stop) for start, stop in zip(R_start, R_stop)]
k = [slice(start,stop) for start, stop in zip(K17_start, K17_stop)]
R[r]=K17[k]
print(K17)
print(R)

z1 =  random.uniform(0,1,(10,10))
rank = linalg.matrix_rank(z1)
                 





