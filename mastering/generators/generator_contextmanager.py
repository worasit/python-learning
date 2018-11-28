import datetime
import contextlib


# Context manager that shows how long a context was active
@contextlib.contextmanager
def timer(name):
    start_time = datetime.datetime.now()
    yield
    stop_time = datetime.datetime.now()
    print('%s took %s' % (name, stop_time - start_time))


# The write to log function writes all stdout (regular print data) to
# a file.  The contextlib.redirect_stdout context wrapper
# temporarily redirects standard output to a given file handle, in
# this case the file we just opened for writing.
@contextlib.contextmanager
def write_to_log(name):
    with open('%s.txt' % name, 'w') as fh:
        with contextlib.redirect_stdout(fh):
            with timer(name):
                yield


# Use the context manager as a decorator
@write_to_log('some function')
def some_function():
    print('This function take a bit of time to execute')
    for i in range(100000):
        for j in range(1000):
            continue
    print('Done')


# some_function()


# ExitStack : easy combining of multiple context manager
@contextlib.contextmanager
def write_to_log_v2(name):
    with contextlib.ExitStack() as exit_stack:
        fh = exit_stack.enter_context(open('stdout.txt', 'w'))
        exit_stack.enter_context(contextlib.redirect_stdout(fh))
        exit_stack.enter_context(timer(name))
        yield


@write_to_log_v2('some_function_v2')
def some_function_v2():
    print('This function_v2 take a bit of time to execute')
    for i in range(100000):
        for j in range(1000):
            continue
    print('Done')


some_function_v2()
