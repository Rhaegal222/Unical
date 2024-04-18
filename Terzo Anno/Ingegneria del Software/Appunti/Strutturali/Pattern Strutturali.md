# Pattern Strutturali

- Adapter (AD)
- Bridge (BR)
- Composite (CO)
- Decorator (DE)
- Facade (FA)
- Proxy (PR)

## Adapter (AD)

Il pattern Adapter (AD) ha l'intento di convertire l'interfaccia di una classe in un'altra interfaccia che i client si aspettano. Questo permette a classi di collaborare tra loro che altrimenti non potrebbero farlo a causa di interfacce incompatibili. L'Adapter, noto anche come Wrapper, funge da intermediario, consentendo la comunicazione armoniosa tra componenti con interfacce eterogenee. In questo modo, il pattern Adapter favorisce la riusabilità del codice, poiché permette l'integrazione di classi esistenti in contesti in cui le loro interfacce originali potrebbero risultare inconciliabili.

### AD Motivation

La motivazione di utilizzare il pattern Adapter (AD) si presenta quando una classe progettata per essere riutilizzata non può essere impiegata a causa dell'incompatibilità della sua interfaccia con quella richiesta dal dominio specifico. Ad esempio, consideriamo un editor grafico che consente agli utenti di disegnare e organizzare linee, poligoni, testi, ecc. L'editor implementa un'interfaccia astratta Shape che definisce una forma modificabile e in grado di disegnarsi. Utilizzando la sottoclasse Shape, implementiamo classi come LineShape per linee e PolygonShape per poligoni.

Tuttavia, la gestione di forme testuali risulta complessa rispetto alle linee. Supponiamo che esista un toolkit sofisticato, basato su una classe TextView, progettato per visualizzare ed editare testo. Questa classe ha un'interfaccia diversa da quella di Shape, rendendo impossibile l'uso intercambiabile di oggetti TextView e Shape.

In questo contesto, possiamo definire TextShape in modo che adatti l'interfaccia TextView a quella di Shape. Questo adattamento può essere realizzato utilizzando l'ereditarietà o la composizione di oggetti, consentendo così l'integrazione fluida di oggetti con interfacce eterogenee nel sistema, migliorando la riusabilità del codice e la flessibilità del design.
