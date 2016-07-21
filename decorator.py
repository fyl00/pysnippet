# coding=utf8

""" Some convenience decorators """

import time
import logging
from random import randint
from functools import wraps


def retry(ExceptionToCheck, tries=3, delay=3, backoff=1):
    """Retry calling the decorated function using an exponential backoff.

    original from: http://www.saltycrane.com/blog/2009/11/trying-out-retry-decorator-python/

    :param ExceptionToCheck: the exception to check. may be a tuple of
        exceptions to check
    :type ExceptionToCheck: Exception or tuple
    :param tries: number of times to try (not retry) before giving up
    :type tries: int
    :param delay: initial delay between retries in seconds
    :type delay: int
    :param backoff: backoff multiplier e.g. value of 2 will double the delay
        each retry
    :type backoff: int
    """
    def deco_retry(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except ExceptionToCheck, e:
                    msg = "Retry **%s** in %d seconds. (ERROR: %s) " \
                          % (f.__name__, mdelay, str(e))
                    logging.warning(msg)

                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return f(*args, **kwargs)

        return f_retry  # true decorator

    return deco_retry


@retry(NameError)
def test():
    x = randint(1, 10)
    if x < 8:
        raise NameError('Ops... Error happened')
    else:
        print 'Function test() was called successfully'

if __name__ == "__main__":
    test()