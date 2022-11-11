# type: ignore
# pylint: skip-file

from predicate_dispatch import predicate, predicate_cache, predicate_cache_result
from multipledispatch import dispatch as multipledispatch
from plum import dispatch as plum_dispatch

import pytest


# multipledispatch


@multipledispatch(int)
def isint(x):
    return True


@multipledispatch(object)
def isint(x):
    return False


@pytest.mark.parametrize("val", [1, "a"])
def test_benchmark_multipledispatch_call_single_dispatch(benchmark, val):
    benchmark(isint, val)


# predicate_dispatch


@predicate(lambda x: isinstance(x, int))
def isint2(x):
    return True


@predicate()
def isint2(x):
    return False


@pytest.mark.parametrize("val", [1, "a"])
def test_benchmark_predicate_dispatch_call_single_dispatch(benchmark, val):
    benchmark(isint2, val)


@predicate_cache(lambda x: isinstance(x, int))
def isint3(x):
    return True


@predicate_cache()
def isint3(x):
    return False


@pytest.mark.parametrize("val", [1, "a"])
def test_benchmark_predicate_cache_call_single_dispatch(benchmark, val):
    benchmark(isint3, val)


@predicate_cache_result(lambda x: isinstance(x, int))
def isint4(x):
    return True


@predicate_cache_result()
def isint4(x):
    return False


@pytest.mark.parametrize("val", [1, "a"])
def test_benchmark_predicate_cache_result_call_single_dispatch(benchmark, val):
    benchmark(isint4, val)


if __name__ == "__main__":
    pytest.main()

# plum


@plum_dispatch
def isint5(x: int):
    return True


@plum_dispatch
def isint5(x: object):
    return False


@pytest.mark.parametrize("val", [1, "a"])
def test_benchmark_plum_dispatch_call_single_dispatch(benchmark, val):
    benchmark(isint5, val)
