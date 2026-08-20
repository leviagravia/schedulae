# Schedulae — Autorità tecnica, architettura, validazione e roadmap

**Documento canonico 2 di 3**  
**Versione:** 3.3
**Data:** 20 agosto 2026
**Stato:** AUTHORITATIVE — B00/B01 CLOSED / PUBLISHED / DOCUMENTATION FINALIZED — B02 CLOSED / T480 DESKTOP CERTIFIED / PUBLISHED P1 / DOCUMENTATION FINALIZER P2 AUTHORIZED / T480 PENDING — B03 NOT OPENED
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

## 35. B01 Publication P1 — T480 PASS / published authority

```text
PARENT_COMMIT=daf6da276b44a490793526d278098fba261c5afe
B01_COMMIT=0831d9818c7feb67d2943edf4d8591fa12dd2b14
B01_TREE=bc554be161ec84bbfcee8870afe1dc4e905519d0
HEAD=0831d9818c7feb67d2943edf4d8591fa12dd2b14
ORIGIN_MAIN=0831d9818c7feb67d2943edf4d8591fa12dd2b14
REMOTE_MAIN=0831d9818c7feb67d2943edf4d8591fa12dd2b14
REMOTE_URL=https://github.com/leviagravia/schedulae.git
WORKTREE=CLEAN
TEST_CASES=101
TEST_EXECUTIONS=101
B01_TEST_RESULT=101/101_PASS
SOURCE_MANIFEST_SHA256=121c6409d81f38ba39a2fc20a1babfd38954293f0636c944155b4835983610fb
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

B01 R1 is **CLOSED / T480 CERTIFIED / PUBLISHED**. Commit `0831d9818c7feb67d2943edf4d8591fa12dd2b14` is the B01 product-source authority; tree `bc554be161ec84bbfcee8870afe1dc4e905519d0` is the exact published B01 product tree. The P1 commit cannot contain its own final SHA, so this receipt remains external to that commit until an optional documentation-only P2 is explicitly authorized.

`NEXT_ACTION = B01_P2_DOCUMENTATION_FINALIZER_OR_B02_AUDIT_AUTHORIZATION_PENDING`

## 36. B01 P2 documentation finalizer — authorized contract

P2 is a **documentation-only** finalizer.

Exact parent authority:

```text
B01_PRODUCT_COMMIT=0831d9818c7feb67d2943edf4d8591fa12dd2b14
B01_PRODUCT_TREE=bc554be161ec84bbfcee8870afe1dc4e905519d0
SOURCE_MANIFEST_SHA256=121c6409d81f38ba39a2fc20a1babfd38954293f0636c944155b4835983610fb
REMOTE=https://github.com/leviagravia/schedulae.git
```

Mutation envelope:

- only these three files may change:
  - `01_SCHEDULAE_PRODUCT_AND_GOVERNANCE.md`
  - `02_SCHEDULAE_TECHNICAL_AUTHORITY_AND_ROADMAP.md`
  - `03_SCHEDULAE_MEMORIA_OPERATIVA.md`;
- `schedulae/`, `tests/`, `tools/`, `provenance/`, `.gitignore`, `LICENSE`, and `PROJECT_IDENTITY.toml` must remain byte-identical to the published B01 product tree;
- source manifest must still verify;
- exactly 101 tests before and 101 tests after the document update: **202 test executions**;
- commit subject: `docs: finalize B01 publication receipt`;
- push only after the mutation-scope gate passes;
- after push require `HEAD = origin/main = remote main`, CLEAN worktree, and exact parent `0831d9818c7feb67d2943edf4d8591fa12dd2b14`;
- B02 remains unopened.

The B01 product-source authority remains commit `0831d9818c7feb67d2943edf4d8591fa12dd2b14` / tree `bc554be161ec84bbfcee8870afe1dc4e905519d0`. P2 only synchronizes documentation and does not redefine the certified product tree.

`NEXT_ACTION = RUN_B01_P2_DOCUMENTATION_FINALIZER_ON_T480`

## 37. B01 P2 documentation finalizer — T480 PASS / final closure

The user executed the exact B01 P2 documentation finalizer on the Lenovo ThinkPad T480.

```text
TEST_CASES=101
TEST_EXECUTIONS=202
B01_TEST_RESULT=101/101_PASS_X2
B01_PRODUCT_COMMIT=0831d9818c7feb67d2943edf4d8591fa12dd2b14
B01_PRODUCT_TREE=bc554be161ec84bbfcee8870afe1dc4e905519d0
B01_P2_DOCUMENTATION_COMMIT=3e0010a0679e9ba4e541e6fa854186806f83a08a
B01_P2_DOCUMENTATION_TREE=a03cb52013e6acef4233b4c5a5b00995d50ac40f
HEAD=3e0010a0679e9ba4e541e6fa854186806f83a08a
ORIGIN_MAIN=3e0010a0679e9ba4e541e6fa854186806f83a08a
REMOTE_MAIN=3e0010a0679e9ba4e541e6fa854186806f83a08a
WORKTREE=CLEAN
SOURCE_MANIFEST_SHA256=121c6409d81f38ba39a2fc20a1babfd38954293f0636c944155b4835983610fb
NON_DOCUMENT_BYTES_UNCHANGED=YES
CANONICAL_DOCUMENTS=3
B02=NOT_OPENED
B01_STATUS=CLOSED_T480_CERTIFIED_PUBLISHED_DOCUMENTATION_FINALIZED
EXIT=0
ERR=NONE
FINAL_PHASE=SCHEDULAE_B01_P2_DOCUMENTATION_FINALIZER_PASS
```

Authority distinction:

- **B01 product-source authority:** commit `0831d9818c7feb67d2943edf4d8591fa12dd2b14`, tree `bc554be161ec84bbfcee8870afe1dc4e905519d0`;
- **B01 documentation/audit finalizer:** commit `3e0010a0679e9ba4e541e6fa854186806f83a08a`, tree `a03cb52013e6acef4233b4c5a5b00995d50ac40f`.

No P3 is required. A further documentation-only commit would merely recreate the same self-reference cycle without adding product authority.

B01 is fully closed. B02 remains unopened.

`NEXT_ACTION = B02_AUDIT_AUTHORIZATION_PENDING`

## 38. B02 — Pre-implementation native GTK shell audit

**Audit status:** COMPLETE  
**Implementation status:** NOT OPENED  
**Candidate:** NO  
**Git/product mutation:** NO

Baseline authority:

```text
B01_PRODUCT_COMMIT=0831d9818c7feb67d2943edf4d8591fa12dd2b14
B01_PRODUCT_TREE=bc554be161ec84bbfcee8870afe1dc4e905519d0
CURRENT_DOCUMENTATION_HEAD=3e0010a0679e9ba4e541e6fa854186806f83a08a
CURRENT_DOCUMENTATION_TREE=a03cb52013e6acef4233b4c5a5b00995d50ac40f
```

### 38.1 Source authority used

Direct-source audit uses the already-authoritative corpus:

```text
Mousepad         SHA-256 5d82f89421a0c8a29d4f6f5dcfbf450c2d86c104b25ceb6e8863f75ed496f169
GNOME Citations  SHA-256 2ab04a778ef9dc9c4e681ebb006f25adb71e685f038c6f58af679b1c6263f89c
KBibTeX          SHA-256 f65701b654d0db4b797fcd6ccdca4d244dcc7189ddf894ec409b80d4b11a9ee1
JabRef           SHA-256 aa62a954f5206a3f300d21de68f0a3027a860e15413aed95ae17db6323f99cfb
coBib            SHA-256 1d74456354d6be52abe8dbd10193396159bbb84a0a56fb086f437cc849f867a3
Pandoc           SHA-256 d813fbb68007a697358c515f434ae951ae6d5ee8a4cca66c611acf63bf45083e
novelWriter      SHA-256 e44192ee8309862f1d16487c8419731ed1439d33f7e1f59cf1de94f04a8cafb2
```

Also re-read: the direct Calamus W97 bibliography lifecycle evidence and the historical reference-dialog source boundary.

No additional mature source is required before B02 implementation.

### 38.2 Exact B01 seam

B01 already has the correct non-GTK ownership split:

- `MarkdownReferenceStore(path)` owns one explicit library file;
- `ReferenceController` owns records, filters, semantic selected key and persist-first mutations;
- `ReferenceView` is a narrow protocol;
- `CoalescedQueryDispatcher` already owns latest-only search delivery;
- `format_reference_detail()` derives read-only detail;
- `duplicate_reference()` produces a safe duplicate draft;
- `build_delete_impact()` reports Schedulae-owned Related References only.

B02 therefore requires a shell adapter, not a domain rewrite.

### 38.3 GTK stack — FROZEN

```text
GTK_MAJOR=3
PYTHON_BINDING=PyGObject
GTK_SOURCEVIEW=NO
LIBADWAITA=NO
ELECTRON=NO
THIRD_PARTY_PYTHON_GUI_FRAMEWORK=NO
```

Rationale:

- Mousepad provides a mature native GTK3 lifecycle comparator;
- Schedulae needs only standard widgets;
- GTK4/libadwaita would add a migration/dependency surface without solving a B02 product need;
- B01 domain modules must remain importable and testable without GTK.

### 38.4 Application/window lifecycle — FROZEN

B02 uses:

- one `Gtk.Application`;
- application id target: `io.github.leviagravia.Schedulae`;
- one `Gtk.ApplicationWindow`;
- `activate()` presents the existing window instead of constructing duplicates;
- Open/New Library bind one explicit library path into the active window;
- dialogs are transient/modal to that window;
- closing the window disposes pending search sources and releases the controller/view composition.

B02 explicitly rejects:

- server/daemon ownership;
- multi-window/multi-library framework;
- automatic reopening of a last library;
- hidden Recent-file authority;
- background services.

### 38.5 Library lifecycle — FROZEN

#### Open Library

- native GTK file chooser selects the path;
- shell constructs `MarkdownReferenceStore(path)` and `ReferenceController`;
- existing valid library opens read/write;
- malformed library opens diagnostic/read-only;
- file identity remains B01 domain authority.

#### New Library

A truthful New Library must create the canonical empty file immediately rather than merely remember a missing path until first record save.

B02 may add one tiny GTK-free creation boundary using the existing serializer/atomic-write rules, for example:

```python
create_empty_reference_library(path)
```

or an equivalent store method.

Rules:

- explicit chosen path only;
- canonical `# Calamus References v1` header;
- refuse silent overwrite of an existing file;
- same guarded-write safety as B01;
- no second library format.

