# Schedulae — Autorità tecnica, architettura, validazione e roadmap

**Documento canonico 2 di 3**  
**Versione:** 1.3  
**Data:** 19 agosto 2026  
**Stato:** AUTHORITATIVE — B00 CLOSED / T480 CERTIFIED / GPL-3.0-or-later ADOPTED / FIRST PUBLICATION P1 AUTHORIZED / B01 NOT OPENED  
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

**Stato:** CLOSED / T480 CERTIFIED / UNPUBLISHED — 74/74 PASS, 3 canonical documents, 0 bytecode artifacts, branch `main`, no commit/remote.

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

La prima pubblicazione Git B00 licenziata è stata **autorizzata** il 19 agosto 2026.

P1 deve:

1. verificare prima di ogni mutazione Git: branch unborn `main`, nessun commit, nessun remote locale, remote GitHub raggiungibile e senza heads/tags, `LICENSE` esatto, tre documenti canonici, core/test B00 byte-identici e 74/74 PASS;
2. installare soltanto le authority canoniche aggiornate e aggiornare `PROJECT_IDENTITY.toml` con licenza/remoto/autorizzazione di pubblicazione;
3. rieseguire 74/74 dopo le sole modifiche documentali/identity;
4. eseguire `git add -A`;
5. creare il primo commit con subject `B00: bootstrap Schedulae bibliography core`;
6. configurare `origin` su `https://github.com/leviagravia/schedulae.git`;
7. push di `main`;
8. verificare `HEAD = origin/main = remote main`, tree e worktree CLEAN;
9. riportare commit/tree reali alla MO in un successivo finalizer, evitando il problema circolare di incorporare nel commit il proprio SHA.

B01 resta chiuso durante tutta P1.
