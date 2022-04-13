# from package.subpackage.submodule import ok
from ..subpackage.submodule import ok


def run():
    print("hey it works")
    return ok()