### 38.6 Main-window information architecture — FROZEN

Minimal layout:

```text
File / Reference / Help
SearchEntry + compact Filter control

+----------------------+---------------------------+
| Reference list       | Read-only detail          |
| model-backed         | selected citation key     |
|                      | bibliographic fields      |
+----------------------+---------------------------+
| compact status / diagnostics                     |
+--------------------------------------------------+
```

No toolbar.

Menus in B02:

```text
File
  New Library…
  Open Library…
  Quit

Reference
  New…
  Edit…
  Duplicate…
  Delete…

Help
  About
```

BibTeX/BibLaTeX Import/Export remain B03.

### 38.7 List/model/selection lifecycle — FROZEN

Use a persistent GTK3 model boundary:

- `Gtk.ListStore`;
- `Gtk.TreeView`;
- one persistent `Gtk.TreeSelection`;
- hidden canonical citation key column;
- visible compact bibliographic summary columns.

The semantic selected key remains in `ReferenceController`.

Render transaction:

1. block the application selection callback;
2. update/replace model rows as one transaction;
3. restore selection by canonical key if still visible;
4. unblock;
5. refresh detail once after the model is stable.

Forbidden during render/filter refresh:

- widget row identity as semantic authority;
- `scroll_to_cell()` as part of correctness;
- automatic `grab_focus()`;
- `Gtk.events_pending()` / manual event-loop pumping;
- callbacks into the controller while the model is only partially rebuilt;
- destruction/recreation of selected row widgets as the normal filter mechanism.

### 38.8 Search/filter — FROZEN

Search:

- `Gtk.SearchEntry`;
- existing `CoalescedQueryDispatcher`;
- existing 150 ms default quiet period;
- GLib timeout scheduling injected only at the GTK adapter;
- pending source removed on replacement/dispose;
- only the latest generation reaches `controller.set_query()`.

Filter control:

One compact popover/menu next to Search may expose the already-existing B01 projections:

- Type;
- Tag;
- File (`all/present/missing/unset`);
- Integrity;
- Sort.

This is not a toolbar and introduces no new domain filtering logic.

### 38.9 Detail — FROZEN

- read-only;
- derived from the selected canonical key and `format_reference_detail()`;
- selectable/copyable text is acceptable;
- never becomes mutation authority;
- empty selection has an explicit empty state.

### 38.10 New/Edit dialog — FROZEN

One dialog family creates an immutable `ReferenceRecord` draft.

New:

- editable key;
- Suggest action;
- full validation before apply.

Edit:

- primary key is read-only;
- Suggest disabled;
- aliases preserved;
- unknown `extra_fields` preserved;
- changing fields does not mutate live records.

Validation:

- construct/validate complete draft;
- any invalid field blocks the whole apply;
- only after a valid result does the shell call the controller.

No autosave and no live model mutation while the dialog is open.

### 38.11 Duplicate — FROZEN

Workflow:

```text
selected record
  -> duplicate_reference(...)
  -> non-colliding draft key
  -> aliases cleared
  -> review in New-like dialog
  -> valid OK
  -> controller.add()
```

Cancel produces zero persistent mutation.

### 38.12 Delete — FROZEN

- confirmation always;
- use `build_delete_impact()` before delete;
- show Related References impact when present;
- no silent cascade;
- if deletion leaves another record with a missing relation, objective integrity reports it;
- read-only/malformed library disables Delete.

### 38.13 Read-only and action sensitivity — FROZEN

Mutation actions New/Edit/Duplicate/Delete are disabled when:

- no library is open where appropriate;
- library is malformed/read-only;
- Edit/Duplicate/Delete have no valid selection.

Open/New Library and About remain available independently.

### 38.14 Conflict/error UX — FROZEN

The controller's conflict contract remains:

```text
Reload / Overwrite / Cancel
```

GTK only presents the choice.

- Overwrite must be explicit;
- no silent retry;
- diagnostics are user-visible;
- malformed load remains read-only rather than being silently rewritten.

### 38.15 Modal lifecycle — FROZEN

Every B02 modal:

