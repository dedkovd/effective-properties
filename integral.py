import math

class AbstractIntegral(object):
  def __init__(self, values):
    self._values = values
  
  def function(self,x,y,z):
    return sum((i*j(x,y,z) for i,j in zip(self._values,self.shape_function)))
  
  x = lambda self, idx: self.points[idx][0]

  y = lambda self, idx: self.points[idx][1]
  
  z = lambda self, idx: self.points[idx][2]
  
  p = lambda self: xrange(len(self.points))
  
  volume = lambda self: sum(self.weight)
  
  @classmethod
  def nodes_count(self): 
    return len(self.shape_function)
  
  def I(self):
    return sum((self.weight[i]*self.function(self.x(i),self.y(i),self.z(i)) for i in self.p()))
  
class TetrahedronIntegral(AbstractIntegral):
  shape_function = (lambda x,y,z: y*(2*y-1),                 #1
		    lambda x,y,z: z*(2*z-1),                 #2
		    lambda x,y,z: (1-x-y-z)*(1-2*x-2*y-2*z), #3
		    lambda x,y,z: x*(2*x-1),                 #4
		    lambda x,y,z: 4*y*z,                     #5
		    lambda x,y,z: 4*z*(1-x-y-z),             #6
		    lambda x,y,z: 4*y*(1-x-y-z),             #7
		    lambda x,y,z: 4*x*y,                     #8
		    lambda x,y,z: 4*x*z,                     #9
		    lambda x,y,z: 4*x*(1-x-y-z))             #10
  
  a = 0.25
  b = 1./6.
  c = 0.5
  
  points = ((a,a,a),
	    (b,b,b),
	    (b,b,c),
	    (b,c,b),
	    (c,b,b))
  
  weight = (-2./15., 3./40., 3./40., 3./40., 3./40.)  

class HexahedronIntegral(AbstractIntegral):
  shape_function = (lambda x,y,z: (1./8.)*(1-x)*(1-y)*(1-z)*(-2-x-y-z), #1
		    lambda x,y,z: (1./8.)*(1+x)*(1-y)*(1-z)*(-2+x-y-z), #2
		    lambda x,y,z: (1./8.)*(1+x)*(1+y)*(1-z)*(-2+x+y-z), #3
		    lambda x,y,z: (1./8.)*(1-x)*(1+y)*(1-z)*(-2-x+y-z), #4
		    lambda x,y,z: (1./8.)*(1-x)*(1-y)*(1+z)*(-2-x-y+z), #5
		    lambda x,y,z: (1./8.)*(1+x)*(1-y)*(1+z)*(-2+x-y+z), #6
		    lambda x,y,z: (1./8.)*(1+x)*(1+y)*(1+z)*(-2+x+y+z), #7
		    lambda x,y,z: (1./8.)*(1-x)*(1+y)*(1+z)*(-2-x+y+z), #8
		    lambda x,y,z: (1./4.)*(1-x**2)*(1-y)*(1-z),         #9
		    lambda x,y,z: (1./4.)*(1-y**2)*(1+x)*(1-z),         #10
		    lambda x,y,z: (1./4.)*(1-x**2)*(1+y)*(1-z),         #11
		    lambda x,y,z: (1./4.)*(1-y**2)*(1-x)*(1-z),         #12
		    lambda x,y,z: (1./4.)*(1-z**2)*(1-x)*(1-y),         #13
		    lambda x,y,z: (1./4.)*(1-z**2)*(1+x)*(1-y),         #14
		    lambda x,y,z: (1./4.)*(1-z**2)*(1+x)*(1+y),         #15
		    lambda x,y,z: (1./4.)*(1-z**2)*(1-x)*(1+y),         #16
		    lambda x,y,z: (1./4.)*(1-x**2)*(1-y)*(1+z),         #17
		    lambda x,y,z: (1./4.)*(1-y**2)*(1+x)*(1+z),         #18
		    lambda x,y,z: (1./4.)*(1-x**2)*(1+y)*(1+z),         #19
		    lambda x,y,z: (1./4.)*(1-y**2)*(1-x)*(1+z),         #20
		    )
  
  points = ((-1./math.sqrt(3),-1./math.sqrt(3),-1./math.sqrt(3)),
	    (-1./math.sqrt(3),-1./math.sqrt(3), 1./math.sqrt(3)),
	    (-1./math.sqrt(3), 1./math.sqrt(3),-1./math.sqrt(3)),
	    (-1./math.sqrt(3), 1./math.sqrt(3), 1./math.sqrt(3)),
	    ( 1./math.sqrt(3),-1./math.sqrt(3),-1./math.sqrt(3)),
	    ( 1./math.sqrt(3),-1./math.sqrt(3), 1./math.sqrt(3)),
	    ( 1./math.sqrt(3), 1./math.sqrt(3),-1./math.sqrt(3)),
	    ( 1./math.sqrt(3), 1./math.sqrt(3), 1./math.sqrt(3)))
  
  weight = tuple(1. for _ in xrange(len(points)))
  
