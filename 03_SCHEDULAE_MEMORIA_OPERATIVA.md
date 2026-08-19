# Schedulae — Memoria Operativa incrementale (MO)

**Documento canonico 3 di 3**  
**Versione MO:** 3.0  
**Data di apertura:** 19 agosto 2026  
**Stato:** ACTIVE / INCREMENTAL  
**Regola:** questa è l'unica Memoria Operativa di Schedulae. Ogni nuovo evento significativo viene aggiunto qui; non si crea una seconda MO.

---

## A. Snapshot operativo corrente

**Project:** Schedulae  
**Phase:** B00 CLOSED / DOCUMENTATION FINALIZED — B01 IMPLEMENTATION R1 / T480 PENDING  
**B00 state:** CLOSED / T480 CERTIFIED / PUBLISHED / DOCUMENTATION FINALIZED  
**Repository Schedulae:** `/home/luciano/Projects/schedulae-work`  
**Git mutation Schedulae:** P1 product commit `4d71e7f0e868d8229b0e05dd2682acc4d887f535` + P2 documentation commit `daf6da276b44a490793526d278098fba261c5afe` published; worktree CLEAN  
**Candidate attempts:** 0 — B00 è headless/non-candidate  
**GTK:** NOT OPENED  
**Next allowed technical boundary:** isolated T480 qualification of B01 Implementation R1; no Git publication yet.

### Exact source authority

- Calamus W118 product commit: `54456a147f4d65996c73f8a13326fed0e4cc31b7`
- Calamus governance commit: `c316a3aec8c7fba63969a9fa47726809f2d3f43c`
- Calamus governance tree: `2b700469f68c626247558d7b5c56eff1c92f8d8c`
- B00 core: **11 modules / 3,259 physical LOC**
- dependency edges: **17**
- max fan-out: **4**
- inherited tests: **74**
- isolated extraction: **74/74 PASS**
- GTK imports: **0**
- third-party Python deps: **0**
- runtime Calamus repo dependency: **none**
- canonical format header: `# Calamus References v1`

### Handover authority

`CALAMUS_BIBLIOGRAPHY_B00_BOOTSTRAP_ONE_UPLOAD_HANDOVER_20260819.zip`

- SHA-256: `f69cfcd47c30b3c228b1e67e82f80d4cd96582dc4e20224d4e32420ebd556318`
- size: `7,374,773` bytes
- internal manifest: 87 files
- manifest SHA-256: `d20397be6ab7534df7c388d1f22130f95ca84a31970d77f67ec6381f409aab3f`

### Verification run — 2026-08-19

```text
B00_HANDOVER_STATIC=PASS
CORE_MODULES=11
CORE_PHYSICAL_LOC=3259
EXPECTED_TESTS=74
MATURE_SOURCE_RAW=2_ARCHIVES_PASS
B00_HANDOVER_VERIFY=PASS
EXIT=0
ERR=NONE
FINAL_PHASE=B00_ONE_UPLOAD_HANDOVER_VERIFY_PASS
```

---

## B. Tre documenti canonici — limite permanente

Schedulae mantiene **esattamente tre documenti canonici**:

1. `01_SCHEDULAE_PRODUCT_AND_GOVERNANCE.md`
   - identità;
   - definizione pubblica;
   - scopo;
   - posizionamento;
   - anti-bloat;
   - compatibilità;
   - governance.

2. `02_SCHEDULAE_TECHNICAL_AUTHORITY_AND_ROADMAP.md`
   - source/provenance;
   - architettura;
   - moduli;
   - test;
   - safety contracts;
   - validation/failure policy;
   - Git;
   - licensing;
   - roadmap B00–B04.

3. `03_SCHEDULAE_MEMORIA_OPERATIVA.md`
   - stato corrente;
   - cronologia;
   - decision register;
   - FAIL/PASS;
   - commit/tree futuri;
   - next action;
   - debito aperto.

**Nessun quarto documento canonico sarà creato.**  
Nuove informazioni vanno integrate in uno di questi tre.

---

## C. Decision register

### D-001 — Spin-off method
**Data:** 2026-08-18  
**Decisione:** ADOPT. Schedulae nasce dal domain core separabile di Calamus, non da una copia del `App` con rimozione di menu.  
**Ragione:** core bibliografico già indipendente, GTK-free e testabile in isolamento.  
**Vincolo:** no runtime import Calamus; no shared cross-project core prematuro.

### D-002 — Bibliography/BibTeX come primo spin-off ingegneristico
**Data:** 2026-08-19  
**Decisione:** ADOPT. Il Bibliography/BibTeX Workbench è il primo progetto su cui provare l'intero metodo di spin-off.  
**Evidenza:** 11 modules / 3,259 LOC / 74 tests, contro boundary alternativi più complessi.  
**Ragione:** una sola authority persistente, due controller esistenti, minor fan-out e bootstrap più pulito.

### D-003 — Product name
**Data:** 2026-08-19  
**Decisione:** nome prodotto **Schedulae**.  
**Audit:** nessuna collisione esatta software/app/package rilevante nelle superfici verificate; near-name **Schedula** presente.  
**Constraint:** descrizione pubblica sempre bibliografica; mai scheduling semantics; rifare collision check prima della pubblicazione.

### D-004 — Product scope
**Data:** 2026-08-19  
**Decisione:** lightweight local-first Bibliography/BibTeX workbench.  
**Reject:** Zotero clone, cloud, AI, database authority, PDF manager, browser extension, plugin platform, background indexing, full-text editor.

### D-005 — File authority
**Data:** inherited/frozen 2026-08-19  
**Decisione:** `references.md` resta canonical bibliography authority.  
**Formato:** `# Calamus References v1` preservato in B00 e usato come interoperability contract in B01+.  
**Constraint:** branding prodotto e format identity sono separati.

### D-006 — B00 no-rename
**Data:** 2026-08-19  
**Decisione:** in B00 gli 11 moduli e i 74 test restano byte-identici e `calamus_*`.  
**Reason:** prima si congela equivalenza; namespace migration appartiene a B01.

### D-007 — B00 no-GTK
**Data:** 2026-08-19  
**Decisione:** B00 è headless.  
**Constraint:** nessuna GUI, nessun Candidate desktop, nessun attempt consumato.

### D-008 — Failure policy
**Data:** inherited/frozen  
**Decisione:** dopo ogni FAIL: stop -> classify -> mature-source audit -> ownership/lifecycle/identity comparison -> repair constraint -> minimal repair -> focused rerun -> broad regression.  
**Reject:** trial-and-error patching.

### D-009 — Git authority
**Data:** 2026-08-19  
**Decisione:** bootstrap repo richiede autorizzazione esplicita; commit/push restano user-controlled salvo autorizzazione separata.  
**Constraint:** non mutare Calamus canonical repo.

### D-010 — Document cap
**Data:** 2026-08-19  
**Decisione:** massimo tre documenti canonici; questo limite è permanente.  
**Conseguenza:** nessun README/contract/roadmap/MO aggiuntivo come nuova authority; integrare i tre esistenti.

---

## D. Chronology

### 2026-08-18 — Spin-off feasibility audit

Direct source inspection del Calamus governance source.

Finding Bibliography/BibTeX:

- exact runtime closure: 11 modules;
- 3,259 physical LOC;
- no GTK;
- no external Python dependency;
- portable inherited tests: 74/74 PASS;
- typed references + identity/aliases;
- canonical Markdown store;
- stale/conflict detection;
- atomic UTF-8 persistence;
- BibTeX/BibLaTeX parser/import/export;
- bibliography projections/search/detail;
- CRUD controller.

Decisione: **ADOPT**.

### 2026-08-19 — Comparative extraction probe

B00 Bibliography/BibTeX:

- 11 modules;
- 3,259 LOC;
- 74 tests;
- 74/74 PASS;
- 17 edges;
- max fan-out 4;
- 1 persistent Markdown authority;
- 2 domain controllers.

Conclusione: best first engineering bootstrap.

### 2026-08-19 — Name study

Dopo confronto fra nomi latini, **Schedulae** è emerso come nome preferito e sottoposto ad audit dedicato.

Risultato operativo:

- no exact software/app/package collision rilevante nelle superfici controllate;
- near-name `Schedula` materialmente presente;
- prodotto da descrivere sempre come bibliography/citation manager;
- non presentare come calendar/scheduler;
- nessuna pretesa di legal trademark clearance.

### 2026-08-19 — One-upload B00 handover

Creato handover autosufficiente:

`CALAMUS_BIBLIOGRAPHY_B00_BOOTSTRAP_ONE_UPLOAD_HANDOVER_20260819.zip`

Authority:

- SHA-256 `f69cfcd47c30b3c228b1e67e82f80d4cd96582dc4e20224d4e32420ebd556318`
- 7,374,773 bytes
- 87 manifested files
- manifest SHA-256 `d20397be6ab7534df7c388d1f22130f95ca84a31970d77f67ec6381f409aab3f`

Il handover contiene:

- exact B00 seed;
- provenance;
- 74 inherited tests;
- B00 contracts;
- roadmap B00–B04;
- W97 evidence;
- Mousepad mature source;
- novelWriter mature source;
- bootstrap/verify/test tools.

### 2026-08-19 — Handover verification in current Schedulae session

Eseguito:

`python3 TOOLS/VERIFY_HANDOVER.py`

Result: **PASS**

Final marker:

`FINAL_PHASE=B00_ONE_UPLOAD_HANDOVER_VERIFY_PASS`

Nessun Git mutation.

### 2026-08-19 — Canonical documentation consolidation

Creati e congelati i soli tre documenti canonici:

1. Product & Governance;
2. Technical Authority & Roadmap;
3. Memoria Operativa incrementale.

Scopo: evitare proliferazione documentale e rendere il progetto trasferibile con tre authority soltanto.


### 2026-08-19 — Implementation audit started / B00 seed revalidation

Audit eseguito direttamente sul seed B00 e sulle fonti mature raw già incluse nel handover; nessuna implementazione e nessuna Git mutation.

Revalidation NON-CANDIDATE:

```text
TOTAL_TESTS=74
EXPECTED_TESTS=74
B00_TEST_TOTAL=74
B00_TEST_RESULT=74/74_PASS
SKIPS=0
EXIT=0
ERR=NONE
FINAL_PHASE=B00_EXACT_EXTRACTION_PASS
```

Findings preliminari:

- il core resta architetturalmente piccolo: 11 moduli, 17 dependency edges, max fan-out 4, GTK 0, dipendenze Python terze 0;
- `MarkdownReferenceStore(path=...)` possiede già il seam per una libreria esplicita: B01 non richiede un nuovo framework di storage;
- il bootstrap tool B00 esistente è diventato obsoleto rispetto alla governance Schedulae: copia tutti i `CONTRACTS/*` in `docs/contracts`, crea un ulteriore `README.md` e quindi violerebbe il limite permanente dei tre documenti canonici;
- lo stesso bootstrap copia ricorsivamente `CORE` e `tests`, quindi trascinerebbe anche gli attuali `__pycache__/*.pyc`: packaging cleanliness defect, non product defect;
- `calamus_bibliography.py` contiene ancora semantica standalone-inappropriata proveniente da Calamus (`cited`, `source-notes`, `unused`, Current Document, Source Notes, Reference Sets). In Schedulae, se mantenuta invariata, produrrebbe informazioni fuorvianti perché tali authority non esistono;
- il diagnostic per header errato contiene un difetto ereditato verificato: restituisce letteralmente `Expected library header: {_HEADER}.` invece del valore dell'header;
- la policy per symlink della libreria canonica e la robustezza della write race fra stale-token check e atomic replace richiedono probe B01 specifici prima di qualunque modifica.

Classificazione:

```text
CORE_REGRESSION=NO
B00_SEED_TESTS=74/74_PASS
BOOTSTRAP_TOOL_GOVERNANCE_DEFECT=YES
BOOTSTRAP_TOOL_PYC_CLEANLINESS_DEFECT=YES
STANDALONE_SEMANTIC_ADAPTATION_REQUIRED=B01
CANONICAL_LIBRARY_FILE_SAFETY=PROBE_REQUIRED_B01
GIT_MUTATION=NONE
CANDIDATE=NO
```

Decisione preliminare: **non eseguire `BOOTSTRAP_B00_REPO.py` invariato**. Prima del bootstrap reale va adattato il tooling senza toccare i 11 moduli e i 74 test B00.
---

## E. B00 contract — current frozen state

### MUST

- source identity verificata;
- nome Schedulae;
- repository indipendente dopo authorization;
- copy byte-identico degli 11 moduli;
- copy byte-identico dei 74 test;
- provenance hashes;
- exactly 74 discovered tests;
- 74/74 PASS;
- References v1 compatibility;
- anti-bloat budget;
- no GTK;
- no behavior change.

### MUST NOT

- rename `calamus_*` in B00;
- cambiare References v1 header;
- cambiare di nascosto XDG semantics legacy;
- aggiungere GUI;
- aggiungere rete/cloud/AI/database/PDF manager/plugins;
- creare shared core;
- copiare Calamus `App`;
- creare remote/push senza autorizzazione;
- aprire B01 prima della closure B00.

### B00 closure marker target

`B00_EXACT_EXTRACTION_CONTRACT=PASS`

---

## F. B01 debt register

B01 deve possedere esplicitamente:

- independent library identity;
- arbitrary library paths;
- Schedulae XDG namespace;
- nessuna ownership implicita di `~/.local/share/calamus/research/references.md`;
- `calamus_*` -> Schedulae namespace migration con behavior equivalence;
- diagnostics/docstrings branding migration;
- stale/external modification hostile tests;
- References v1 read/write interoperability.

Questo debt è intenzionale. Non correggerlo in B00.

---

## G. B02–B04 intent register

### B02
Minimal native GTK shell + reference workflow.

### B03
BibTeX/BibLaTeX preview/import/export UI/lifecycle.

### B04
Trust/performance/desktop certification, large/malformed/stale/lifecycle/True GTK, poi packaging.

Nessun dettaglio ulteriore è autorizzato a trasformarsi in scope creep senza passare dall'anti-bloat gate.

---

## H. Validation state

### Proven before independent repo

```text
B00_EXTRACTION_PROBE=PASS
AUTOMATED_TESTS=74/74_PASS
MANUAL_TESTS=0
CANDIDATE=NO
GIT_MUTATION=NONE
EXIT=0
ERR=NONE
FINAL_PHASE=B00_EXTRACTION_PROBE_PASS
```

### Required after independent bootstrap

Prima dell'esecuzione:

`TOTAL TESTS = 74`

Required final:

```text
B00_TEST_TOTAL=74
B00_TEST_RESULT=74/74_PASS
SKIPS=0
EXIT=0
ERR=NONE
FINAL_PHASE=B00_EXACT_EXTRACTION_PASS
```

---

## I. Open issues / blockers

### O-001 — B00 bootstrap authorization
**State:** OPEN  
Creazione di `/home/luciano/Projects/schedulae-work`, copy seed e `git init` non sono ancora implicati dalla sola richiesta documentale. Serve autorizzazione esplicita.

### O-002 — License
**State:** CLOSED / FROZEN 2026-08-19  
Licenza Schedulae: **GNU General Public License v3.0 or later**, SPDX **`GPL-3.0-or-later`**. Root `LICENSE` obbligatorio prima della prima pubblicazione del codice. Header SPDX/copyright per-file differiti a B01 per preservare l'identità byte-for-byte certificata B00.

### O-003 — Desktop app ID
**State:** OPEN / DEFER TO PACKAGING IDENTITY  
Non inventare un app ID prima di freeze dell'autorità di distribuzione.

### O-004 — Final namespace recheck
**State:** OPEN / BEFORE PUBLICATION  
Rifare exact-name/repo/PyPI/Flathub/package collision audit immediatamente prima della pubblicazione.

---

## J. Source retrieval rule

Per B00 il handover è sufficiente: non chiedere altro source.

Se B02/B03 richiedono componenti GTK Calamus non inclusi nel seed, l'autorità locale conosciuta è:

`/home/luciano/Projects/calamus-work`

Branch canonico: `main`.

Prima di usare source esterno al handover, verificare commit/tree pertinente e non sostituire source audit con web summaries.

---

## K. Operational rules carried forward

- Fail-visible runner con `EXIT/ERR/FINAL_PHASE`.
- Dichiarare sempre il test count prima di una validation user-executed.
- Post-FAIL: source maturo prima della riparazione.
- Web consentito per informazioni correnti di namespace; non come sostituto dell'audit source.
- User controls commit/push salvo esplicita autorizzazione.
- Candidate desktop future richiedono autorizzazione esplicita.
- Consegnare comando terminale insieme a ogni Candidate desktop futuro.
- No hidden background work.
- No extra canonical project documents.

---

## L. Next action

**NEXT_ACTION = RUN_B01_IMPLEMENTATION_R1_ON_T480**

Una volta autorizzato:

1. bootstrap esatto di `/home/luciano/Projects/schedulae-work`;
2. nessun rename;
3. provenance verify;
4. dichiarare `TOTAL TESTS = 74`;
5. eseguire exactly 74;
6. richiedere 74/74 PASS;
7. preparare closure/commit-ready evidence;
8. nessun push implicito;
9. solo dopo B00 closure aprire B01.

---

## M. Protocollo incrementale della MO

Ad ogni avanzamento futuro:

1. aggiornare **Snapshot operativo corrente**;
2. aggiungere una voce a **Chronology**;
3. aggiungere/modificare una voce nel **Decision register** solo se è cambiata una decisione;
4. registrare ogni FAIL con:
   - exact boundary;
   - classification;
   - mature source consulted;
   - repair constraint;
   - focused rerun;
   - final status;