- has `transient_for` main window;
- is modal;
- returns a typed/semantic result;
- copies the result before destruction;
- hides before destroy where the helper controls both;
- leaves no GLib source owned by the dialog;
- does not manually pump the GTK event loop.

Real-GTK automated validation uses one named modal workflow per fresh subprocess. Full native-dialog chains remain part of manual desktop validation rather than one monolithic nested-loop test.

### 38.16 Thin-shell topology — target

Expected production shell modules:

```text
schedulae/gtk_app.py
schedulae/gtk_window.py
schedulae/gtk_reference_view.py
schedulae/gtk_dialogs.py
schedulae/gtk_modal.py        # only if needed to centralize lifecycle
schedulae/__main__.py
```

This is a target topology, not an obligation to create an unnecessary module.

Rules:

- 11 B01 domain modules stay GTK-free;
- GTK imports occur only in shell modules;
- no service locator;
- no event bus;
- no database;
- no duplicate bibliography model.

Historical feasibility estimated roughly 700–1,100 production GTK LOC. This remains a comparison signal, not a hard LOC quota; substantial excess requires a scope/bloat audit before Candidate.

### 38.17 Validation topology — FROZEN scenario classes

The exact numerical test count is frozen only after implementation exists.

Mandatory classes:

#### Layer A — B01 domain regression
- all 101 B01 tests remain PASS.

#### Layer B — shell contract/headless adapter tests
- controller remains selection owner;
- model render transaction suppresses semantic callbacks during rebuild;
- stable selection restoration;
- query coalescer scheduled/cancelled/disposed correctly;
- action sensitivity;
- draft validation and cancel/no-mutation;
- duplicate review semantics;
- delete-impact presentation contract;
- read-only action gating.

#### Layer C — real GTK component lanes, fresh subprocess
- application/window construct-show-destroy;
- ListStore/TreeView/TreeSelection render/selection;
- search/filter transitions;
- New dialog;
- Edit dialog;
- Duplicate dialog;
- Delete confirmation;
- conflict dialog;
- malformed/read-only presentation.

Each lane runs with fatal GTK criticals enabled where practical.

#### Layer D — True Application lane
- real `Gtk.Application`;
- disposable explicit library;
- map main window;
- load records;
- select key -> detail;
- repeated search/filter transitions;
- mutation workflow through controller;
- clean quit;
- no surviving GLib source;
- no GTK critical.

#### Layer E — startup/responsiveness probe
Before fixing hard thresholds, obtain T480 non-candidate baseline measurements:

- process start -> first mapped usable window, repeated fresh processes;
- moderate reference library projection/search;
- search coalescing delivery count;
- no synchronous viewport/focus work in render.

Candidate thresholds are derived from measured T480 evidence, not guessed in the audit.

#### Layer F — manual desktop
At minimum:

- New Library;
- Open Library;
- search + each compact filter class;
- selection/detail;
- New;
- Edit with immutable citation key;
- Duplicate review/cancel/save;
- Delete confirmation/impact;
- malformed library read-only;
- stale conflict Reload/Overwrite/Cancel;
- About/Quit;
- visual check under light/system theme as applicable.

### 38.18 B02 anti-bloat matrix

**ADOPT**

- native GTK application/window lifecycle;
- explicit file ownership;
- persistent list model + separate selection;
- controller-owned semantic key;
- search coalescing;
- draft/validate/commit;
- action sensitivity;
- native modal ownership.

**ADAPT**

- GNOME Citations list/filter/detail architecture to GTK3;
- KBibTeX validation/read-only discipline to immutable Python drafts;
- Calamus W97 lifecycle lessons without copying its destructive row-rebuild mechanism;
- Calamus reference dialog field coverage without Calamus-only workflow semantics.

**REJECT B02**

- toolbar;
- multi-window;
- tabs;
- database;
- plugin system;
- network metadata lookup;
- PDF viewer/manager;
- file watcher/background indexer;
- automatic last-library reopen;
- BibTeX import/export UI;
- GTK4/libadwaita migration;
- custom model framework where `Gtk.ListStore` suffices.

**DEFER**

- import/export UI -> B03;
- large-library hard certification -> B04;
- desktop packaging/icons/installer polish -> B04;
- Recent Files unless separately justified by later evidence.

### 38.19 Audit verdict

```text
B02_DIRECT_SOURCE_AUDIT=PASS
B02_IMPLEMENTATION=NOT_OPENED
B02_CANDIDATE=NO
PRODUCT_SOURCE_MUTATION=NO
GIT_MUTATION=NO
MATURE_SOURCE_SUFFICIENT=YES
ADDITIONAL_SOURCE_REQUIRED=NO
GTK_STACK=GTK3_PYGOBJECT
WINDOW_MODEL=SINGLE_APPLICATION_SINGLE_WINDOW
DOMAIN_GTK_IMPORTS=0
LIST_MODEL=GTK_LISTSTORE_TREEVIEW
SEMANTIC_SELECTION_OWNER=REFERENCE_CONTROLLER
SEARCH_COALESCER_MS=150
TOOLBAR=NO
IMPORT_EXPORT_UI=B03
PACKAGING=B04
NEXT_ACTION=B02_IMPLEMENTATION_AUTHORIZATION_PENDING
```
## 39. B02 Implementation R1 — isolated build / pre-T480 qualification

**Implementation:** BUILT  
**Candidate:** NO  
**Canonical Git mutation:** NO  
**Real-GTK target qualification:** PENDING T480

Baseline authority:

```text
B01_PRODUCT_COMMIT=0831d9818c7feb67d2943edf4d8591fa12dd2b14
B01_PRODUCT_TREE=bc554be161ec84bbfcee8870afe1dc4e905519d0
CANONICAL_HEAD=3e0010a0679e9ba4e541e6fa854186806f83a08a
CANONICAL_TREE=a03cb52013e6acef4233b4c5a5b00995d50ac40f
```

### 39.1 Implemented production delta

Five thin shell files were added:

```text
schedulae/gtk_app.py
schedulae/gtk_window.py
schedulae/gtk_reference_view.py
schedulae/gtk_dialogs.py
schedulae/__main__.py
```

GTK shell physical LOC: **1,045**. This is inside the audit feasibility signal (~700–1,100 LOC) and does not create a new domain subsystem.

Two narrow GTK-free additions were made:

- `create_empty_reference_library(path)` creates a canonical empty `# Calamus References v1` file immediately, refuses any pre-existing filesystem object, and uses the B01 guarded atomic writer;
- `ReferenceController.read_only` / `diagnostics` expose already-owned load state, and the optional `set_context()` view seam lets the GTK projection render objective integrity without owning it.

### 39.2 Shell behavior implemented

- GTK3 + PyGObject only;
- application id `io.github.leviagravia.Schedulae`;
- one `Gtk.Application` + one `Gtk.ApplicationWindow`;
- explicit New/Open Library only;
- File / Reference / Help menu;
- SearchEntry + compact filter popover;
- persistent `Gtk.ListStore` + `Gtk.TreeView` + `Gtk.TreeSelection`;
- semantic key stays in `ReferenceController`;
- read-only detail pane;
- New/Edit validated immutable draft dialog;
- immutable key on Edit;
- Duplicate -> generated non-colliding draft -> mandatory review;
- Delete confirmation + Related References impact, no silent cascade;
- conflict Reload / Overwrite / Cancel;
- malformed library visible/read-only;
- no toolbar, no Import/Export UI, no database, no network, no background indexer.

