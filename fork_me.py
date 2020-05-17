import os


"""
The system function call fork() creates a copy of the process, which has called it. This copy runs as a child process of the calling process. 
The child process gets the data and the code of the parent process. The child process receives a process number (PID, Process IDentifier) of 
its own from the operating system. The child process runs as an independent instance, this means independent of a parent process. 
With the return value of fork() we can decide in which process we are: 0 means that we are in the child process while a positive 
return value means that we are in the parent process. A negative return value means that an error occurred while trying to fork.

To be able to fork processes we need to import the os module in Python.

The following Python3 example shows a parent process, which forks every time the user types in a "c", when prompted. Both the child process 
and the parent process continue after the "if newpid == 0:" statement. The value of newpid is greater than 0 in the parent process 
and 0 in the child process. The exit statement os.exit(0) of the child function is necessary, because otherwise the child process 
would return into the parent process, i.e. to the input statement.
"""

def child():
    print("\n A new child process : ", os.getpid())
    os._exit(0)


def parent():
    while True:
        # When this statement is run, 2 processes will run 1) that has new_pid as 0 and another which has new_pid as > 0
        # process with new_pid is 0 will go to child() and exits. Uses same terminal.
        # process with new_pid is not 0 will go to else part and displays, & waits for input
        new_pid = os.fork()
        # print(new_pid)
        if new_pid == 0:
            child()
        else:
            parent_pid, child_pid = os.getpid(), new_pid
            print("parent: %d, child: %d\n" % (parent_pid, child_pid))
        reply = input("q for quit / c for new fork")
        if reply == 'c':
            continue
        else:
            break


parent()