5. registrare ogni PASS con exact test count e marker;
6. registrare commit/tree solo dopo evidenza reale;
7. aggiornare **Open issues / blockers**;
8. aggiornare **Next action**;
9. incrementare `Versione MO`;
10. non cancellare la storia utile: correggere con una nuova voce che sostituisce esplicitamente l'autorità precedente.

### Template per nuova voce

```text
### YYYY-MM-DD — <evento>

Boundary:
Authority:
Action:
Tests:
Result:
Classification (se FAIL):
Mature-source audit (se FAIL):
Repair constraint (se applicabile):
Git mutation:
Commit/tree (se pubblicato):
Decision:
Next action:
```

Questa MO deve restare sufficiente, insieme ai documenti 1 e 2, per riprendere Schedulae in una nuova sessione senza ricostruire il progetto da conversazioni precedenti.

---

## N. Audit di implementazione — stato iniziale

### N.1 Metodo

Ordine vincolante usato:

1. exact Schedulae/Calamus seed source first;
2. identificazione dei seam e dei rischi reali;
3. confronto con mature source raw già disponibile;
4. richiesta di ulteriore mature source solo dove serve a una domanda concreta;
5. nessuna patch durante l'audit.

### N.2 B00 — verdict iniziale

**ADOPT il core, REPAIR il bootstrap tooling.**

Il seed applicativo non richiede un redesign. I 74 test sono nuovamente PASS. Prima della creazione del repository indipendente, tuttavia, `BOOTSTRAP_B00_REPO.py` deve essere adattato perché:

1. non copi `__pycache__` o `.pyc`;
2. non ricrei una foresta di `docs/contracts`;
3. installi nel repository soltanto i tre documenti canonici Schedulae;
4. preservi byte-identici gli 11 `.py` core e i test source;
5. mantenga provenance come dati/evidence senza trasformarli in nuove authority documentali;
6. non inizializzi Git senza autorizzazione esplicita.

Questo repair è tooling-only e non deve consumare un candidate attempt.

### N.3 B01 — seam reale individuato

Il seam più importante è già presente:

```python
MarkdownReferenceStore(path=...)
```

Quindi Schedulae **non ha bisogno di inventare un nuovo storage framework**. Il piano più piccolo è:

- rendere il path della libreria una scelta/identità esplicita dell'applicazione;
- non usare il legacy default Calamus come ownership implicita;
- usare XDG soltanto per preferenze minime/app state, non come autorità bibliografica;
- mantenere `references.md` come authority della libreria;
- rendere l'iniezione dei path direttamente testabile.

Il mature source novelWriter incluso nel handover conferma una disciplina utile: config/data roots separati tramite standard toolkit e override espliciti dei path destinati anche alla test suite. La soluzione Schedulae deve adottare il principio, non la dipendenza Qt.

### N.4 B01 — de-Calamus semantic boundary

`calamus_bibliography.py` non è interamente standalone nonostante sia GTK-free.

Calamus-specific oggi:

- filter `use = cited`;
- filter `use = source-notes`;
- filter `use = unused`;
- `BibliographyContext.cited_keys`;
- `source_note_keys`;
- `set_names_by_key`;
- dettaglio `Current Document`;
- dettaglio `Source Notes`;
- dettaglio `Reference Sets`;
- delete impact su current document / source notes / reference sets;
- advisory `unused` calcolato da authority che Schedulae standalone non possiede.

Decisione preliminare per Schedulae Core:

**ADOPT**
- query;
- Type;
- Tag;
- File;
- bibliographic Integrity realmente derivabile dalla libreria;
- sort;
- related references;
- duplicate identifier checks;
- local file status.

**ADAPT**
- delete impact: solo authority realmente possedute/conosciute da Schedulae;
- detail: solo dati bibliografici e integrità reale;
- citation utilities: conservarle come low-cost command utility, non come scansione automatica di documenti.

**REJECT dal Core standalone**
- Current Document semantics;
- Source Notes semantics;
- Reference Sets semantics finché Schedulae non possiede realmente tale modello;
- filtro `unused` basato sull'assenza di contesto Calamus.

Questa adaptation deve avvenire prima che B02 esponga una UI, altrimenti l'interfaccia renderebbe visibile semantica falsa.

### N.5 B01 — minor inherited defect verificato

Probe diretto:

```python
parse_references_markdown("# Wrong Header\n")
```

produce:

```text
Expected library header: {_HEADER}.
```

La stringa contiene le parentesi letterali perché il source usa `{{_HEADER}}`.

Classificazione:

`INHERITED_USER_VISIBLE_DIAGNOSTIC_DEFECT`

Non va corretto in B00, dove è vietato cambiare comportamento. Va registrato come repair B01 con test specifico.

### N.6 B01 — canonical-library file-safety questions

Il core usa:

- `os.stat()` + SHA-256 per `FileToken`;
- stale token comparison prima di save;
- temp path fisso `<library>.tmp`;
- `os.replace()` per pubblicazione atomica.

Le garanzie correnti sono buone per l'uso normale, ma due boundary non sono ancora contrattualmente risolti per una app standalone:

1. **canonical library symlink policy** — load segue un symlink; import/export invece li rifiuta esplicitamente;
2. **multi-process/race ownership** — token check e replace non costituiscono una transazione atomica unica; il temp name fisso merita hostile probe.

Stato: `RISK / PROBE REQUIRED`, non defect dichiarato.

### N.7 B02 — mature-source need

Per B02 il source Mousepad raw già incluso è sufficiente per molte domande di GTK application/window lifecycle, ma non per la specifica ergonomia bibliografica.

Mature source prioritario da avere direttamente:

1. **GNOME Citations** — massima priorità per list/detail, selection authority, empty state, open/save bibliography lifecycle.
2. **KBibTeX** — massima priorità per filter/projection, element editor, validation-before-apply, read-only state e local-file actions.
3. **JabRef** — alta priorità per field editor, citation-key lifecycle, duplicate handling e import/merge review.
4. **coBib** — utile per mantenere Schedulae lightweight: command/projection separation, selected-key restoration, explicit open/delete/export.

### N.8 B03 — mature-source need

Per B03:

1. **JabRef** — BibTeX/BibLaTeX import/export writer semantics e collision workflow;
2. **KBibTeX** — typed field/value semantics e importer/exporter boundary;
3. **Pandoc** — verifica di interoperabilità downstream, soprattutto differenze semantiche BibTeX/BibLaTeX;
4. **GNOME Citations** — file lifecycle e parser/serializer separation.

### N.9 Sources non prioritari per v1

- **Zotero**: utile come anti-pattern/benchmark per duplicate merge e selected-item detail, ma troppo ampio e database-centric per guidare il core v1; non è necessario prima di B04/feature Full.
- **Referencer**: storico GTK bibliografico utile, ma meno prioritario di GNOME Citations + Mousepad.
- **Better BibTeX for Zotero**: utile solo se in futuro si amplia la citation-key policy; non necessario per B00–B02.

### N.10 Exact historical source revisions desiderate

Per evitare drift, se disponibili si preferiscono le stesse revisioni già usate nel mature-source audit Calamus W97:

```text
GNOME Citations  citations-master(1).zip
SHA-256 2ab04a778ef9dc9c4e681ebb006f25adb71e685f038c6f58af679b1c6263f89c

JabRef           jabref-main(5).zip
SHA-256 aa62a954f5206a3f300d21de68f0a3027a860e15413aed95ae17db6323f99cfb

KBibTeX          kbibtex-master(5).zip
SHA-256 f65701b654d0db4b797fcd6ccdca4d244dcc7189ddf894ec409b80d4b11a9ee1

coBib            cobib-master(1).zip
SHA-256 1d74456354d6be52abe8dbd10193396159bbb84a0a56fb086f437cc849f867a3

Pandoc           pandoc-main(1).zip
SHA-256 d813fbb68007a697358c515f434ae951ae6d5ee8a4cca66c611acf63bf45083e
```

Il W97 audit storico documenta anche Zotero e Referencer, ma non sono richiesti per iniziare l'implementazione Schedulae.

### N.11 Audit next action

Prima di B00 bootstrap reale:

1. repair design del bootstrap tool sotto il nuovo cap di tre documenti;
2. definire exact cleanliness gate (no `__pycache__`, no `.pyc`);
3. mantenere core/test source byte-identici;
4. nessuna Git mutation;
5. dopo autorizzazione, B00 bootstrap + exactly 74 tests.

In parallelo, se vengono forniti i quattro comparator source prioritari (Citations, KBibTeX, JabRef, coBib), il direct implementation audit può congelare B01/B02 senza usare web come sostituto.




---

## N2. Audit di implementazione autorizzato — B00 repair + mature-source freeze

**Data:** 2026-08-19  
**Authorization:** user explicitly authorized next step.  
**Candidate:** NO — B00 remains headless/non-candidate.  
**Git authority granted in this step:** fresh local Schedulae repository creation + `git init -b main`.  
**Git authority NOT granted:** `git add`, commit, remote, push.

### N2.1 Comparator source identity — exact W97 corpus confirmed

The five newly supplied archives match the exact revisions requested by the historical W97 audit:

```text
GNOME Citations  2ab04a778ef9dc9c4e681ebb006f25adb71e685f038c6f58af679b1c6263f89c
KBibTeX          f65701b654d0db4b797fcd6ccdca4d244dcc7189ddf894ec409b80d4b11a9ee1
JabRef           aa62a954f5206a3f300d21de68f0a3027a860e15413aed95ae17db6323f99cfb
coBib            1d74456354d6be52abe8dbd10193396159bbb84a0a56fb086f437cc849f867a3
Pandoc           d813fbb68007a697358c515f434ae951ae6d5ee8a4cca66c611acf63bf45083e
```

`MATURE_SOURCE_IDENTITY=5/5_EXACT_MATCH`

No web source was substituted for these direct source audits.

### N2.2 Direct mature-source findings

#### GNOME Citations — ADOPT principles, not implementation

Direct source inspected: `src/window.rs`, `src/entry_list.rs`, `src/entry_page.rs`, `cratebibtex/src/bib.rs`.

Findings:

- bibliography file identity is explicit (`gio::File`) and Open/New are file actions, not hidden global-database ownership;
- replacing an open bibliography is guarded when the current bibliography is modified;
- list rendering is a projection of the bibliography model through filter + selection models;
- selection is a distinct model that emits the selected entry; detail reacts to that semantic selection;
- search uses a derived expression and does not mutate the bibliography;
- duplicate citation keys are checked before New and before citation-key apply;
- modified state belongs to the bibliography model and changes on entry mutation;
- save clears modified state only after successful file replacement.

Schedulae decision:

- **ADOPT** explicit library-file ownership, list/filter projection, model-level selection and successful-save boundary;
- **ADAPT** selection ownership to Schedulae's stronger existing semantic citation-key authority in `ReferenceController` rather than GTK row/position authority;
- **REJECT** Citations' network/PDF conveniences from v1;
- **DO NOT REGRESS** from Schedulae's stronger stale-token/persist-first safety to Citations' simpler modified flag.

#### KBibTeX — ADOPT validation/read-only discipline

Direct source inspected: `src/gui/element/elementeditor.cpp`, `elementwidgets.cpp`, `sortfilterfilemodel.cpp`.

Findings:

- the editor works on an internal/cloned element state;
- per-field validation runs before accepting problematic data and focuses the offending field;
- explicit read-only propagates to field editors and prevents `apply()` from writing;
- filter projection searches ID, type and entry fields without changing source data;
- duplicate IDs are treated as an explicit decision boundary, not silently overwritten.

Schedulae decision:

- **ADOPT** draft/editor separation + validation-before-controller-commit + explicit read-only UI state;
- **ADOPT** projection-only filters;
- **ADAPT** duplicate-key behavior to Schedulae's stricter policy: ambiguous identity collision remains blocking; do not offer a casual “keep duplicate ids” path;
- **REJECT** PDF-content searching and broad document management in v1.

#### JabRef — ADOPT deterministic key uniqueness and explicit duplicate integrity

Direct source inspected: `CitationKeyGenerator.java`, `CitationKeyDuplicationChecker.java`, merge/duplicate boundaries.

Findings:

- citation-key generation sanitizes disallowed characters and deterministically searches for a free suffixed key;
- duplicate citation keys are a first-class integrity condition;
- large merge machinery keeps field-level conflict resolution explicit.

Schedulae decision:

- existing `suggest_reference_key()` + alias collision policy already satisfies the required v1 boundary;
- **ADOPT principle** that key uniqueness is library-aware and deterministic;
- **DEFER** user-configurable key-pattern language and field-by-field three-way merge: disproportionate complexity for v1;
- B03 import keeps the existing smaller explicit decisions (`skip/replace/merge/new-key`) rather than cloning JabRef's merge UI.

#### coBib — ADOPT command/domain separation; reject singleton/cache authority

Direct source inspected: `database/database.py`, commands, parser/exporter boundaries.

Findings:

- commands are separated from database/domain and from UI;
- label disambiguation is deterministic and library-aware;
- import/export are explicit command boundaries;
- however the runtime database is a singleton and includes cache/unsaved-entry machinery.

Schedulae decision:

- **ADOPT** thin command/controller boundaries and deterministic key disambiguation;
- **REJECT** singleton database, persistent cache authority and generalized event/plugin architecture;
- Schedulae's explicit controller/store composition is already simpler and safer for its scale.

#### Pandoc — freeze BibTeX/BibLaTeX as separate interoperability modes

Direct source inspected: `Text/Pandoc/Readers/BibTeX.hs`, `Citeproc/BibTeX.hs`, writer registration.

Findings:

- Pandoc exposes BibTeX and BibLaTeX as distinct reader/writer variants;
- its mapping accounts for mode-sensitive fields such as `date`, `entrysubtype`, `langid` and related bibliography semantics.

Schedulae decision:

- retain explicit `bibtex` vs `biblatex` mode in B03;
- no “generic .bib mode” that silently guesses semantic mappings after the user has selected a format;
- keep deterministic lossiness diagnostics where Schedulae cannot preserve an exact cross-mode meaning.

### N2.3 B01 architectural freeze after mature-source audit

B01 is now constrained to the smallest useful standalone adaptation:

1. introduce Schedulae application/library identity without changing the References v1 interoperability format;
2. explicit library path is the primary authority; no silent ownership of Calamus' default path;
3. XDG is for application preferences/state only, not the bibliography authority;
4. keep `MarkdownReferenceStore(path=...)`; no new repository/database layer;
5. remove/adapt Calamus-only context semantics before B02 UI (`Current Document`, `Source Notes`, `Reference Sets`, `cited/source-notes/unused` filters);
6. keep Type/Tag/File/Integrity/search/sort projections that derive from the library itself;
7. keep semantic selected citation key in the controller;
8. editor UI must operate on a draft and call controller commit only after validation;
9. blocking malformed-library state must surface as read-only rather than being auto-repaired;
10. collision policy remains stricter than KBibTeX/Citations: no silent duplicate primary/alias identities;
11. explicit BibTeX/BibLaTeX mode remains frozen for B03;
12. no background index, database, singleton, cache authority, plugins, network lookup or PDF library.

### N2.4 B00 bootstrap tooling repair — implementation

The old bootstrap tool was retired before use because it violated the new three-document governance and package cleanliness.

R1 repair rules:

- enumerate source/test files from exact provenance instead of recursive copying;
- never copy `__pycache__` or `.pyc`;
- package and repository contain exactly three Markdown project documents;
- no README and no `docs/contracts` tree;
- provenance/identity remain machine-readable TSV/TOML, not additional canonical documents;
- exact 11 core sources and 11 test modules remain byte-identical;
- `tests/__init__.py` remains exact empty source;
- runner disables bytecode generation so validation itself does not dirty the repository;
- fresh repository initialization is authorized;
- no staging, commit, remote or push.

Artifact line: `SCHEDULAE_B00_BOOTSTRAP_R1_20260819`.

### N2.5 B00 validation disclosure

For the T480 run:

```text
TOTAL TESTS = 74
CANDIDATE = NO
GIT INIT = AUTHORIZED
GIT ADD/COMMIT/REMOTE/PUSH = NO
```

The run must stop on any failure and emit `EXIT/ERR/FINAL_PHASE`.

### N2.6 Current next action

`NEXT_ACTION = RUN_B00_BOOTSTRAP_R1_ON_T480`

Expected outcome:

- fresh `/home/luciano/Projects/schedulae-work`;
- branch `main` initialized;
- source/test provenance exact;
- exactly three Markdown project documents;
- zero bytecode artifacts;
- 74/74 PASS;
- no commit and no remote.


### 2026-08-19 — B00 Bootstrap R1 T480 certification PASS

User executed the exact B00 R1 runner on the Lenovo ThinkPad T480.

Declared test count before run:

```text
TOTAL_TESTS=74
```

Observed bootstrap/package results:

```text
B00_PACKAGE_VERIFY=PASS
CORE_MODULES=11
TEST_MODULES=11
EXPECTED_TESTS=74
CANONICAL_DOCUMENTS=3
BYTECODE_ARTIFACTS=0
FINAL_PHASE=B00_PACKAGE_VERIFY_PASS
```

Repository creation:

```text
PROJECT_ROOT=/home/luciano/Projects/schedulae-work
B00_BOOTSTRAP=PASS
GIT_INITIALIZED=YES
BRANCH=main
GIT_ADD=NO
GIT_COMMIT=NONE
GIT_REMOTE=NONE
FINAL_PHASE=B00_BOOTSTRAP_TREE_READY
```

