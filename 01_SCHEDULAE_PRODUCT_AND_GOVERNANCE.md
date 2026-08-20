# Schedulae — Identità, prodotto e governance

**Documento canonico 1 di 3**  
**Versione:** 3.1  
**Data:** 19 agosto 2026  
**Stato:** AUTHORITATIVE — B00/B01 CLOSED / B02 R1 RETIRED / B02 R2 T480 PROVEN NON-CANDIDATE / CANDIDATE PREFLIGHT PASS / PERF BUDGET FROZEN / B02 CANDIDATE R1 BUILT / T480 PENDING  
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

## 13.2 B02 — principi di prodotto congelati dall'audit pre-implementazione

B02 introduce la prima shell desktop nativa di Schedulae, ma non deve cambiare il modello di autorità stabilito da B01.

Decisioni congelate:

- stack desktop: **GTK 3 + PyGObject**;
- una sola `Gtk.Application` e una sola `Gtk.ApplicationWindow` per processo in B02;
- una sola libreria attiva per finestra/processo;
- la libreria resta un file esplicito scelto dall'utente; nessun auto-open nascosto, nessuna libreria XDG implicita;
- i 11 moduli di dominio B01 restano GTK-free;
- il controller resta proprietario della citation key selezionata semanticamente;
- la view GTK usa un modello persistente e una selection separata; righe/widget non sono autorità semantica;
- ricerca con `Gtk.SearchEntry` + coalescing già esistente a 150 ms;
- layout minimo: menu, ricerca/filtro compatto, lista, detail read-only;
- niente toolbar;
- New/Edit/Duplicate/Delete sono workflow espliciti e persist-first;
- Edit non rinomina citation key o aliases;
- Duplicate produce un draft con key non collidente e aliases vuoti, poi richiede review;
- Delete richiede sempre conferma e mostra l'impatto Related References senza cascata silenziosa;
- libreria malformata resta apribile in read-only con azioni mutative disabilitate;
- dialog GTK: transient/modal rispetto alla finestra, risultato semantico copiato prima della distruzione, nessun event-loop pumping;
- import/export BibTeX/BibLaTeX restano B03;
- packaging/distribuzione e hard performance certification restano B04;
- nessun database, rete, background indexer, plugin system, PDF manager o multi-window framework viene introdotto in B02.

B02 non è ancora implementato. L'audit autorizzato è concluso; qualsiasi source-writing B02 richiede autorizzazione separata.
## 13.3 B02 Implementation R1 — stato pre-T480

B02 R1 è stata costruita in copia isolata senza mutare la repository canonica.

```text
B02_IMPLEMENTATION_R1=BUILT
B02_HEADLESS_TEST_RESULT=130/130_PASS
B01_REGRESSION_TESTS=101
B02_NEW_HEADLESS_TESTS=29
B02_REAL_GTK_LANES=10_PENDING_T480
B02_STARTUP_SAMPLES=5_PENDING_T480
SOURCE_MANIFEST_SHA256=f7eee624e0d646e7033dfbeb82893c196ddcb6ded45000c041e991099811f6d6
CANONICAL_HEAD=3e0010a0679e9ba4e541e6fa854186806f83a08a
CANONICAL_TREE=a03cb52013e6acef4233b4c5a5b00995d50ac40f
CANONICAL_REPO_MUTATION=NO
CANDIDATE=NO
```

La shell realizzata resta nel contratto B02: GTK3/PyGObject, una finestra, `Gtk.ListStore`/`Gtk.TreeView` con selection separata, controller proprietario della key semantica, New/Edit/Duplicate/Delete persist-first, ricerca coalesced 150 ms, nessuna toolbar e nessun Import/Export UI.

La qualifica real-GTK è deliberatamente pendente perché l'ambiente di costruzione non dispone di PyGObject/GTK3. Il T480 è il target autoritativo per tali lane.
## 13.4 B02 R1 failure and evidence-based R2 repair

B02 R1 is **RETIRED / NOT QUALIFIED** after the T480 real-GTK `search-filter` lane failed with `delivery_count=0` after three earlier GTK lanes passed. No Candidate attempt was involved.