class PentahedronIntegral(AbstractIntegral):
  shape_function = (lambda x,y,z: (y*(1-x)*(2*y-2-x))/2.,           #1
		    lambda x,y,z: (z*(1-x)*(2*z-2-x))/2.,           #2
		    lambda x,y,z: ((x-1)*(1-y-z)*(x+2*y+2*z))/2.,   #3
		    lambda x,y,z: (y*(1+x)*(2*y-2+x))/2.,           #4
		    lambda x,y,z: (z*(1+x)*(2*y-2+x))/2.,           #5
		    lambda x,y,z: ((-x-1)*(1-y-z)*(-x+2*y+2*z))/2., #6
		    lambda x,y,z: 2*y*z*(1-x),                      #7
		    lambda x,y,z: 2*z*(1-y-z)*(1-x),                #8
		    lambda x,y,z: 2*y*(1-y-z)*(1-x),                #9
		    lambda x,y,z: y*(1-x**2),                       #10
		    lambda x,y,z: z*(1-x**2),                       #11
		    lambda x,y,z: (1-y-z)*(1-x**2),                 #12
		    lambda x,y,z: 2*y*z*(1+x),                      #13
		    lambda x,y,z: 2*z*(1-y-z)*(1+x),                #14
		    lambda x,y,z: 2*y*(1-y-z)*(1+x),                #15
		    )
  
  a = 0.577350269189626
  
  points = ((-a, 1./3., 1./3.),
	    (-a, 0.6,   0.2),
	    (-a, 0.2,   0.6),
	    (-a, 0.2,   0.2),
	    ( a, 1./3., 1./3.),
	    ( a, 0.6,   0.2),
	    ( a, 0.2,   0.6),
	    ( a, 0.2,   0.2))
  
  weight = (-27./96., 
	    25./96., 
	    25./96., 
	    25./96., 
	    -27./96., 
	    25./96., 
	    25./96., 
	    25./96.)
  
class PyramidIntegral(AbstractIntegral):
  shape_function = (lambda x,y,z: ((-x+y+z-1)*(-x-y+z-1)*(x-0.5))/(2*(1-z)),   #1
		    lambda x,y,z: ((-x-y+z-1)*(x-y+z-1)*(y-0.5))/(2*(1-z)),    #2
		    lambda x,y,z: ((x-y+z-1)*(x+y+z-1)*(-x-0.5))/(2*(1-z)),    #3
		    lambda x,y,z: ((x+y+z-1)*(-x+y+z-1)*(-y-0.5))/(2*(1-z)),   #4
		    lambda x,y,z: 2*z*(z-0.5),                                 #5
		    lambda x,y,z: ((-x+y+z-1)*(-x-y+z-1)*(x-y+z-1))/(2*(1-z)), #6
		    lambda x,y,z: ((-x-y+z-1)*(x-y+z-1)*(x+y+z-1))/(2*(1-z)),  #7
		    lambda x,y,z: ((x-y+z-1)*(x+y+z-1)*(-x+y+z-1))/(2*(1-z)),  #8
		    lambda x,y,z: ((x+y+z-1)*(-x+y+z-1)*(-x-y+z-1))/(2*(1-z)), #9
		    lambda x,y,z: (z*(-x+y+z-1)*(-x-y+z-1))/(1-z),             #10
		    lambda x,y,z: (z*(-x-y+z-1)*(x-y+z-1))/(1-z),              #11
		    lambda x,y,z: (z*(x-y+z-1)*(x+y+z-1))/(1-z),               #12
		    lambda x,y,z: (z*(x+y+z-1)*(-x+y+z-1))/(1-z),              #13
		    )

  h1 = 0.1531754163448146
  h2 = 0.6372983346207416
  
  points = (( 0.5,    0, h1),
	    (   0,  0.5, h1),
	    (-0.5,    0, h1),
	    (   0, -0.5, h1),
	    (   0,    0, h2))
  
  weight = tuple(2./15. for _ in xrange(len(points)))
  
class TestIntegral(AbstractIntegral):
  shape_function = (lambda x, y, z: 4*x**3,)

  points = ((-0.906179846,),(-0.538469310,),(0,),(0.53846931,),(0.906179846,))
  
  weight = (0.236926885, 0.478628670, 0.568888889, 0.478628670, 0.236926885)

class Integral(object):
  integrals = {TetrahedronIntegral.nodes_count(): TetrahedronIntegral,
	       HexahedronIntegral.nodes_count(): HexahedronIntegral,
	       PentahedronIntegral.nodes_count(): PentahedronIntegral,
	       PyramidIntegral.nodes_count(): PyramidIntegral,
	       TestIntegral.nodes_count(): TestIntegral}
  
  @classmethod
  def get_integral(self, values):
    cnt = len(values)
    return self.integrals[cnt](values)