Exact inherited test run:

```text
Ran 74 tests in 0.157s
OK
B00_TEST_TOTAL=74
B00_TEST_RESULT=74/74_PASS
SKIPS=0
EXIT=0
ERR=NONE
FINAL_PHASE=B00_EXACT_EXTRACTION_PASS
```

Final repository verification:

```text
B00_REPO_VERIFY=PASS
CORE_MODULES=11
TEST_MODULES=11
CANONICAL_DOCUMENTS=3
BYTECODE_ARTIFACTS=0
GIT_INITIALIZED=YES
GIT_COMMIT=NONE
GIT_REMOTE=NONE
FINAL_PHASE=B00_REPO_VERIFY_PASS
```

Final closure marker:

```text
B00_EXACT_EXTRACTION_CONTRACT=PASS
RUNNER_RC=0
EXIT=0
ERR=NONE
FINAL_PHASE=SCHEDULAE_B00_BOOTSTRAP_R1_PASS
```

Classification:

```text
B00_STATUS=CLOSED_T480_CERTIFIED_UNPUBLISHED
PRODUCT_FAIL=NO
ORACLE_FAIL=NO
PACKAGING_FAIL=NO
CANDIDATE=NO
CANDIDATE_ATTEMPTS=0
GIT_COMMIT=NONE
GIT_REMOTE=NONE
```

Decision:

- B00 exact extraction contract is fully satisfied on target hardware.
- The Schedulae repository now exists independently on the T480.
- B00 requires no further repair.
- B01 is technically unlocked but is **not opened automatically**.
- No commit/push is authorized by this closure.

Next action:

`NEXT_ACTION = RUN_B00_P2_DOCUMENTATION_FINALIZER_ON_T480`

### 2026-08-19 — GitHub repository created

User created the public GitHub repository:

`https://github.com/leviagravia/schedulae`

Status recorded from user report:

```text
REMOTE_REPOSITORY_CREATED=YES
REMOTE_URL=https://github.com/leviagravia/schedulae
REMOTE_PROVIDER=GitHub
LOCAL_REPO=/home/luciano/Projects/schedulae-work
LOCAL_BRANCH=main
LOCAL_COMMIT=NONE
LOCAL_REMOTE_CONFIGURED=NO
PUSH_PERFORMED=NO
B00_STATUS=CLOSED_T480_CERTIFIED_UNPUBLISHED
```

Governance consequence:

- the remote destination now exists;
- creating the GitHub repository does not itself publish the certified B00 tree;
- commit/push remain separate publication actions;
- before the first public code publication, the Schedulae license must be explicitly frozen;
- no Git mutation is inferred from the creation of the remote repository.

Next action:

`NEXT_ACTION = RUN_B00_P2_DOCUMENTATION_FINALIZER_ON_T480`

### 2026-08-19 — Schedulae license frozen: GPL-3.0-or-later

Decision:

```text
LICENSE_FULL_NAME=GNU General Public License v3.0 or later
SPDX_LICENSE_IDENTIFIER=GPL-3.0-or-later
LICENSE_FILE=LICENSE
LICENSE_STATUS=FROZEN
```

Rationale:

- Schedulae is a complete desktop application rather than a reusable linking library;
- strong copyleft matches the product intent that distributed modified versions remain free/open;
- GPL v3 includes the current GPLv3 protections and the `or later` formulation preserves a future upgrade path;
- a permissive license such as MIT was not selected because it permits proprietary redistribution/derivatives;
- LGPL was not selected because the Schedulae product is an application, not a library whose main purpose is proprietary linking.

Provenance constraint:

- the B00 handover exposes no Calamus root license and no third-party license headers in the 11 extracted core modules;
- licensing Schedulae can cover only rights actually held by the licensor;
- any third-party material discovered later retains its own copyright/license obligations.

B00 identity preservation:

- no source/test header is changed during license adoption;
- the 11 core modules and inherited tests remain the exact B00-certified bytes;
- per-file SPDX/copyright notices are deferred to B01, the first source-modifying work item;
- root `LICENSE` is a required legal artifact and does not count against the three-canonical-document cap.

Publication state after this decision:

```text
REMOTE_REPOSITORY=https://github.com/leviagravia/schedulae
REMOTE_EXISTS=YES
LOCAL_COMMIT=NONE
LOCAL_REMOTE_CONFIGURED=NO
PUSH=NO
B00_STATUS=CLOSED_T480_CERTIFIED_UNPUBLISHED
```

Next action:

`NEXT_ACTION = RUN_B00_P2_DOCUMENTATION_FINALIZER_ON_T480`

### 2026-08-19 — License Adoption R1 pre-delivery self-test harness FAIL and oracle repair

Fresh sandbox self-test of `APPLY_LICENSE_T480.sh` stopped before any license mutation.

Observed:

```text
LICENSE_ADOPTION=FAIL
EXIT=3
ERR=branch_not_main
FINAL_PHASE=LICENSE_PRECONDITION_FAIL
```

Classification:

```text
PRODUCT_FAIL=NO
LICENSE_DECISION_FAIL=NO
HARNESS_FAIL=YES
ROOT_CAUSE=GIT_UNBORN_BRANCH_ORACLE
USER_T480_NOT_AFFECTED=YES
```

Failure-specific Git boundary audit:

- in a freshly initialized repository with `git init -b main` and no commits, `git rev-parse --abbrev-ref HEAD` exits 128 because `HEAD` does not yet resolve to a commit;
- the repository nevertheless has an exact symbolic branch reference `refs/heads/main`;
- `git symbolic-ref --quiet --short HEAD` returns `main` with exit 0;
- `git status --short --branch` reports `No commits yet on main`.

Repair constraint:

**On an unborn Git branch, verify branch identity from the symbolic reference, not from commit-resolving `rev-parse HEAD`.**

Repair:

- changed only the License Adoption runner oracle;
- replaced `git rev-parse --abbrev-ref HEAD` with `git symbolic-ref --quiet --short HEAD`;
- no Schedulae product/core/test source modified;
- no candidate attempt consumed.

Status after repair:

`REQUALIFICATION_REQUIRED_BEFORE_T480_DELIVERY`

### 2026-08-19 — License Adoption R1 second pre-delivery self-test harness FAIL and test-root repair

After the unborn-branch oracle repair, a second fresh sandbox self-test stopped before license mutation.

Observed:

```text
B00_TEST_RUN=FAIL
ERR=missing_core_or_tests
FINAL_PHASE=B00_TEST_SETUP_FAIL
LICENSE_ADOPTION=FAIL
EXIT=10
ERR=prelicense_tests_failed
FINAL_PHASE=LICENSE_PRETEST_FAIL
```

Classification:

```text
PRODUCT_FAIL=NO
LICENSE_DECISION_FAIL=NO
HARNESS_FAIL=YES
ROOT_CAUSE=TEST_ROOT_OWNERSHIP_NOT_PASSED
USER_T480_NOT_AFFECTED=YES
```

Failure-specific audit of the exact B00 test runner:

- `tools/RUN_B00_TESTS.py` exposes `--root`;
- its default root is the caller's current directory (`.`);
- the License Adoption runner lives outside the target repository;
- therefore invoking the test runner without `--root "$ROOT"` makes it search the wrong filesystem boundary.

Repair constraint:

**Every external invocation of the B00 runner must pass the target repository root explicitly.**

Repair:

- both pre-license and post-license invocations now use `--root "$ROOT"`;
- no product/core/test source changed;
- no candidate attempt consumed.

Status after repair:

`REQUALIFICATION_REQUIRED_BEFORE_T480_DELIVERY`

### 2026-08-19 — License Adoption R1 fresh sandbox requalification PASS

After the two harness-only repairs, the License Adoption package was requalified from a newly bootstrapped B00 repository with an unborn `main` branch.

Pre-license regression:

```text
TOTAL_TESTS=74
EXPECTED_TESTS=74
B00_TEST_RESULT=74/74_PASS
SKIPS=0
FINAL_PHASE=B00_EXACT_EXTRACTION_PASS
```

Post-license regression:

```text
TOTAL_TESTS=74
EXPECTED_TESTS=74
B00_TEST_RESULT=74/74_PASS
SKIPS=0
FINAL_PHASE=B00_EXACT_EXTRACTION_PASS
```

License and identity gates:

```text
LICENSE_FILE=PASS
SPDX_LICENSE_IDENTIFIER=GPL-3.0-or-later
CANONICAL_DOCUMENTS=3
SOURCE_TEST_BYTES_UNCHANGED=YES
BYTECODE_ARTIFACTS=0
GIT_COMMIT=NONE
GIT_REMOTE=NONE
LICENSE_ADOPTION=PASS
EXIT=0
ERR=NONE
FINAL_PHASE=SCHEDULAE_GPL3_OR_LATER_LICENSE_ADOPTION_PASS
```

Fresh-environment classification:

```text
PRODUCT_FAIL=NO
HARNESS_REQUALIFICATION=PASS
TEST_CASES=74
TEST_EXECUTIONS=148
SOURCE_TEST_MUTATION=NO
CANDIDATE=NO
GIT_MUTATION=WORKTREE_FILES_ONLY
COMMIT=NONE
REMOTE=NONE
```

The License Adoption R1 line is now ready for the T480. It is not a desktop candidate and consumes no candidate attempt.

Next action:

`NEXT_ACTION = RUN_B00_P2_DOCUMENTATION_FINALIZER_ON_T480`

### 2026-08-19 — GPL-3.0-or-later License Adoption R1 T480 PASS

User executed the exact License Adoption R1 runner on the Lenovo ThinkPad T480.

Observed post-adoption regression:

```text
Ran 74 tests in 0.148s
OK
B00_TEST_TOTAL=74
B00_TEST_RESULT=74/74_PASS
SKIPS=0
EXIT=0
ERR=NONE
FINAL_PHASE=B00_EXACT_EXTRACTION_PASS
```

Final license and integrity gates:

```text
LICENSE_FILE=PASS
SPDX_LICENSE_IDENTIFIER=GPL-3.0-or-later
CANONICAL_DOCUMENTS=3
SOURCE_TEST_BYTES_UNCHANGED=YES
BYTECODE_ARTIFACTS=0
GIT_COMMIT=NONE
GIT_REMOTE=NONE
LICENSE_ADOPTION=PASS
EXIT=0
ERR=NONE
FINAL_PHASE=SCHEDULAE_GPL3_OR_LATER_LICENSE_ADOPTION_PASS
```

Classification:

```text
LICENSE_STATUS=ADOPTED_T480_VERIFIED
B00_STATUS=CLOSED_T480_CERTIFIED_UNPUBLISHED
PRODUCT_FAIL=NO
SOURCE_TEST_MUTATION=NO
CANONICAL_DOCUMENTS=3
BYTECODE_ARTIFACTS=0
GIT_COMMIT=NONE
GIT_REMOTE=NONE
CANDIDATE=NO
CANDIDATE_ATTEMPTS=0
```

Decision:

- Schedulae is now licensed under **GNU GPL v3.0 or later (`GPL-3.0-or-later`)** at repository level.
- Root `LICENSE` is installed and verified.
- The B00-certified source/test bytes remain unchanged.
- The three-document cap remains satisfied.
- The public GitHub repository exists, but no code has yet been committed or pushed.
- B01 remains unopened.

Next action:

`NEXT_ACTION = RUN_B00_P2_DOCUMENTATION_FINALIZER_ON_T480`

### 2026-08-19 — First Git publication P1 explicitly authorized

User explicitly authorized the next step after B00 T480 certification and GPL-3.0-or-later adoption.

Authorized mutation envelope:

```text
GIT_ADD=AUTHORIZED
FIRST_COMMIT=AUTHORIZED
REMOTE_ADD_ORIGIN=AUTHORIZED
PUSH_MAIN=AUTHORIZED
REMOTE_URL=https://github.com/leviagravia/schedulae.git
B01=NOT_AUTHORIZED_BY_THIS_ACTION
```

P1 publication contract:

- preflight must occur before Git staging/commit/remote mutation;
- remote must be reachable and expose no heads/tags before first push;
- B00 core/test bytes must still match exact provenance;
- root `LICENSE` must match the frozen GPLv3 text;
- exactly three Markdown canonical project documents must exist;
- test count is 74 cases;
- tests run once before authority update and once after authority/identity update: **148 test executions** total;
- no source/test mutation;
- no B01 namespace or behavior change;
- first commit subject: `B00: bootstrap Schedulae bibliography core`;
- publication is not closed until `HEAD = origin/main = remote main`, tree/worktree checks pass, and the exact commit/tree are recorded in the next MO increment.

Because a Git commit cannot reliably contain its own final SHA without changing that SHA, P1 deliberately does **not** attempt to write its own final commit hash into the same commit. Exact publication receipt is a post-P1 MO update.

Next action:

`NEXT_ACTION = RUN_B00_P2_DOCUMENTATION_FINALIZER_ON_T480`

### 2026-08-19 — First Publication P1 pre-delivery self-test post-push oracle FAIL

Fresh end-to-end self-test used a newly bootstrapped/licensed Schedulae repository and an empty local bare Git remote.

The following product/publication operations succeeded before the harness failed:

```text
REMOTE_EMPTY_PREFLIGHT=PASS
B00_SOURCE_TEST_PROVENANCE=PASS
74/74 PREPUBLICATION PASS
SOURCE_TEST_BYTES_UNCHANGED=YES
74/74 POST-AUTHORITY PASS
ROOT_COMMIT=CREATED
PUSH_MAIN=SUCCESS
UPSTREAM_ORIGIN_MAIN=SET
```

The runner then failed only while reading the remote SHA:

```text
fatal: 'origin' does not appear to be a git repository
PUBLICATION_P1=FAIL
EXIT=40
ERR=cannot_read_remote_main
FINAL_PHASE=P1_POSTPUSH_VERIFY_FAIL
```

Classification:

```text
PRODUCT_FAIL=NO
GIT_COMMIT_FAIL=NO
GIT_PUSH_FAIL=NO
REMOTE_STATE_FAIL=NO
HARNESS_ORACLE_FAIL=YES
USER_T480_NOT_AFFECTED=YES
```

Failure-specific Git boundary audit:

- Git remotes are repository configuration;
- `origin` existed in the Schedulae test repository and the preceding `git -C "$ROOT" push -u origin main` succeeded;
- the failing `git ls-remote origin ...` was executed from the package directory, not with repository context;
- therefore `origin` was resolved against the wrong Git context.

Repair constraint:

**Every command that resolves a remote by its configured name must execute with the target repository as Git context.**

Repair:

```text
OLD: git ls-remote origin refs/heads/main
NEW: git -C "$ROOT" ls-remote origin refs/heads/main
```

No Schedulae core/test/product source changed. The failure occurred only in a disposable local self-test remote; no user GitHub state was touched.

Status:

`P1_REQUALIFICATION_REQUIRED_BEFORE_T480_DELIVERY`

### 2026-08-19 — First Publication P1 fresh end-to-end requalification PASS

After the remote-context oracle repair, P1 was rerun from a freshly bootstrapped B00 repository, with GPL-3.0-or-later freshly adopted, against a new empty local bare Git remote.

Result:

```text
REMOTE_EMPTY_PREFLIGHT=PASS
B00_SOURCE_TEST_PROVENANCE=PASS
TEST_CASES=74
TEST_EXECUTIONS=148
B00_TEST_RESULT=74/74_PASS_X2
LICENSE=GPL-3.0-or-later
CANONICAL_DOCUMENTS=3
SOURCE_TEST_BYTES_UNCHANGED=YES
BYTECODE_ARTIFACTS=0
ROOT_COMMIT=CREATED
PUSH_MAIN=PASS
HEAD_EQUALS_ORIGIN_MAIN=YES
HEAD_EQUALS_REMOTE_MAIN=YES
WORKTREE=CLEAN
COMMIT_COUNT=1
B01=NOT_OPENED
PUBLICATION_P1=PASS
EXIT=0
ERR=NONE
FINAL_PHASE=SCHEDULAE_B00_FIRST_PUBLICATION_P1_PASS
```

The commit/tree produced in this disposable self-test are not Schedulae publication authority and are intentionally not recorded as project commit identity.

Classification:

```text
PRODUCT_FAIL=NO
HARNESS_REQUALIFICATION=PASS
PUBLICATION_FLOW_REQUALIFIED=YES
USER_GITHUB_MUTATION=NO
CANDIDATE=NO
```

P1 is ready for the T480 against the official GitHub remote.

Next action:

`NEXT_ACTION = RUN_B00_P2_DOCUMENTATION_FINALIZER_ON_T480`

### 2026-08-19 — B00 First Publication P1 T480 PASS / B00 PUBLISHED

User executed the exact First Publication P1 runner on the Lenovo ThinkPad T480 against the official GitHub repository.

Push result:

```text
To https://github.com/leviagravia/schedulae.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

Final P1 evidence:

```text
PUBLICATION_P1=PASS
TEST_CASES=74
TEST_EXECUTIONS=148
B00_TEST_RESULT=74/74_PASS_X2
LICENSE=GPL-3.0-or-later
CANONICAL_DOCUMENTS=3
SOURCE_TEST_BYTES_UNCHANGED=YES
BYTECODE_ARTIFACTS=0
COMMIT=4d71e7f0e868d8229b0e05dd2682acc4d887f535
TREE=f0a0b49af500c6cefec180af6ec317738ab0919f
HEAD=4d71e7f0e868d8229b0e05dd2682acc4d887f535
ORIGIN_MAIN=4d71e7f0e868d8229b0e05dd2682acc4d887f535
REMOTE_MAIN=4d71e7f0e868d8229b0e05dd2682acc4d887f535
REMOTE_URL=https://github.com/leviagravia/schedulae.git
WORKTREE=CLEAN
B01=NOT_OPENED
EXIT=0
ERR=NONE
FINAL_PHASE=SCHEDULAE_B00_FIRST_PUBLICATION_P1_PASS
```

Publication classification:

```text
B00_STATUS=CLOSED_T480_CERTIFIED_PUBLISHED
PUBLICATION_P1=PASS
PRODUCT_FAIL=NO
CORE_TEST_MUTATION=NO
TEST_CASES=74
TEST_EXECUTIONS=148
LICENSE=GPL-3.0-or-later
HEAD_EQUALS_ORIGIN_MAIN=YES
HEAD_EQUALS_REMOTE_MAIN=YES
WORKTREE=CLEAN
B01=NOT_OPENED
```

Canonical publication authority:

- commit: `4d71e7f0e868d8229b0e05dd2682acc4d887f535`
- tree: `f0a0b49af500c6cefec180af6ec317738ab0919f`
- subject: `B00: bootstrap Schedulae bibliography core`
- remote: `https://github.com/leviagravia/schedulae.git`
- branch: `main`

Decision:

- B00 is fully CLOSED / T480 CERTIFIED / PUBLISHED.
- The first public Git history of Schedulae is established.
- No B01 work was included in the publication.
- This MO v2.3 records the exact publication receipt externally to the already-published P1 commit.
- Publishing this receipt back into the repository would require a separate P2 document-only commit/push authorization.

Next action:

`NEXT_ACTION = RUN_B00_P2_DOCUMENTATION_FINALIZER_ON_T480`

### 2026-08-19 — B01 direct-source pre-implementation audit COMPLETE

Scope:

- exact published B00 source model;
- GNOME Citations;
- KBibTeX;
- JabRef;
- coBib;
- Pandoc;
- Mousepad;
- novelWriter.

Comparator SHA authority was reverified and matches the historical W97 corpus exactly.

Key architecture verdict:

```text
B01_DIRECT_SOURCE_AUDIT=PASS
B01_IMPLEMENTATION=NOT_OPENED
MATURE_SOURCE_SUFFICIENT=YES
ADDITIONAL_SOURCE_REQUIRED=NO
ARCHITECTURAL_REWRITE_REQUIRED=NO
DATABASE_REQUIRED=NO
GTK_REQUIRED=NO
```

Two isolated hostile file probes against the exact B00 seed exposed valid inherited product defects:

```text
DEFECT_1=CANONICAL_SYMLINK_SAVE_IDENTITY
SYMLINK_SAVE_STATUS=saved
LIBRARY_PATH_IS_SYMLINK_AFTER=False
TARGET_CHANGED=False
LINK_FILE_CHANGED=True

DEFECT_2=FIXED_TEMP_SYMLINK_OVERWRITE
TMP_SYMLINK_WRITE=RETURNED_SUCCESS
VICTIM_CONTENT=SAFE DATA
```

Both probes used temporary sandbox files only.

Frozen B01 direction:

- package namespace `schedulae`;
- explicit library path only;
- no automatic Calamus or Schedulae XDG bibliography;
- preserve `# Calamus References v1` interoperability;
- unique same-directory exclusive temp files;
- canonical selected symlink resolves/fixes target identity rather than replacing the link;
- reject non-regular canonical targets;
- recheck stale token immediately before publish;
- remove Calamus-only Current Document / Source Notes / Reference Sets / Use filters;
- integrity becomes objective only;
- keep persist-first controller, semantic key selection, aliases, deterministic Bib modes;
- no database/singleton/plugin/network/GTK.

The detailed frozen audit contract is incorporated in Canonical Document 2, section 31.


### 2026-08-19 — B00 P2 documentation finalizer authorized

The user instructed that B00 be closed correctly while the B01 audit proceeds. This authorizes a final **documentation-only** P2.

Expected parent authority:

```text
P1_COMMIT=4d71e7f0e868d8229b0e05dd2682acc4d887f535
P1_TREE=f0a0b49af500c6cefec180af6ec317738ab0919f
REMOTE=https://github.com/leviagravia/schedulae.git
```

P2 mutation envelope:

```text
ALLOWED_CHANGES=
  01_SCHEDULAE_PRODUCT_AND_GOVERNANCE.md
  02_SCHEDULAE_TECHNICAL_AUTHORITY_AND_ROADMAP.md
  03_SCHEDULAE_MEMORIA_OPERATIVA.md

CORE_TEST_MUTATION=FORBIDDEN
B01_IMPLEMENTATION=FORBIDDEN
TEST_CASES=74
TEST_EXECUTIONS=148
COMMIT_SUBJECT=docs: finalize B00 publication and record B01 audit
```

P1 remains B00 product-source authority. P2 only synchronizes the exact publication receipt and pre-implementation B01 audit into the public repository.

Next action:

`NEXT_ACTION = RUN_B00_P2_DOCUMENTATION_FINALIZER_ON_T480`

### 2026-08-19 — B00 P2 documentation finalizer fresh end-to-end requalification PASS

P2 was tested from a new isolated history:

1. fresh exact B00 bootstrap;
2. fresh GPL-3.0-or-later adoption;
3. fresh P1 first publication to a new empty local bare Git remote;
4. P2 against that exact P1 commit/tree.

Observed P2 result:

```text
B00_P2=PASS
TEST_CASES=74
TEST_EXECUTIONS=148
B00_TEST_RESULT=74/74_PASS_X2
CANONICAL_DOCUMENTS=3
SOURCE_TEST_BYTES_UNCHANGED=YES
ROOT_P1_COMMIT=UNCHANGED_PARENT
P2_DOCUMENTATION_COMMIT=CREATED
PUSH_MAIN=PASS
HEAD_EQUALS_ORIGIN_MAIN=YES
HEAD_EQUALS_REMOTE_MAIN=YES
WORKTREE=CLEAN
B01_AUDIT=COMPLETE
B01_IMPLEMENTATION=NOT_OPENED
B00_STATUS=CLOSED_T480_CERTIFIED_PUBLISHED_DOCUMENTATION_FINALIZED
EXIT=0
ERR=NONE
FINAL_PHASE=SCHEDULAE_B00_P2_DOCUMENTATION_FINALIZER_PASS
```

The exact disposable self-test commit SHA is intentionally not project authority.

Classification:

```text
P2_REQUALIFICATION=PASS
PRODUCT_FAIL=NO
HARNESS_FAIL=NO
CORE_TEST_MUTATION=NO
USER_GITHUB_MUTATION=NO
CANDIDATE=NO
```

P2 is ready for the official T480/GitHub repository.

Next action:

`NEXT_ACTION = RUN_B00_P2_DOCUMENTATION_FINALIZER_ON_T480`
### 2026-08-19 — B00 P2 official T480 PASS / documentation finalized

```text
B00_P2=PASS
TEST_CASES=74
TEST_EXECUTIONS=148
B00_TEST_RESULT=74/74_PASS_X2
P1_PRODUCT_COMMIT=4d71e7f0e868d8229b0e05dd2682acc4d887f535
P1_PRODUCT_TREE=f0a0b49af500c6cefec180af6ec317738ab0919f
P2_DOCUMENTATION_COMMIT=daf6da276b44a490793526d278098fba261c5afe
P2_DOCUMENTATION_TREE=8666041a2d5dd83166cbe9a87ae844715eb7fc7c
HEAD=daf6da276b44a490793526d278098fba261c5afe
ORIGIN_MAIN=daf6da276b44a490793526d278098fba261c5afe
REMOTE_MAIN=daf6da276b44a490793526d278098fba261c5afe
WORKTREE=CLEAN
CANONICAL_DOCUMENTS=3
SOURCE_TEST_BYTES_UNCHANGED=YES
B01_AUDIT=COMPLETE
B01_IMPLEMENTATION=NOT_OPENED_AT_P2
B00_STATUS=CLOSED_T480_CERTIFIED_PUBLISHED_DOCUMENTATION_FINALIZED
EXIT=0
ERR=NONE
FINAL_PHASE=SCHEDULAE_B00_P2_DOCUMENTATION_FINALIZER_PASS
```

No P3 is required. P1 is product-source authority; P2 is the final B00 documentation/audit authority.

### 2026-08-19 — B01 implementation explicitly authorized and R1 built

User explicitly authorized B01 implementation after B00 final closure.

Implementation envelope:

```text
B01_IMPLEMENTATION=AUTHORIZED
GTK=FORBIDDEN
CANONICAL_REPO_MUTATION=NO
GIT_COMMIT_PUSH=NO
CANDIDATE=NO
```

A focused mature-source re-audit at the two valid B00 save defects confirmed the repair ownership:

- GNOME Citations: explicit bibliography `gio::File` + replace-content save;
- KBibTeX: explicit symlink-resolution behavior specifically to avoid replacing the symlink on save; unique temporary-file primitives.

R1 implementation results in sandbox:

```text
PYTHON_NAMESPACE=schedulae
DOMAIN_MODULES=11
CALAMUS_RUNTIME_IMPORTS=0
INTENTIONAL_CALAMUS_RUNTIME_STRINGS=1
COMPATIBILITY_HEADER=# Calamus References v1
GTK_IMPORTS=0
THIRD_PARTY_PYTHON_DEPS=0
HIDDEN_XDG_LIBRARY_PATH=NO
TEST_CASES=101
B01_SANDBOX_TEST_RESULT=101/101_PASS
SKIPS=0
B01_SOURCE_VERIFY=PASS
B01_T480=PENDING
```

Hostile defect-repair probes on R1:

```text
B01_SYMLINK_SAVE_STATUS=saved
B01_LIBRARY_PATH_IS_SYMLINK_AFTER=TRUE
B01_TARGET_CHANGED=TRUE
B01_TMP_SYMLINK_SAVE_STATUS=saved
B01_VICTIM_UNCHANGED=TRUE
B01_LEGACY_TMP_SYMLINK_PRESERVED=TRUE
```

R1 remains isolated and unpublished. The canonical Git repository remains at P2.

`NEXT_ACTION = RUN_B01_IMPLEMENTATION_R1_ON_T480`
### 2026-08-19 — B01 R1 packaging harness generation FAIL / repair

During construction of the T480 wrapper, the generator shell command used the same heredoc delimiter for an outer generator block and an inner embedded Python block. The outer heredoc therefore terminated early and the remaining text was interpreted by the shell.

Classification:

```text
PRODUCT_FAIL=NO
B01_SOURCE_MUTATION_FROM_FAILURE=NO
CANONICAL_REPO_MUTATION=NO
HARNESS_PACKAGING_FAIL=YES
ROOT_CAUSE=NESTED_HEREDOC_DELIMITER_COLLISION
```

Repair constraint:

**Generator and embedded runtime heredocs must use distinct delimiters.**

Only the packaging harness generator was rebuilt. The already-qualified B01 product source remained unchanged.

### 2026-08-19 — B01 R1 fresh end-to-end packaging requalification PASS

The repaired wrapper was executed from a fresh ZIP extraction against an isolated two-commit canonical Git repository synchronized with a fresh bare remote. Environment overrides substituted disposable commit/tree/remote identities; no user GitHub state was involved.

```text
B01_PACKAGE_VERIFY=PASS
CANONICAL_B00_P2_AUTHORITY=PASS
B01_SOURCE_VERIFY=PASS
DOMAIN_MODULES=11
PYTHON_NAMESPACE=schedulae
CALAMUS_RUNTIME_IMPORTS=0
INTENTIONAL_CALAMUS_RUNTIME_STRINGS=1
COMPATIBILITY_HEADER=# Calamus References v1
GTK_IMPORTS=0
THIRD_PARTY_PYTHON_DEPS=0
HIDDEN_XDG_LIBRARY_PATH=NO
CANONICAL_DOCUMENTS=3
TOTAL_TESTS=101
B01_TEST_RESULT=101/101_PASS
SKIPS=0
BYTECODE_ARTIFACTS=0
SOURCE_MANIFEST_SHA256=121c6409d81f38ba39a2fc20a1babfd38954293f0636c944155b4835983610fb
CANONICAL_REPO_MUTATION=NO
GIT_COMMIT_PUSH=NO
CANDIDATE=NO
EXIT=0
ERR=NONE
FINAL_PHASE=SCHEDULAE_B01_IMPLEMENTATION_R1_T480_PASS
```

The commit shown by the disposable self-test is not project authority and is intentionally omitted.

R1 is ready for target-hardware qualification. The official canonical repository must remain at P2 commit `daf6da276b44a490793526d278098fba261c5afe`, tree `8666041a2d5dd83166cbe9a87ae844715eb7fc7c`, until a later publication step is separately authorized.

`NEXT_ACTION = RUN_B01_IMPLEMENTATION_R1_ON_T480`

### 2026-08-19 — B01 Implementation R1 T480 PASS

User executed the exact B01 Implementation R1 runner on the Lenovo ThinkPad T480.

Result:

```text
B01_PACKAGE_VERIFY=PASS
B01_SOURCE_VERIFY=PASS
TOTAL_TESTS=101
EXPECTED_TESTS=101
Ran 101 tests in 0.210s
OK
B01_TEST_TOTAL=101
B01_TEST_RESULT=101/101_PASS
SKIPS=0
DOMAIN_MODULES=11
PYTHON_NAMESPACE=schedulae
CALAMUS_RUNTIME_IMPORTS=0
INTENTIONAL_CALAMUS_RUNTIME_STRINGS=1
COMPATIBILITY_HEADER=# Calamus References v1
GTK_IMPORTS=0
THIRD_PARTY_PYTHON_DEPS=0
HIDDEN_XDG_LIBRARY_PATH=NO
CANONICAL_DOCUMENTS=3
BYTECODE_ARTIFACTS=0
SOURCE_MANIFEST_SHA256=121c6409d81f38ba39a2fc20a1babfd38954293f0636c944155b4835983610fb
CANONICAL_HEAD=daf6da276b44a490793526d278098fba261c5afe
CANONICAL_REPO_MUTATION=NO
GIT_COMMIT_PUSH=NO
CANDIDATE=NO
EXIT=0
ERR=NONE
FINAL_PHASE=SCHEDULAE_B01_IMPLEMENTATION_R1_T480_PASS
```

Classification:

```text
B01_STATUS=T480_CERTIFIED_PUBLICATION_READY
PRODUCT_FAIL=NO
ORACLE_FAIL=NO
PACKAGING_FAIL=NO
SOURCE_VERIFY_FAIL=NO
CANONICAL_REPO_MUTATION=NO
PUBLICATION=NO
CANDIDATE=NO
```

Decision:

- B01 R1 is T480 certified.
- The exact source manifest is `121c6409d81f38ba39a2fc20a1babfd38954293f0636c944155b4835983610fb`.
- The canonical repository remains on B00 P2 commit `daf6da276b44a490793526d278098fba261c5afe`.
- B01 is publication ready; commit/push require explicit authorization.
- B02 remains unopened.

Next action:

`NEXT_ACTION = RUN_B01_PUBLICATION_P1_ON_T480`

### 2026-08-19 — B01 Publication P1 explicitly authorized

The user explicitly authorized publication of the already T480-certified B01 R1 tree.

Authority:

```text
PARENT_COMMIT=daf6da276b44a490793526d278098fba261c5afe
PARENT_TREE=8666041a2d5dd83166cbe9a87ae844715eb7fc7c
CERTIFIED_SOURCE_MANIFEST_SHA256=121c6409d81f38ba39a2fc20a1babfd38954293f0636c944155b4835983610fb
TEST_CASES=101
TEST_EXECUTIONS=101
REMOTE=https://github.com/leviagravia/schedulae.git
```

Authorized mutations:

```text
INSTALL_CERTIFIED_B01_TREE=YES
GIT_ADD=YES
COMMIT=YES
PUSH_MAIN=YES
B02=NO
GTK=NO
```

Publication subject:

`B01: establish standalone library identity and safety`

P1 must fail before staging if the canonical parent, remote, source manifest, document cap, license, namespace, dependency boundary, or 101-test gate differs from the frozen authority.

Next action:

`NEXT_ACTION = RUN_B01_PUBLICATION_P1_ON_T480`

### 2026-08-19 — B01 Publication P1 pre-delivery requalification

First disposable publication simulation STOP:

```text
B01_PUBLICATION_P1=FAIL
EXIT=34
ERR=canonical_document_cap
FINAL_PHASE=B01_PUB_DOCUMENT_CAP_FAIL
```

Classification:

```text
PRODUCT_FAIL=NO
PUBLICATION_RUNNER_FAIL=NO
INVALID_SELFTEST_FIXTURE=YES
CAUSE=DISPOSABLE_CANONICAL_REPO_EXPOSED_VIA_SYMLINK
USER_T480_NOT_AFFECTED=YES
```

The document-cap gate intentionally operates on the real canonical root path. The first disposable fixture exposed that repository through a symlink, unlike the real T480 topology `/home/luciano/Projects/schedulae-work`.

No product or publication-runner repair was made.

The simulation was rebuilt with a real directory at the canonical root location. Fresh end-to-end result:

```text
B01_PUBLICATION_P1=PASS
TEST_CASES=101
TEST_EXECUTIONS=101
B01_TEST_RESULT=101/101_PASS
SOURCE_MANIFEST_SHA256=121c6409d81f38ba39a2fc20a1babfd38954293f0636c944155b4835983610fb
COMMIT=CREATED
PUSH_MAIN=PASS
HEAD_EQUALS_ORIGIN_MAIN=YES
HEAD_EQUALS_REMOTE_MAIN=YES
WORKTREE=CLEAN
PYTHON_NAMESPACE=schedulae
GTK_IMPORTS=0
THIRD_PARTY_PYTHON_DEPS=0
HIDDEN_XDG_LIBRARY_PATH=NO
CANONICAL_DOCUMENTS=3
B02=NOT_OPENED
EXIT=0
ERR=NONE
FINAL_PHASE=SCHEDULAE_B01_PUBLICATION_P1_PASS
```

Disposable commit/tree identities are not project authority.

`NEXT_ACTION = RUN_B01_PUBLICATION_P1_ON_T480`
---

## O. INCORPORAZIONE INTEGRALE — DOCUMENTO CANONICO 1

<!-- BEGIN VERBATIM DOC1 -->
# Schedulae — Identità, prodotto e governance

**Documento canonico 1 di 3**  
**Versione:** 1.7  
**Data:** 19 agosto 2026  
**Stato:** AUTHORITATIVE — B00 CLOSED / T480 CERTIFIED / PUBLISHED / DOCUMENTATION FINALIZED / B01 IMPLEMENTATION R1 BUILT / T480 PENDING  
**Regola documentale:** Schedulae ammette al massimo tre documenti canonici di progetto. Questo documento assorbe in futuro tutte le modifiche riguardanti identità, scopo, principi di prodotto, compatibilità, anti-bloat e governance generale. Non creare documenti paralleli.

## 1. Identità del prodotto

**Nome:** Schedulae  
**Pronuncia/forma pubblica:** *Schedulae*  
**Tipo di prodotto:** applicazione desktop bibliografica e citation/reference manager, local-first, orientata a librerie trasparenti su file e a flussi BibTeX/BibLaTeX.  
**Piattaforma iniziale:** Linux, con shell nativa GTK prevista da B02.  
**Origine tecnica:** spin-off indipendente del sottosistema References/BibTeX di Calamus; non è una versione di Calamus con menu rimossi e non deve importare Calamus a runtime.

### 1.1 Definizione pubblica consigliata

> **Schedulae is an independent desktop bibliography and citation manager for organizing scholarly references, bibliographic metadata, notes, and citation data. Schedulae is designed specifically for bibliographic and research-reference workflows; it is not a calendar, appointment, timetable, workforce, or event-scheduling application. Schedulae is not affiliated with or endorsed by any scheduling software or service.**

Per una pagina GitHub/About in italiano:

> **Schedulae è un gestore desktop indipendente di bibliografie, riferimenti e citazioni, progettato per organizzare riferimenti accademici, metadati bibliografici, annotazioni e dati di citazione. È destinato specificamente ai flussi bibliografici e di ricerca; non è un calendario, un’agenda, un sistema di turnazione, un timetable o un software di scheduling. Schedulae non è affiliato né approvato da servizi o prodotti di scheduling.**

Schedulae è software libero/open source sotto **GNU General Public License version 3 or later**, identificatore SPDX **`GPL-3.0-or-later`**. Salvo indicazione esplicita diversa, il codice sorgente Schedulae distribuito dal repository ufficiale è offerto secondo questi termini. La licenza è stata congelata il 19 agosto 2026 dopo verifica della provenance B00; eventuale codice di terzi conserva sempre i propri copyright e termini di licenza.

## 2. Stato del nome e del namespace

Il 19 agosto 2026 è stato eseguito un audit dedicato del nome **Schedulae**. Nelle superfici controllate non è emersa una collisione esatta rilevante come software/app/package; è però presente un nome molto vicino, **Schedula**, utilizzato in altri contesti software. Per questo:

- usare sempre la grafia esatta **Schedulae**;
- evitare ogni linguaggio che suggerisca calendario, turni o scheduling;
- accompagnare il nome con la descrizione bibliografica sopra riportata;
- considerare l'audit di namespace un controllo tecnico/commerciale, **non un parere legale o una clearance di marchio**;
- rifare un controllo corrente immediatamente prima della prima pubblicazione pubblica, perché namespace e registri possono cambiare.

### 2.1 Identità tecnica target

B01 Implementation R1 ha applicato il namespace Python del prodotto in copia isolata; l’autorità pubblicata resta B00 finché B01 non supera il T480 e non viene pubblicato.

```toml
product_name = "Schedulae"
repo_slug = "schedulae"
python_namespace = "schedulae"
future_xdg_namespace = "schedulae"
future_desktop_app_id = "TBD_BEFORE_PACKAGING"
calamus_source_commit = "c316a3aec8c7fba63969a9fa47726809f2d3f43c"
calamus_source_tree = "2b700469f68c626247558d7b5c56eff1c92f8d8c"
b00_core_modules = 11
b00_tests = 74
open_source_intent = true
license = "GPL-3.0-or-later"
```

`future_desktop_app_id` resta volutamente non assegnato finché non viene congelata anche l'autorità di distribuzione/namespace desktop. Non deve essere inventato per comodità.

## 3. Missione

Schedulae deve essere un **lightweight bibliography/BibTeX workbench**: uno strumento affidabile per creare, mantenere, cercare, importare ed esportare una libreria bibliografica locale senza trasformare il lavoro dell'utente in un database opaco o in un servizio cloud.

La promessa centrale è:

**FAST + SIMPLE + SAFE + TRANSPARENT + LOCAL-FIRST**

In termini operativi:

- la libreria rimane leggibile e ispezionabile come file;
- l'autorità bibliografica non è un database nascosto;
- le mutazioni sono atomiche e protette da conflitti/staleness;
- import ed export non cambiano silenziosamente l'autorità canonica;
- le collisioni di identità vengono rese esplicite;
- il programma non richiede account, rete o servizi esterni per il suo core;
- la UI deve essere sottile rispetto al dominio, non il luogo in cui vive la logica bibliografica.

## 4. Posizionamento

Schedulae **non è un clone di Zotero o Mendeley** e non deve inseguirne l'ampiezza funzionale. Il suo spazio è diverso: una libreria bibliografica desktop più piccola, trasparente, deterministica e controllabile.

### 4.1 Utente ideale

- studente, ricercatore, docente, autore accademico;
- utente Markdown/Pandoc/BibTeX/BibLaTeX;
- utente che preferisce file locali e ispezionabili;
- utente che vuole un reference manager senza account, sync obbligatorio, database opaco o gestione documentale pesante;
- utente che attribuisce valore a conflitti esterni rilevati, scritture atomiche e import non distruttivi.

### 4.2 Lavori principali che deve rendere facili

1. creare o aprire una libreria;
2. aggiungere, modificare, duplicare ed eliminare riferimenti;
3. trovare rapidamente un riferimento per qualsiasi campo significativo;
4. mantenere chiavi di citazione stabili e alias coerenti;
5. importare BibTeX/BibLaTeX vedendo prima cosa succederà;
6. risolvere collisioni con azioni esplicite, non con “last wins”;
7. esportare BibTeX/BibLaTeX in modo deterministico;
8. conservare interoperabilità con librerie Calamus References v1;
9. vedere errori o ambiguità senza riparazioni automatiche nascoste.

## 5. Principi permanenti

### 5.1 File authority

La persistenza deve restare **file-based**. La libreria Markdown è l'autorità. Search, filtri, dettaglio, conteggi, integrità e altre viste sono proiezioni ricostruibili.

### 5.2 Local-first

Nessuna funzione core deve dipendere dalla rete. Dati e operazioni fondamentali devono funzionare offline.

### 5.3 Fail-safe

Input malformati, collisioni, file sostituiti, symlink inattesi, destinazioni non regolari, scritture fallite e modifiche esterne devono fallire in modo visibile e non distruttivo.

### 5.4 Persist-first

Una mutazione non diventa stato runtime “vero” prima che la persistenza sia riuscita. Se il salvataggio fallisce, lo stato applicativo non deve fingere che la modifica sia avvenuta.

### 5.5 Compatibilità separata dal branding

Il formato esistente:

```text
# Calamus References v1
```

resta inizialmente un **contratto di interoperabilità**, non un errore di rebranding. Il nome del formato e il nome del prodotto sono due autorità diverse.

### 5.6 UI sottile

La futura UI GTK deve coordinare e presentare il dominio. Non deve duplicare parser, persistence policy, identity logic o collision handling.

## 6. Envelope funzionale v1

### ADOPT / ADAPT

- New Library;
- Open Library;
- reference CRUD: New, Edit, Duplicate, Delete;
- ricerca completa;
- filtri essenziali;
- dettaglio del riferimento;
- BibTeX/BibLaTeX preview/import;
- BibTeX/BibLaTeX deterministic export;
- salvataggio atomico e stale/conflict handling;
- alias e identità di citation key;
- interoperabilità trasparente con Calamus References v1;
- minimal About/Help;
- shell GTK nativa solo dopo B00/B01;
- eventuali azioni semplici legate al file locale del riferimento se rimangono coerenti con il modello lightweight.

### REJECT per v1, salvo nuova evidenza sostanziale

- AI;
- cloud sync e account;
- DOI/Crossref/network lookup come dipendenza core;
- sincronizzazione Zotero/Mendeley;
- gestione di una biblioteca di PDF;
- browser extension;
- citation graph/knowledge graph;
- database come autorità;
- plugin architecture;
- scripting platform;
- editor accademico full-text;
- collaborazione;
- background daemon/indexer;
- condivisione prematura di un package `calamus-research-core`.

### DEFER

- CSL style editor;
- estrazione metadata da PDF;
- duplicate-resolution wizard complesso;
- online lookup;
- bulk repair;
- merge field-by-field avanzato;
- attachment multipli/relative-path policy;
- query language avanzato;
- virtualizzazione per librerie enormi, finché misure reali non la giustificano.

## 7. Anti-bloat gate obbligatorio

Ogni feature nuova da B01 in poi deve ricevere **ADOPT / ADAPT / DEFER / REJECT** rispondendo a queste domande:

1. migliora direttamente il workflow bibliografico o BibTeX/BibLaTeX?
2. preserva un modello mentale semplice e file-based?
3. aggiunge stato persistente oltre libreria trasparente e preferenze minime?
4. aggiunge processi in background, indexing, polling, rete o costo di startup?
5. richiede database o cache nascosta come autorità?
6. duplica inutilmente file manager, editor o funzioni del sistema?
7. espande l'ownership delle mutazioni su più autorità?
8. indebolisce stale detection, conflict safety o atomic write?
9. introduce un layer/framework prima che esista un vero secondo consumer?
10. quale costo aggiunge in test, manutenzione e Help?

Una feature che non supera questo gate non entra nel core per inerzia.

## 8. Menu target minimo

Il menu iniziale desiderato, da implementare solo nella fase GTK appropriata:

### File
- New Library
- Open Library
- Import BibTeX/BibLaTeX
- Export BibTeX/BibLaTeX
- Quit

### Reference
- New
- Edit
- Duplicate
- Delete

### Help
- About

La ricerca/filtraggio appartiene alla vista principale e non richiede necessariamente un altro menu. Toolbar e ulteriori menu sono esclusi finché un lightweight gate non ne dimostra il valore.

## 9. Compatibilità con Calamus

Schedulae nasce da Calamus ma deve essere **un prodotto indipendente**.

Vincoli:

- nessun import runtime dal repository Calamus;
- nessuna copia del `App` Calamus;
- nessuna mutazione del repository canonico Calamus durante lo spin-off;
- il seed B00 resta byte-identico alla sorgente di provenienza;
- in B01 Schedulae deve ottenere il proprio namespace XDG;
- Schedulae non deve prendere silenziosamente possesso del file Calamus preesistente:
  `~/.local/share/calamus/research/references.md`;
- l'utente deve poter aprire esplicitamente librerie arbitrarie, comprese quelle Calamus compatibili;
- la migrazione del namespace è un work item con equivalence test, non una sostituzione testuale.

## 10. Modello di fiducia

Schedulae deve guadagnare fiducia soprattutto tramite proprietà verificabili:

- niente modifica automatica di librerie malformate;
- nessun overwrite implicito della libreria canonica tramite export;
- conflitti esterni rilevati prima della scrittura;
- import source preservato;
- parser e importer non distruttivi;
- collisioni identità esplicite;
- unknown fields preservati quando possibile;
- output deterministico;
- operazioni pericolose senza “last wins” nascosto;
- errori visibili con runner e marker precisi.

## 11. Cosa Schedulae deve evitare di diventare

Schedulae non deve diventare:

- una suite di knowledge management;
- un file/PDF manager;
- un cloud client;
- un servizio online;
- un database bibliografico proprietario;
- un editor di testi;
- un framework condiviso fra più progetti;
- una collezione di feature accessorie che mascheri il nucleo Reference/BibTeX.

Il criterio di maturità non è il numero di funzioni, ma la qualità del workflow essenziale.

## 12. Regole di governance

- I documenti canonici sono **esattamente tre**:
  1. questo documento: identità/prodotto/governance;
  2. `02_SCHEDULAE_TECHNICAL_AUTHORITY_AND_ROADMAP.md`;
  3. `03_SCHEDULAE_MEMORIA_OPERATIVA.md`.
- Non si creano documenti canonici aggiuntivi.
- Le modifiche concettuali vanno integrate nel documento pertinente.
- Gli eventi, risultati, FAIL, PASS, commit, decisioni e next action vanno aggiunti alla MO.
- L'utente mantiene l'autorità su commit e push salvo autorizzazione esplicita diversa.
- Prima di una pubblicazione pubblica rilevante: rifare l'audit namespace. La licenza è congelata a `GPL-3.0-or-later`; il desktop app ID resta da congelare prima del packaging desktop.


## 12.1 Licenza e artefatti legali

Licenza del progetto:

```text
SPDX-License-Identifier: GPL-3.0-or-later
Full name: GNU General Public License v3.0 or later
```

Regole:

- il repository deve contenere alla root il testo integrale e non modificato della GNU GPL v3 in un file `LICENSE`;
- `LICENSE` è un **artefatto legale obbligatorio**, non un quarto documento canonico di progetto e quindi non altera il cap dei tre documenti;
- i tre documenti canonici dichiarano esplicitamente `GPL-3.0-or-later`;
- la provenance B00 verso Calamus resta conservata;
- eventuali copyright/licenze di terzi prevalgono per il materiale a cui si applicano;
- gli header SPDX/copyright per-file vengono aggiunti nel primo work item che modifica il source (B01), evitando di invalidare retroattivamente l'identità byte-for-byte certificata in B00;
- nessun contributor può essere presentato come titolare di diritti che non possiede.

## 13. Stato corrente sintetico

Alla data di questo documento:

- nome prodotto: **Schedulae**;
- concetto: congelato;
- B00 seed: disponibile e verificato;
- core: 11 moduli / 3.259 LOC;
- test ereditati: 74/74 PASS in estrazione isolata;
- GTK nel core: 0;
- dipendenze Python terze nel core: 0;
- repository indipendente Schedulae: `/home/luciano/Projects/schedulae-work`, branch `main`;
- B00: **CLOSED / T480 CERTIFIED / PUBLISHED / DOCUMENTATION FINALIZED**;
- remote GitHub pubblico creato: `https://github.com/leviagravia/schedulae`;
- Git authority corrente: P2 documentation finalizer `daf6da276b44a490793526d278098fba261c5afe`, tree `8666041a2d5dd83166cbe9a87ae844715eb7fc7c`, `HEAD = origin/main = remote main`, worktree CLEAN;
- licenza pubblica: **GNU GPL v3.0 or later (`GPL-3.0-or-later`)**, adottata e verificata sul T480 il 19 agosto 2026;
- root `LICENSE`: installato e verificato;
- source/test B00: byte-identici dopo l'adozione della licenza;
- first publication P1: **PASS** il 19 agosto 2026;
- published commit: `4d71e7f0e868d8229b0e05dd2682acc4d887f535`;
- published tree: `f0a0b49af500c6cefec180af6ec317738ab0919f`;
- `HEAD = origin/main = remote main` al commit pubblicato;
- remote: `https://github.com/leviagravia/schedulae.git`;
- B01 pre-implementation audit: **COMPLETE**; B01 Implementation R1: **BUILT / SANDBOX 101/101 PASS / T480 PENDING**; nessuna mutazione Git B01.

## 13.1 B01 — principi di prodotto congelati dall'audit

L'audit pre-implementazione B01 non amplia il prodotto: riduce ambiguità ereditate da Calamus.

Decisioni di prodotto:

- una libreria Schedulae è **un file scelto esplicitamente**, non un file posseduto automaticamente sotto XDG;
- il domain core non deve avere un default path implicito;
- XDG sarà usato in B02 soltanto per preferenze/app state minimi, non come autorità bibliografica;
- il formato `# Calamus References v1` resta leggibile/scrivibile come formato di interoperabilità; non viene rinominato per branding;
- il namespace Python del prodotto diventa `schedulae`;
- la semantica esclusiva di Calamus (`Current Document`, `Source Notes`, `Reference Sets`, filtri `cited/source-notes/unused`) non appartiene a Schedulae standalone;
- l'integrità bibliografica deve mostrare solo condizioni oggettivamente verificabili, non giudizi soggettivi come “unused”, assenza di tag o assenza di identificatori;
- ogni salvataggio della libreria deve essere safe contro file non regolari e collisioni sul temporary path;
- nessun database, service locator, singleton database, cache authority, background service o rete viene introdotto in B01;
- B01 resta GTK-free.

## 13.2 B01 Implementation R1 — stato pre-T480

Il tree R1 applica il contratto congelato senza ampliare il prodotto:

