#!/usr/bin/env python
# bsmake_api: BSMake Task Runner API

import os
import sys

# represents a task runner
class BSMake:
    """BSMake Task Runner DSL"""
    # constructor
    def __init__(self):
        self._lastExitCode = 0
    
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

    # static dictionary which holds all tasks
    tasks = {}

    # a decorator for tasks
    def task(self, name):
        """BSMake Task Decorator"""
        # add the task to the dictionary
        tasks[name] = self.Task(name, func)
        def decorator(func):
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
    # find if there's a file named "bsmake.py" in the current directory
    if os.path.isfile("bsmake.py"):
        # import the file
        from bsmake import engine

        # if the first argument isn't specified, behave like Make and run the first task
        if len(sys.argv) == 1:
            engine.run(engine.tasks.keys()[0], sys.argv[1:])

        # run the task
        engine.run(sys.argv[1], sys.argv[2:])
    else:
        # complain about the missing file in the style of Make
        print("No rule to make target '" + sys.argv[1] + "'")
        sys.exit(1)