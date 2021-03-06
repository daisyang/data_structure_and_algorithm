from time import sleep,time,ctime
import thread

loops = [4,2]

def loop(nloop, nsec, lock):
	print 'start loop', nloop, 'at: ', ctime(time())
	sleep(nloop)
	print 'loop ', nloop, 'at: ', ctime(time())
	lock.release()

def main():
	print 'starting thread...'
	locks = []
	nloops = range(len(loops))
	
	for i in nloops:
		lock = thread.allocate_lock()
		lock.acquire()
		locks.append(lock)
	for i in nloops:
		thread.start_new_thread(loop,(i,loops[i],locks[i]))

	for i in nloops:
		while locks[i].locked(): pass
	print 'all done at :' , ctime(time())

if __name__== '__main__':
	main()
