# type: ignore
# pylint: skip-file

from predicate_dispatch import predicate
from multipledispatch import dispatch

import pytest


# multipledispatch

@dispatch(int)
def isint(x):
    return True


@dispatch(object)
def isint(x):
    return False


@dispatch(object, object)
def isint(x, y):
    return False


@pytest.mark.parametrize("val", [1, 'a'])
def test_benchmark_multipledispatch_call_single_dispatch(benchmark, val):
    benchmark(isint, val)

def test_benchmark_add_and_use_instance(benchmark):
    namespace = {}

    @benchmark
    def inner():
        @dispatch(int, int, namespace=namespace)
        def mul(x, y):
            return x * y

        @dispatch(str, int, namespace=namespace)
        def mul(x, y):
            return x * y

        mul(4, 5)
        mul('x', 5)

# /multipledispatch


# predicate_dispatch

@predicate(lambda x: x is int)
def isint2(x):
    return True

@predicate(lambda x: x is object)
def isint2(x):
    return False

@predicate()
def isint2(x):
    return False

@pytest.mark.parametrize("val", [1, 'a'])
def test_benchmark_call_single_dispatch2(benchmark, val):
    benchmark(isint2, val)


# @pytest.mark.parametrize("val", [(1, 4)])
# def test_benchmark_call_multiple_dispatch2(benchmark, val):
#     benchmark(isint, *val)


# def test_benchmark_add_and_use_instance2(benchmark):
#     namespace = {}

#     @benchmark
#     def inner():
#         @predicate_cache(lambda x, y: (x is int) and (y is int))
#         def mul(x, y):
#             return x * y

#         @predicate_cache(lambda x, y: (x is str) and (y is int))
#         def mul(x, y):
#             return x * y

#         @predicate_cache()
#         def mul(x, y):
#             return x * y

#         # @predicate_cache(lambda x, y, z: (x is int) and (y is int) and (z is list))
#         # def mul(x, y, *args):
#         #     return x * y

#         # @predicate_cache(lambda x: x is list)
#         # def mul(*args):
#         #     return sum(args)

#         mul(4, 5)
#         mul('x', 5)
#         # mul(1, 2, 3., 4., 5.)
#         # mul(1, 2, 3, 4, 5)

# # /predicate_dispatch
