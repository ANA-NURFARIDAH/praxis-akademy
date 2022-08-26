# exc must be exception instance or None.
raise RuntimeError from exc

def func():
    raiseConnectionError

try:
    func()
except ConnectionError as exc:
        raise RuntimeError('Failed to open database') from exc

Traceback (most recent call last):
    File "<stdin>", line 2, in <module>
    File "<stdin>", line 2, in func

try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None