### 39.3 First regression gate FAIL — stale B01 oracle

Initial Layer-A run:

```text
B01_TEST_RESULT=100/101_NOT_FULL_PASS
FAIL=test_b01_identity.B01IdentityTests.test_package_contains_eleven_domain_modules_and_no_calamus_runtime_module
OBSERVED_PACKAGE_PY_MODULES=16
EXPECTED_BY_STALE_ORACLE=11
```

Classification:

```text
PRODUCT_FAIL=NO
ORACLE_FAIL=YES
CAUSE=B01_TEST_COUNTED_ALL_PACKAGE_PY_FILES_AS_DOMAIN_MODULES
```

Before repair, failure-specific re-audit returned to the frozen B02 topology and mature Mousepad source. B02 explicitly requires 11 B01 domain modules **plus** shell modules; Mousepad likewise separates `MousepadApplication` (`GTK_TYPE_APPLICATION`) and `MousepadWindow` (`GTK_TYPE_APPLICATION_WINDOW`).

Minimal oracle repair: the B01 identity test now names the exact 11 domain modules and separately continues to forbid any `calamus_*` runtime file. It does not forbid the B02 shell modules mandated by the audit.

Post-repair Layer A:

```text
B01_TEST_RESULT=101/101_PASS
```

### 39.4 Source verifier tooling FAIL

A later static source gate initially failed because its handwritten stdlib allowlist omitted Python's `importlib`, used by one B02 headless test.

```text
PRODUCT_FAIL=NO
SOURCE_FAIL=NO
TOOLING_VERIFIER_FAIL=YES
CAUSE=INCOMPLETE_STDLIB_ALLOWLIST
```

Repair was verifier-only: use `sys.stdlib_module_names` as Python stdlib authority, plus explicit `schedulae` and `gi` allowances.

Final source gate:

```text
B02_SOURCE_VERIFY=PASS
DOMAIN_MODULES=11
SHELL_MODULES=5
DOMAIN_GTK_IMPORTS=0
SHELL_GTK_STACK=GTK3_PYGOBJECT
INTENTIONAL_CALAMUS_RUNTIME_STRINGS=1
APPLICATION_ID=io.github.leviagravia.Schedulae
THIRD_PARTY_RUNTIME_DEPS=PyGObject_ONLY
TOOLBAR=NO
IMPORT_EXPORT_UI=NO
```

### 39.5 Frozen headless count

```text
TOTAL_HEADLESS_TESTS=130
B01_REGRESSION_TESTS=101
B02_NEW_HEADLESS_TESTS=29
B02_HEADLESS_TEST_RESULT=130/130_PASS
SKIPS=0
```

Source manifest:

```text
SOURCE_MANIFEST_SHA256=f7eee624e0d646e7033dfbeb82893c196ddcb6ded45000c041e991099811f6d6
```

### 39.6 Real-GTK topology prepared for T480

Ten fresh-process lanes:

1. view-selection;
2. window-shell;
3. library-open;
4. search-filter;
5. new-dialog;
6. edit-duplicate-dialog;
7. delete-dialog;
8. conflict-dialog;
9. malformed-read-only;
10. true-application.

Each lane is executed in a separate Python process with `G_DEBUG=fatal-criticals`.

### 39.7 Non-candidate performance probe prepared

Before any candidate threshold is frozen, T480 measures:

- 5 fresh-process start -> first mapped window samples;
- 1,000-record projection time;
- 1,000-record search projection time.

No performance threshold is imposed in R1; measurements are evidence for the later Candidate gate.

### 39.8 Build-environment limitation

The construction container has no `gi` / PyGObject GTK3 runtime. Therefore:

- source syntax/static gates: PASS;
- headless behavior: 130/130 PASS;
- real-GTK execution: **not claimed locally**;
- T480 real-GTK qualification is mandatory before R1 can be called T480-proven.

### 39.9 R1 pre-T480 verdict

```text
B02_IMPLEMENTATION_R1=BUILT
B02_SOURCE_VERIFY=PASS
B02_HEADLESS_TEST_RESULT=130/130_PASS
B02_REAL_GTK=PENDING_T480
B02_PERF_PROBE=PENDING_T480
CANONICAL_REPO_MUTATION=NO
GIT_COMMIT_PUSH=NO
CANDIDATE=NO
NEXT_ACTION=B02_R1_T480_NONCANDIDATE_QUALIFICATION
```
## 40. B02 R1 T480 real-GTK FAIL and failure-specific mature-source audit

R1 T480 evidence:

```text
B02_HEADLESS_TEST_RESULT=130/130_PASS
GTK TEST 1/10 view-selection=PASS
GTK TEST 2/10 window-shell=PASS
GTK TEST 3/10 library-open=PASS
GTK TEST 4/10 search-filter=FAIL
ERR=AssertionError:delivery_count=0
FINAL_PHASE=B02_REAL_GTK_FAIL
```

Classification:

```text
B02_R1=RETIRED_NOT_QUALIFIED
VALID_GTK_ADAPTER_PRODUCT_DEFECT=YES
TIMING_ORACLE_DESIGN_DEFECT=YES
COALESCER_DOMAIN_DEFECT=NO
CONTROLLER_DEFECT=NO
LIST_MODEL_DEFECT=NO_EVIDENCE
ENVIRONMENT_DEFECT=NO_EVIDENCE
CANDIDATE=NO
CANDIDATE_ATTEMPTS=0
```

### 40.1 Comparative direct-source result

The failure-specific audit returned to mature source before repair.

- **Calamus W97 final contract:** `Gtk.SearchEntry.changed` -> one explicit 150 ms `CoalescedQueryDispatcher`; the earlier `search-changed` pattern had already been rejected after delayed-delivery failures.
- **GNOME Citations:** `GtkSearchEntry` uses immediate `changed`; no second debounce owner.
- **Mousepad GTK3:** entry text uses immediate `changed`; no second debounce owner.
- **KBibTeX:** immediate `textChanged` -> one owned single-shot timer.
- **JabRef:** immediate text property change -> one owned restartable timer.

Convergent rule: **one timing owner only**. When Schedulae wants a 150 ms coalescer, `Gtk.SearchEntry` must feed it from `changed`, not from the already-delayed `search-changed` signal.

### 40.2 R1 oracle defect

R1 checked correctness at one fixed time (`GLib.timeout_add(260, check)`). That oracle is retired. Increasing 260 ms is explicitly forbidden as trial-and-error. The correct oracle is bounded semantic completion: latest query delivered exactly once, dispatcher no longer pending, controller query equals `alpha`, and projection equals the expected row count.

## 41. B02 Implementation R2 — evidence-based repair build

**Implementation:** BUILT / ISOLATED
**Candidate:** NO
**Canonical Git mutation:** NO
**T480 real-GTK qualification:** PENDING

Baseline remains:

```text
CANONICAL_HEAD=3e0010a0679e9ba4e541e6fa854186806f83a08a
CANONICAL_TREE=a03cb52013e6acef4233b4c5a5b00995d50ac40f
```

### 41.1 Production delta from R1

Exactly one production behavior change:

```python
self.search_entry.connect("changed", self._on_search_changed)
```

No changes to:

- `CoalescedQueryDispatcher`;
- `DEFAULT_BIBLIOGRAPHY_SEARCH_DELAY_MS = 150`;
- `ReferenceController`;
- bibliography filtering semantics;
- list/selection model;
- dialog workflows.

### 41.2 Oracle/gate repair

The real-GTK `search-filter` lane now polls boundedly (1.5 s safety ceiling, 10 ms polling cadence) for semantic completion and fails immediately if `delivery_count > 1`. Completion requires:

```text
delivery_count == 1
pending == false
last_delivered_query == "alpha"
controller.filters.query == "alpha"
visible_rows == 1
```

A new headless/source contract requires the exact `changed` binding and forbids `search-changed`. The source verifier also rejects the retired fixed-time `GLib.timeout_add(260, check)` oracle.

### 41.3 Frozen R2 counts

```text
B01_REGRESSION_TESTS=101
B02_NEW_HEADLESS_TESTS=30
HEADLESS_TEST_CASES=131
FOCUSED_REPAIR_GTK_LANES=1
FULL_REAL_GTK_LANES=10
TOTAL_VALIDATION_EXECUTIONS=142
STARTUP_SAMPLES=5
```

The focused `search-filter` lane is intentionally executed twice in a successful T480 qualification: first by itself as the failure-specific repair gate, then again inside the full 10-lane regression matrix.

### 41.4 Local non-GTK qualification

```text
B02_SOURCE_VERIFY=PASS
B02_HEADLESS_TEST_RESULT=131/131_PASS
SKIPS=0
SOURCE_MANIFEST_SHA256=bd6f934e4b9d2cb91c1539eb8a273e9315bdbc3d6e91168074bb6274eedae018
```

The build environment still lacks PyGObject/GTK3, so no local real-GTK PASS is claimed.

A verifier integration typo (`root` instead of `ROOT`) was caught before package delivery, classified tooling-only, and repaired without product change.

### 41.5 T480 execution order — binding

1. package/canonical/source identity;
2. GTK3 runtime;
3. **focused `search-filter` lane only**;
4. only after focused PASS: 131/131 headless;
5. full 10/10 real-GTK fresh-process matrix;
6. measurement-only performance/startup probe;
7. canonical Git postcheck.

```text
NEXT_ACTION=B02_R2_T480_NONCANDIDATE_QUALIFICATION
```

## 41. B02 R2 — T480 non-candidate qualification PASS

Exact B01 canonical repository authority remained unchanged:

```text
CANONICAL_HEAD=3e0010a0679e9ba4e541e6fa854186806f83a08a
CANONICAL_TREE=a03cb52013e6acef4233b4c5a5b00995d50ac40f
CANONICAL_REPO_MUTATION=NO
GIT_COMMIT_PUSH=NO
```

R2 source authority:

```text
SOURCE_MANIFEST_SHA256=bd6f934e4b9d2cb91c1539eb8a273e9315bdbc3d6e91168074bb6274eedae018
DOMAIN_MODULES=11
SHELL_MODULES=5
APPLICATION_ID=io.github.leviagravia.Schedulae
GTK_STACK=GTK3_PYGOBJECT
TOOLBAR=NO
IMPORT_EXPORT_UI=NO
```

Validation:

```text
FOCUSED_REPAIR_GTK_LANES=1
B02_R2_FOCUSED_BOUNDARY_RESULT=1/1_PASS

HEADLESS_TEST_CASES=131
B01_REGRESSION_TESTS=101
B02_NEW_HEADLESS_TESTS=30
B02_HEADLESS_TEST_RESULT=131/131_PASS

B02_REAL_GTK_LANES=10
B02_REAL_GTK_RESULT=10/10_PASS

STARTUP_SAMPLES=5
STARTUP_FIRST_MAPPED_MIN_MS=198.645
STARTUP_FIRST_MAPPED_MEDIAN_MS=210.746
STARTUP_FIRST_MAPPED_MAX_MS=222.084
PROJECTION_1000_MS=53.678
SEARCH_1000_MS=2.459
THRESHOLD_GATE=NOT_FROZEN_NONCANDIDATE_MEASUREMENT_ONLY
B02_PERF_PROBE=PASS

BYTECODE_ARTIFACTS=0
CANDIDATE=NO
EXIT=0
ERR=NONE
FINAL_PHASE=SCHEDULAE_B02_IMPLEMENTATION_R2_T480_PASS
```

### 41.1 Qualification decision

```text
B02_R1=RETIRED
B02_R2=T480_PROVEN_NONCANDIDATE
PRODUCT_FAIL=NO
REAL_GTK_FAIL=NO
PERF_PROBE_FAIL=NO
CANONICAL_REPO_MUTATION=NO
CANDIDATE_ATTEMPTS_USED=0
PUBLICATION=NO
MANUAL_DESKTOP_VALIDATION=NOT_RUN
```

The focused failure-specific boundary now passes before the full matrix, proving the R1 `search-filter` defect has been repaired without changing the 150 ms coalescer contract.

### 41.2 Performance-budget rule before Candidate

The T480 values above are measurements, not thresholds. The Candidate budget must be derived explicitly and documented before a Candidate run.

The freeze step must:

1. preserve the measured R2 baseline verbatim;
2. define a conservative guardrail separately from the observed median/max;
3. use the guardrail as a regression detector, not as an optimization target;
4. avoid thresholds tighter than the observed natural spread;
5. keep projection/search budgets distinct from startup mapping;
6. require the same measurement fixture and library cardinality as the non-candidate probe;
7. freeze the exact automated + real-GTK + performance + manual validation sequence before attempt authorization.

No additional feature implementation is allowed in that freeze step.

`NEXT_ACTION = B02_CANDIDATE_PREFLIGHT_AND_PERFORMANCE_BUDGET_FREEZE_AUTHORIZATION_PENDING`

## 42. B02 Candidate preflight and performance-budget methodology freeze

**Status:** CONTRACT FROZEN / T480 PREFLIGHT PENDING  
**Candidate:** NO  
**Candidate attempts used:** 0  
**Product/source mutation:** NO  
**Git mutation:** NO

Exact R2 authority:

```text
SOURCE_MANIFEST_SHA256=bd6f934e4b9d2cb91c1539eb8a273e9315bdbc3d6e91168074bb6274eedae018
CANONICAL_HEAD=3e0010a0679e9ba4e541e6fa854186806f83a08a
CANONICAL_TREE=a03cb52013e6acef4233b4c5a5b00995d50ac40f
```

### 42.1 Candidate automated sequence — FROZEN

```text
1 focused repaired search-filter GTK lane
131 headless tests
10 full real-GTK fresh-process lanes
performance budget gate
```

Automated validation-unit count:

```text
1 + 131 + 10 = 142
```

The focused lane is intentionally repeated inside the 10-lane full matrix.

### 42.2 Candidate manual sequence — FROZEN

Exactly **12** desktop tests, delivered by terminal runner in **4 batches of 3**:

```text
Batch 1: New Library / Open Library / Search + filters
Batch 2: Selection + detail / New Reference / Edit Reference
Batch 3: Duplicate / Delete / malformed read-only
Batch 4: stale conflict / About + Quit / visual light-system check
```

The terminal runner must stop immediately on a reported FAIL. Candidate manual validation is not started until all automated/performance gates pass.

### 42.3 Second performance distribution — FROZEN

