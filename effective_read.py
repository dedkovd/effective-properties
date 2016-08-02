import re
  
def split_list(alist, wanted_parts=1):
  length = len(alist)
  return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
           for i in range(wanted_parts) ]

def process_file(filename):
  print 'Reading file %s' % filename
  res = {}
  M = re.compile('^ M[0-9]+')
  N = re.compile('^ N[0-9]+')
  with open(filename, 'r') as f:
    el = None
    while True:
      l = f.readline()
      if not l:
	if el != None:
	  res[el] = zip(*res[el])
	break
      if M.match(l):
	if el != None:
	  res[el] = zip(*res[el])
	l = l + f.readline()
	s = l.split()
	el = s[0]
	res[el] = []
      if N.match(l):
	l = l + f.readline()
	s = l.split()
	res[el].append((float(x) for x in s[4:]))
  return res