- package `schedulae/` con 11 moduli di dominio e `__init__.py`;
- nessun modulo/import runtime `calamus_*`;
- `MarkdownReferenceStore(path)` richiede un path esplicito;
- nessuna libreria bibliografica automatica sotto XDG;
- symlink selezionato risolto una volta al target reale, che resta l’autorità di save;
- temp file univoco, same-directory, exclusive e operation-owned;
- token stale ricontrollato immediatamente prima di publish;
- target non regolari rifiutati senza blocco su FIFO/socket;
- mode esistente preservato; nuovo file privato `0600`;
- `Current Document`, `Source Notes`, `Reference Sets` e filtro `use` rimossi;
- integrity solo oggettiva;
- `# Calamus References v1` preservato come unico identificatore Calamus intenzionale nel runtime;
- SPDX `GPL-3.0-or-later` applicato ai source/test migrati;
- zero GTK e zero dipendenze Python terze.

Sandbox qualification: **101/101 PASS**, T480 ancora pending.
<!-- END VERBATIM DOC1 -->

---

## P. INCORPORAZIONE INTEGRALE — DOCUMENTO CANONICO 2

<!-- BEGIN VERBATIM DOC2 -->
# Schedulae — Autorità tecnica, architettura, validazione e roadmap

**Documento canonico 2 di 3**  
**Versione:** 1.7  
**Data:** 19 agosto 2026  
**Stato:** AUTHORITATIVE — B00 CLOSED / T480 CERTIFIED / PUBLISHED / DOCUMENTATION FINALIZED / B01 IMPLEMENTATION R1 BUILT / T480 PENDING  
**Scopo:** raccogliere in un'unica autorità tutto ciò che serve per costruire, verificare e far evolvere Schedulae senza dover ricostruire il contesto da Calamus o da documenti storici separati.

## 1. Source authority

Schedulae parte dall'estrazione esatta del dominio Bibliography/BibTeX di Calamus.

### 1.1 Baseline Calamus

- Calamus functional baseline pubblicata W118:  
  `54456a147f4d65996c73f8a13326fed0e4cc31b7`
- governance publication post-W118:  
  `c316a3aec8c7fba63969a9fa47726809f2d3f43c`
- tree governance:  
  `2b700469f68c626247558d7b5c56eff1c92f8d8c`

Il seed B00 è stato estratto **byte-identicamente** da questa authority.

### 1.2 Handover B00 disponibile

File di origine:

`CALAMUS_BIBLIOGRAPHY_B00_BOOTSTRAP_ONE_UPLOAD_HANDOVER_20260819.zip`

Authority verificata:

- SHA-256 ZIP: `f69cfcd47c30b3c228b1e67e82f80d4cd96582dc4e20224d4e32420ebd556318`
- size: `7,374,773` bytes
- manifest interno: 87 file
- SHA-256 `HANDOVER_MANIFEST.tsv`:  
  `d20397be6ab7534df7c388d1f22130f95ca84a31970d77f67ec6381f409aab3f`

Verifica eseguita il 19 agosto 2026:

```text
B00_HANDOVER_STATIC=PASS
CORE_MODULES=11
CORE_PHYSICAL_LOC=3259
EXPECTED_TESTS=74
MATURE_SOURCE_RAW=2_ARCHIVES_PASS
B00_HANDOVER_VERIFY=PASS
EXIT=0
ERR=NONE
FINAL_PHASE=B00_ONE_UPLOAD_HANDOVER_VERIFY_PASS
```

### 1.3 Il full source di Calamus serve?

**Non per B00.** Il handover contiene tutto ciò che serve per il bootstrap headless esatto: core, test, provenance, contratti, evidence e mature source necessari alla failure policy.

Il repository canonico Calamus dell'utente resta:

`/home/luciano/Projects/calamus-work`

Dovrà essere consultato solo quando una fase successiva richieda materiale non incluso nel seed, per esempio adattamento di view/runtime GTK durante B02/B03. Non va chiesto un nuovo upload del full source per certificare B00.

## 2. B00 exact extraction authority

### 2.1 Numeri congelati

- core modules: **11**
- physical LOC: **3.259**
- local dependency edges: **17**
- max fan-out: **4**
- GTK imports: **0**
- third-party Python dependencies: **0**
- runtime import from Calamus repo: **NO**
- persistent native Markdown authorities nel core: **1**
- directly-owned inherited tests: **74**
- isolated extraction result: **74/74 PASS**
- skips: **0**
- candidate semantics: **NON-CANDIDATE / HEADLESS**

Questi numeri sono evidenza eseguita, non una stima.

## 3. Gli 11 moduli esatti

| # | Modulo B00 | Ruolo |
|---:|---|---|
| 1 | `calamus_bibliography.py` | proiezioni bibliografiche, search text completo, filtri/sort, contesto, duplicate/delete impact, dettaglio, render plain/Markdown |
| 2 | `calamus_bibliography_search.py` | coalescing della ricerca, quiet period 150 ms, generazioni/cancel/dispose |
| 3 | `calamus_bibtex.py` | parser BibTeX/BibLaTeX, mapping, collision model, preview import, decisioni, merge, export deterministico |
| 4 | `calamus_bibtex_controller.py` | ownership di import/export su file, stale checks, policy path/destination, apply/plan |
| 5 | `calamus_bibtex_import_session.py` | stato UI-agnostico delle decisioni di import per entry |
| 6 | `calamus_citations.py` | parsing/formatting citazioni Pandoc, lookup e cited keys |
| 7 | `calamus_reference_controller.py` | controller principale CRUD/search/selection, persist-first mutations, conflict handling |
| 8 | `calamus_reference_store.py` | parser/serializer References v1, diagnostics, identity collisions, stale-aware atomic store |
| 9 | `calamus_references.py` | modello `ReferenceRecord`, tipi, normalizzazione chiavi/alias/tag, suggestion key |
| 10 | `calamus_related_references.py` | related-reference symmetry, integrity, update plan |
| 11 | `calamus_research_file.py` | `FileToken` e atomic UTF-8 replacement |

## 4. Provenance SHA-256 dei moduli core

| Modulo | SHA-256 |
|---|---|
| `calamus_bibliography.py` | `30b8e1a4fb9bf7d9d72a165e1850672dce56e58fe7fa3f296063d05078809819` |
| `calamus_bibliography_search.py` | `e427632ff75b0954c452d89862035f4a71cc995c2b1d194e549d34aff177419e` |
| `calamus_bibtex.py` | `ecf59198dd74670e28c8f06339860d10a94aff2de362d7b32d1e06adf78d2c1c` |
| `calamus_bibtex_controller.py` | `9fe3e3a5ff8a8c11fc7764c904ee437e0f95968498769c0a8c0343b68416a14b` |
| `calamus_bibtex_import_session.py` | `44bc7e51eccd3d60076f4455b81d56023c781d23adf05329ce1631c08fe01beb` |
| `calamus_citations.py` | `fae4445c8accf5a27967fcad226f8c9094bb55575a1156cfba819095d1c4364e` |
| `calamus_reference_controller.py` | `e1e14cdb28690a3536bd5a0a2afdf3f04b20ff3dc4d3f623c4b2f60ceb53a45c` |
| `calamus_reference_store.py` | `a428596d7319b4d442c512acc02f27481ab87a21c1f0186d8160e940b7cdd5a3` |
| `calamus_references.py` | `77f9cc1a4afd75461dc7faabf4a5c9d4c7c5fa3286a0ae7e73f3b2437a9eddb6` |
| `calamus_related_references.py` | `f98a2ee3c1a7dcf63aaf1ff501788ae0ad1ffff3f239879e32af332d7c254c59` |
| `calamus_research_file.py` | `eb14bcc77c5fef82e38ab11963f54d7541f042e3075ea43a0453702dd3637e83` |

L'autorità completa per core e test resta il `B00_SEED/PROVENANCE.tsv` nel handover.

## 5. Data authority e file format

### 5.1 Autorità canonica

L'autorità bibliografica corrente è il file:

`references.md`

con header esatto:

```text
# Calamus References v1
```

In B00 l'header è **immutabile**.

### 5.2 Semantica del formato

Il modello supporta riferimenti tipizzati con:

- citation key primaria;
- alias;
- type;
- authors/editors;
- title;
- date/year e campi di pubblicazione;
- DOI/ISBN/ISSN;
- URL;
- language;
- tags;
- annotation;
- un local file path;
- additional/unknown fields preservati per forward compatibility.

Il serializer mantiene una rappresentazione canonica semantica. Non promette la conservazione byte-for-byte di commenti/layout arbitrari di un file scritto manualmente.

### 5.3 Path legacy Calamus

Il default attuale del core estratto è:

`~/.local/share/calamus/research/references.md`

Questo path rimane intenzionalmente invariato in B00 per provare l'equivalenza. **B01 deve rimuovere l'ownership implicita Calamus** e introdurre un namespace Schedulae e librerie arbitrarie esplicite.

## 6. Identity model

### 6.1 Citation keys

- le key sono normalizzate e validate;
- la suggestion key è leggibile, ASCII e deterministica;
- in collisione viene disambiguata con suffissi prevedibili;
- una key rinominata può essere preservata come alias;
- alias e primary key non possono collidere ambiguamente;
- collisioni cross-record sono blocking;
- un generic edit non può rinominare key/alias senza passare dal boundary appropriato.

### 6.2 Forward compatibility

Un reference type non conosciuto non viene necessariamente distrutto: il modello preserva unknown type/fields quando il contratto lo consente.

## 7. Persistence e conflict safety

`MarkdownReferenceStore` + `calamus_research_file.py` forniscono:

- UTF-8;
- atomic replace;
- file token;
- stale/external-modification detection;
- blocking diagnostics;
- read-only load quando la libreria è malformata;
- nessuna riscrittura automatica al solo load;
- fail-safe su conflitti.

Principio: **persist first, runtime state second**.

Il controller applica una mutazione runtime solo dopo una scrittura valida. Un save fallito non deve lasciare lo stato in memoria divergente dal disco.

## 8. Bibliography projection

`calamus_bibliography.py` non persiste nulla. Costruisce proiezioni derivate.

### 8.1 Ricerca

La ricerca può includere l'intero contenuto significativo del riferimento, non solo title/key:

- campi canonici;
- aliases;
- publication fields;
- local path;
- annotation;
- additional fields.

### 8.2 Filtri/sort storicamente già definiti

Il contratto W97 include combinazioni di:

- Type;
- Tag;
- Use;
- File;
- Integrity;

con sort stabile per:

- author/year;
- title;
- year;
- key;
- type;

e missing values collocati deterministicamente in fondo.

### 8.3 Selection ownership

La selected citation key appartiene al `ReferenceController`, non a un widget GTK o a una row. Questa separazione è fondamentale per evitare drift di selezione durante refresh/filter/render.

## 9. Search coalescing

`CoalescedQueryDispatcher` usa un quiet period di:

**150 ms**

Contratto:

1. una nuova query incrementa la generation;
2. il pending delivery precedente viene cancellato;
3. viene consegnata solo l'ultima query;
4. cancel impedisce delivery stale;
5. dispose è idempotente e impedisce nuovo lavoro;
6. il dispatcher è GTK-free e usa scheduler iniettato.

Questa scelta nasce da un audit W97: non trattare eventi UI differiti come sincroni e non usare un singolo GTK pump come oracle di completamento.

## 10. ReferenceController

Il controller esistente costituisce il boundary principale tra dominio e futura shell.

Responsabilità:

- load / ensure_loaded;
- records / keys / identity keys;
- resolve alias -> canonical key;
- filters/context;
- search refresh;
- selected semantic key;
- add/update/delete;
- reload;
- replace_records;
- commit persist-first;
- conflict reload/overwrite policy.

Il design evita un secondo writer della libreria.

## 11. Related References

Le relazioni fra riferimenti restano trasparenti dentro `references.md`.

Il core supporta:

- estrazione delle related keys;
- deduplicazione;
- canonical field;
- symmetric relation planning;
- add/remove dei due endpoints;
- reject di self/missing/ambiguous identity;
- detection di duplicate/self/missing/alias/asymmetry;
- replacement canonico di identity.

Nessun grafo/database separato è autorizzato.

## 12. Citazioni Pandoc

Il core include parser e formatter per syntax Pandoc:

- singole e grouped citations;
- bare citations supportate dal contratto esistente;
- locator normalizzato;
- lookup vicino/al cursore;
- de-duplicazione in document order;
- fenced code e inline code esclusi dal parsing;
- invalid keys/input types fail closed.

Questa capacità è riutilizzabile, ma Schedulae non deve per questo diventare un editor full-text.

## 13. BibTeX/BibLaTeX parser e mapping

Il parser è deliberatamente conservativo e orientato alla sicurezza.

Supporta:

- BibTeX e BibLaTeX come mode espliciti;
- `@string`/string resolution;
- braces e parenthesis entry delimiters;
- conservative LaTeX -> Unicode decoding;
- person names incluse corporate names;
- keywords;
- preservation/reporting di fields sconosciuti o mode-specific;
- diagnostics per blocchi non-entry, malformed fields e lossiness;
- duplicate input keys/fields senza “last wins” silenzioso.

## 14. Import preview-first

L'import non modifica direttamente la libreria appena letto il file.

Pipeline:

```text
source file
  -> parse
  -> map
  -> inspect collisions
  -> preview
  -> explicit decisions
  -> plan
  -> stale/source/reference checks
  -> atomic apply to references.md
```

Collision classes esistenti:

- `new`
- `same-key-same-content`
- `same-key-different-content`
- `alias-collision`
- `probable-duplicate`
- `duplicate-input-key`

Azioni esistenti:

- import
- skip
- replace
- merge
- new-key

Le collisioni ambigue rimangono unresolved finché l'utente non sceglie un'azione consentita. Le default decisions sono non distruttive.

## 15. Import safety

I test dimostrano già:

- source import preservato;
- stale source blocca apply;
- stale `references.md` blocca apply;
- symlink import/export rifiutati;
- wrong suffix rifiutato;
- source sostituito con symlink dopo preview -> fail closed;
- merge/new-key deterministici;
- una import valida aggiorna solo la libreria canonica.

## 16. Export

L'export è un artefatto derivato.

Contratto:

- output deterministico;
- mode BibTeX/BibLaTeX esplicito;
- non può sostituire la canonical `references.md`;
- atomic write;
- stale/writer failure fail closed;
- existing non-regular destination rifiutata;
- canonical export reimportabile senza perdita di key/title nel contratto provato;
- lossiness di type/date/field collision viene diagnosticata invece di essere nascosta.

## 17. Safe delete e duplicate

### Duplicate

Il duplicate draft:

- propone key non collidente;
- non copia aliases;
- richiede review prima del save.

### Delete

Il modello può costruire un impact summary sui known authorities/context. Storicamente Calamus considerava current-document citations, Source Notes, Related References e Reference Sets. Schedulae standalone non deve affermare di aver scannerizzato tutto il filesystem.

Regola: **nessuna cascata silenziosa**.

## 18. Malformed and hostile files

Il core già stabilisce la direzione:

- libreria malformata -> load diagnostico/read-only;
- duplicate/malformed records -> blocking diagnostics;
- bad input non deve nascondere blocchi successivi validi nel parser Bib;
- invalid inputs fail closed;
- symlink/path replacement race controllata;
- writer failure non deve produrre successo apparente.

B04 estenderà questi principi a large library, lifecycle e desktop certification.

## 19. Test inventory — 74 esatti

| Modulo test | Test |
|---|---:|
| `test_bibtex` | 15 |
| `test_bibtex_controller` | 9 |
| `test_bibtex_import_session` | 6 |
| `test_citations` | 10 |
| `test_reference_alias_store` | 4 |
| `test_reference_controller` | 9 |
| `test_reference_markdown_store` | 6 |
| `test_references` | 4 |
| `test_related_references` | 5 |
| `test_research_file` | 2 |
| `test_w97_bibliography_search_coalescer` | 4 |
| **TOTAL** | **74** |

### 19.1 Categorie provate

**Bib parser/export**
- string resolution;
- duplicate key/field diagnostics;
- malformed field containment;
- LaTeX/name decoding;
- unknown-field preservation;
- collision preview/actions;
- non-destructive defaults;
- reimport of canonical export;
- literal-list fields;
- mode determinism;
- parenthesis/braces safety;
- alternate fields;
- corporate authors/backslashes;
- extended accents;
- lossiness reporting.

**Bib controller**
- real import isolation;
- stale source;
- stale references;
- deterministic merge/new-key;
- atomic derived export;
- writer failure;
- symlink and suffix rejection;
- source-replaced-by-symlink race;
- non-regular destination rejection.

**Import session**
- unresolved ambiguous collisions;
- explicit action unlock;
- disallowed action;
- unknown index;
- local collision summary;
- decisions refused while unresolved.

**Citations**
- formatting;
- invalid key rejection;
- single/grouped/bare parsing;
- Markdown code exclusion;
- lookup;
- document-order dedupe;
- model validation;
- invalid input types.

**Aliases**
- roundtrip/dedupe;
- primary/alias collision;
- alias validity;
- old key preservation.

**Reference controller**
- load/search/selection;
- programmatic select;
- semantic selection ownership;
- persist-first add;
- add/update/delete save;
- protected identity update;
- alias resolution;
- conflict reload;
- conflict overwrite.

**Reference Markdown store**
- XDG default;
- semantic roundtrip;
- malformed/duplicate blocking;
- no rewrite on load;
- atomic save + external change;
- malformed library read-only.

**Reference record**
- normalization/search text;
- invalid key/empty title;
- unknown type preservation;
- deterministic suggested key.