Preflight collects, without changing product source:

- 9 additional fresh-process startup -> first-mapped samples;
- 9 additional projection-1000 samples;
- 9 additional search-1000 samples.

The R2 observed baseline is preserved verbatim:

```text
startup: 198.645, 217.372, 209.828, 222.084, 210.746 ms
projection_1000: 53.678 ms
search_1000: 2.459 ms
```

Projection/search sampling uses the same deterministic 1,000-record fixture and same query (`Title 999`) as R2.

### 42.4 Numeric budget formula — FROZEN

For each metric after T480 preflight:

```text
combined = R2 baseline samples + preflight samples
median   = median(combined)
MAD      = median(abs(sample - median))
raw      = max(max(combined) * 1.10, median + 6 * MAD)
```

Rounding:

```text
startup:         ceil upward to 5 ms
projection_1000: ceil upward to 5 ms
search_1000:     ceil upward to 0.5 ms
```

The 10% guardband is a same-machine measurement-noise allowance. It is not a feature target and must not be tightened merely to make a benchmark look better.

If preflight evidence is internally pathological or inconsistent with the fixed fixture, the budget is **not** frozen by guessing or rerunning with looser limits; the run is classified and audited first.

### 42.5 Preflight execution

The preflight itself is NON-CANDIDATE and repeats the exact R2 verification sequence before collecting the second distribution:

```text
source/package/canonical identity
focused search-filter
131 headless
10 real-GTK
9 startup samples
9 projection/search samples
canonical Git postcheck
```

No commit/push and no product mutation.

A successful T480 preflight must end with:

```text
B02_CANDIDATE_PREFLIGHT=PASS
BUDGET_FREEZE_INPUT=READY
CANDIDATE=NO
CANDIDATE_ATTEMPTS_USED=0
CANONICAL_REPO_MUTATION=NO
```

Only after that output may the numeric budgets be calculated using section 42.4 and frozen into the Candidate contract.

`NEXT_ACTION = B02_CANDIDATE_PREFLIGHT_T480_RUN`

## 43. B02 Candidate preflight T480 PASS and numeric budget freeze

The user executed the preflight on the Lenovo ThinkPad T480.

Validation before performance sampling:

```text
B02_HEADLESS_TEST_RESULT=131/131_PASS
B02_REAL_GTK_RESULT=10/10_PASS
B02_CANDIDATE_PREFLIGHT=PASS
AUTOMATED_VALIDATION_UNITS=142
CANONICAL_REPO_MUTATION=NO
GIT_COMMIT_PUSH=NO
CANDIDATE=NO
CANDIDATE_ATTEMPTS_USED=0
BYTECODE_ARTIFACTS=0
```

Second T480 distribution:

```text
PREFLIGHT_STARTUP_SAMPLES=9
startup_ms =
197.455
209.735
213.028
207.727
216.885
211.324
210.712
212.766
215.095

PREFLIGHT_PROJECTION_SEARCH_SAMPLES=9
projection_1000_ms =
50.074
48.944
47.540
50.397
54.744
47.814
48.326
49.058
47.250

search_1000_ms =
2.052
2.188
2.043
2.353
2.326
2.104
2.005
2.142
2.026
```

Combined statistics reported by the frozen preflight runner:

```text
COMBINED_STARTUP_N=14
COMBINED_STARTUP_MEDIAN_MS=211.035
COMBINED_STARTUP_MAD_MS=2.650
COMBINED_STARTUP_MAX_MS=222.084
STARTUP_GUARDRAIL_RAW_MS=244.292
STARTUP_GUARDRAIL_RECOMMENDED_MS=245.000

COMBINED_PROJECTION_N=10
COMBINED_PROJECTION_MEDIAN_MS=49.001
COMBINED_PROJECTION_MAD_MS=1.291
COMBINED_PROJECTION_MAX_MS=54.744
PROJECTION_GUARDRAIL_RAW_MS=60.218
PROJECTION_GUARDRAIL_RECOMMENDED_MS=65.000

COMBINED_SEARCH_N=10
COMBINED_SEARCH_MEDIAN_MS=2.123
COMBINED_SEARCH_MAD_MS=0.089
COMBINED_SEARCH_MAX_MS=2.459
SEARCH_GUARDRAIL_RAW_MS=2.705
SEARCH_GUARDRAIL_RECOMMENDED_MS=3.000
```

The methodology frozen before the run was:

```text
raw_guardrail = max(combined_max*1.10, combined_median + 6*MAD)
startup/projection -> round upward to 5 ms
search             -> round upward to 0.5 ms
```

Therefore the exact B02 Candidate performance budget is now FROZEN:

```text
STARTUP_FIRST_MAPPED_MAX_MS=245.000
PROJECTION_1000_MAX_MS=65.000
SEARCH_1000_MAX_MS=3.000
```

### 43.1 Candidate validation contract — FINAL FROZEN

Exact source authority:

```text
R2_SOURCE_MANIFEST_SHA256=bd6f934e4b9d2cb91c1539eb8a273e9315bdbc3d6e91168074bb6274eedae018
CANONICAL_HEAD=3e0010a0679e9ba4e541e6fa854186806f83a08a
CANONICAL_TREE=a03cb52013e6acef4233b4c5a5b00995d50ac40f
```

Automated order:

```text
1. package/source/canonical identity
2. focused repaired search-filter fresh-process lane
3. 131 headless tests
4. full 10-lane real-GTK matrix
5. performance gate:
   startup first-mapped <= 245.000 ms
   projection-1000     <= 65.000 ms
   search-1000         <= 3.000 ms
6. canonical Git postcheck
```

Automated validation units:

```text
1 + 131 + 10 = 142
```

Performance samples are measurement gates and do not inflate the validation-unit count.

Manual desktop validation after automated PASS:

```text
12 tests total
4 batches of 3
terminal-delivered
STOP immediately on first FAIL
```

No feature change is permitted between this freeze and Candidate build. Any source delta beyond packaging/runner/oracle material invalidates the Candidate lineage and requires requalification.

### 43.2 Status

```text
B02_CANDIDATE_PREFLIGHT=PASS
B02_NUMERIC_PERFORMANCE_BUDGET=FROZEN
B02_CANDIDATE_CONTRACT=FROZEN
B02_CANDIDATE=NOT_OPENED
CANDIDATE_ATTEMPTS_USED=0
PRODUCT_SOURCE_MUTATION=NO
GIT_MUTATION=NO
```

`NEXT_ACTION = B02_CANDIDATE_R1_AUTHORIZATION_PENDING`

## 44. B02 Candidate R1 — exact build and validation contract

**Status:** BUILT / T480 AUTOMATED PENDING  
**Product source delta from R2:** NONE  
**Git mutation:** NO

Exact product source authority:

```text
R2_SOURCE_MANIFEST_SHA256=bd6f934e4b9d2cb91c1539eb8a273e9315bdbc3d6e91168074bb6274eedae018
CANONICAL_HEAD=3e0010a0679e9ba4e541e6fa854186806f83a08a
CANONICAL_TREE=a03cb52013e6acef4233b4c5a5b00995d50ac40f
```

Frozen Candidate performance budget:

```text
STARTUP_FIRST_MAPPED_MAX_MS=245.000
PROJECTION_1000_MAX_MS=65.000
SEARCH_1000_MAX_MS=3.000
```