A direct comparative mature-source audit (Calamus W97, GNOME Citations, Mousepad, KBibTeX, JabRef) established one timing-owner rule: the widget emits the immediate text-change signal and Schedulae alone owns the explicit 150 ms coalescer. R2 therefore changes only the GTK adapter binding from `search-changed` to `changed`; it does not alter the domain coalescer, delay, controller or filtering semantics.

The R1 fixed-time GTK oracle is also retired. R2 waits boundedly for the semantic completion state rather than increasing a guessed sleep. The repaired `search-filter` boundary must pass alone before broad regression/full GTK reruns are allowed.

## 13.4 B02 R2 — T480 non-candidate qualification

B02 R2 has completed the full non-candidate T480 qualification.

Result:

```text
B02_IMPLEMENTATION_R2=PASS
B02_R2_FOCUSED_BOUNDARY_RESULT=1/1_PASS
B02_HEADLESS_TEST_RESULT=131/131_PASS
B02_REAL_GTK_RESULT=10/10_PASS
B02_PERF_PROBE=PASS
STARTUP_SAMPLES=5
CANONICAL_REPO_MUTATION=NO
GIT_COMMIT_PUSH=NO
CANDIDATE=NO
BYTECODE_ARTIFACTS=0
```

Observed T480 measurements:

```text
STARTUP_FIRST_MAPPED_MIN_MS=198.645
STARTUP_FIRST_MAPPED_MEDIAN_MS=210.746
STARTUP_FIRST_MAPPED_MAX_MS=222.084
PROJECTION_1000_MS=53.678
SEARCH_1000_MS=2.459
THRESHOLD_GATE=NOT_FROZEN_NONCANDIDATE_MEASUREMENT_ONLY
```

Classification:

- R1 remains retired after the real-GTK `search-filter` failure.
- R2 is T480 proven as a non-candidate implementation.
- Candidate attempts consumed: 0.
- No publication, commit, or push has occurred for B02.
- These performance values are observational baseline evidence only; they do not become Candidate thresholds by inference.
- Candidate authorization must not occur until the performance budget and exact Candidate validation contract are explicitly frozen from this evidence.

B02 manual desktop validation has not yet been performed.

## 13.5 B02 Candidate preflight contract

No Candidate attempt is opened by this step.

Frozen before Candidate:

- exact R2 source authority remains unchanged;
- automated Candidate order: focused repaired GTK boundary -> 131 headless -> full 10 real-GTK lanes -> performance budget gate;
- automated validation units: **142**;
- manual desktop tests: **12**, presented by terminal runner in four batches of three;
- manual validation is never dumped as a full checklist into chat;
- performance measurements use the same 1,000-record fixture as R2;
- a second T480 distribution is required before numeric guardrails are frozen;
- no feature changes are permitted during preflight/budget freeze.

Performance budget method:

```text
combined_samples = R2 observed baseline + preflight samples
MAD = median absolute deviation
raw_guardrail = max(combined_max * 1.10, combined_median + 6 * MAD)

startup/projection: round upward to 5 ms
search:             round upward to 0.5 ms
```

The 10% outer guardband is explicitly a regression-noise allowance on the same T480/fixture, not an optimization target. Numeric thresholds are not authoritative until the T480 preflight completes successfully.

## 13.6 B02 Candidate numeric performance budget — FROZEN

The T480 preflight completed successfully and the previously frozen formula has been applied without modification.

Authoritative Candidate guardrails:

```text
STARTUP_FIRST_MAPPED_MAX_MS=245.000
PROJECTION_1000_MAX_MS=65.000
SEARCH_1000_MAX_MS=3.000
```

These values are regression guardrails, not optimization targets.

Candidate contract remains:

```text
AUTOMATED_VALIDATION_UNITS=142
  focused repaired search-filter lane=1
  headless tests=131
  full real-GTK lanes=10

MANUAL_DESKTOP_TESTS=12
MANUAL_BATCH_SIZE=3
```

No Candidate has been built or run. Candidate attempts consumed remain 0.

## 13.7 B02 Candidate R1 — build authority

B02 Candidate R1 is authorized and built from the exact T480-proven R2 product source.

```text
R2_SOURCE_MANIFEST_SHA256=bd6f934e4b9d2cb91c1539eb8a273e9315bdbc3d6e91168074bb6274eedae018
CANDIDATE_PRODUCT_SOURCE_DELTA=NONE
STARTUP_FIRST_MAPPED_MAX_MS=245.000
PROJECTION_1000_MAX_MS=65.000
SEARCH_1000_MAX_MS=3.000
AUTOMATED_VALIDATION_UNITS=142
MANUAL_DESKTOP_TESTS=12
MANUAL_BATCH_SIZE=3
```