**Related references**
- canonical roundtrip;
- symmetric add/remove;
- reject self/missing/ambiguous;
- integrity detection;
- canonical identity replacement.

**Research file**
- token + atomic write;
- invalid write input.

**Search coalescer**
- latest-only delivery;
- cancel;
- dispose;
- invalid dependency/query fail closed.

## 20. B00 validation contract

Prima di un'esecuzione B00 user-facing dichiarare sempre:

**TOTAL TESTS = 74**

Runner previsto: `TOOLS/RUN_B00_TESTS.py`

Marker attesi:

```text
B00_TEST_TOTAL=74
B00_TEST_RESULT=74/74_PASS
SKIPS=0
EXIT=0
ERR=NONE
FINAL_PHASE=B00_EXACT_EXTRACTION_PASS
```

B00 deve inoltre provare:

- core byte-identico al seed;
- test byte-identici al seed;
- no external Calamus import;
- no GTK;
- no third-party Python imports;
- header References v1 invariato;
- discovery esattamente 74;
- 74/74 PASS.

## 21. Failure policy permanente

Per **QUALSIASI FAIL**:

1. STOP;
2. classificare: product / test-oracle / packaging / lifecycle / authority / environment;
3. ispezionare source maturo diretto pertinente prima della riparazione;
4. confrontare ownership/lifecycle/identity;
5. derivare un repair constraint;
6. riparare minimamente;
7. rieseguire prima il boundary specifico, poi le regressioni ampie.

È vietato il trial-and-error patching prima dell'audit.

## 22. Mature-source authority

Nel handover sono inclusi:

- `MATURE_SOURCE/mousepad-master.zip`
  - SHA-256 `5d82f89421a0c8a29d4f6f5dcfbf450c2d86c104b25ceb6e8863f75ed496f169`
- `MATURE_SOURCE/novelwriter-26.1.tar.gz`
  - SHA-256 `e44192ee8309862f1d16487c8419731ed1439d33f7e1f59cf1de94f04a8cafb2`

Uso:

- repository/build/test/packaging -> novelWriter + Mousepad;
- lifecycle/GTK -> Mousepad;
- bibliography/search/controller -> prima exact B00 seed + evidence W97;
- current namespace collision -> web, perché è informazione temporale.

Le fonti web non sostituiscono il source audit dopo un FAIL.

## 23. Materiale GTK Calamus potenzialmente adattabile in futuro

L'audit di fattibilità ha identificato, nel full Calamus, materiale utile:

- `calamus_reference_panel.py` — 331 LOC
- `calamus_reference_dialogs.py` — 276 LOC
- `calamus_bibtex_import_view.py` — 317 LOC
- `calamus_bibtex_dialogs.py` — 219 LOC
- `calamus_bibtex_runtime.py` — 67 LOC
- `calamus_reference_runtime.py` — 364 LOC
- `calamus_related_reference_dialogs.py` — 170 LOC
- `calamus_modal_dialog.py` — 121 LOC

Questi file **non appartengono al B00 core** e non devono essere copiati in B00. Saranno auditati/adattati solo quando B02/B03 lo richiederanno.

Stima storica del codice realmente nuovo/adattato per una shell GTK indipendente minima: circa **700–1.100 LOC**. È una stima, non un budget vincolante.

## 24. Git e repository rules

Remote pubblico creato il 19 agosto 2026:

`https://github.com/leviagravia/schedulae`

Il remote esiste su GitHub ma, alla closure B00, non è ancora configurato nel repository locale e non è stato eseguito alcun push.


Convenzione proposta dopo bootstrap:

`/home/luciano/Projects/schedulae-work`

branch:

`main`

Regole:

- lettura/verifica/audit/pianificazione: consentiti;
- creazione directory progetto, copy bootstrap tree, `git init`: richiedono autorizzazione B00 esplicita;
- `git add`, commit, remote e push: restano user-controlled o richiedono autorizzazione separata;
- bootstrap authorization non implica push;
- non mutare mai il repo canonico Calamus per creare Schedulae.

## 25. Licensing/provenance

Nel source package Calamus usato per il handover non è stato trovato un root `LICENSE`, `COPYING` o equivalente, né gli 11 moduli B00 espongono header di licenza di terzi.

Il 19 agosto 2026 la licenza Schedulae è stata congelata e successivamente adottata/verificata sul T480 come:

```text
GNU General Public License v3.0 or later
SPDX-License-Identifier: GPL-3.0-or-later
```

Contratto:

- il repository pubblico Schedulae deve contenere alla root il testo integrale non modificato della GNU GPL v3 nel file `LICENSE`;
- la dichiarazione `GPL-3.0-or-later` stabilisce che il codice Schedulae, salvo parti marcate diversamente, è offerto sotto GPL versione 3 oppure, a scelta del destinatario, una versione successiva;
- il file `LICENSE` è un artefatto legale obbligatorio e **non conta come quarto documento canonico**;
- la provenance Calamus del seed B00 resta conservata;
- la scelta di licenza vale soltanto per diritti che il licenziante possiede; eventuale materiale di terzi resta soggetto ai relativi termini;
- gli header SPDX/copyright per-file sono differiti a B01 per non alterare retroattivamente i byte dei 22 file source/test certificati B00;
- prima di introdurre nuovo codice o dipendenze, verificare compatibilità con `GPL-3.0-or-later`.

## 26. Roadmap congelata B00–B04

### B00 — Exact extraction / contract freeze / independent bootstrap

**Stato:** CLOSED / T480 CERTIFIED / PUBLISHED — commit `4d71e7f0e868d8229b0e05dd2682acc4d887f535`, tree `f0a0b49af500c6cefec180af6ec317738ab0919f`; 74/74 PASS, 3 canonical documents, 0 bytecode artifacts; `HEAD = origin/main = remote main`.

Obiettivi:

- nome/namespace target;
- repo locale indipendente;
- 11 core modules byte-identici;
- 74 test byte-identici;
- provenance manifest;
- 74/74 PASS;
- References v1 compatibility;
- anti-bloat budget;
- **no GTK, no rename, no behavior change**.

Closure marker:

`B00_EXACT_EXTRACTION_CONTRACT=PASS`

### B01 — Library identity / path / XDG ownership

- path libreria esplicito;
- new app XDG namespace;
- nessuna ownership silenziosa del file Calamus;
- arbitrary library path;
- hostile stale/external modification;
- branding/namespace migration con behavior-equivalence proof.

### B02 — Minimal native GTK shell / reference workflow

- una main window;
- reference list/search/detail;
- New/Edit/Duplicate/Delete;
- thin GTK;
- niente toolbar salvo gate;
- True GTK;
- startup/responsiveness proof.

### B03 — BibTeX/BibLaTeX workflow

- import preview/review;
- hostile/bounded parser inputs;
- deterministic export;
- file picker ownership/lifecycle;
- canonical library overwrite impossibile attraverso export.

### B04 — Trust/performance/desktop certification

- large library;
- malformed files;
- stale conflicts;
- repeated open/close;
- True App/True GTK;
- lightweight/anti-bloat gate;
- packaging solo dopo stabilizzazione del boundary.

## 27. Candidate semantics future

B00 è headless: **nessun candidate attempt**.

Quando comincia il desktop:

- ogni Candidate T480 richiede autorizzazione esplicita;
- dichiarare il numero esatto di test prima dell'avvio;
- fornire il comando terminale esatto;
- True App/True GTK obbligatori per boundary cambiati;
- hostile/stale/malformed file tests obbligatori;
- manual desktop validation terminal-driven;
- background bianco quando serve una validazione visiva coerente;
- dopo FAIL tornare prima alle fonti mature pertinenti.

## 28. Architectural invariants

Non violare senza un work item esplicito e una nuova prova:

1. una sola authority bibliografica;
2. nessun database authority;
3. nessun runtime import Calamus;
4. no GTK nel domain core;
5. controllers/ports fra dominio e shell;
6. persist-first mutations;
7. stale-aware atomic writes;
8. preview-first import;
9. deterministic derived export;
10. no silent cascade/repair;
11. identity/alias collision detection;
12. unknown-field/unknown-type forward compatibility dove già supportata;
13. selection semantic ownership fuori dai widget;
14. search projection ricostruibile;
15. no shared cross-project core prima di reale necessità.

## 29. Debt intenzionalmente differito a B01+

Non “riparare” durante B00:

- `calamus_*` module/class branding;
- path XDG Calamus;
- diagnostics/docstrings Calamus;
- header `# Calamus References v1`;
- arbitrary library path;
- Schedulae Python namespace;
- Schedulae XDG namespace;
- shell/runtime wiring.

Questi sono debiti **frozen**, non dimenticanze.

## 30. Next technical action

La prima pubblicazione Git B00 licenziata è **PASS** sul T480.

Authority pubblicata:

```text
COMMIT=4d71e7f0e868d8229b0e05dd2682acc4d887f535
TREE=f0a0b49af500c6cefec180af6ec317738ab0919f
HEAD=4d71e7f0e868d8229b0e05dd2682acc4d887f535
ORIGIN_MAIN=4d71e7f0e868d8229b0e05dd2682acc4d887f535
REMOTE_MAIN=4d71e7f0e868d8229b0e05dd2682acc4d887f535
REMOTE_URL=https://github.com/leviagravia/schedulae.git
WORKTREE=CLEAN
```

B00 è quindi **CLOSED / T480 CERTIFIED / PUBLISHED**.

Il prossimo confine di prodotto è B01, ma resta chiuso fino ad autorizzazione esplicita. Prima di aprirlo, è possibile eseguire un P2 strettamente documentale per pubblicare nel repository questa ricevuta finale; tale P2 richiede una nuova autorizzazione perché comporta un secondo commit/push.

## 31. B01 — Pre-implementation direct-source audit

**Audit status:** COMPLETE  
**Implementation status:** NOT OPENED  
**Candidate:** NO — B01 remains headless/GTK-free.  
**Audit method:** exact Schedulae B00 seed + direct mature source; no web substitute.

### 31.1 Mature-source authority verified

The five bibliography comparators supplied for B01 exactly match the historical W97 revisions:

```text
GNOME Citations  SHA-256 2ab04a778ef9dc9c4e681ebb006f25adb71e685f038c6f58af679b1c6263f89c
KBibTeX          SHA-256 f65701b654d0db4b797fcd6ccdca4d244dcc7189ddf894ec409b80d4b11a9ee1
JabRef           SHA-256 aa62a954f5206a3f300d21de68f0a3027a860e15413aed95ae17db6323f99cfb
coBib            SHA-256 1d74456354d6be52abe8dbd10193396159bbb84a0a56fb086f437cc849f867a3
Pandoc           SHA-256 d813fbb68007a697358c515f434ae951ae6d5ee8a4cca66c611acf63bf45083e
```

Also retained from the B00 handover:

```text
Mousepad         SHA-256 5d82f89421a0c8a29d4f6f5dcfbf450c2d86c104b25ceb6e8863f75ed496f169
novelWriter      SHA-256 e44192ee8309862f1d16487c8419731ed1439d33f7e1f59cf1de94f04a8cafb2
```

No further mature source is required before B01 implementation.

### 31.2 Mature-source findings adopted

#### GNOME Citations

Direct source shows:

- the window owns an explicit `gio::File`;
- New/Open choose a concrete bibliography file;
- `open()` loads that file and binds the bibliography to it;
- save writes back to that explicit file;
- list filtering and selection are separate model responsibilities;
- save/open lifecycle is independent from a hidden application-global bibliography path.

**Schedulae constraint:** library identity is explicit-file identity. Do not create an automatic canonical bibliography under XDG.

#### KBibTeX

Direct source shows:

- read-only is a real behavioral state;
- an edit request in read-only mode is reduced to View;
- editor values are validated before `apply()`;
- one invalid field prevents the full apply.

**Schedulae constraint:** malformed/blocked libraries remain operationally read-only; future editors use draft -> validate -> controller commit, never live mutation.

#### JabRef

Direct source `CitationKeyGenerator` consults the complete library database when generating keys and appends deterministic suffixes until the key is unique.

**Schedulae constraint:** keep key generation library-aware and deterministic; primary-key and alias collisions remain blocking and explicit.

#### coBib

Direct source strongly separates commands such as Open/Delete/Export from entry/database objects, which is useful for workflow boundaries. Its `Database` is explicitly a singleton, and its broader plugin/cache/event architecture is not appropriate for Schedulae.

**Schedulae constraint:** adopt command/domain separation where useful; reject singleton database, cache authority and plugin/event expansion.

#### Pandoc

Direct source exposes distinct BibTeX and BibLaTeX reader/writer variants.

**Schedulae constraint:** retain explicit BibTeX vs BibLaTeX mode; never collapse them into one implicit dialect.

### 31.3 Exact B00 standalone seam

The existing constructor already exposes the correct architectural seam:

```python
MarkdownReferenceStore(path=...)
```

The B01 problem is therefore not a new storage architecture. It is:

1. remove implicit Calamus path ownership;
2. make file identity explicit and stable;
3. repair unsafe atomic-write edge cases;
4. migrate the Python namespace;
5. remove Calamus-only semantic projections.

### 31.4 B01 file-safety probes — verified product defects

Two isolated probes were run against the exact B00 seed in temporary directories only.

#### Probe A — canonical library symlink

Setup:

```text
library.md -> target.md
```

B00 load follows the symlink through `os.stat()`/`open()`. On save, `atomic_write_utf8()` writes `library.md.tmp` and then calls:

```python
os.replace(tmp_path, path)
```

Observed:

```text
SYMLINK_SAVE_STATUS=saved
LIBRARY_PATH_IS_SYMLINK_AFTER=False
TARGET_CHANGED=False
LINK_FILE_CHANGED=True
```

The save replaces the **symlink itself** with a new regular file instead of updating the target originally loaded.

Classification:

`VALID PRODUCT FILE-IDENTITY DEFECT`

#### Probe B — fixed temporary path is a symlink

Setup:

```text
safe.md.tmp -> victim.txt
victim.txt = DO_NOT_TOUCH
```

Observed:

```text
TMP_SYMLINK_WRITE=RETURNED_SUCCESS
VICTIM_CONTENT=SAFE DATA
LIB2_EXISTS=True
TMP_EXISTS=False
```

Because B00 uses a predictable `<path>.tmp` and opens it normally, a pre-existing temp symlink is followed and the unrelated target is overwritten before the rename.

Classification:

`VALID PRODUCT GUARDED-SAVE DEFECT`

No user file was involved; both probes ran under an isolated temporary directory.

### 31.5 B01 storage/path contract — FROZEN

B01 must implement the smallest safe standalone boundary:

1. `MarkdownReferenceStore` requires an explicit non-empty path.
2. Remove `default_references_path()` from the domain API.
3. Do not auto-open `~/.local/share/calamus/research/references.md`.
4. Do not replace it with an implicit `~/.local/share/schedulae/...` library.
5. Normalize one explicit selected path once at store construction.
6. If the selected path is a symlink, resolve/freeze its target so later save updates the file that was actually loaded; do not replace the symlink object.
7. Existing canonical targets must be regular files; directory/FIFO/socket/device targets fail visibly instead of being treated as “missing”.
8. Atomic writes must use a **unique same-directory temporary file** created with exclusive semantics (`tempfile.mkstemp` or equivalent), never a predictable `<path>.tmp`.
9. Flush + `fsync()` the temporary file before publish.
10. Preserve existing regular-file mode when replacing an existing library; a new private library may use restrictive creation permissions.
11. Re-check the expected `FileToken` immediately before `os.replace()`; abort and delete the temp file if the library changed during serialization/write.
12. After successful replace, fsync the parent directory on Linux where supported.
13. Cleanup of a failed temporary write must never follow a symlink or remove a path not created by the current operation.
14. Explicit `force=True` remains the only stale-conflict overwrite boundary and must stay user/controller-owned.

This remains a simple file authority; no lock database or hidden journal is introduced.

### 31.6 Residual concurrency policy

A non-cooperating external program can theoretically change a file in the tiny interval after the final token check and before `os.replace()`. B01 must narrow this interval and protect against Schedulae's own temp-path hazards, but it must **not** introduce a database, daemon or complex lock protocol merely to claim impossible filesystem-wide transactional ownership.

A future multi-process Schedulae-specific lock may be considered only if a reproducible same-application race survives B01 hostile tests.

### 31.7 Python namespace migration — FROZEN

Target package:

```text
schedulae/
    __init__.py
    bibliography.py
    bibliography_search.py
    bibtex.py
    bibtex_controller.py
    bibtex_import_session.py
    citations.py
    reference_controller.py
    reference_store.py
    references.py
    related_references.py
    research_file.py
```

Rules:

- remove the product runtime files `core/calamus_*.py`;
- internal imports become `schedulae.*`;
- do not keep `calamus_*` compatibility shim modules;
- tests import only `schedulae.*`;
- rename the historical `test_w97_bibliography_search_coalescer.py` to a product-neutral test filename;
- product/runtime strings and docstrings use Schedulae or neutral wording;
- the literal format header `# Calamus References v1` is explicitly exempt because it is interoperability authority, not product branding;
- preserve 11 domain modules; `schedulae/__init__.py` is package boundary, not a twelfth domain subsystem.

### 31.8 GPL source identity — FROZEN

B01 is the first source-modifying work item. Add:

```python
# SPDX-License-Identifier: GPL-3.0-or-later
```

to maintained Python source/test files touched by the migration. No invented copyright holder line is required.

Root `LICENSE` remains the full license authority.

### 31.9 References v1 compatibility — FROZEN

B01 must continue to read and serialize:

```text
# Calamus References v1
```