Automated Candidate sequence:

```text
preconditions/package/source/canonical identity
CANDIDATE_ATTEMPT_STARTED=1
1 focused search-filter fresh-process lane
131 headless tests
10 full real-GTK fresh-process lanes
5 startup fresh-process samples + 1000-record projection/search
hard performance comparison against frozen budget
canonical Git postcheck
```

Validation-unit count remains:

```text
1 + 131 + 10 = 142
```

Performance measurements are gates but do not inflate this count.

Automated PASS yields:

```text
B02_CANDIDATE_R1_AUTOMATED=PASS
CANDIDATE_ATTEMPT_USED=1
MANUAL_DESKTOP_VALIDATION=PENDING
```

Only then may the separate manual runner execute exactly 12 tests, four batches of three, stopping on the first reported FAIL.

Manual tests:

```text
1  New Library
2  Open Library
3  Search and filters
4  Selection and detail
5  New Reference
6  Edit Reference
7  Duplicate Reference
8  Delete Reference
9  Malformed library read-only
10 Stale conflict Reload / Overwrite / Cancel
11 About and Quit
12 Visual light/system readability
```

No source repair is allowed inside Candidate R1. Any Candidate product FAIL retires R1 before any repair analysis.

`NEXT_ACTION = B02_CANDIDATE_R1_T480_AUTOMATED_RUN`

### 44.1 Candidate R1 pre-delivery harness/fixture requalification

Before T480 delivery, two Candidate-package defects were detected:

```text
DEFECT_1=AUTOMATED_RUNNER_PRECONDITION_CONTROL_FLOW
CLASSIFICATION=PACKAGING_HARNESS
PRODUCT_SOURCE_MUTATION=NO
ATTEMPT_CONSUMED=NO

DEFECT_2=MANUAL_LIBRARY_FIXTURE_NONCANONICAL_FIELD_PREFIX
CLASSIFICATION=MANUAL_ORACLE_FIXTURE
PRODUCT_SOURCE_MUTATION=NO
ATTEMPT_CONSUMED=NO
```

Repairs:

- GTK-runtime/package preconditions now route through the explicit fail-visible precondition classifier and report `CANDIDATE_ATTEMPT_USED=0`;
- manual valid-library fixture uses canonical `Type:`, `Author:`, `Title:`, `Year:`, `Tags:` and `Related Keys:` fields;
- stale-conflict helper appends a canonical valid record.

Fresh checks:

```text
FRESH_PACKAGE_VERIFY=PASS
B02_SOURCE_VERIFY=PASS
B02_HEADLESS_TEST_RESULT=131/131_PASS
RUNNER_SYNTAX=PASS
PERF_GATE_SYNTHETIC_PASS_FAIL=PASS
PRECONDITION_ATTEMPT_ACCOUNTING=PASS
MANUAL_VALID_FIXTURE_RECORDS=3
MANUAL_VALID_FIXTURE_DIAGNOSTICS=0
STALE_HELPER_RECORDS=4
STALE_HELPER_DIAGNOSTICS=0
PRODUCT_SOURCE_DELTA_FROM_R2=NONE
CANDIDATE_ATTEMPT_USED=0_BEFORE_T480_RUN
```

No T480 Candidate run has occurred yet.

### 44.2 Candidate R1 pre-delivery bytecode contamination catch

A final fresh-extraction audit detected staging-only Python bytecode created by the fixture-validation import:

```text
CLASSIFICATION=PACKAGING_CLEANLINESS
PRODUCT_DEFECT=NO
PRODUCT_SOURCE_MUTATION=NO
T480_CANDIDATE_RUN=NOT_STARTED
CANDIDATE_ATTEMPT_USED=0
```

The staging bytecode was removed and the package was rebuilt. Final delivery requires `BYTECODE_ARTIFACTS=0` on the exact ZIP.

## 45. B02 Candidate R1 — automated T480 PASS / manual authorization

The user executed the automated Candidate R1 runner on T480.

```text
B02_CANDIDATE_R1_AUTOMATED=PASS
B02_R2_FOCUSED_BOUNDARY_RESULT=1/1_PASS
B02_HEADLESS_TEST_RESULT=131/131_PASS
B02_REAL_GTK_RESULT=10/10_PASS
B02_CANDIDATE_PERF_GATE=PASS
AUTOMATED_VALIDATION_UNITS=142
CANDIDATE_ATTEMPT_USED=1
MANUAL_DESKTOP_VALIDATION=PENDING
SOURCE_MANIFEST_SHA256=bd6f934e4b9d2cb91c1539eb8a273e9315bdbc3d6e91168074bb6274eedae018
CANONICAL_HEAD=3e0010a0679e9ba4e541e6fa854186806f83a08a
CANONICAL_TREE=a03cb52013e6acef4233b4c5a5b00995d50ac40f
CANONICAL_REPO_MUTATION=NO
GIT_COMMIT_PUSH=NO
BYTECODE_ARTIFACTS=0
EXIT=0
ERR=NONE
FINAL_PHASE=SCHEDULAE_B02_CANDIDATE_R1_AUTOMATED_PASS_MANUAL_PENDING
```

Candidate performance measurements:

```text
STARTUP_FIRST_MAPPED_MAX_MS=215.097
FROZEN_STARTUP_MAX_MS=245.000
PROJECTION_1000_MS=52.851
FROZEN_PROJECTION_1000_MAX_MS=65.000
SEARCH_1000_MS=2.076
FROZEN_SEARCH_1000_MAX_MS=3.000
```

Decision:

- automated qualification is complete and valid;
- Candidate attempt 1 is already consumed;
- the manual validation is continuation of the same Candidate R1 attempt, not a second attempt;
- manual scope remains exactly 12 tests in 4 terminal batches of 3;
- stop immediately on first reported FAIL;
- no source repair, commit, or push during manual validation.

`NEXT_ACTION = B02_CANDIDATE_R1_T480_MANUAL_RUN`
## 46. B02 Candidate R1 manual T480 PASS / publication authorization

```text
B02_CANDIDATE_R1_AUTOMATED=PASS
AUTOMATED_VALIDATION_UNITS=142
B02_R2_FOCUSED_BOUNDARY_RESULT=1/1_PASS
B02_HEADLESS_TEST_RESULT=131/131_PASS
B02_REAL_GTK_RESULT=10/10_PASS
B02_CANDIDATE_PERF_GATE=PASS
STARTUP_MAX_MEASURED_MS=215.097
STARTUP_MAX_FROZEN_MS=245.000
PROJECTION_1000_MEASURED_MS=52.851
PROJECTION_1000_FROZEN_MS=65.000
SEARCH_1000_MEASURED_MS=2.076
SEARCH_1000_FROZEN_MS=3.000

B02_CANDIDATE_R1_MANUAL=PASS
MANUAL_DESKTOP_RESULT=12/12_PASS
MALFORMED_FILE_BYTES_UNCHANGED=YES
CANDIDATE_ATTEMPT_USED=1
B02_CANDIDATE_R1=DESKTOP_CERTIFIED_PUBLICATION_READY
CANONICAL_REPO_MUTATION=NO
GIT_COMMIT_PUSH=NO
```

All twelve manual tests have explicit user PASS verdicts and are final for B02. They must not be repeated merely because future harness wording is improved.

### 46.1 Future desktop-validation harness rule

