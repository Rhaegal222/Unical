# **Relazione del Progetto: Sistema di Previsione per il Motomondiale**

## **Breve Descrizione del Progetto**

Il progetto in esame è un'applicazione JavaFX progettata per calcolare previsioni analitiche sul possibile esito dei Gran Premi nel Motomondiale. L'applicazione dovrebbe consentire agli utenti di accedere ai dati storici e attuali sui piloti e sulle gare, e di contribuire con informazioni aggiuntive che possono influenzare le previsioni. Le funzionalità chiave dovrebbero includere l'analisi delle prestazioni dei piloti, la gestione delle impostazioni utente e la condivisione dei dati attraverso social network o email.

## **Implementazione Attuale**

Al momento attuale, il progetto ha visto l'implementazione completa del caso d'uso relativo all'autenticazione dell'utente. Questo include il login, la registrazione, e l'interfaccia utente associata. L'utente puó creare un account, accedere e gestire le proprie informazioni di login attraverso un'interfaccia intuitiva e sicura, puó inoltre personalizzare l'interfaccia cambiando il tema e scegliere la lingua. Nonostante le altre funzionalitá pianificate, come la previsione delle gare e la condivisione dei dati attraverso social network o email, non siano state ancora realizzate, l'applicazione ha una solida base su cui costruire grazie all'utilizzo di pattern architetturali e di design appropriati.

## **Il Pattern Command nel Progetto**

Il design pattern Command è stato implementato per incapsulare le richieste di azione come oggetti, consentendo così una maggiore flessibilità nell'ordine delle operazioni e nella loro esecuzione. Nel contesto dell'applicazione, il pattern è stato utilizzato per gestire le interazioni dell'utente con l'interfaccia grafica, come il cambio di scene, l'autenticazione degli utenti, la registrazione, il salvataggio delle impostazioni, e altri comandi specifici dell'interfaccia.

Questo approccio ha portato numerosi benefici al progetto. Primo fra tutti, ha aumentato la modularità del codice, poiché le azioni sono state separate dalla loro esecuzione. In secondo luogo, ha reso il sistema più estensibile e manutenibile, dato che l'aggiunta di nuove funzionalità o la modifica di quelle esistenti non richiede grandi cambiamenti nel codice preesistente.

## **Tecnologie Utilizzate**

Il sistema sfrutta varie tecnologie per fornire un'esperienza utente ricca e interattiva. Tra queste, il feed RSS è utilizzato per recuperare notizie e aggiornamenti in tempo reale che possono influenzare le previsioni delle gare. L'invio di email è integrato per permettere la comunicazione diretta con gli utenti, fornendo notifiche e conferme, come nel caso di registrazione o reset della password. Inoltre, l'applicazione utilizza un database SQLite per immagazzinare dati sugli utenti e le loro impostazioni.

L'interfaccia utente è costruita su JavaFX e FXML, offrendo un'interazione intuitiva e una presentazione grafica che può essere personalizzata attraverso temi CSS. La possibilità di scegliere tra diverse lingue rende l'applicazione accessibile a un pubblico internazionale, aumentandone l'usabilità. Infine, il sistema implementa il font FontAwesome per aggiungere icone vettoriali, migliorando l'estetica e la comprensibilità delle interfacce utente.

## **Conclusioni**

L'uso del pattern Command e la scelta delle tecnologie hanno creato un sistema robusto e facilmente espandibile che serve come solida piattaforma per le previsioni analitiche nel campo del Motomondiale, promettendo di essere uno strumento prezioso per gli appassionati e gli analisti del settore. Nonostante l'implementazione attuale sia limitata all'autenticazione degli utenti e alla visualizzazione delle notizie, le fondamenta architetturali poste forniscono una base solida per l'espansione futura e l'integrazione delle funzionalità pianificate.
