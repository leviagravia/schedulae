#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations
import ast, hashlib, re, sys, unittest
from pathlib import Path
sys.dont_write_bytecode=True
EXPECTED_TESTS=101
DOCS={
 '01_SCHEDULAE_PRODUCT_AND_GOVERNANCE.md',
 '02_SCHEDULAE_TECHNICAL_AUTHORITY_AND_ROADMAP.md',
 '03_SCHEDULAE_MEMORIA_OPERATIVA.md',
}
DOMAIN={
 'bibliography.py','bibliography_search.py','bibtex.py','bibtex_controller.py',
 'bibtex_import_session.py','citations.py','reference_controller.py','reference_store.py',
 'references.py','related_references.py','research_file.py',
}

def fail(code,err,phase):
    print('B01_SOURCE_VERIFY=FAIL'); print(f'EXIT={code}'); print(f'ERR={err}'); print(f'FINAL_PHASE={phase}'); return code

def flatten(s):
    out=[]
    for x in s:
        if isinstance(x,unittest.TestSuite): out.extend(flatten(x))
        else: out.append(x)
    return out

def main():
    root=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve(); pkg=root/'schedulae'; tests=root/'tests'
    if not pkg.is_dir() or not tests.is_dir(): return fail(2,'missing_package_or_tests','B01_SOURCE_VERIFY_FAIL')
    names={p.name for p in pkg.glob('*.py') if p.name!='__init__.py'}
    if names!=DOMAIN: return fail(3,f'domain_modules:{sorted(names)}','B01_NAMESPACE_VERIFY_FAIL')
    if list(root.rglob('calamus_*.py')): return fail(4,'calamus_runtime_filename','B01_NAMESPACE_VERIFY_FAIL')
    calamus_runtime=[]; xdg=[]; gtk=[]; third=set(); calamus_occ=[]
    stdlib=sys.stdlib_module_names
    for p in pkg.glob('*.py'):
        text=p.read_text(encoding='utf-8')
        if 'SPDX-License-Identifier: GPL-3.0-or-later' not in text: return fail(5,f'spdx:{p.name}','B01_LICENSE_VERIFY_FAIL')
        if re.search(r'(?m)^\s*(from|import)\s+calamus_',text): calamus_runtime.append(p.name)
        if re.search(r'default_references_path|XDG_DATA_HOME|\.local/share|calamus/research',text): xdg.append(p.name)
        for n,line in enumerate(text.splitlines(),1):
            if 'Calamus' in line: calamus_occ.append((p.name,n,line.strip()))
        tree=ast.parse(text)
        for node in ast.walk(tree):
            roots=[]
            if isinstance(node,ast.Import): roots=[a.name.split('.')[0] for a in node.names]
            elif isinstance(node,ast.ImportFrom) and node.module: roots=[node.module.split('.')[0]]
            for m in roots:
                if m in {'gi','gtk','PyQt5','PyQt6','PySide2','PySide6'}: gtk.append((p.name,m))
                if m not in stdlib and m not in {'schedulae','__future__'}: third.add(m)
    if calamus_runtime: return fail(6,f'calamus_import:{calamus_runtime}','B01_NAMESPACE_VERIFY_FAIL')
    if xdg: return fail(7,f'hidden_library_path:{xdg}','B01_PATH_VERIFY_FAIL')
    if gtk: return fail(8,f'gtk_import:{gtk}','B01_GTK_BOUNDARY_FAIL')
    if third: return fail(9,f'third_party:{sorted(third)}','B01_DEPENDENCY_VERIFY_FAIL')
    expected_occ=[('reference_store.py',12,'_HEADER = "# Calamus References v1"')]
    if calamus_occ!=expected_occ: return fail(10,f'calamus_occurrences:{calamus_occ}','B01_COMPATIBILITY_IDENTITY_FAIL')
    for p in tests.glob('*.py'):
        if 'SPDX-License-Identifier: GPL-3.0-or-later' not in p.read_text(encoding='utf-8'): return fail(11,f'test_spdx:{p.name}','B01_LICENSE_VERIFY_FAIL')
    docs={p.name for p in root.glob('*.md')}
    if docs!=DOCS: return fail(12,f'canonical_documents:{sorted(docs)}','B01_DOCUMENT_CAP_FAIL')
    bytecode=[str(p.relative_to(root)) for p in root.rglob('*') if p.name=='__pycache__' or p.suffix in {'.pyc','.pyo'}]
    if bytecode: return fail(13,f'bytecode:{bytecode[:5]}','B01_CLEANLINESS_FAIL')
    sys.path.insert(0,str(root)); suite=unittest.defaultTestLoader.discover(str(tests),pattern='test_*.py'); total=len(flatten(suite))
    if total!=EXPECTED_TESTS: return fail(14,f'test_count:{total}','B01_TEST_COUNT_FAIL')
    if not (root/'LICENSE').is_file(): return fail(15,'license_missing','B01_LICENSE_VERIFY_FAIL')
    identity=(root/'PROJECT_IDENTITY.toml').read_text(encoding='utf-8')
    if 'python_namespace = "schedulae"' not in identity or 'license = "GPL-3.0-or-later"' not in identity:
        return fail(16,'project_identity','B01_IDENTITY_VERIFY_FAIL')
    print('B01_SOURCE_VERIFY=PASS'); print('DOMAIN_MODULES=11'); print('PYTHON_NAMESPACE=schedulae'); print('CALAMUS_RUNTIME_IMPORTS=0')
    print('INTENTIONAL_CALAMUS_RUNTIME_STRINGS=1'); print('COMPATIBILITY_HEADER=# Calamus References v1')
    print('GTK_IMPORTS=0'); print('THIRD_PARTY_PYTHON_DEPS=0'); print('HIDDEN_XDG_LIBRARY_PATH=NO')
    print('CANONICAL_DOCUMENTS=3'); print(f'EXPECTED_TESTS={EXPECTED_TESTS}'); print('BYTECODE_ARTIFACTS=0')
    print('EXIT=0'); print('ERR=NONE'); print('FINAL_PHASE=B01_SOURCE_VERIFY_PASS'); return 0
if __name__=='__main__': raise SystemExit(main())
