#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,subprocess,sys,tomllib
from pathlib import Path
sys.dont_write_bytecode=True
DOCS=(
 '01_SCHEDULAE_PRODUCT_AND_GOVERNANCE.md',
 '02_SCHEDULAE_TECHNICAL_AUTHORITY_AND_ROADMAP.md',
 '03_SCHEDULAE_MEMORIA_OPERATIVA.md',
)
def dig(p:Path)->str:
 h=hashlib.sha256();
 with p.open('rb') as f:
  for c in iter(lambda:f.read(1<<20),b''): h.update(c)
 return h.hexdigest()
def fail(err:str)->int:
 print('B00_REPO_VERIFY=FAIL'); print('EXIT=1'); print(f'ERR={err}'); print('FINAL_PHASE=B00_REPO_VERIFY_FAIL'); return 1
def main()->int:
 ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ns=ap.parse_args(); root=Path(ns.root).expanduser().resolve()
 if not root.is_dir(): return fail('missing_root')
 prov=root/'provenance/CALAMUS_B00_PROVENANCE.tsv'
 if not prov.is_file(): return fail('missing_provenance')
 with prov.open(newline='',encoding='utf-8') as f: rows=list(csv.DictReader(f,delimiter='\t'))
 core=[r for r in rows if r['kind']=='core']; tests=[r for r in rows if r['kind']=='test']
 if len(core)!=11: return fail(f'core_count:{len(core)}')
 for r in rows:
  rel=Path(r['path']); p=(root/'core'/rel.name) if r['kind']=='core' else (root/'tests'/rel.name)
  if not p.is_file() or dig(p)!=r['sha256']: return fail(f'source_identity:{p.name}')
 core_names=sorted(p.name for p in (root/'core').glob('*.py'))
 exp_core=sorted(Path(r['path']).name for r in core)
 if core_names!=exp_core: return fail(f'core_file_set:{core_names}')
 test_names=sorted(p.name for p in (root/'tests').glob('test_*.py'))
 exp_tests=sorted(Path(r['path']).name for r in tests)
 if test_names!=exp_tests: return fail(f'test_file_set:{test_names}')
 if dig(root/'tests/__init__.py')!='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855': return fail('test_init_identity')
 pycache=list(root.rglob('__pycache__')); pyc=list(root.rglob('*.pyc'))
 if pycache or pyc: return fail(f'bytecode_artifacts:pycache={len(pycache)} pyc={len(pyc)}')
 md=sorted(p.name for p in root.rglob('*.md'))
 if md!=sorted(DOCS): return fail(f'document_cap:{md}')
 doc_table=root/'provenance/CANONICAL_DOCS_SHA256.tsv'
 with doc_table.open(newline='',encoding='utf-8') as f: drows=list(csv.DictReader(f,delimiter='\t'))
 for r in drows:
  p=root/r['path']
  if not p.is_file() or dig(p)!=r['sha256'] or p.stat().st_size!=int(r['bytes']): return fail(f'doc_identity:{r["path"]}')
 with (root/'PROJECT_IDENTITY.toml').open('rb') as f: ident=tomllib.load(f)
 expected={'product_name':'Schedulae','repo_slug':'schedulae','future_python_namespace':'schedulae','future_xdg_namespace':'schedulae','b00_core_modules':11,'b00_inherited_tests':74,'b00_source_module_rename':False,'b00_gtk':False,'b00_git_init_authorized':True,'b00_git_commit_authorized':False}
 for k,v in expected.items():
  if ident.get(k)!=v: return fail(f'identity:{k}:{ident.get(k)!r}')
 git=root/'.git'
 if git.is_dir():
  branch=subprocess.run(['git','-C',str(root),'branch','--show-current'],capture_output=True,text=True,check=True).stdout.strip()
  if branch!='main': return fail(f'git_branch:{branch}')
  head=subprocess.run(['git','-C',str(root),'rev-parse','--verify','HEAD'],capture_output=True,text=True)
  if head.returncode==0: return fail('unexpected_git_commit')
  remotes=subprocess.run(['git','-C',str(root),'remote'],capture_output=True,text=True,check=True).stdout.strip()
  if remotes: return fail(f'unexpected_git_remote:{remotes}')
 print('B00_REPO_VERIFY=PASS'); print('CORE_MODULES=11'); print('TEST_MODULES=11'); print('CANONICAL_DOCUMENTS=3'); print('BYTECODE_ARTIFACTS=0')
 print(f'GIT_INITIALIZED={"YES" if git.is_dir() else "NO"}'); print('GIT_COMMIT=NONE'); print('GIT_REMOTE=NONE'); print('EXIT=0'); print('ERR=NONE'); print('FINAL_PHASE=B00_REPO_VERIFY_PASS'); return 0
if __name__=='__main__': raise SystemExit(main())