Candidate R1 has not yet been executed on the T480. The first Candidate attempt begins only after immutable package/source/canonical preconditions pass and the runner prints `CANDIDATE_ATTEMPT_STARTED=1`.

No Git commit/push occurs during Candidate qualification.

### Candidate R1 pre-delivery harness qualification

Two pre-delivery issues were found and repaired without changing product source:

1. automated runner GTK-runtime precondition exited directly instead of using the fail-visible precondition classifier;
2. manual fixture records used non-canonical `- Field:` syntax.

Both are packaging/oracle-fixture defects, not product defects. The automated runner now reports precondition failure with `CANDIDATE_ATTEMPT_USED=0`, and manual fixtures parse as valid canonical libraries. Candidate product source remains byte-identical to R2.

A final fresh-package cleanliness check also detected build-environment bytecode created by the fixture audit itself. All `__pycache__`/`.pyc` artifacts were removed before final packaging; no maintained source byte changed.

## 13.8 B02 Candidate R1 — automated T480 PASS / manual pending

```text
B02_CANDIDATE_R1_AUTOMATED=PASS
B02_R2_FOCUSED_BOUNDARY_RESULT=1/1_PASS
B02_HEADLESS_TEST_RESULT=131/131_PASS
B02_REAL_GTK_RESULT=10/10_PASS
B02_CANDIDATE_PERF_GATE=PASS
AUTOMATED_VALIDATION_UNITS=142
CANDIDATE_ATTEMPT_USED=1
MANUAL_DESKTOP_VALIDATION=PENDING
MANUAL_DESKTOP_TESTS=12
MANUAL_BATCH_SIZE=3
SOURCE_MANIFEST_SHA256=bd6f934e4b9d2cb91c1539eb8a273e9315bdbc3d6e91168074bb6274eedae018
CANONICAL_HEAD=3e0010a0679e9ba4e541e6fa854186806f83a08a
CANONICAL_TREE=a03cb52013e6acef4233b4c5a5b00995d50ac40f
CANONICAL_REPO_MUTATION=NO
GIT_COMMIT_PUSH=NO
BYTECODE_ARTIFACTS=0
```

Measured Candidate performance:

```text
startup max = 215.097 ms <= 245.000 ms
projection-1000 = 52.851 ms <= 65.000 ms
search-1000 = 2.076 ms <= 3.000 ms
```

Candidate R1 is not yet desktop certified. The same attempt continues into the frozen 12-test manual desktop validation.
## 13.9 B02 Candidate R1 — desktop certified / publication authorized

Manual desktop validation completed with explicit user verdicts for all twelve frozen tests.

```text
B02_CANDIDATE_R1_MANUAL=PASS
MANUAL_DESKTOP_RESULT=12/12_PASS
MANUAL_TEST_1=PASS
MANUAL_TEST_2=PASS
MANUAL_TEST_3=PASS
MANUAL_TEST_4=PASS
MANUAL_TEST_5=PASS
MANUAL_TEST_6=PASS
MANUAL_TEST_7=PASS
MANUAL_TEST_8=PASS
MANUAL_TEST_9=PASS
MANUAL_TEST_10=PASS
MANUAL_TEST_11=PASS
MANUAL_TEST_12=PASS
MALFORMED_FILE_BYTES_UNCHANGED=YES
CANDIDATE_ATTEMPT_USED=1
B02_CANDIDATE_R1=DESKTOP_CERTIFIED_PUBLICATION_READY
GIT_COMMIT_PUSH=NO
EXIT=0
ERR=NONE
FINAL_PHASE=SCHEDULAE_B02_CANDIDATE_R1_MANUAL_PASS
```

The user explicitly confirmed that all twelve test verdicts remain valid and must not be repeated or retroactively downgraded.

Open harness debt for future work only: manual validation instructions from B03 onward must be click-by-click and operationally self-contained; a runner must either launch the application itself or state the second-terminal launch step before asking for a verdict. This debt does not alter B02's 12/12 PASS.

B02 Publication P1 is authorized.

