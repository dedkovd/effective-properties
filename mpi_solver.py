import integral, sys, time
from effective_read import *
from mpi4py import MPI

def getI(values):
  res_I = [0., 0., 0., 0., 0., 0.]
  res_V = [0., 0., 0., 0., 0., 0.]
  for i in values:
    idx = 0
    for j in i:
      intg = integral.Integral.get_integral(j)
      I = intg.I()
      res_I[idx] += I
      res_V[idx] += intg.volume()
      idx += 1
  return res_I, res_V

if __name__ == '__main__':
  comm = MPI.COMM_WORLD
  rank = comm.Get_rank()
  size = comm.Get_size()
  
  if rank == 0:
    props = process_file(sys.argv[1]).values()
    print 'File was readed. Items count:', len(props)
    props = split_list(props, size)
    start_time = time.time()
  else:
    props = None
    result_I = None
    result_V = None

  result_I = [0., 0., 0., 0., 0., 0.]
  result_V = [0., 0., 0., 0., 0., 0.]
 
  my_props = comm.scatter(props, 0)
  
  res_I, res_V = getI(my_props)
  result_I = [x+y for x,y in zip(result_I, res_I)]
  result_V = [x+y for x,y in zip(result_V, res_V)]
    
  result_I = comm.gather(result_I, 0)
  result_V = comm.gather(result_V, 0)
  
  if rank == 0:
    result_I = (sum(i) for i in zip(*result_I))
    result_V = (sum(i) for i in zip(*result_V))
    result = [x/y for x,y in zip(result_I, result_V)]
    
    print 'Time executing: ', time.time() - start_time
    print result