From B03 onward every manual desktop test must be operationally click-by-click. Each test must state:

1. exact starting state and fixture;
2. exact menu/button/widget sequence;
3. exact text/path/value to enter;
4. exact visible or persisted result to inspect;
5. one unambiguous PASS criterion;
6. one unambiguous FAIL criterion;
7. exact terminal helper command when external mutation is required;
8. STOP-on-FAIL instruction.

Broad instructions such as “exercise the workflow” or “visual check” are forbidden for future Candidate certification. A manual runner must explicitly manage or announce application startup before soliciting a verdict.

This is a methodology/harness debt only; it does not invalidate B02 Candidate R1.

### 46.2 B02 Publication P1 contract

Publication is authorized from the exact certified source authority:

```text
SOURCE_MANIFEST_SHA256=bd6f934e4b9d2cb91c1539eb8a273e9315bdbc3d6e91168074bb6274eedae018
EXPECTED_PARENT=3e0010a0679e9ba4e541e6fa854186806f83a08a
EXPECTED_PARENT_TREE=a03cb52013e6acef4233b4c5a5b00995d50ac40f
COMMIT_SUBJECT=B02: add native GTK shell
AUTOMATED_VALIDATION_UNITS=142
STARTUP_FIRST_MAPPED_MAX_MS=245.000
PROJECTION_1000_MAX_MS=65.000
SEARCH_1000_MAX_MS=3.000
```

Publication P1 must re-run source verification, focused GTK, 131 headless, 10 full real-GTK and frozen performance gates on the canonical worktree before stage/commit/push. It must verify the real remote after push and leave the worktree CLEAN.

B03 remains NOT OPENED.

`NEXT_ACTION = B02_PUBLICATION_P1_T480_RUN`
### 46.3 Publication P1 pre-delivery packaging repair

A final package audit caught a publication-tool path defect before T480 execution: the copied performance gate still looked for the Candidate topology `ROOT/SOURCE`, while the publication package exposes the certified source directly at its root.

```text
CLASSIFICATION=PUBLICATION_PACKAGING_TOOLING
PRODUCT_DEFECT=NO
PRODUCT_SOURCE_MUTATION=NO
GIT_MUTATION=NO
T480_PUBLICATION_RUN=NOT_STARTED
REPAIR=PERFORMANCE_GATE_SOURCE_ROOT
```

The publication performance gate now points to the package root and emits publication-specific PASS/FAIL markers. The exact final publication ZIP was fresh-extracted, package-manifest verified, B02 source-verified, headless 131/131 requalified, and its frozen-budget PASS/FAIL logic was synthetically checked.

## 46. B02 Publication P1 — T480 PASS

Canonical publication receipt:

```text
B02_PUBLICATION_P1=PASS
AUTOMATED_VALIDATION_UNITS=142
B02_R2_FOCUSED_BOUNDARY_RESULT=1/1_PASS
B02_HEADLESS_TEST_RESULT=131/131_PASS
B02_REAL_GTK_RESULT=10/10_PASS
B02_PUBLICATION_PERF_GATE=PASS

STARTUP_FIRST_MAPPED_MAX_MS=221.400
FROZEN_STARTUP_MAX_MS=245.000
PROJECTION_1000_MS=54.146
FROZEN_PROJECTION_1000_MAX_MS=65.000
SEARCH_1000_MS=2.492
FROZEN_SEARCH_1000_MAX_MS=3.000

SOURCE_MANIFEST_SHA256=bd6f934e4b9d2cb91c1539eb8a273e9315bdbc3d6e91168074bb6274eedae018
PARENT_COMMIT=3e0010a0679e9ba4e541e6fa854186806f83a08a
B02_PRODUCT_COMMIT=b35c9969c574cc366bb8318a6da16397c38b8009
B02_PRODUCT_TREE=f06418a99f790d3dc6e265d14395457fa050686c
HEAD=b35c9969c574cc366bb8318a6da16397c38b8009
ORIGIN_MAIN=b35c9969c574cc366bb8318a6da16397c38b8009
REMOTE_MAIN=b35c9969c574cc366bb8318a6da16397c38b8009
REMOTE_URL=https://github.com/leviagravia/schedulae.git
WORKTREE=CLEAN
CANONICAL_DOCUMENTS=3
CANDIDATE_ATTEMPT_USED=1
B02_MANUAL_DESKTOP_RESULT=12/12_PASS
B03=NOT_OPENED
EXIT=0
ERR=NONE
FINAL_PHASE=SCHEDULAE_B02_PUBLICATION_P1_PASS
```

### 46.1 Authority distinction

```text
B02_PRODUCT_SOURCE_AUTHORITY_COMMIT=b35c9969c574cc366bb8318a6da16397c38b8009
B02_PRODUCT_SOURCE_AUTHORITY_TREE=f06418a99f790d3dc6e265d14395457fa050686c
B02_SOURCE_MANIFEST_SHA256=bd6f934e4b9d2cb91c1539eb8a273e9315bdbc3d6e91168074bb6274eedae018
```

The earlier commit `3e0010a0679e9ba4e541e6fa854186806f83a08a` / tree `a03cb52013e6acef4233b4c5a5b00995d50ac40f` remains the B01 documentation-finalized parent.

### 46.2 B02 P2 documentation finalizer — authorized contract

The user explicitly authorized the exact next step on 20 August 2026. P2 is a **documentation-only finalizer**, not a Candidate attempt, and B03 remains unopened.

Exact parent authority:

```text
B02_PRODUCT_COMMIT=b35c9969c574cc366bb8318a6da16397c38b8009
B02_PRODUCT_TREE=f06418a99f790d3dc6e265d14395457fa050686c
B02_SOURCE_MANIFEST_SHA256=bd6f934e4b9d2cb91c1539eb8a273e9315bdbc3d6e91168074bb6274eedae018
REMOTE=https://github.com/leviagravia/schedulae.git
```

P2 contract:

- only the three canonical Markdown documents may change;
- all product source, tests, tools, provenance, `LICENSE`, `.gitignore`, and `PROJECT_IDENTITY.toml` remain byte-identical to the published B02 product tree;
- `tools/VERIFY_B02_SOURCE.py` must PASS before and after the document update;
- exactly 131 B02 headless tests must PASS before and 131 after the document update: **262 test executions** total;
- commit subject: `docs: finalize B02 publication receipt`;
- push only after the mutation-scope gate proves that exactly the three canonical Markdown files changed and no untracked paths exist;
- after push require `HEAD = origin/main = real remote main`, CLEAN worktree, and exact parent `b35c9969c574cc366bb8318a6da16397c38b8009`;
- B02 manual desktop validation remains final at **12/12 PASS** and must not be repeated;
- B03 remains **NOT OPENED** until P2 PASS.

The B02 product-source authority remains commit `b35c9969c574cc366bb8318a6da16397c38b8009` / tree `f06418a99f790d3dc6e265d14395457fa050686c`. P2 synchronizes documentation only and does not redefine the certified product tree. No P3 shall be created merely to insert P2's own commit hash.

After P2 PASS the external receipt/handover may advance to `NEXT_ACTION = B03_DIRECT_SOURCE_AUDIT_AUTHORIZATION_PENDING`.

`NEXT_ACTION = RUN_B02_P2_DOCUMENTATION_FINALIZER_ON_T480`
