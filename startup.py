import subprocess
import sys

def getCmds():
	file = open('config.txt', 'r')
	lines = file.readlines()

	cmds = [];
	for line in lines:
		segments = line.split(" ")
		path = line.replace(segments[0], '', 1).replace(segments[1], '', 1).strip()
		cmd = segments[0] + " " + path + "\\" + segments[1]
		cmds.append(cmd)
	return cmds

def list():
	cmds = getCmds();
	for index in xrange(len(cmds)):
		print '%d\t%s' % (index+1, cmds[index])

def start():
	if len(sys.argv) < 3:
		print 'format \'start|s [name]\''
		return
	name = sys.argv[2]
	cmds = getCmds();
	for cmd in cmds:
		cmdexe = cmd.split(" ")
		if cmdexe[0].lower() == name.lower():
			cmdStr = '"' + cmd.replace(cmdexe[0], '', 1).strip() + '"'
			subprocess.Popen(cmdStr)
			return
	print 'not found %s, use \'add\'' % name
		
def add():
	if len(sys.argv) < 5:
		print 'format \'add [name] [exeName] [path]\''
		return
	name = sys.argv[2]
	exeName = sys.argv[3]
	path = sys.argv[4]
	file = open('config.txt', 'a')
	file.writelines('%s %s %s\n' % (name, exeName, path))
	file.close()

def delete():
	if len(sys.argv) < 3:
		print 'format \'delete|d [name]\''
		return
	name = sys.argv[2]
	with open("config.txt","r") as r:
	    lines = r.readlines()

	with open("config.txt","w") as w:
	    for line in lines:
	        if line.split(" ")[0].lower() == name.lower():
	            continue
	        w.write(line)

def set():
	if len(sys.argv) < 5:
		print 'format \'set [name] [exeName] [path]\''
		return
	name = sys.argv[2]
	exeName = sys.argv[3]
	path = sys.argv[4]
	with open("config.txt","r") as r:
	    lines = r.readlines()

	res = False
	with open("config.txt","w") as w:
	    for line in lines:
	        if line.split(" ")[0].lower() == name.lower():
	        	w.write('%s %s %s\n' % (name, exeName, path))
	        	res = True
	        else:    
	        	w.write(line)

	if not res:
		print '%s not found' % name

def printHelper():
	print 'use list|ls add delete set start|s'

def main():
	if len(sys.argv) < 2:
		printHelper()
		return

	opt = sys.argv[1]
	if opt == 'list' or opt == 'ls':
		list()
	elif opt == 'add':
		add()
	elif opt == 'delete' or opt == 'd':
		delete()
	elif opt == 'set':
		set()
	elif opt == 'start' or opt == 's':
		start()
	else:
		printHelper()

if __name__ == '__main__':
	main()