import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def status(msgstring,destination=sys.stdout,verbose=True):
	if verbose==False:
		return
	print (bcolors.OKBLUE +bcolors.BOLD+"<Status>: "+bcolors.ENDC + msgstring,file=destination)

def error(msgstring,error=False,errorType=RuntimeError,destination=sys.stdout,verbose=True):
	if verbose==False:
		return
	action,msgstart=(lambda x:(_ for _ in ()).throw(errorType(x)),"<Error>: ") if error else (lambda x:destination.write(str(x)+'\n'),bcolors.WARNING+bcolors.BOLD+"<Warning>: "+bcolors.ENDC)
	action("%s%s"%(msgstart,msgstring))

def success(msgstring,destination=sys.stdout,verbose=True):
	if verbose==False:
		return
	print(bcolors.OKGREEN+bcolors.BOLD+"<Success>: "+ bcolors.ENDC+msgstring,file=destination)

def progress_spinner(message,progress,speed=1./5000):
	print ("%s%s"%(message,'/-\|'[int(progress*speed)%4]),end="\r")

