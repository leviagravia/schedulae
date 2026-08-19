# Schedulae — Identità, prodotto e governance

**Documento canonico 1 di 3**  
**Versione:** 1.5  
**Data:** 19 agosto 2026  
**Stato:** AUTHORITATIVE — B00 CLOSED / T480 CERTIFIED / PUBLISHED / GPL-3.0-or-later / B01 AUDIT COMPLETE / IMPLEMENTATION NOT OPENED  
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

Questi valori sono il target di identità dopo la selezione del nome; la migrazione effettiva dei moduli Python appartiene a B01, non a B00.

```toml
product_name = "Schedulae"
repo_slug = "schedulae"
future_python_namespace = "schedulae"
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
- B00: **CLOSED / T480 CERTIFIED / UNPUBLISHED**;
- remote GitHub pubblico creato: `https://github.com/leviagravia/schedulae`;
- Git locale: repository inizializzato, nessun commit e nessun remote configurato al momento della closure B00;
- licenza pubblica: **GNU GPL v3.0 or later (`GPL-3.0-or-later`)**, adottata e verificata sul T480 il 19 agosto 2026;
- root `LICENSE`: installato e verificato;
- source/test B00: byte-identici dopo l'adozione della licenza;
- first publication P1: **PASS** il 19 agosto 2026;
- published commit: `4d71e7f0e868d8229b0e05dd2682acc4d887f535`;
- published tree: `f0a0b49af500c6cefec180af6ec317738ab0919f`;
- `HEAD = origin/main = remote main` al commit pubblicato;
- remote: `https://github.com/leviagravia/schedulae.git`;
- B01 implementation non è ancora aperta; il **pre-implementation audit B01 è COMPLETE** e il relativo contratto tecnico è congelato nel Documento 2.

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