There is **no** `# Schedulae References v1` fork in B01.

Required repair:

B00 currently emits the wrong-header diagnostic literally as:

```text
Expected library header: {_HEADER}.
```

B01 must emit the actual compatibility header:

```text
Expected library header: # Calamus References v1.
```

The format identity and product identity remain separate.

### 31.10 Standalone bibliography semantics — FROZEN

The B00 `calamus_bibliography.py` contains projections that depend on Calamus authorities which do not exist in standalone Schedulae:

- `Current Document`;
- `Source Notes`;
- `Reference Sets`;
- filter `cited`;
- filter `source-notes`;
- filter `unused`;
- `BibliographyContext.cited_keys`;
- `source_note_keys`;
- `set_names_by_key`;
- delete-impact counts for those authorities;
- “unused” advisory derived from Calamus context.

They must not survive as fake/empty features.

#### ADOPT

- complete search;
- Type;
- Tag;
- File (`present/missing/unset`);
- stable sorts;
- duplicate-identifier detection;
- Related References;
- detail fields;
- local-file status.

#### ADAPT

- `BibliographyContext` becomes a standalone integrity projection with no current-document/source-note/reference-set ownership;
- delete impact reports only real Schedulae-owned relationships, initially Related References;
- controller refresh/detail receives only standalone data;
- citation parser remains a utility for Pandoc citation strings but does not imply that Schedulae owns or scans an academic document.

#### REMOVE

- Use filter;
- Current Document detail;
- Source Notes detail;
- Reference Sets detail;
- `unused` advisory.

### 31.11 Integrity semantics — objective only

B00 currently marks some records advisory/warning because they lack tags, identifiers, author/year, or are not “used”. Those conditions are not universally bibliographic errors.

B01 integrity must be limited to conditions Schedulae can objectively establish, initially:

- **error:** duplicate normalized DOI/ISBN/ISSN across different records;
- **warning:** a configured local file path is missing;
- **related-reference integrity:** self/missing/ambiguous/asymmetric relations according to the existing Related References model;
- **clean:** no objective issue.

Do not label these conditions as integrity failures merely by policy preference:

- record is not cited;
- no tag;
- no DOI/ISBN/ISSN/URL;
- no author where the reference type may legitimately lack one;
- no year/date where the reference type may legitimately lack one.

### 31.12 Controller contract

Preserve:

- one controller-owned semantic selected citation key;
- persist-first mutations;
- alias -> canonical key resolution;
- collision blocking;
- malformed-library read-only;
- explicit conflict decision: reload / overwrite / cancel;
- no widget-owned data authority.

Change:

- remove external Calamus `set_context()` ownership;
- recompute standalone integrity from the library snapshot;
- error messages say `reference library` / `Schedulae`, not `Calamus`.

### 31.13 BibTeX/BibLaTeX contract in B01

B01 is not a BibTeX feature work item.

Allowed changes:

- namespace/import migration;
- SPDX;
- product-neutral wording;
- behavior-equivalence tests.

Not allowed:

- new parser grammar;
- new mapping policy;
- new merge behavior;
- new export fields;
- implicit BibTeX/BibLaTeX mode.

B03 remains the UI/lifecycle work item for import/export.

### 31.14 Anti-bloat decisions from the audit

**REJECT B01:**

- database authority;
- SQLite;
- singleton library object;
- application-global hidden bibliography;
- plugin/event system;
- network metadata lookup;
- background indexing;
- PDF library/attachment manager;
- lock daemon;
- general filesystem watcher;
- shared Calamus/Schedulae core package.

### 31.15 B01 mandatory validation scenarios

The exact numerical test count will be frozen only after the B01 implementation tree exists. The following scenario classes are mandatory in addition to migrated B00 regression coverage:

#### Namespace/identity
- no `calamus_*` runtime module filenames/imports;
- `schedulae.*` import closure succeeds in isolation;
- no runtime dependency on Calamus repo;
- SPDX present where required;
- only the compatibility header retains intentional Calamus format identity.

#### Explicit library path
- missing/empty path rejected;
- arbitrary absolute path works;
- legacy Calamus path is never opened implicitly;
- no Schedulae XDG bibliography default exists.

#### Compatibility
- Calamus References v1 load;
- semantic roundtrip;
- exact header preserved;
- wrong-header diagnostic repaired;
- malformed file remains read-only.

#### File safety
- symlink-selected library updates the resolved original target without replacing the symlink;
- fixed `.tmp` symlink cannot affect another file;
- unique temp lifecycle;
- directory/FIFO/socket destination fails visibly without blocking;
- external stale change before save blocks;
- mutation during write-before-replace blocks;
- writer failure preserves previous library;
- failed temp cleanup touches only operation-owned temp;
- successful save remains atomic/persist-first.

#### Standalone semantics
- no Use filter;
- no Current Document / Source Notes / Reference Sets detail;
- no `unused` advisory;
- duplicate identifier integrity;
- missing local file warning;
- Related References integrity preserved;
- search/type/tag/file/integrity/sort deterministic;
- semantic selection remains stable across refresh/filter.

#### Regression
- all still-applicable B00 BibTeX/BibLaTeX, citations, aliases, controller, related-reference and search-coalescer behavior remains PASS after namespace migration.

### 31.16 B01 implementation topology

Recommended implementation order:

1. build a B01 isolated working copy from published B00;
2. namespace/package migration only;
3. run migrated regression baseline;
4. explicit-path identity change;
5. guarded atomic-write repair and hostile probes;
6. standalone bibliography semantic cleanup;
7. wrong-header diagnostic + branding/SPDX cleanup;
8. full automated regression;
9. T480 headless certification;
10. only after PASS: publication.

No GTK work is permitted in B01.

### 31.17 B01 audit verdict

```text
B01_DIRECT_SOURCE_AUDIT=PASS
B01_IMPLEMENTATION=NOT_OPENED
MATURE_SOURCE_SUFFICIENT=YES
ADDITIONAL_SOURCE_REQUIRED=NO
VALID_PRODUCT_DEFECTS_FOUND=2
  - CANONICAL_SYMLINK_SAVE_IDENTITY
  - FIXED_TEMP_SYMLINK_OVERWRITE
ARCHITECTURAL_REWRITE_REQUIRED=NO
NEW_DATABASE_REQUIRED=NO
GTK_REQUIRED=NO
NEXT_B01_ACTION=IMPLEMENT_ISOLATED_HEADLESS_TREE_AFTER_AUTHORIZATION
```

## 32. B00 P2 documentation finalizer

P2 is authorized by the user's instruction to close B00 correctly while recording the B01 audit.

P2 is **documentation-only**:

- parent must be exact P1 commit `4d71e7f0e868d8229b0e05dd2682acc4d887f535`;
- parent tree must be `f0a0b49af500c6cefec180af6ec317738ab0919f`;
- only the three canonical Markdown documents may change;
- core/test source must remain byte-identical to B00 provenance;
- 74 tests run before and after the document update: 148 executions;
- no B01 product implementation;
- commit subject: `docs: finalize B00 publication and record B01 audit`;
- after push require `HEAD = origin/main = remote main` and CLEAN worktree.

The P1 commit remains the **B00 product-source authority**. P2 is a later documentation/audit finalizer and does not redefine the certified core tree.

## 33. B00 P2 official closure receipt

```text
P1_PRODUCT_COMMIT=4d71e7f0e868d8229b0e05dd2682acc4d887f535
P1_PRODUCT_TREE=f0a0b49af500c6cefec180af6ec317738ab0919f
P2_DOCUMENTATION_COMMIT=daf6da276b44a490793526d278098fba261c5afe
P2_DOCUMENTATION_TREE=8666041a2d5dd83166cbe9a87ae844715eb7fc7c
HEAD=daf6da276b44a490793526d278098fba261c5afe
ORIGIN_MAIN=daf6da276b44a490793526d278098fba261c5afe
REMOTE_MAIN=daf6da276b44a490793526d278098fba261c5afe
WORKTREE=CLEAN
B00_STATUS=CLOSED_T480_CERTIFIED_PUBLISHED_DOCUMENTATION_FINALIZED
```

P1 remains the B00 product-source authority; P2 is the documentation/audit finalizer.

## 34. B01 Implementation R1 — isolated headless tree

**Status:** BUILT / SANDBOX QUALIFIED / T480 PENDING / NOT GIT-PUBLISHED  
**Candidate:** NO  
**GTK:** NO

### 34.1 Implementation topology

```text
schedulae/
  __init__.py
  bibliography.py
  bibliography_search.py
  bibtex.py
  bibtex_controller.py
  bibtex_import_session.py
  citations.py
  reference_controller.py
  reference_store.py
  references.py
  related_references.py
  research_file.py
```

The historical `core/calamus_*.py` runtime topology is removed in R1. Tests import only `schedulae.*`. The historical `test_w97_bibliography_search_coalescer.py` name becomes product-neutral `test_bibliography_search_coalescer.py`.

### 34.2 Focused mature-source repair audit after the B00 file-safety defects

Before implementing the guarded-save repair, direct source was re-read at the failure boundary:

- **GNOME Citations** keeps an explicit `gio::File` as bibliography ownership and saves through `replace_contents_future(..., make_backup=true, ...)`;
- **KBibTeX** explicitly documents the exact symlink failure mode found in B00 and resolves a selected symlink to its real target before writing, so the user-visible symlink is not replaced;
- KBibTeX also uses unique `QTemporaryFile` objects for temporary output instead of a predictable fixed `<destination>.tmp` path.

Repair constraint confirmed: preserve explicit file identity, resolve/freeze selected symlink target, and use an operation-owned unique temporary file. No database/lock service is justified.

### 34.3 Guarded save R1

`research_file.atomic_write_utf8()` now:

1. rejects existing symlink/non-regular destinations;
2. creates a unique same-directory temp with `tempfile.mkstemp`;
3. tracks temp `(st_dev, st_ino)` so cleanup affects only the operation-owned file;
4. preserves existing file mode or uses `0600` for a new file;
5. writes UTF-8, flushes and `fsync()`s the temp;
6. verifies temp identity;
7. checks destination type and rechecks `expected_token` immediately before publish;
8. publishes with `os.replace()`;
9. fsyncs the parent directory where supported.

`MarkdownReferenceStore` freezes `selected_path` and resolved target `path` at construction. A selected symlink therefore remains a symlink while saves update the target originally opened.

### 34.4 Standalone semantics R1

Removed:

- `BibliographyFilters.use`;
- cited/source-notes/unused projections;
- current-document/source-note/reference-set context;
- corresponding detail fields and delete-impact claims;
- subjective integrity advisory for no tags/identifier/author/year.

Preserved/adapted:

- query/type/tag/file/integrity/sort projection;
- related references;
- duplicate DOI/ISBN/ISSN objective errors;
- missing configured local file warning;
- related-reference error/warning severities;
- persist-first controller and semantic selected key.

### 34.5 Compatibility and identity

```text
PYTHON_NAMESPACE=schedulae
DOMAIN_MODULES=11
CALAMUS_RUNTIME_IMPORTS=0
INTENTIONAL_CALAMUS_RUNTIME_STRINGS=1
COMPATIBILITY_HEADER=# Calamus References v1
GTK_IMPORTS=0
THIRD_PARTY_PYTHON_DEPS=0
HIDDEN_XDG_LIBRARY_PATH=NO
```

The wrong-header diagnostic now expands the actual compatibility header instead of the inherited literal `{_HEADER}` defect.

### 34.6 Sandbox test inventory

B00 had 74 cases. B01 retains the still-applicable regression coverage, replaces the one intentional default-path expectation with explicit-path behavior, and adds focused namespace, guarded-save, standalone-semantics and controller tests.

```text
TEST_CASES=101
SANDBOX_RESULT=101/101_PASS
SKIPS=0
```

New scenario coverage includes:

- selected library symlink remains intact and target changes;
- legacy fixed `.tmp` symlink cannot touch a victim file;
- unique same-dir temp ownership;
- existing mode preservation/new `0600` mode;
- directory/FIFO/socket fail visibly without blocking;
- stale change before save;
- mutation during write-before-replace;
- writer failure preserves previous library and cleans owned temp;
- no default library API/XDG authority;
- package/import/SPDX closure;
- Calamus compatibility-header identity only;
- objective integrity and de-Calamus projections;
- controller-owned context recomputation and selection stability.

### 34.7 R1 verdict before T480

```text
B01_IMPLEMENTATION_R1=BUILT
B01_SANDBOX_TESTS=101/101_PASS
B01_SOURCE_VERIFY=PASS
B01_T480=PENDING
B01_GIT_MUTATION=NO
B01_PUBLICATION=NO
CANDIDATE=NO
```

The next valid action is isolated T480 headless qualification of this exact R1 source. No commit/push is authorized by the implementation step alone.

## 33. B01 Implementation R1 — T480 certification receipt

**Status:** T480 CERTIFIED / PUBLICATION READY  
**Candidate:** NO  
**GTK:** NO  
**Canonical Git mutation:** NO  
**Publication:** NOT YET PERFORMED

The user executed the exact B01 R1 isolated runner on the Lenovo ThinkPad T480.

Canonical repository authority verified before and after the run:

```text
CANONICAL_HEAD=daf6da276b44a490793526d278098fba261c5afe
CANONICAL_REPO_MUTATION=NO
GIT_COMMIT_PUSH=NO
```

Source and topology gates:

```text
B01_PACKAGE_VERIFY=PASS
B01_SOURCE_VERIFY=PASS
DOMAIN_MODULES=11
PYTHON_NAMESPACE=schedulae
CALAMUS_RUNTIME_IMPORTS=0
INTENTIONAL_CALAMUS_RUNTIME_STRINGS=1
COMPATIBILITY_HEADER=# Calamus References v1
GTK_IMPORTS=0
THIRD_PARTY_PYTHON_DEPS=0
HIDDEN_XDG_LIBRARY_PATH=NO
CANONICAL_DOCUMENTS=3
BYTECODE_ARTIFACTS=0
SOURCE_MANIFEST_SHA256=121c6409d81f38ba39a2fc20a1babfd38954293f0636c944155b4835983610fb
```

Exact headless validation:

```text
TOTAL_TESTS=101
EXPECTED_TESTS=101
Ran 101 tests in 0.210s
OK
B01_TEST_TOTAL=101
B01_TEST_RESULT=101/101_PASS
SKIPS=0
EXIT=0
ERR=NONE
FINAL_PHASE=B01_HEADLESS_TESTS_PASS
```

Final runner marker:

```text
B01_IMPLEMENTATION_R1=PASS
B01_TEST_TOTAL=101
B01_TEST_RESULT=101/101_PASS
SKIPS=0
DOMAIN_MODULES=11
PYTHON_NAMESPACE=schedulae
CALAMUS_RUNTIME_IMPORTS=0
INTENTIONAL_CALAMUS_RUNTIME_STRINGS=1
COMPATIBILITY_HEADER=# Calamus References v1
GTK_IMPORTS=0
THIRD_PARTY_PYTHON_DEPS=0
HIDDEN_XDG_LIBRARY_PATH=NO
CANONICAL_DOCUMENTS=3
BYTECODE_ARTIFACTS=0
SOURCE_MANIFEST_SHA256=121c6409d81f38ba39a2fc20a1babfd38954293f0636c944155b4835983610fb
CANONICAL_HEAD=daf6da276b44a490793526d278098fba261c5afe
CANONICAL_REPO_MUTATION=NO
GIT_COMMIT_PUSH=NO
CANDIDATE=NO
EXIT=0
ERR=NONE
FINAL_PHASE=SCHEDULAE_B01_IMPLEMENTATION_R1_T480_PASS
```

Certification decision:

- B01 R1 satisfies the frozen direct-source audit contract on target hardware.
- The two inherited guarded-save defects are covered by the new hostile tests and pass.
- The namespace migration and standalone semantic cleanup are T480 proven.
- The published B00/P2 repository was not modified by qualification.
- B01 is now **publication ready** but is not yet published.
- No B02/GTK work is opened by this certification.

`NEXT_ACTION = B01_PUBLICATION_AUTHORIZATION_PENDING`

## 34. B01 Publication P1 — authorized contract

**Status:** AUTHORIZED / NOT YET RUN ON T480

Exact parent:

```text
PARENT_COMMIT=daf6da276b44a490793526d278098fba261c5afe
PARENT_TREE=8666041a2d5dd83166cbe9a87ae844715eb7fc7c
REMOTE=https://github.com/leviagravia/schedulae.git
```

Exact certified source authority:

```text
SOURCE_MANIFEST_SHA256=121c6409d81f38ba39a2fc20a1babfd38954293f0636c944155b4835983610fb
TEST_CASES=101
TEST_EXECUTIONS=101
```

Publication mutation envelope:

- replace the B00 `core/` runtime with the certified `schedulae/` package;
- replace B00 tests/tools/provenance with the exact B01 certified versions;
- install the three updated canonical documents;
- preserve root `LICENSE` unchanged;
- update `PROJECT_IDENTITY.toml` only with B01 publication metadata;
- no GTK or B02 work;
- run source verification and exactly 101/101 tests in the canonical repository before Git staging;
- stage the complete B01 transition;
- commit subject: `B01: establish standalone library identity and safety`;
- push `main` to `https://github.com/leviagravia/schedulae.git`;
- require `HEAD = origin/main = remote main` and CLEAN worktree;
- publication receipt with the real B01 commit/tree is recorded after P1, because the commit cannot contain its own final SHA.

`NEXT_ACTION = RUN_B01_PUBLICATION_P1_ON_T480`
<!-- END VERBATIM DOC2 -->
