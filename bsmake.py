#!/usr/bin/env python
# bsmake_api: BSMake Task Runner API

import os
import sys
import argparse

# represents a task runner
class BSMake:
    """BSMake Task Runner DSL"""
    # constructor
    def __init__(self):
        self._lastExitCode = 0
        self.tasks = {}
    
    # represents a task
    class Task:
        """BSMake Task"""
        # constructor
        def __init__(self, name, func):
            self.name = name
            self.func = func
        
        # run the task
        def run(self, args):
            self.func(args)

    # a decorator for tasks
    def task(self, name):
        """BSMake Task Decorator"""
        # add the task to the dictionary
        def decorator(func):
            tasks[name] = self.Task(name, func)
            return func
        return decorator
         

    # run a task
    def run(self, name, args):
        """Runs a task and exits the program"""
        sys.exit(self.tasks[name].run(args))

    # execute a program
    def exec(self, program, args):
        """Executes an external program"""
        # if args is an array, join it and run the program
        if type(args) is list:
            self._lastExitCode = os.system(program + " " + " ".join(args))
        # otherwise, it should be specifying the command line to run
        else:
           self._lastExitCode = os.system(program + " " + args)
    
    # access an environment variable
    def env(self, name):
        """Hosts the environment variables"""
        return os.environ[name]
    
    # set an environment variable
    def setenv(self, name, value):
        """Sets an environment variable"""
        os.environ[name] = value
    
    # get the last exit code
    def exitcode(self):
        """Gets the last exit code"""
        return self._lastExitCode

# host the task runner, if the script is run directly
if __name__ == "__main__":
    # prepare the parser
    parser = argparse.ArgumentParser(description="bmake - Boruasn Make", prog="bsmake")
    parser.add_argument("task", help="The task to run")
    parser.add_help = True
    parser.add_argument("-v", "--version", action="version", version="bsmake 0.1.0")
    parser.add_argument("-f", "--file", help="The file to load the tasks from", default="bsmake.py")

   # parse the arguments
   # if the task is not specified, print the help
   # otherwise, run the task
   # if the task is not found, print an error
   # if the file is not found, print an error
   # if the file is not a valid python file, print an error
   # if the task throws an exception, print an error
    try:
        args = parser.parse_args()
        if args.task is None:
            parser.print_help()
        else:
            if os.path.isfile(args.file):
                try:
                    exec(open(args.file).read())
                    if args.task in engine.tasks:
                        engine.run(args.task, sys.argv[2:])
                    else:
                        print("Task '" + args.task + "' not found")
                except Exception as e:
                    print("Error: " + str(e))
    except IOError:
                print("File '" + args.file + "' not found")        
