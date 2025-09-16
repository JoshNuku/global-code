"""Run the unittest suite for this project and exit with appropriate code."""

import sys
import unittest


def run():
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='.', pattern='test_*.py')
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    sys.exit(run())
