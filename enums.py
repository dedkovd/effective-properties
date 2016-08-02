class EProblem(object):
	CC_Without_Contact = 0
	CC_With_Contact = 1
	CS_Without_Contact = 2
	CS_With_Contact = 3
	CC_Without_Contact_Big = 4

class ESchema(object):
	X1X3_Tension = 0
	X1_Tension = 1
	X1_Tension_X3_Compression = 2
	X1X3_Compression = 3
	X1_Compression = 4
	X1X3_Unequal_Compression = 5
	X3_Tension = 6

class EDefect(object):
	Regular = 0
	Fiber_Skip = 1
	Fiber_Skip_Matrix = 2
	One_Fiber_Break = 3
	One_Fiber_Break_Matrix = 4
	Two_Fibers_Break = 5
	Two_Fibers_Break_Matrix = 6
	Pore = 7

class EPhase(object):
	Matrix = 0
	Fibers = 1
