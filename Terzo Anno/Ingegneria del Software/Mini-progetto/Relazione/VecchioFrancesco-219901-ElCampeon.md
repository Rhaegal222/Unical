## Indice

:::indice

- [**1. Analisi dei requisiti utente**](#1-analisi-dei-requisiti-utente)
- [**2. Analisi dei requisiti di sistema**](#2-analisi-dei-requisiti-di-sistema)
  - [2.1. Diagramma dei casi d'uso](#21-diagramma-dei-casi-duso)
  - [2.2. Schede dei casi d'uso](#22-schede-dei-casi-duso)
  - [2.2.1 Caso d'uso UC1: Autenticare utente](#221-caso-duso-uc1-autenticare-utente)
  - [2.2.2 Caso d'uso UC2: Inserimento e Validazione dei Dati](#222-caso-duso-uc2-inserimento-e-validazione-dei-dati)
  - [2.2.3 Caso d'uso UC3: Visualizzazione Statistiche e Analisi](#223-caso-duso-uc3-visualizzazione-statistiche-e-analisi)
- [**3. Modello di dominio**](#3-modello-di-dominio)
  - [3.1 Diagramma del modello di dominio](#31-diagramma-del-modello-di-dominio)
  - [3.2 Descrizione del modello di dominio](#32-descrizione-del-modello-di-dominio)
- [**4. SSD di sistema**](#4-ssd-di-sistema)
  - [4.1 UC1-SSD: Autenticare utente](#41-uc1-ssd-autenticare-utente)
    - [4.1.1 SSD Principale per il Flusso Base di Successo](#411-ssd-principale-per-il-flusso-base-di-successo)
    - [4.1.2 SSD per Flussi Alternativi](#412-ssd-per-flussi-alternativi)
      - [4.1.2.1 Autenticazione con Google](#4121-autenticazione-con-google)
      - [4.1.2.2 Recupero Password](#4122-recupero-password)
  - [4.2 UC2-SSD: Inserimento e Validazione dei Dati](#42-uc2-ssd-inserimento-e-validazione-dei-dati)
    - [4.2.1 SSD Principale per il Flusso Base di Successo](#421-ssd-principale-per-il-flusso-base-di-successo)
    - [4.2.2 SSD per Flussi Alternativi](#422-ssd-per-flussi-alternativi)
      - [4.2.2.1 Errore nell'Inserimento dei Dati](#4221-errore-nellinserimento-dei-dati)
  - [4.3 UC3-SSD: Visualizzazione Statistiche e Analisi](#43-uc3-ssd-visualizzazione-statistiche-e-analisi)
    - [4.3.1 SSD Principale per il Flusso Base di Successo](#431-ssd-principale-per-il-flusso-base-di-successo)
    - [4.3.2 SSD per Flussi Alternativi](#432-ssd-per-flussi-alternativi)
      - [4.3.2.1 Condivisione delle Analisi](#4321-condivisione-delle-analisi)
        - [4.3.2.1.1 Condivisione delle analisi tramite email](#43211-condivisione-delle-analisi-tramite-email)
        - [4.3.2.1.2 Condivisione delle analisi sui social network](#43212-condivisione-delle-analisi-sui-social-network)
- [**5. Contratti delle operazioni**](#5-contratti-delle-operazioni)
   - [5.1 Contratto CO1: registraAccount(username, email, password, confermaPassword)](#51-contratto-co1-registraaccountusername-email-password-confermapassword)
   - [5.2 Contratto CO2: accessoAccount(email, password)](#52-contratto-co2-accessoaccountemail-password)
   - [5.3 Contratto CO3: recuperaPassword(email)](#53-contratto-co3-recuperapasswordemail)
   - [5.4 Contratto CO4: inserisciDato(dato)](#54-contratto-co4-inseriscidatidato)
   - [5.5 Contratto C05: calcolaPronostico()](#55-contratto-c05-calcolapronostico)
   - [5.6 Contratto C06: visualizzaAnalisi()](#56-contratto-c06-visualizzaanalisi)
   - [5.7 Contratto C07: condividiAnalisi(utente, analisi)](#57-contratto-c07-condividianalisiutente-analisi)



- [**6. Architettura del sistema**](#6-architettura-del-sistema)
   - [6.1 Descrizione dell'architettura del sistema](#61-descrizione-dellarchitettura-del-sistema)
:::

<div class="page"/>

## **1. Analisi dei requisiti utente**

Il sistema è stato progettato per calcolare il possibile vincitore del prossimo Gran Premio del Motomondiale, utilizzando un'ampia gamma di dati per un'analisi approfondita. Gli utenti possono accedere al sistema durante la settimana del Gran Premio sia per consultare l'analisi esistente sia per contribuire con nuovi dati rilevanti, come informazioni sugli eventi interni o esterni al circuito che potrebbero influenzare le prestazioni dei piloti. Inoltre, il sistema recupera autonomamente i risultati delle sessioni di prove libere e qualifiche.

La funzione principale del sistema è il calcolo del pronostico, che si basa sulla raccolta e l'elaborazione di dati quali i risultati ottenuti dai piloti nelle sessioni di prove, nelle qualifiche, i risultati dei precedenti Gran Premi dell'anno corrente e quelli ottenuti sullo stesso tracciato negli anni precedenti. L'analisi non si limita alle prestazioni individuali dei piloti, ma include anche informazioni sul team di appartenenza, offrendo un'analisi completa e personalizzata.

Un aspetto distintivo del sistema è la possibilità per gli utenti di contribuire con nuovi dati, arricchendo il database con informazioni come penalità, infortuni dei piloti o incidenti durante le gare. Questa funzionalità non solo aumenta la completezza del sistema, ma assicura anche l'aggiornamento costante delle analisi e delle previsioni.

Le funzionalità aggiuntive del sistema includono la visualizzazione di statistiche dettagliate dei piloti, fornendo un quadro completo dei partecipanti al Gran Premio, con dati personali, record di carriera, prestazioni recenti e affiliazioni alle squadre. Questo permette agli utenti di acquisire una comprensione più profonda dei piloti coinvolti nella competizione.

L'integrazione delle previsioni meteorologiche nel sistema fornisce informazioni specifiche per il giorno della gara, un aspetto cruciale poiché le condizioni atmosferiche possono influenzare significativamente le prestazioni dei piloti. La previsione accurata delle condizioni meteorologiche aggiunge un ulteriore livello di dettaglio per gli utenti.

La condivisione delle analisi tramite social network o email facilita un'interazione più ampia tra gli appassionati del Motomondiale, permettendo agli utenti di partecipare alle discussioni e condividere le proprie prospettive e previsioni. Questo scambio di informazioni contribuisce a creare una comunità virtuale di appassionati, arricchendo l'esperienza complessiva del sistema.

Il sistema implementa una chiara suddivisione dei ruoli per gli utenti, stabilendo specifiche azioni che possono essere svolte da ciascun ruolo. Gli utenti con ruolo standard hanno la possibilità di accedere e condividere le analisi dei pronostici, utilizzando i social media o l'email. Tuttavia, il loro coinvolgimento attivo è circoscritto principalmente all'inserimento di nuovi dati, i quali sono soggetti a un processo di moderazione e verifica da parte degli analisti.

Gli analisti, da parte loro, hanno il compito di gestire e supervisionare i dati forniti dagli utenti standard. Questo ruolo include la responsabilità di assicurare l'accuratezza e l'affidabilità dei dati inseriti. Inoltre, gli analisti sono incaricati dell'elaborazione e dell'analisi approfondita di questi dati, con l'obiettivo di aggiornare continuamente i modelli analitici. Questo processo è fondamentale per mantenere l'alta precisione delle previsioni fornite dal sistema e per offrire una rappresentazione realistica delle prestazioni dei piloti e delle potenziali dinamiche dei Gran Premi.

</div>

<div class="page"/>

## **2. Analisi dei requisiti di sistema**

### **2.1. Diagramma dei casi d'uso**

![Alt text](<img/png/Use Case Diagram.png>)

</div>

<div class="page"/>

### **2.2. Schede dei casi d'uso**

#### **2.2.1. Caso d'uso UC1: Autenticare utente**

**Portata:** Sistema di pronostici per il Motomondiale

**Livello:** Obiettivo utente

**Attore primario:** Utente

**Parti interessate e interessi:**

- **Utente:** Desidera autenticarsi in modo semplice, veloce e sicuro sulla piattaforma per accedere alle funzionalità offerte.
- **Provider di autenticazione:** Intende autenticare l’utente in modo persistente e rapido, garantendo l'integrità del processo.
- **Sistema:** Mira a portare a termine la registrazione e l'autenticazione dell'utente con successo per permettergli di accedere e contribuire alle analisi e previsioni della piattaforma.

**Precondizioni:** Nessuna

**Garanzia di successo (Post-condizioni):** L’utente viene registrato e autenticato correttamente all’interno del sistema ed è in grado di accedere a quest'ultimo e alle sue funzionalità.

**Scenario principale di successo (Flusso base):**

**1.** L’utente vuole registrarsi al sistema di previsione del vincitore del Gran Premio del Motomondiale per accedere alle analisi dettagliate e contribuire con nuovi dati.
**2.** Il sistema per la registrazione richiede all'utente di inserire l'username, l'email e la password, e di confermare la password inserita.
**3.** Il sistema controlla che i dati inseriti rispettino i criteri di validità (es. formati di email corretti, password sicura).
**4.** Se i dati sono validi, il sistema invia un'email di conferma all'indirizzo email fornito.
**5.** L’utente conferma la registrazione attraverso un link o un codice fornito nella mail di conferma.
**6.** Dopo la conferma, l'utente viene aggiunto al sistema e la procedura di registrazione termina.
**7.** L’utente desidera autenticarsi e accede alla pagina di login dove inserisce l'email e la password.
**8.** Il sistema verifica le credenziali e, se corrette, concede all'utente l'accesso alla piattaforma.
**9.** Una volta autenticato, l'utente può:

   - Consultare le analisi esistenti basate su un'ampia gamma di dati relativi ai Gran Premi passati e alle prestazioni attuali.
   - Inserire nuovi dati rilevanti, che verranno moderati dagli analisti prima dell'inclusione nel database del sistema.
   - Visualizzare statistiche dettagliate dei piloti e delle loro prestazioni in relazione alle variabili del sistema, inclusi eventi e condizioni meteorologiche.
   - Contribuire alla comunità condividendo analisi e previsioni attraverso i social network o via email.

**10.** Gli analisti, con credenziali speciali, hanno accesso a funzioni avanzate per la gestione dei dati e la supervisione delle analisi, assicurando l'accuratezza e l'affidabilità delle previsioni fornite dal sistema.

</div>

<div class="page"/>

**Estensioni (Flussi alternativi):**

***a.** **Durante la registrazione il sistema fallisce:**

:::indice
   - **1.** Il sistema informa l’utente del fallimento e lo invita a riprovare.
   - **2.** L’utente ritenta la registrazione, tornando al punto 1 del flusso principale.
:::

***b.** **Durante la registrazione l'utente torna alla aschemata principale:**

:::indice
   - **1.** Il sistema annulla la registrazione e l'utente viene reindirizzato alla pagina principale.
:::

***c.** **Durante la registrazione l'utente chiude l'applicazione**

:::indice
   - **1.** Il caso d'uso termina.
:::

**1a.** **L’utente si è già registrato e decide di effettuare il login invece della registrazione:**

:::indice
   - **1.** Il sistema riconosce che l'email fornita è già associata a un account esistente.
   - **2.** L'utente viene indirizzato alla pagina di login e invitato a utilizzare la funzione di recupero password se necessario.
   - **3.** L’utente continua dal punto 7 del flusso principale.
:::

**1b.** **L’utente decide di utilizzare l’account Google per autenticarsi:**

:::indice
   - **1.** Il sistema reindirizza l'utente al servizio di autenticazione di Google.
   - **2.** Google gestisce l'autenticazione e, una volta completata, reindirizza l'utente al sistema con le credenziali verificate.
   - **3.** L’utente non riesce ad accedere con l’account Google.
       - **3.1.** L’utente ha la possibilità di tentare nuovamente con un account Google diverso o di utilizzare l'autenticazione standard del sistema, tornando al punto 1 del flusso principale.
   - **4.** Google richiede all’utente la condivisione dei dati con la piattaforma.
   - **5.** L’utente acconsente alla condivisione dei dati.
   - **6.** Google fornisce al sistema l’accesso ai dati dell’account.
   - **7.** Il sistema fa accedere l’utente sulla piattaforma.
:::indice

**2a.** **L’utente non ha una mail:**

:::indice
   - **1.** Il sistema richiede che venga fornito un indirizzo email valido seguendo lo standard RFC-2822.
   - **2.** Se l'utente non dispone di una mail valida, viene invitato a crearne una per poter procedere con la registrazione.
:::

**2b.** **L’utente non ha inserito tutti i campi richiesti:**

:::indice
   - **1.** Il sistema segnala i campi obbligatori mancanti.
   - **2.** L'utente completa i campi richiesti per proseguire con la registrazione.
:::

**3a.** **La password non segue i parametri di validità imposti dal sistema:**

:::indice
   - **1.** Il sistema fornisce un feedback dettagliato sui criteri di sicurezza non rispettati.
   - **2.** L'utente crea una nuova password che rispetta i criteri richiesti.
:::

</div>

<div class="page"/>

**3b.** **La password e la password di conferma sono diverse:**

:::indice
   - **1.** Il sistema non permette la registrazione e avvisa l’utente.
   - **2.** L’utente inserisce nuovamente la password e la password di conferma.
:::

**3c.** **L’email non rispetta il formato corretto:**

:::indice
   - **1.** Il sistema rileva l'errore di formato e notifica l'utente.
   - **2.** L’utente corregge l’email secondo il formato richiesto.
:::

**3d.** **L’email è già stata usata:**

:::indice
   - **1.** Il sistema non permette la registrazione e avvisa l’utente.
   - **2.** L’utente prova ad effettuare nuovamente il login, continua dal punto 7 del flusso principale.
:::

**4a.** **L’utente non conferma l’email in tempo:**

:::indice
   - **1.** Il sistema non permette la conferma e informa l’utente che l’email di verifica non è più valida.
   - **2.** L’utente si registra nuovamente, ritornando al punto 1 del flusso principale.
:::

**7a.** **L’utente non ricorda la password o non riesce ad inserire la password corretta:**

:::indice
   - **1.** Il sistema non permette l’autenticazione.
   - **2.** L’utente richiede il recupero della password e inserisce l’email.
      - **2.1.** L’email non rispetta il formato corretto:
        - **2.1.1.** Il sistema non invia la mail e avvisa l’utente.
        - **2.1.2.** L’utente controlla e corregge l’email inserita.
      - **2.2.** L’email non è associata ad un utente:
        - **2.2.1.** Il sistema non invia la mail e avvisa l’utente.
        - **2.2.2.** L’utente prova a registrarsi, tornando al punto 1 del flusso principale.
:::

**7b.** **L’utente entra nella procedura di recupero password:**

:::indice
   - **1.** L’utente non entra in tempo nella procedura di recupero password:
       - **1.1.** Il sistema non permette il recupero della password e informa l’utente che la procedura non è più valida.
       - **1.2.** L’utente richiede nuovamente il recupero della password, ritornando al punto 2 del flusso alternativo 7a.
   - **2.** L’utente entra in tempo nella procedura di recupero password:
      - **2.1.** Il sistema invia una mail all’utente con il codice per il recupero della password.
      - **2.2.** Il sistema richiede all’utente di inserire il codice ricevuto.
      - **2.3.** L’utente inserisce il codice ricevuto.
      - **2.4.** Il sistema verifica il codice inserito dall’utente.
      - **2.5.** Il sistema richiede all’utente di inserire la nuova password e la nuova password di conferma.
      - **2.6.** L’utente inserisce la nuova password e la nuova password di conferma.
      - **2.7.** Il sistema controlla la nuova password e la sostituisce a quella precedente.
      - **2.8.** Il sistema invia una mail all’utente per confermare il cambio password.
      - **2.9.** L’utente effettua il login con la nuova password. Ritornerà al punto 7 del flusso principale.
:::

</div>

<div class="page"/>

**7c.** **L’utente inserisce la nuova password e la nuova password di conferma:**

:::indice
   - **1.** La password non segue i parametri di validità imposti dal sistema:
      - **1.1.** Il sistema non permette il recupero della password e avvisa l’utente.
      - **1.2.** L’utente inserisce una nuova password che rispetta i parametri.
      - **1.3.** Il sistema controlla la nuova password e la sostituisce a quella precedente.
      - **1.4.** Il sistema invia una mail all’utente per confermare il cambio password.
      - **1.5.** L’utente effettua il login con la nuova password.
   - **2.** La password e la password di conferma sono diverse:
      - **2.1.** Il sistema non permette il recupero della password e avvisa l’utente.
      - **2.2.** L’utente inserisce nuovamente la password e la password di conferma.
:::

**Requisiti speciali:** nessuno

**Elenco delle varianti tecnologiche e dei dati:**

1. L’email deve seguire lo standard RFC-2822
2. La password deve seguire i parametri di validità imposti dal sistema.

**Frequenza di ripetizione:** Viene effettuata ogni qualvolta un utente vuole registrarsi o accedere alla piattaforma.

**Problemi aperti:**

- Se in futuro dovesse cambiare il metodo di autenticazione di Google un
utente sarebbe ancora in grado di registrarsi nel sistema?

#### 2.2.2. Caso d'uso UC2: Inserimento e Validazione dei Dati

**Portata:** Sistema di pronostici per il Motomondiale

**Livello:** Obiettivo utente

**Attore primario:** Utente Registrato

**Parti interessate e interessi:**

- **Utente Registrato:** Vuole inserire dati aggiuntivi per arricchire l'analisi del sistema.
- **Analisti dei Dati:** Vogliono assicurarsi che i dati inseriti siano accurati e validi.
- **Sistema:** Vuole integrare dati affidabili per mantenere l'accuratezza delle analisi.

**Precondizioni:** L'utente deve essere registrato e autenticato nel sistema.

**Garanzia di successo (Post-condizioni):** I dati inseriti vengono validati e integrati nel sistema per l'analisi.

</div>

<div class="page"/>

**Scenario principale di successo (Flusso base):**

**1.** L'utente desidera contribuire al sistema di previsione del vincitore del Gran Premio del Motomondiale e accede alla sezione di inserimento dati dopo essersi autenticato.
**2.** Il sistema mostra all'utente le categorie di dati disponibili per l'inserimento, che includono: condizioni del circuito, informazioni sui piloti, risultati delle sessioni di prove libere e qualifiche, penalità, infortuni e incidenti.
**3.** L'utente seleziona la categoria di dati di interesse e procede con l'inserimento dei dati utilizzando i formati e le strutture richieste dal sistema, come form specifici o campi di input.
**4.** Il sistema esegue una verifica formale dei dati inseriti per assicurarsi che siano completi e conformi ai formati attesi, come la correttezza delle date, dei tempi, e delle informazioni numeriche.
**5.** Se i dati soddisfano i controlli formali, il sistema li inoltra automaticamente agli analisti per la validazione sostanziale.
**6.** Gli analisti ricevono una notifica dei nuovi dati sottoposti e iniziano la loro revisione, controllando l'accuratezza, la pertinenza e la credibilità delle informazioni fornite.
**7.** Una volta che gli analisti hanno confermato la validità dei dati, il sistema aggiorna le analisi complessive, integrando i nuovi dati nel modello di previsione e nelle statistiche disponibili agli altri utenti.
**8.** Il sistema invia una notifica all'utente che ha fornito i dati, confermando l'accettazione e l'integrazione dei dati nel sistema.
**9.** L'utente può poi visualizzare l'impatto del proprio contributo attraverso le analisi aggiornate disponibili nella piattaforma.

**Estensioni (Flussi alternativi):**

***a.** **In qualunque momento, il sistema fallisce:**

:::indice
   - **1.** Il sistema viene riavviato.
   - **2.** Il sistema notifica un errore.
      - **A.** L'utente ritorna al punto 1 del flusso principale.
      - **B.** Se il problema persiste, l'utente può contattare il supporto tecnico.
      - **C.** Se il problema persiste, l'utente può riprovare più tardi.**
      - **D.** L'utente rinuncia all'inserimento dei dati. Il caso d'uso termina.
:::

***b.** **Durante l'inserimento dei dati, l'utente chiude l'applicazione:**

:::indice
   - **1.** Il caso d'uso termina.
:::

***c.** **Durante l'inserimento dei dati, l'utente torna alla schermata principale:**

:::indice
   - **1.** Il sistema annulla l'inserimento dei dati e l'utente viene reindirizzato alla pagina principale. Il caso d'uso termina.
:::

**1a.** **L'utente non riesce ad accedere alla sezione di inserimento dati:**

:::indice
   - **1.** Il sistema notifica un errore di accesso.
   - **2.** L'utente può riprovare o contattare il supporto tecnico.
:::

</div>

<div class="page"/>

**3a.** **L'utente seleziona una categoria di dati non disponibile o errata:**

:::indice
   - **1.** Il sistema notifica la non disponibilità o l'errore.
   - **2.** L'utente ritorna alla selezione della categoria di dati.
:::

**3b.** **L'utente inserisce i dati e questi non vengono accettati dal sistema:**

:::indice
   - **1.** L'utente inserisce dati in un formato non supportato:
     - **1.1.** Il sistema notifica l'errore di formato.
     - **1.2.** L'utente modifica i dati nel formato corretto.
   - **2.** L'utente inserisce dati incompleti:
     - **2.1.** Il sistema notifica la mancanza di dati.
     - **2.2.** L'utente completa l'inserimento dei dati.
:::

**4a.** **I dati non superano la verifica formale:**

:::indice
   - **1.** Il sistema notifica l'errore nei dati.
   - **2.** L'utente corregge i dati e ripete l'inserimento.
:::

**5a.** **Il sistema non riesce a inviare i dati agli analisti:**

:::indice
   - **1.** Il sistema notifica un errore di trasmissione.
   - **2.** L'utente può riprovare l'inserimento.
:::

**6a** **Gli analisti non validano i dati:**

:::indice
   - **1.** Gli analisti trovano inesattezze nei dati:
     - **1.1.** Gli analisti segnalano i dati come non validi.
     - **1.2.** Il sistema notifica l'utente della non validità.
     - **1.3.** L'utente può modificare e reinserire i dati.
   - **2.** Ritardo nella risposta degli analisti:
     - **2.1.** Il sistema notifica l'utente del ritardo.
     - **2.2.** L'utente può attendere o ritirare i dati.
:::

**7a.** **Il sistema non riesce ad integrare i dati:**

:::indice
   - **1.** Il sistema notifica un errore di integrazione.
   - **2.** L'utente può riprovare l'inserimento.
:::

**8a.** **L'utente non riceve la notifica:**

:::indice
   - **1.** Il sistema tenta di reinviare la notifica.
   - **2.** Se il problema persiste, l'utente può verificare lo stato dell'inserimento manualmente.
:::

**Requisiti speciali:**

- Interfaccia intuitiva per l'inserimento dei dati.
- Sistema di notifica per informare l'utente sullo stato dei dati inseriti.
- Integrazione con API di servizi meteorologici per l'aggiornamento in tempo reale delle condizioni atmosferiche.

</div>

<div class="page"/>

**Elenco delle varianti tecnologiche e dei dati:**

- Formati accettati per l'inserimento dei dati (es. CSV, XML, JSON).
- Protocolli di comunicazione con gli analisti (es. API REST, WebSocket).

**Frequenza di ripetizione:** L'inserimento dei dati può avvenire in qualsiasi momento prima dell'elaborazione del pronostico finale.

**Problemi aperti:**

- Come gestire l'inserimento di grandi volumi di dati in modo efficiente?
- Quali misure adottare per garantire la sicurezza dei dati durante la trasmissione e la validazione?
- Come assicurare la stabilità e l'affidabilità dell'integrazione con le API dei servizi meteorologici?

#### 2.2.3. Caso d'uso UC3: Visualizzazione Statistiche e Analisi

**Portata:** Sistema di pronostici per il Motomondiale

**Livello:** Obiettivo utente

**Attore primario:** Utente Registrato

**Parti interessate e interessi:**

- **Utente Registrato:** Desidera visualizzare statistiche dettagliate e analisi per comprendere meglio le prestazioni dei piloti e le dinamiche del Gran Premio.

- **Sistema:** Vuole fornire informazioni accurate e aggiornate per migliorare l'esperienza utente e la qualità delle previsioni.

- **API di risultati sportivi:** Fornisce dati aggiornati e precisi sui risultati sportivi, compresi i dettagli sulle prestazioni dei piloti e le classifiche.

- **API del servizio meteorologico:** Fornisce informazioni meteorologiche precise e aggiornate, inclusi dati sulle condizioni meteorologiche attuali e previsioni future.

- **Social network:** Possono essere coinvolti se gli utenti desiderano condividere analisi, statistiche o previsioni con i loro contatti o seguaci. Possono offrire opzioni di condivisione per consentire agli utenti di diffondere informazioni interessanti o rilevanti attraverso le loro piattaforme.

**Precondizioni:** L'utente deve essere registrato e autenticato nel sistema.

**Garanzia di successo (Post-condizioni):** L'utente accede e visualizza le statistiche e le analisi desiderate.

</div>

<div class="page"/>

**Scenario Principale di Successo (Flusso Base):**

**1.** L'utente, interessato a consultare le statistiche e le analisi dei piloti e delle gare del Motomondiale, accede alla sezione dedicata del sistema dopo aver completato l'autenticazione.
**2.** Il sistema inizia il suo aggiornamento dati effettuando una chiamata ad API esterne per ottenere le informazioni più recenti sui piloti, sui tempi di gara, sui risultati delle qualifiche e delle prove libere, e su altri dati pertinenti. In parallelo, il sistema richiede e recupera automaticamente i dati meteorologici attuali e le previsioni per i giorni di gara da un servizio meteorologico esterno, attraverso la relativa API.
**3.** Il sistema elabora e presenta all'utente diverse categorie di dati, quali le prestazioni dei piloti, i dati storici dei circuiti, e le condizioni meteorologiche, offrendo un'interfaccia intuitiva per la navigazione.
**4.** L'utente naviga tra le categorie disponibili e seleziona quella di interesse per una visualizzazione più dettagliata.
**5.** Il sistema mostra una panoramica generale della categoria selezionata, fornendo un sommario delle informazioni disponibili.
**6.** L'utente decide di esaminare in dettaglio un'area specifica, ad esempio le prestazioni di un pilota in particolare o l'analisi di un Gran Premio specifico.
**7.** Il sistema risponde fornendo dettagli approfonditi sulla selezione dell'utente, inclusi grafici interattivi, un storico delle prestazioni, e comparazioni con altri piloti o gare precedenti.
**8.** L'utente utilizza gli strumenti forniti dal sistema per filtrare o ordinare i dati secondo vari criteri, personalizzando così la visualizzazione in base alle proprie esigenze o interessi specifici.
**9.** Navigando tra le analisi e le statistiche, l'utente acquisisce le informazioni desiderate, potendo approfondire gli aspetti di interesse con ulteriori dettagli e analisi predictive.
**10.** L'utente ha la possibilità di condividere le analisi visualizzate sui social network o inviarle via email attraverso le funzioni di condivisione integrate nel sistema, facilitando la diffusione delle informazioni e promuovendo la partecipazione e l'interazione all'interno della comunità di appassionati.

**Estensioni (Flussi Alternativi):**

***a.** **In qualunque momento, il sistema fallisce:**

:::indice
   - **1.** Il sistema viene riavviato.
   - **2.** Il sistema notifica un errore.
      - **A.** L'utente ritorna al punto 1 del flusso principale.
      - **B.** Se il problema persiste, l'utente può contattare il supporto tecnico.
      - **C.** Se il problema persiste, l'utente può riprovare più tardi.**
      - **D.** L'utente rinuncia alla visualizzazione del pronostico. Il caso d'uso termina.
:::

***b.** **Durante la visualizzazione delle analisi, l'utente chiude l'applicazione:**

:::indice
   - **1.** Il caso d'uso termina.
:::

**1a.** **L'utente non riesce ad accedere alla sezione:**

:::indice
   - **1.** Il sistema notifica un errore di accesso.
   - **2.** L'utente può riprovare o contattare il supporto tecnico.
:::

**2a.** **Il sistema non riesce a recuperare i dati:**

:::indice
   - **1.** Il sistema notifica un errore di caricamento.
   - **2.** L'utente può riprovare più tardi.
:::

**3a.** **Il sistema non riesce a presentare le categorie di dati:**

:::indice
   - **1.** Il sistema notifica un errore di caricamento.
   - **2.** L'utente può riprovare più tardi.
:::

**4a.** **L'utente seleziona una categoria non disponibile o errata:**

:::indice
   - **1.** Il sistema notifica che la categoria non è disponibile.
   - **2.** L'utente ritorna alla selezione della categoria.
:::

**5a.** **Il sistema non riesce a mostrare la panoramica:**

:::indice
   - **1.** Il sistema notifica un errore di visualizzazione.
   - **2.** L'utente può riprovare o scegliere un'altra categoria.
:::

**5b.** **L'utente non riesce a visualizzare la panoramica:**

:::indice
   - **1.** Il sistema notifica un errore di visualizzazione.
   - **2.** L'utente può riprovare o scegliere un'altra categoria.
:::

**6a.** **L'area specifica scelta non è disponibile:**

:::indice
   - **1.** Il sistema notifica la non disponibilità dell'area.
   - **2.** L'utente ritorna alla panoramica generale per scegliere un'altra area.
:::

**7a.** **Il sistema non riesce a fornire dettagli approfonditi:**

:::indice
   - **1.** Il sistema notifica un errore di caricamento dei dettagli.
   - **2.** L'utente può riprovare o scegliere un'altra area di approfondimento.
:::

**7b.** **L'utente non riesce a visualizzare i dettagli approfonditi:**

:::indice
   - **1.** Il sistema notifica un errore di visualizzazione.
   - **2.** L'utente può riprovare o scegliere un'altra area di approfondimento.
:::

**8a.** **L'utente non riesce a filtrare o ordinare i dati:**

:::indice
   - **1.** Il sistema notifica un errore di filtraggio o ordinamento.
   - **2.** L'utente può riprovare o scegliere un'altra area di approfondimento.
:::

**9a.** **L'utente non riesce a visualizzare le analisi:**

:::indice
   - **1.** Il sistema notifica un errore di visualizzazione.
   - **2.** L'utente può riprovare o scegliere un'altra area di approfondimento.
:::

</div>

<div class="page"/>

**10a.** **L'utente non riesce a condividere le analisi:**

:::indice
   - **1.** L'utente sceglie di condividere le analisi/statistiche sui social network.
     - **1.1.** Il sistema fornisce opzioni per la condivisione su varie piattaforme (es. Facebook, Twitter).
       - **1.1.1.** Se la condivisione non riesce:
         - **A.** Il sistema notifica un errore di condivisione.
         - **B.** L'utente può riprovare o scegliere un'altra piattaforma o la condivisione tramite email.
      - **1.1.2.** Il sistema genera un riferimento (URL) all'analisi che viene condiviso sulla piattaforma scelta dall'utente.
   - **2.** L'utente sceglie di condividere le analisi/statistiche tramite email.
       - **2.1.** Se la condivisione non riesce:
          - **A.** Il sistema notifica un errore di condivisione.
          - **B.** L'utente può riprovare o scegliere un'altra piattaforma o scegliere nuovamente la condivisione tramite email.
       - **2.2.** Il sistema genera un URI (mailto) all'analisi.
:::
</div>

**Requisiti speciali:**

- Interfaccia grafica intuitiva e reattiva per la visualizzazione dei dati.
- Capacità di generare grafici e rappresentazioni visive dei dati.
- Funzionalità di condivisione integrata per permettere agli utenti di condividere analisi e statistiche sui social network.

**Elenco delle varianti tecnologiche e dei dati:**

- Diversi formati di visualizzazione dei dati (grafici a barre, linee, torta, ecc.).
- Opzioni di filtraggio e ordinamento avanzate.

**Frequenza di ripetizione:** Gli utenti possono accedere a questa funzionalità in qualsiasi momento.

**Problemi aperti:**

- Come garantire che le statistiche e le analisi siano sempre aggiornate e accurate?
- Quali strumenti di visualizzazione dati implementare per massimizzare la comprensione dell'utente?
- Quali misure di sicurezza implementare per proteggere i dati degli utenti durante la condivisione sui social network?

</div>

<div class="page"/>

## **3. Modello di dominio**

### **3.1. Diagramma del modello di dominio**

![Alt text](<img/png/Modello di dominio.png>)

### **3.2. Descrizione del modello di dominio**

Il modello di dominio per il sistema di pronostici del Motomondiale riflette la distinzione tra le varie tipologie di utenti: gli appassionati di sport, gli analisti di dati, e gli amministratori, che ereditano tutti dalla classe Utente. A seconda del ruolo, l'utente potrà avere accesso a funzionalità differenti all'interno del sistema.

Gli appassionati di sport possono inserire dati rilevanti, come informazioni su eventi specifici o condizioni atmosferiche, e visualizzare statistiche e analisi dettagliate. Possono anche partecipare a discussioni sui pronostici e condividere le proprie previsioni sui social media o via email.

Gli analisti di dati, con accessi più avanzati, possono esaminare i dati forniti dagli utenti, convalidare le informazioni e integrarle nel sistema per affinare i modelli di previsione. Hanno la capacità di generare pronostici complessi basati su un ampio insieme di variabili, inclusi i dati storici delle performance dei piloti e delle squadre, nonché le condizioni del tracciato.

</div>

<div class="page"/>

## **4. SSD di sistema**

### **4.1. UC1-SSD: Autenticare utente**

#### 4.1.1. SSD principale per il flusso base di successo

![Alt text](<img/png/UC1/UC1 - FP - Autenticare Utente.png>)

</div>

<div class="page"/>

#### 4.1.2. SSD per flussi alternativi

##### 4.1.2.1. Autenticazione con Google

![Alt text](<img/png/UC1/UC1 - FA - Autenticare Utente Google.png>)

</div>

<div class="page"/>

##### 4.1.2.2. Recupero Password

![Alt text](<img/png/UC1/UC1 - FA - Recupero password.png>)

</div>

<div class="page"/>

### **4.2. UC2-SSD: Inserimento e Validazione dei Dati**

#### 4.2.1. SSD principale per il flusso base di successo

![Alt text](<img/png/UC2/UC2 - FP - Inserimento e Validazione dei Dati.png>)

</div>

<div class="page"/>

#### 4.2.2. SSD per flussi alternativi

##### 4.2.2.1. Errore nell'Inserimento dei Dati

![Alt text](<img/png/UC2/UC2 - FA - Errore inserimento dei dati.png>)

</div>

<div class="page"/>

### **4.3. UC3-SSD: Visualizzazione Statistiche e Analisi**

#### 4.3.1. SSD principale per il flusso base di successo

![Alt text](<img/png/UC3/UC3 - FP - Visualizzazione Statistiche e Analisi.png>)

</div>

<div class="page"/>

#### 4.3.2. SSD per flussi alternativi

##### 4.3.2.1. Condivisione delle Analisi

###### 4.3.2.1.1. Condivisione delle analisi tramite email

![Alt text](<img/png/UC3/UC3 - FA - Condivisione Analisi Email.png>)

###### 4.3.2.1.2. Condivisione delle analisi sui social network

![Alt text](<img/png/UC3/UC3 - FA - Condivisione Analisi Social.png>)

</div>

<div class="page"/>

## **5. Contratti delle operazioni**

### **5.1. Contratto CO1:** `registraAccount(username, email, password)`

**Operazione:** `registraAccount(username: String, email: String, password: String)`
**Riferimenti:** casi d’uso: Autenticare un utente.
**Pre-condizioni:**

- I dati inseriti dall’utente (username, email, password) sono validi e conformi ai requisiti del sistema (es. formato email corretto, password con requisiti di sicurezza).
- L'email fornita non è già associata a un altro account esistente nel sistema.

**Post-condizioni:**

- È stata creata un’istanza `u` di `Utente`:
  - `u.username` è stato impostato al valore di `username`.
  - `u.email` è stato impostato al valore di `email`.
  - `u.password` è stato impostato al valore di `password`.
- È stata creata un’istanza `p` di `Profilo`:
  - Gli attributi di `p` sono stati inizializzati (ad esempio, impostazioni di default, data di creazione, ecc.).
- È stata creata un’associazione tra `p` (Profilo) e `u` (Utente), collegando il profilo all'utente appena creato.

### **5.2. Contratto CO2:** `accessoAccount(email, password)`

**Operazione:** `accessoAccount(email: String, password: String)`
**Riferimenti:** casi d’uso: Autenticare un utente.
**Pre-condizioni:**

- L'email fornita è associata a un account esistente nel sistema.
- La password fornita è corretta per l'account specificato.

**Post-condizioni:**

- L'utente è autenticato e può accedere alle funzionalità del sistema.

### **5.3. Contratto CO3:** `recuperaPassword(email)`

**Operazione:** `recuperaPassword(email: String)`
**Riferimenti:** casi d’uso: Autenticare un utente.
**Pre-condizioni:**

- L'email fornita è associata a un account esistente nel sistema.

**Post-condizioni:**

- L'utente riceve un'email con un link per il recupero della password.
- Il link è valido per un periodo di tempo limitato.

### **5.4. Contratto CO4:** `aggiungiDato(dato)`

**Operazione:** `aggiungiDato(dato: Dato)`
**Riferimenti:** casi d’uso: Inserimento e Validazione dei Dati.
**Pre-condizioni:**

- L'utente è autenticato e autorizzato ad aggiungere dati.
- Il dato fornito è nel formato corretto e contiene tutte le informazioni necessarie.

**Post-condizioni:**

- È stata creata un’istanza `d` di `Dato`.
- Gli attributi di `d` sono stati impostati con i valori forniti.
- Il dato `d` è stato aggiunto al sistema per l'analisi.

### **5.5. Contratto CO5:** `calcolaPronostico()`

**Operazione:** `calcolaPronostico()`
**Riferimenti:** casi d’uso: Inserimento e Validazione dei Dati.
**Pre-condizioni:**

- I dati sono stati inseriti dall'utente e validati dagli analisti.
- I dati necessari per il calcolo del pronostico sono disponibili e aggiornati.

**Post-condizioni:**

- Il sistema ha calcolato il pronostico per il Gran Premio corrente.
- Il pronostico è disponibile per la visualizzazione da parte degli utenti.

### **5.6. Contratto CO6:** `visualizzaAnalisi(categoria)`

**Operazione:** `visualizzaAnalisi(categoria: Categoria)`
**Riferimenti:** casi d’uso: Visualizzazione Statistiche e Analisi.
**Pre-condizioni:**

- L'utente è autenticato.
- La categoria specificata è valida e disponibile nel sistema.

**Post-condizioni:**

- Il sistema recupera e mostra le statistiche e le analisi relative alla categoria specificata.
- Le informazioni visualizzate sono aggiornate e accurate secondo i dati più recenti disponibili.

</div>

<div class="page"/>

### **5.7. Contratto CO7:** `condividiAnalisi(metodoCondivisione, analisi)`

**Operazione:** `condividiAnalisi(metodoCondivisione: MetodoCondivisione, analisi: Analisi)`
**Riferimenti:** casi d’uso: Visualizzazione Statistiche e Analisi.
**Pre-condizioni:**

- L'utente è autenticato.
- L'analisi da condividere è stata precedentemente generata e è disponibile.
- Il metodo di condivisione specificato (es. social network, email) è supportato e configurato.

**Post-condizioni:**

- L'analisi è stata condivisa attraverso il metodo specificato.
- Il sistema registra la condivisione effettuata.

</div>

<div class="page"/>

## **6. Architettura del sistema**

<br>

![Alt text](<img/png/Architettura del sistema.png>)

</div>

<div class="page"/>

### **6.1. Descrizione dell'architettura del sistema**

L'architettura del sistema "El Campeón" è concepita per fornire un ambiente robusto e scalabile per il calcolo dei pronostici nel contesto dei Gran Premi del Motomondiale. Il sistema è strutturato secondo un modello a strati che separa le responsabilità in modo chiaro e definisce interfacce specifiche per le diverse categorie di utenti e i servizi tecnici. Di seguito viene illustrata l'organizzazione dei vari strati e componenti dell'architettura.

#### UI (User Interface):
Il livello più alto dell'architettura è rappresentato dalle interfacce utente, distinte in:
- **Interfaccia utenti standard**: Consente agli utenti di interagire con il sistema per visualizzare le analisi, inserire dati e condividere le informazioni attraverso i social media.
- **Interfaccia analisti**: Fornisce agli analisti un accesso a funzioni avanzate per la modifica, la validazione e l'analisi dei dati.

#### Applicazione:
Il livello dell'applicazione funge da mediatore tra l'UI e il dominio, con:
- **Controller Utenti**: Gestisce le richieste provenienti dagli utenti standard, orchestrando le operazioni di visualizzazione e inserimento dati.
- **Controller Analisti**: Coordina le richieste degli analisti, garantendo che la logica di business venga eseguita in modo sicuro ed efficiente.

#### Dominio:
Il cuore dell'architettura è il dominio, dove risiede la logica di business, composto da:
- **Pronostici**: Contiene algoritmi e processi per calcolare i pronostici basati sui dati storici e correnti.
- **Dati utente**: Gestisce l'integrità e la validazione dei dati forniti dagli utenti, assicurandosi che siano affidabili e utili per le analisi.

#### Servizi Tecnici:
Questo strato fornisce servizi di supporto fondamentali per l'operatività del sistema, inclusi:
- **Persistenza**: Assicura la gestione ottimale dei dati, permettendone il salvataggio e il recupero.
- **Logging**: Registra le attività del sistema per monitoraggio, auditing e troubleshooting.
- **Integrazione API**: Permette l'integrazione con API esterne, essenziale per l'acquisizione di dati aggiornati e per l'arricchimento delle analisi.

#### Dati e API:
Il livello dati e API si occupa della gestione delle informazioni e delle connessioni esterne con:
- **Database Dati**: Archiviazione centralizzata dei dati raccolti dal sistema.
- **API esterne**: Interfacce per integrare dati di terze parti, come i risultati delle gare e le condizioni meteorologiche.

</div>
