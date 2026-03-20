RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RESET='\033[0m'

def good(msg):
    return f"{GREEN}{msg}{RESET}"

def bad(msg):
    return f"{RED}{msg}{RESET}"

def info(msg):
    return f"{BLUE}{msg}{RESET}"

def testEqual(msg, x, y, results):
    (nfails, ntests) = results
    if(x == y):
        print(f"  {msg} ... {good('PASS')}")
        return (nfails, ntests + 1)
    else:
        print(f"  {msg} ... {bad('FAIL')}")
        print(f"    expected: {y!r}")
        print(f"    got:      {x!r}")
        return (nfails + 1, ntests + 1)

def testTrue(msg, x, results):
    return testEqual(msg, x, True, results)

def testInRange(msg, val, lo, hi, results):
    (nfails, ntests) = results
    if lo <= val <= hi:
        print(f"  {msg} ... {good('PASS')}")
        return (nfails, ntests + 1)
    else:
        print(f"  {msg} ... {bad('FAIL')}")
        print(f"    expected: {lo!r} <= x <= {hi!r}")
        print(f"    got:      {val!r}")
        return (nfails + 1, ntests + 1)

def testLength(msg, xs, n, results):
    (nfails, ntests) = results
    if len(xs) == n:
        print(f"  {msg} ... {good('PASS')}")
        return (nfails, ntests + 1)
    else:
        print(f"  {msg} ... {bad('FAIL')}")
        print(f"    expected length: {n}")
        print(f"    got length:      {len(xs)}")
        return (nfails + 1, ntests + 1)

def testContains(msg, xs, val, results):
    (nfails, ntests) = results
    if val in xs:
        print(f"  {msg} ... {good('PASS')}")
        return (nfails, ntests + 1)
    else:
        print(f"  {msg} ... {bad('FAIL')}")
        print(f"    expected {val!r} in {xs!r}")
        return (nfails + 1, ntests + 1)

def testSubset(msg, xs, ys, results):
    (nfails, ntests) = results
    if all(x in ys for x in xs):
        print(f"  {msg} ... {good('PASS')}")
        return (nfails, ntests + 1)
    else:
        missing = [x for x in xs if x not in ys]
        print(f"  {msg} ... {bad('FAIL')}")
        print(f"    not in superset: {missing!r}")
        return (nfails + 1, ntests + 1)

def testSameElements(msg, xs, ys, results):
    (nfails, ntests) = results
    if sorted(xs) == sorted(ys):
        print(f"  {msg} ... {good('PASS')}")
        return (nfails, ntests + 1)
    else:
        print(f"  {msg} ... {bad('FAIL')}")
        print(f"    expected sorted: {sorted(ys)!r}")
        print(f"    got sorted:      {sorted(xs)!r}")
        return (nfails + 1, ntests + 1)

def testNoDuplicates(msg, xs, results):
    (nfails, ntests) = results
    if len(xs) == len(set(xs)):
        print(f"  {msg} ... {good('PASS')}")
        return (nfails, ntests + 1)
    else:
        from collections import Counter
        dupes = {k: v for k, v in Counter(xs).items() if v > 1}
        print(f"  {msg} ... {bad('FAIL')}")
        print(f"    duplicates: {dupes!r}")
        return (nfails + 1, ntests + 1)

def printMsg(msg, x):
    print(info(msg))
    return x

def printResult(x):
    if(x[0] == 0):
        print(good(f"All {x[1]!s} tests pass"))
    else:
        print(bad(f"{x[0]!s}/{x[1]!s} tests failed"))
    return x
