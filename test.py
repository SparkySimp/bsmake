# test bsmake here
import bsmake

# create a task runner
engine = bsmake.BSMake()

# define a task
@engine.task("hello")
def hello(args):
    print("Hello, world!")

# define another task
@engine.task("echo")
def echo(args):
    print(" ".join(args))

# define a task which executes an external program
@engine.task("exec")
def exec(args):
    bsmake.exec(args[0], args[1:])

# define a task which accesses an environment variable
@engine.task("get")
def get(args):
    print(bsmake.env(args[0]))

# define a task which sets an environment variable
@engine.task("set")
def set(args):
    bsmake.setenv(args[0], args[1])

