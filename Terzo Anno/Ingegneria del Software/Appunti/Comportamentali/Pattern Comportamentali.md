# Pattern Comportamentali

- [Template Method](template-method)
- [Interpreter](interpreter)
- [Mediator](mediator)
- [Chain of Responsibility](chain-of-responsibility)
- [Observer](observer)
- [Strategy](strategy)
- [Command](command)
- [State](state)
- [Visitor](visitor)
- [Iterator](iterator)
- [Memento](memento)

## Template Method

- **Scopo**: definire lo scheletro di un algoritmo in una operazione, posticipando alcuni passi a sottoclassi. Template Method permette alle sottoclassi di ridefinire certi passi di un algoritmo senza modificare la struttura dell'algoritmo stesso.

- **Applicabilità**: quando si vuole che le sottoclassi estendano certi passi di un algoritmo, ma non la struttura dell'algoritmo stesso. Quando si hanno più classi che contengono algoritmi simili con qualche differenza. Quando si vuole evitare duplicazione di codice. Quando si vuole controllare l'estensione di una classe.
