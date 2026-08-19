#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations
import argparse, sys, unittest
from pathlib import Path
sys.dont_write_bytecode = True
EXPECTED = 101

def flatten(suite):
    out=[]
    for item in suite:
        if isinstance(item, unittest.TestSuite): out.extend(flatten(item))
        else: out.append(item)
    return out

class ProgressResult(unittest.TextTestResult):
    def __init__(self,*a,total=0,**kw): super().__init__(*a,**kw); self.total=total; self.index=0
    def startTest(self,test):
        self.index+=1; print(f"TEST {self.index}/{self.total} {test.id()}",flush=True); super().startTest(test)

class ProgressRunner(unittest.TextTestRunner):
    resultclass=ProgressResult
    def __init__(self,*a,total=0,**kw): super().__init__(*a,**kw); self.total=total
    def _makeResult(self): return self.resultclass(self.stream,self.descriptions,self.verbosity,total=self.total)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.')
    ns=ap.parse_args(); root=Path(ns.root).resolve(); tests=root/'tests'; package=root/'schedulae'
    if not package.is_dir() or not tests.is_dir():
        print('B01_TEST_RUN=FAIL'); print('ERR=missing_schedulae_or_tests'); print('FINAL_PHASE=B01_TEST_SETUP_FAIL'); return 2
    sys.path.insert(0,str(root))
    suite=unittest.defaultTestLoader.discover(str(tests),pattern='test_*.py')
    flat=flatten(suite); total=len(flat)
    print(f'TOTAL_TESTS={total}'); print(f'EXPECTED_TESTS={EXPECTED}')
    if total!=EXPECTED:
        print('B01_TEST_RUN=FAIL'); print(f'ERR=unexpected_test_count:{total}'); print('FINAL_PHASE=B01_TEST_COUNT_FAIL'); return 3
    result=ProgressRunner(stream=sys.stdout,verbosity=0,total=total).run(unittest.TestSuite(flat))
    passed=total-len(result.failures)-len(result.errors)-len(result.skipped)
    print(f'B01_TEST_TOTAL={total}')
    print(f'B01_TEST_RESULT={passed}/{total}_PASS' if result.wasSuccessful() and not result.skipped else f'B01_TEST_RESULT={passed}/{total}_NOT_FULL_PASS')
    print(f'SKIPS={len(result.skipped)}')
    if result.wasSuccessful() and not result.skipped and passed==EXPECTED:
        print('EXIT=0'); print('ERR=NONE'); print('FINAL_PHASE=B01_HEADLESS_TESTS_PASS'); return 0
    print('EXIT=1'); print(f'ERR=failures:{len(result.failures)} errors:{len(result.errors)} skips:{len(result.skipped)}'); print('FINAL_PHASE=B01_HEADLESS_TESTS_FAIL'); return 1
if __name__=='__main__': raise SystemExit(main())
