"""
Coroutines
    - Init coroutine
    - Execute the first execution
    - Consume and process the message


# coroutines example 001
def is_contain_number():
    print('Prepare for number checking')
    while True:
        msg = yield
        if bool(re.search(r'\d', msg)):
            print('Correct format: %s' % msg)


# Init coroutine
coroutine_001 = is_contain_number()

# Call Preparation step in order to execute the next yield
next(coroutine_001)

# Start operation here, check these messages contain number
coroutine_001.send('worasit.dmk501@hotmail.com')
coroutine_001.send('This message does not contain any numbers')

coroutine_001.close()

"""

# Basic example
import functools
import re


def generator():
    value = yield 'spam'
    print('Generator received: %s' % value)
    yield 'Previous value: %r' % value


g = generator()
print('Result from generator: %s' % next(g))
print(g.send('eggs'))


# Priming
def coroutine(function):
    @functools.wraps(function)
    def _coroutine(*args, **kwargs):
        active_coroutine = function(*args, **kwargs)
        next(active_coroutine)
        return active_coroutine

    return _coroutine


@coroutine
def spam():
    while True:
        print('Waiting for yield...')
        value = yield
        print('spam received: %s' % value)


# coroutines example 001
def is_contain_number():
    print('Prepare for number checking')
    while True:
        msg = yield
        if bool(re.search(r'\d', msg)):
            print('Correct format: %s' % msg)


# Init coroutine
coroutine_001 = is_contain_number()

# Call Preparation step in order to execute the next yield
next(coroutine_001)

# Start operation here, check these messages contain number
coroutine_001.send('worasit.dmk501@hotmail.com')
coroutine_001.send('This message does not contain any numbers')

coroutine_001.close()
