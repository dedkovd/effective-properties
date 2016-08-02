import sys, pp, integral, os
from effective_read import *
from problems import defects, effective_schemas as schemas

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

def solve(filename, ncpus):
  props = process_file(filename).values()
  print 'File was readed. Items count:', len(props)
  result_I = [0., 0., 0., 0., 0., 0.]
  result_V = [0., 0., 0., 0., 0., 0.]
  job_server = pp.Server(ppservers=(), secret='pass')
  job_server.set_ncpus(ncpus)
  print "Starting pp with", job_server.get_ncpus(), "workers"
  parts = job_server.get_ncpus()
  props = split_list(props, parts)
  jobs = [job_server.submit(getI, (i,), (), ('integral',)) for i in props]
  for job in jobs:
    res_I, res_V = job()
    result_I = [x+y for x,y in zip(result_I, res_I)]
    result_V = [x+y for x,y in zip(result_V, res_V)]
  job_server.print_stats()
  result = [x/y for x,y in zip(result_I, result_V)]
  return result


if __name__ == '__main__':
  init_folder = sys.argv[1]
  result_folder = sys.argv[2]
  defect = defects[int(sys.argv[3])]

  files = [{"name": "eps%s", "file": "EPSI_ELNO.resu", "type": "e"}, 
           {"name": "s%s", "file": "SIGM_ELNO.resu", "type": "s"}]

  dir_name = "%s/%s" %(result_folder, defect["folder"])
  if not os.path.exists(dir_name):
    os.mkdir(dir_name)
  with open("%s/data.mac" % dir_name, "w") as res_f, open("%s/data1.mac" % dir_name, "w") as res_f1, open ("%s/data.txt" % dir_name, "w") as res_f2:
    G = {"s": [], "e": []}
    for f in files:
      for s in (1,6):
        filename = "%s/%s/%s/%s" % (init_folder, schemas[s]["folder"], defect["folder"], f["file"])
        res = solve(filename, int(sys.argv[4]) if len(sys.argv)>4 else 1)
        res1 = ['%3.6f' % i for i in res[:3]]
        res_f.write("%s: [%s];\n" %(f["name"]%schemas[s]["index"], ", ".join([i[:i.index('.')+5] for i in res1])))
        G[f["type"]].append(res[3:])
      for s in (0,2):
	filename = "%s/%s/%s/%s" % (init_folder, schemas[s]["folder"], defect["folder"], f["file"])
        res = solve(filename, int(sys.argv[4]) if len(sys.argv)>4 else 1)
        res1 = ['%3.6f' % i for i in res[:3]]
        res_f1.write("%s: [%s];\n" %(f["name"]%schemas[s]["index"], ", ".join([i[:i.index('.')+5] for i in res1])))
	G[f["type"]].append(res[3:])
    for x,y in zip(G["s"], G["e"]):
      for a,b in zip(x,y):
        res_f2.write(str(a/(2*b))+", ")
      res_f2.write("\n")

