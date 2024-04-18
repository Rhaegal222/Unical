# Pattern Creazionali

- Factory Method (FM)
- Abstract Factory (AF)
- Singleton (SI)
- Prototype (PR)
- Builder (BU)

## Factory Method (FM)

Il Factory Method è un design pattern che definisce un'interfaccia per creare un oggetto, ma lascia alle sottoclassi la decisione su quale classe istanziare. Questo permette a una classe di delegare l'istanziazione a sottoclassi specifiche, consentendo una maggiore flessibilità e modularità nel codice. Il Factory Method è anche conosciuto come "costruttore virtuale" e viene utilizzato per posticipare l'istanziazione di un oggetto alle sottoclassi.

### FM Motivation

Consideriamo un framework per applicazioni che possono presentare all'utente più documenti. Ad esempio, per creare un'applicazione di disegno, definiamo le classi DrawingApplication e DrawingDocument. La classe Application è responsabile della gestione dei documenti. Tuttavia, la classe Application non può prevedere quale sottoclasse di Document istanziare. Le sottoclassi di Application ridefiniscono un'operazione astratta CreateDocument per restituire la sottoclasse appropriata di Document.

![alt text](http://web.tiscali.it/sasadangelo/Informatica/design%20patterns/gof/factorymeth/fmeth049.gif)

### FM Applicability

Il Factory Method è un design pattern che viene utilizzato quando una classe non può prevedere la classe degli oggetti che deve creare. Invece, lascia alle sottoclassi la decisione su quale classe istanziare. Questo pattern è utile quando una classe desidera che le sue sottoclassi specificano gli oggetti che crea. Inoltre, può essere utilizzato quando le classi delegano la responsabilità a una delle diverse sottoclassi helper e si desidera localizzare la conoscenza su quale sottoclasse helper è il delegato.

### FM Structure

- Il Creatore è una classe astratta:
    un'operazione() è implementata delegando a un factoryMethod() non implementato la creazione di un Prodotto
- Il Prodotto è un'interfaccia
- Il ConcreteCreator implementa il factoryMethod(), determinando il Prodotto specifico

#### Structure (and Participants and Collaborations)

![alt text](http://web.tiscali.it/sasadangelo/Informatica/design%20patterns/gof/factorymeth/fmethod.gif)

### FM Participants

Il Factory Method è un design pattern che definisce un'interfaccia per creare un oggetto, ma lascia alle sottoclassi la decisione su quale classe istanziare. Questo permette a una classe di delegare l'istanziazione a sottoclassi specifiche, consentendo una maggiore flessibilità e modularità nel codice.

Nel contesto del Factory Method, sono presenti quattro ruoli principali. Il ruolo di "Product" rappresenta l'interfaccia degli oggetti che il factory method crea. Il ruolo di "ConcreteProduct" implementa l'interfaccia del Product. Il ruolo di "Creator" dichiara il factory method, che restituisce un oggetto di tipo Product, e può anche definire un'implementazione di default del Factory Method. Infine, il ruolo di "ConcreteCreator" sovrascrive il factory method per restituire un'istanza di ConcreteProduct.

Questo pattern è utile quando una classe desidera che le sue sottoclassi specificano gli oggetti che crea. Inoltre, può essere utilizzato quando le classi delegano la responsabilità a una delle diverse sottoclassi helper e si desidera localizzare la conoscenza su quale sottoclasse helper è il delegato.

### FM Collaboration

Il Creator si affida alle sue sottoclassi per definire il factory method in modo che restituisca un'istanza del ConcreteProduct appropriato.

### FM Consequences

Il Factory Method elimina la necessità di vincolare classi specifiche dell'applicazione nel tuo codice. Il codice si occupa solo dell'interfaccia del Product. I client potrebbero dover sottoclassificare il Creator solo per creare un oggetto ConcreteProduct specifico. Questo è accettabile quando il client deve comunque sottoclassificare la classe Creator! Altrimenti, è un inconveniente (la gerarchia può esplodere).

Il Factory Method fornisce dei punti di estensione per le sottoclassi. Creare oggetti all'interno di una classe con un Factory Method è sempre più flessibile rispetto alla creazione diretta di un oggetto. Il Factory Method offre alle sottoclassi un punto di estensione per fornire una versione estesa di un oggetto. Inoltre, il Factory Method collega gerarchie di classi parallele. Le gerarchie di classi parallele si verificano quando una classe delega alcune delle sue responsabilità a una classe separata.

![alt text](http://web.tiscali.it/sasadangelo/Informatica/design%20patterns/gof/factorymeth/fmeth048.gif)

### FM Implementation

Il Factory Method offre due possibilità:

1. Il Creator è una classe astratta e non fornisce un'implementazione per i Factory Method che offre.
2. Il Creator è una classe concreta e fornisce un'implementazione predefinita per i Factory Method che offre.

Inoltre, il Factory Method può essere parametrizzato, consentendo la creazione di diversi tipi di prodotti. Il Factory Method prende un parametro che identifica il tipo di oggetto da creare, ma potrebbe richiedere il downcasting.

È buona pratica utilizzare convenzioni di denominazione che rendano chiaro l'uso dei Factory Method.

Infine, è possibile utilizzare i template per evitare la sottoclassificazione.

#### Naming Conventions

```cpp
public class Creator {
    public:
        virtual Product* CreateProduct() = 0;
};

template <class TheProduct>
class StandardCreator : public Creator {
    public:
        virtual Product* CreateProduct();
};

template <class TheProduct>
Product* StandardCreator<TheProduct>::CreateProduct(){
    return new TheProduct;
};
```

### Sample code

```cpp
class MazeGame{
    public:
        Maze* CreateMaze();

    // factory methods:

        virtual Maze* MakeMaze() const {return new Maze;}
        virtual Room* MakeRoom(int n) const {return new Room(n);}
        virtual Wall* MakeWall() const {return new Wall;}
        virtual Door* MakeDoor(Room* r1, Room* r2) const {return new Door(r1, r2);}
};

Maze MazeGame::CreateMaze() {
    Maze* aMaze = MakeMaze();

    Room* r1 = MakeRoom(1);
    Room* r2 = MakeRoom(2);
    Door* theDoor = MakeDoor(r1, r2);
    
    aMaze->AddRoom(r1);
    aMaze->AddRoom(r2);
    
    r1->SetSide(North, MakeWall());
    r1->SetSide(East, theDoor);
    r1->SetSide(South, MakeWall());
    r1->SetSide(West, MakeWall());
    
    r2->SetSide(North, MakeWall());
    r2->SetSide(East, MakeWall());
    r2->SetSide(South, MakeWall());
    r2->SetSide(West, theDoor);
    
    return aMaze;
}

class BombedMazeGame : public MazeGame {
public:
    BombedMazeGame();
    virtual Wall* MakeWall() const { return new BombedWall; }
    virtual Room* MakeRoom(int n) const { return new RoomWithABomb(n); }
};

class EnchantedMazeGame : public MazeGame {
public:
    EnchantedMazeGame();
    virtual Room* MakeRoom(int n) const { return new EnchantedRoom(n, CastSpell()); }
    virtual Door* MakeDoor(Room* r1, Room* r2) const { return new DoorNeedingspell(r1, r2); }
protected:
    Spell CastSpell() const;
};
```

### FM Known uses and Related Patterns

I pattern conosciuti che utilizzano il pattern Factory Method includono Abstract Factory, Template Methods e Prototypes. Questi pattern sono ampiamente utilizzati in molti software. Il pattern Factory Method è strettamente correlato al pattern Abstract Factory, Template Methods e Prototypes. Questi pattern possono essere combinati per creare soluzioni più robuste.

## Abstract Factory (AF)

L'Abstract Factory è un design pattern che fornisce un'interfaccia per creare famiglie di oggetti correlati senza specificare le loro classi concrete. Questo pattern permette di separare la creazione degli oggetti dalla loro implementazione, consentendo di sostituire facilmente una famiglia di oggetti con un'altra. L'Abstract Factory è anche conosciuto come "Kit".

### AF Motivation

Immagina un kit di interfaccia utente che supporti diversi standard di aspetto e comportamento, come Motif e Presentation Manager. Diversi stili definiscono diverse apparenze e comportamenti per gli "elementi" dell'interfaccia utente, come barre di scorrimento, finestre e pulsanti. Per garantire la portabilità tra standard di aspetto e comportamento, un'applicazione non dovrebbe fissare staticamente i suoi elementi per un particolare stile.

### AF Applicability

Utilizza l'Abstract Factory quando è necessario che un sistema sia indipendente dal modo in cui i suoi prodotti sono creati, composti e rappresentati. Quando è richiesta la configurazione di un sistema con una delle molteplici famiglie di prodotti disponibili. Quando una famiglia di oggetti prodotto correlati è progettata per essere utilizzata insieme e è necessario imporre tale vincolo. Infine, quando si desidera fornire una libreria di classi di prodotti e si intende rivelare solo le loro interfacce, mantenendo nascoste le relative implementazioni.

### AF Participants

L'Abstract Factory, anche nota come Widget Factory, definisce un'interfaccia per la creazione di prodotti astratti. Le Concrete Factory, come MotifWidgetFactory, implementano le operazioni per la creazione di prodotti concreti. Gli Abstract Product, come Window e ScrollBar, dichiarano un'interfaccia per un tipo di oggetto prodotto. I Concrete Product, ad esempio MotifWindow, definiscono gli oggetti prodotti da Abstract Factory e implementano l'interfaccia AbstractProduct. Il Cliente utilizza esclusivamente le interfacce dichiarate da Abstract Factory e Abstract Product. In questo modo, il sistema mantiene un alto grado di astrazione, consentendo la sostituzione agevole di famiglie di oggetti correlati.

### AF Collaborations

Durante l'esecuzione, viene creata un'unica istanza di una classe ConcreteFactory. Questa factory concreta genera oggetti prodotto con un'implementazione specifica. Per creare diversi oggetti prodotto, i clienti dovrebbero utilizzare una factory concreta differente. L'AbstractFactory ritarda la creazione degli oggetti prodotto alla sua sottoclasse ConcreteFactory.

### AF Consequences

Il pattern Abstract Factory isola le classi concrete e facilita il controllo sulle classi degli oggetti. I clienti manipolano le istanze attraverso le loro interfacce astratte, evitando che i nomi delle classi dei prodotti compaiano nel codice del cliente. Inoltre, agevola lo scambio di famiglie di prodotti, poiché la classe di una factory concreta compare solo una volta nell'applicazione. Questo semplifica la modifica della factory concreta utilizzata dall'applicazione e consente di adottare diverse configurazioni di prodotti semplicemente cambiando la factory concreta.

Promuove coerenza tra i prodotti, in quanto un'applicazione utilizza oggetti appartenenti a una sola famiglia alla volta. Tuttavia, il supporto per nuovi tipi di prodotti risulta complicato. Estendere le fabbriche astratte per produrre nuovi tipi di prodotti non è un compito facile. Sostenere nuovi tipi di prodotti richiede l'estensione dell'interfaccia della fabbrica, il che implica la modifica della classe della fabbrica astratta e di tutte le sue sottoclassi. Questo problema può essere (parzialmente) risolto (vedi implementazione).

### AF implementation

Le fabbriche come singleton: un'applicazione richiede generalmente una sola istanza di ConcreteFactory, trattata come Singleton.

Creazione dei prodotti: Abstract Factory (AF) definisce solo un'interfaccia per la creazione di prodotti, spettando alle sottoclassi di ConcreteFactory la responsabilità effettiva della creazione. L'implementazione di AF avviene attraverso il Factory Method o il Prototype.

Definizione di fabbriche estensibili: Solitamente, AF definisce un'operazione diversa per ciascun tipo di prodotto, ma un design più flessibile prevede l'aggiunta di un parametro alle operazioni di creazione oggetti. Questo approccio è più agevole nell'utilizzo in linguaggi dinamicamente tipizzati come Smalltalk rispetto a C++ (vedi implementazione del Factory Method).

### AF Sample Code

```cpp
class MazeFactory {
public:
    MazeFactory();
    virtual Maze* MakeMaze() const { return new Maze; }
    virtual Wall* MakeWall() const { return new Wall; }
    virtual Room* MakeRoom(int n) const { return new Room(n); }
    virtual Door* MakeDoor(Room* r1, Room* r2) const { return new Door(r1, r2); }
};

Maze* MazeGame::CreateMaze(MazeFactory& factory) {
    Maze* aMaze = factory.MakeMaze();
    Room* r1 = factory.MakeRoom(1);
    Room* r2 = factory.MakeRoom(2);
    Door* aDoor = factory.MakeDoor(r1, r2);
    
    aMaze->AddRoom(r1);
    aMaze->AddRoom(r2);
    
    r1->SetSide(North, factory.MakeWall());
    r1->SetSide(East, aDoor);
    r1->SetSide(South, factory.MakeWall());
    r1->SetSide(West, factory.MakeWall());
    
    r2->SetSide(North, factory.MakeWall());
    r2->SetSide(East, factory.MakeWall());
    r2->SetSide(South, factory.MakeWall());
    r2->SetSide(West, aDoor);
    
    return aMaze;
}

class EnchantedMazeFactory : public MazeFactory {
public:
    EnchantedMazeFactory();
    virtual Room* MakeRoom(int n) const { return new EnchantedRoom(n, CastSpell()); }
    virtual Door* MakeDoor(Room* r1, Room* r2) const { return new DoorNeedingspell(r1, r2); }
protected:
    Spell* CastSpell() const;
};

Wall* BombedMazeFactory::MakeWall() const { return new BombedWall; }
Room* BombedMazeFactory::MakeRoom(int n) const { return new RoomWithABomb(n); }

MazeGame game;
BombedMazeFactory factory;
game.CreateMaze(factory);
```

### AF Known uses and Related Patterns

Gli utilizzi noti comprendono numerose applicazioni, mentre i pattern correlati includono il "Factory Method", il "Singleton" e il "Prototype". Questi elementi sono spesso associati in contesti che richiedono la progettazione e lo sviluppo di software.

## Singleton (SI)

Il design pattern Singleton ha l'intento di assicurare che una classe abbia una sola istanza e di fornire un punto di accesso globale ad essa. La motivazione dietro questo pattern si basa sulla necessità di avere esattamente un'istanza di una classe. Una variabile globale rende un oggetto accessibile, ma non impedisce l'istanziazione di oggetti multipli. Singleton fa sì che la classe stessa sia responsabile della sua unica istanza, garantendo che nessun'altra istanza possa essere creata mediante l'intercettazione delle richieste di creazione di nuovi oggetti. Inoltre, fornisce un modo per accedere a quest'unica istanza.

### SI Applicability

Il pattern Singleton è indicato quando è necessario che esista esattamente un'istanza di una classe, e questa deve essere accessibile ai clienti da un punto di accesso ben noto. Inoltre, è appropriato quando l'unica istanza deve essere estensibile mediante sottoclassi, consentendo ai clienti di utilizzare un'istanza estesa senza modificare il proprio codice.

### SI Participants and Collaborations

Il Singleton è un partecipante che definisce un'operazione di istanza che consente ai clienti di accedere alla sua istanza unica. L'operazione di istanza è un'operazione di classe (ad esempio, un membro statico) e può essere responsabile della creazione della propria istanza unica. Le collaborazioni coinvolgono il fatto che i clienti accedono a un'istanza del Singleton esclusivamente attraverso l'operazione di istanza del Singleton.

### SI Consequences

Le conseguenze dell'uso del pattern Singleton includono un accesso controllato a un'unica istanza, consentendo un rigoroso controllo su come e quando il cliente può accedere. Ciò comporta anche una riduzione dello spazio dei nomi, eliminando l'inquinamento da variabili globali. Il pattern Singleton permette la raffinazione delle operazioni e delle rappresentazioni, consentendo la creazione di sottoclassi della classe Singleton e l'utilizzo dinamico dell'istanza desiderata durante l'esecuzione. Questo approccio consente un numero variabile di istanze, rendendolo più flessibile rispetto alle operazioni di classe, specialmente considerando che le funzioni membro statiche in C++ non sono mai virtuali.

### SI Implementation

Per garantire un'istanza unica, si cela l'operazione di creazione dell'istanza dietro un'operazione di classe (costruttore privato + membro statico). Nel sottoclasse del singleton, la variabile che fa riferimento all'istanza del singleton deve essere inizializzata con un'istanza della sottoclasse stessa. Si potrebbe anche considerare l'utilizzo flessibile di un registro dei singleton.

```cpp
class Singleton {
public:
    static Singleton* Instance();
protected:
    Singleton();
private:
    static Singleton* _instance;
};

Singleton Singleton::_instance = 0;

Singleton* Singleton::Instance() {
    if (_instance == 0) {
        _instance = new Singleton;
    }
    return _instance;
}

class Singleton {
public:
    static void Register(const char* name, Singleton*);
    static Singleton* Instance();
protected:
    static Singleton* Lookup(const char* name);
private:
    static Singleton* _instance;
    static List<NameSingletonPair>* _registry;
};

Singleton Singleton::_instance = 0;
Singleton* Singleton::Instance() {
    if (_instance == 0) {
        const char* singletonName = getenv("SINGLETON");
        // user or environment supplies this at startup
        _instance = Lookup(singletonName);
        // Lookup returns o if there's no such singleton
    }
    return _instance;
}

MySingleton::MySingleton() {
    // ...
    Singleton::Register("MySingleton", this);
}

static MySingleton theSingleton;
```

### SI Sample Code

```cpp
class MazeFactory {
public:
    static MazeFactory* Instance();
    // existing interface goes here
protected:
    MazeFactory();
private:
    static MazeFactory* _instance;
};

MazeFactory* MazeFactory::_instance = 0;

MazeFactory* MazeFactory::Instance() {
    if (_instance == 0) {
        _instance = new MazeFactory;
    }
    return _instance;
}
```

### SI Known Uses and Related Patterns

Numerose applicazioni hanno implementato questo modello. Inoltre, sono emersi modelli correlati che possono essere considerati in connessione con questo approccio. Tra questi, si annoverano l'Abstract Factory, il Builder e il Prototype.

## Prototype (PR)

Il design pattern del Prototipo mira a specificare i tipi di oggetti da creare utilizzando un'istanza prototipica e a generare nuovi oggetti tramite la copia (clonazione) di questo prototipo. La motivazione dietro l'utilizzo di questo pattern può essere compresa considerando la costruzione di un editor per partiture musicali. In questo contesto, si personalizza un framework generale, consentendo la creazione di partiture attraverso l'aggiunta di nuovi oggetti che rappresentano note, pause e righi da una palette. Questo processo coinvolge la creazione di sottoclassi da una classe astratta Graphic, generando molte sottoclassi che differiscono solo per il tipo di oggetto musicale che istanziano.

### PR Applicability

Il prototipo (PR) trova applicazione in diversi contesti. In particolare, è utile quando si desidera che un sistema sia indipendente dal modo in cui i suoi prodotti vengono creati, composti e rappresentati. Inoltre, il PR è adatto quando le classi da istanziare sono specificate a tempo di esecuzione, e quando la gerarchia Parallela AF può essere molto ampia. Infine, il suo impiego è consigliato quando le istanze presentano solo alcune combinazioni di stato diverse.

### PR Participants and Collaborations

Nel contesto del prototipo (PR), sono coinvolte diverse entità e collaborazioni. Tra i partecipanti, troviamo il Prototipo (Grafico), che dichiara un'interfaccia per la clonazione di sé stesso. Il ConcretePrototype (Personale, NotaIntera, MezzaNota) implementa un'operazione per la sua duplicazione. Il Cliente (StrumentoGrafico) è responsabile di creare un nuovo oggetto richiedendo a un prototipo di clonarsi. Le collaborazioni coinvolgono il cliente che richiede a un prototipo di duplicarsi. In questo modo, il design del prototipo facilita la creazione di nuovi oggetti attraverso la clonazione, fornendo una struttura chiara e modulare per la gestione delle diverse implementazioni di prototipi.

### PR Consequences

Le conseguenze del pattern Prototype (PR) sono simili ad altri pattern come Abstract Factory (AF) e Builder (BU) nel fatto che nasconde le classi di prodotto concrete dal cliente, consentendo a quest'ultimo di interagire con classi specifiche dell'applicazione senza necessità di modifiche.

Un aspetto distintivo è la possibilità di aggiungere e rimuovere prodotti durante l'esecuzione, offrendo una flessibilità leggermente maggiore rispetto ad altri pattern creazionali.

La definizione di nuovi oggetti mediante la variazione dei valori è semplificata attraverso PR, consentendo agli utenti di definire nuove "classi" senza ricorrere alla programmazione.

La riduzione della gerarchia di sottoclassi è un vantaggio del pattern Prototype rispetto a Factory Method (FM).

Mentre FM spesso genera una gerarchia di classi Creator che parallela la gerarchia delle classi di prodotto, PR consente di clonare un prototipo anziché richiedere a un metodo di fabbrica di creare un nuovo oggetto, eliminando la necessità di una gerarchia di classi Creator.

Inoltre, la configurazione dinamica di un'applicazione con classi viene agevolata dal pattern Prototype, diventando chiave per sfruttare strutture come la riflessione Java in linguaggi come C++.

### PR Implementation

L'implementazione del design del prototipo (PR) si rivela particolarmente vantaggiosa nei linguaggi statici come il C++, dove le classi non sono oggetti e le informazioni di tipo disponibili durante l'esecuzione sono limitate o assenti. Alcune questioni di implementazione includono l'uso di un gestore di prototipi, specialmente quando il numero di prototipi in un sistema non è fisso, richiedendo la gestione di un registro di prototipi disponibili. La realizzazione dell'operazione di clonazione diventa particolarmente complessa quando le strutture degli oggetti contengono riferimenti circolari. Per l'inizializzazione dei cloni, se i clienti desiderano inizializzare lo stato interno, si può introdurre un'operazione di Inizializzazione. In questo modo, l'approccio del prototipo affronta le sfide specifiche dei linguaggi statici e fornisce soluzioni per la gestione dinamica dei prototipi in un sistema variabile.

### PR Sample Code

```cpp
class MazePrototypeFactory : public MazeFactory {
public:
    MazePrototypeFactory(Maze*, Wall*, Room*, Door*);
    virtual Maze* MakeMaze() const;
    virtual Room* MakeRoom(int) const;
    virtual Wall* MakeWall() const;
    virtual Door* MakeDoor(Room*, Room*) const;

private:
    Maze* prototypeMaze;
    Room* prototypeRoom;
    Wall* prototypeWall;
    Door* prototypeDoor;
};

MazePrototypeFactory::MazePrototypeFactory(Maze* m, Wall* w, Room* r, Door* d) {
    prototypeMaze = m;
    prototypeWall = w;
    prototypeRoom = r;
    prototypeDoor = d;
}

Wall* MazePrototypeFactory::MakeWall() const {
    return prototypeWall->Clone();
}

Door* MazePrototypeFactory::MakeDoor(Room* r1, Room* r2) const {
    Door* door = prototypeDoor->Clone();
    door->Initialize(r1, r2);
    return door;
}

class BombedWall : public Wall {
public:
    BombedWall();
    BombedWall(const BombedWall&);
    virtual Wall* Clone() const;
    bool HasBomb();

private:
    bool bomb;
};

BombedWall::BombedWall() {
    // constructor implementation
}

BombedWall::BombedWall(const BombedWall& other) : Wall(other) {
    bomb = other.bomb;
}

Wall* BombedWall::Clone() const {
    return new BombedWall(*this);
}

MazeGame game;
MazePrototypeFactory simpleMazeFactory(new Maze, new Wall, new Room, new Door);
Maze* maze = game.CreateMaze(simpleMazeFactory);
MazePrototypeFactory bombedMazeFactory(new Maze, new BombedWall, new RoomWithABomb, new Door);
```

### PR Known Uses and Related Patterns

Il design del prototipo (PR) trova molteplici applicazioni in numerosi contesti. È stato impiegato con successo in molte applicazioni, dimostrando la sua flessibilità e adattabilità. Inoltre, presenta relazioni con altri design pattern, come l'Abstract Factory, il Composite e il Decorator. Questi pattern correlati offrono approcci complementari che, insieme al prototipo, arricchiscono il repertorio di soluzioni architetturali disponibili per la progettazione software. La combinazione e la comprensione delle dinamiche tra questi pattern possono contribuire a sviluppare sistemi sofisticati e modulari, affrontando sfide specifiche attraverso una varietà di approcci strutturali.

## Builder (BU)

Il design pattern denominato "Builder" ha come obiettivo principale la separazione della costruzione di un oggetto complesso dalla sua rappresentazione, permettendo così che lo stesso processo di costruzione possa generare rappresentazioni diverse. Questa separazione si dimostra particolarmente utile in contesti in cui è necessario convertire un formato complesso, come il formato di testo RTF (Rich Text Format), in molteplici formati di testo. Ad esempio, un lettore per il formato RTF dovrebbe essere in grado di convertire il testo RTF in diversi formati di testo, come testo ASCII semplice o in un widget di testo che può essere modificato interattivamente. La facilità nell'aggiungere nuove conversioni senza dover modificare il lettore costituisce un vantaggio chiave di questo approccio, consentendo una maggiore flessibilità e manutenibilità del sistema.

### BU Applicabiliy

Il pattern Builder trova applicazione in situazioni in cui l'algoritmo per la creazione di un oggetto complesso deve essere indipendente dalle parti che costituiscono l'oggetto e da come vengono assemblate. È particolarmente utile quando il processo di costruzione deve consentire rappresentazioni diverse per l'oggetto che viene creato.

In sostanza, il Builder pattern offre un modo per separare la logica di costruzione dall'oggetto complesso stesso, consentendo una maggiore flessibilità nell'assemblaggio di diverse configurazioni dell'oggetto. Questo approccio facilita la gestione di algoritmi di costruzione complessi e la creazione di oggetti con rappresentazioni variabili, contribuendo a rendere il sistema più modulare e adattabile alle esigenze specifiche.

### BU Participants

All'interno del design del Builder (BU), sono coinvolte diverse entità che collaborano per la creazione di un prodotto complesso.

Il Builder, rappresentato dal TextConverter, definisce un'interfaccia astratta per la creazione delle parti di un prodotto.

I ConcreteBuilder, come ASCIIConverter, implementano questa interfaccia, costruendo e assemblando le parti del prodotto.Essi forniscono anche un'interfaccia per recuperare il prodotto finale, ad esempio attraverso metodi come GetASCIIText o GetTextWidget.

Il Direttore, incarnato da RTFReader, gioca un ruolo chiave nel processo, costruendo un oggetto utilizzando l'interfaccia del Builder.

Il Prodotto, rappresentato da ASCIIText, TeXText, e TextWidget, è l'oggetto complesso in fase di costruzione, che include classi che definiscono le sue parti costituenti.

Questo approccio del Builder consente la creazione flessibile e personalizzata di oggetti complessi, facilitando la separazione tra la loro costruzione e la loro rappresentazione finale.

### BU Collaborations

Nel contesto del design del Builder (BU), le collaborazioni coinvolgono diverse entità. Il cliente è responsabile della creazione dell'oggetto Direttore e della sua configurazione con l'oggetto Costruttore desiderato. Il Direttore, una volta creato, notifica il costruttore ogni volta che una parte del prodotto deve essere costruita. Il Costruttore gestisce le richieste provenienti dal direttore e aggiunge le parti al prodotto in costruzione. Successivamente, il cliente recupera il prodotto completo direttamente dal costruttore. Questa struttura collaborativa facilita la creazione flessibile e personalizzata di prodotti complessi, consentendo una chiara separazione tra il processo di costruzione e l'oggetto finale desiderato.

### BU Consequences

Il design pattern Builder (BU) offre diverse conseguenze che migliorano la progettazione e la modularità del sistema. Consente la variazione della rappresentazione interna di un prodotto, fornendo al direttore un'interfaccia astratta attraverso l'oggetto Builder per costruire il prodotto.

Questa interfaccia consente al costruttore di nascondere la rappresentazione e la struttura interna del prodotto, così come il processo di assemblaggio. Ciò isola il codice relativo alla costruzione e alla rappresentazione, migliorando la modularità del sistema.

Inoltre, il Builder migliora la modularità del sistema, incapsulando il modo in cui un oggetto complesso viene costruito e rappresentato. I clienti non devono conoscere nulla sulla struttura interna del prodotto, contribuendo a rendere il sistema più robusto e manutenibile.

Questo approccio fornisce un controllo più preciso sul processo di costruzione, poiché il prodotto viene costruito passo dopo passo sotto il controllo del direttore. Solo al termine della costruzione, il direttore recupera il prodotto dal costruttore, completando il processo in modo ordinato e gestibile.

### BU Implementation

L'implementazione del design del Builder (BU) prevede una classe Builder astratta che definisce un'operazione per ciascun componente che un direttore può richiedere di creare. Per impostazione predefinita, le operazioni non svolgono alcuna azione.

Una classe ConcreteBuilder sovrascrive le operazioni per i componenti di interesse. L'interfaccia di assemblaggio e costruzione consente ai Builder di costruire i loro prodotti passo dopo passo.

L'interfaccia BU permette la costruzione di prodotti per tutti i tipi di builder concreti. Non viene fornita una classe astratta per i prodotti, poiché questi differiscono notevolmente nella loro rappresentazione (ad esempio, ASCIIText e TextWidget sono differenti). I metodi vuoti sono forniti come predefiniti nel Builder. Le funzioni membro virtuali contengono metodi vuoti, consentendo ai clienti di sovrascrivere solo le operazioni di loro interesse.

Questo approccio permette una flessibilità significativa nella costruzione di oggetti complessi attraverso l'interazione di Builder e Director, adattandosi alle specifiche esigenze di creazione dei vari componenti del sistema.

### BU Sample Code

```cpp
class MazeBuilder {
public:
    virtual void BuildMaze() {}
    virtual void BuildRoom(int room) {}
    virtual void BuildDoor(int roomFrom, int roomTo) {}
    virtual Maze* GetMaze() { return 0; }
protected:
    MazeBuilder();
};

class MazeBuilder {
public:
    virtual void BuildMaze() {}
    virtual void BuildRoom(int room) {}
    virtual void BuildDoor(int roomFrom, int roomTo) {}
    virtual Maze* GetMaze() { return 0; }
protected:
    MazeBuilder();
};
```

### BU Known Uses and Related Patterns

Il design del Business Delegate (BU) trova numerose applicazioni in una varietà di contesti. È stato ampiamente impiegato in molte applicazioni, evidenziando la sua versatilità e adattabilità. Inoltre, presenta relazioni con altri design pattern, quali l'Abstract Factory e il Composite. Questi pattern correlati offrono approcci complementari che, insieme al Business Delegate, arricchiscono l'arsenale di soluzioni architetturali disponibili per la progettazione software. La comprensione e l'integrazione di queste dinamiche tra pattern consentono di sviluppare sistemi sofisticati e modulari, affrontando sfide specifiche attraverso una varietà di approcci strutturali.

## Discussion

Esistono due modi comuni per parametrizzare un sistema in base alle classi degli oggetti che crea. Il primo consiste nel creare una sottoclasse della classe che genera gli oggetti, noto come "Factory Method". In questo approccio, la creazione di un nuovo sottotipo può essere necessaria solo per cambiare la classe del prodotto, il che può portare a una cascata di modifiche indesiderate.

Il secondo metodo per parametrizzare un sistema si basa sulla composizione degli oggetti. In questo contesto, si ricorre a pattern come Abstract Factory, Builder e Prototype. L'Abstract Factory coinvolge la creazione di un nuovo "oggetto factory" il cui compito è generare oggetti di diverse classi. Il Builder prevede che l'oggetto factory costruisca incrementalmente un prodotto complesso utilizzando un protocollo articolato. Il Prototype, invece, fa sì che l'oggetto factory, il prototipo stesso, costruisca un prodotto copiando un oggetto prototipo.

Il principale svantaggio del Factory Method è la necessità di creare una nuova sottoclasse solo per modificare la classe del prodotto, con possibili conseguenze a catena. D'altra parte, i pattern basati sulla composizione offrono soluzioni più flessibili, consentendo la creazione di nuovi oggetti factory e la generazione di oggetti di diverse classi senza la creazione di nuove gerarchie di sottotipi.

## Ripasso

## 1. **Comprendere il Concetto dei Design Pattern**

- **Definizione**: I design pattern sono soluzioni tipiche a problemi comuni nella progettazione del software.
- **Obiettivo**: Semplificare lo sviluppo del software rendendo più chiaro e manutenibile il codice.

## 2. **Pattern Creazionali**

- **Singleton**: Garantisce che una classe abbia una sola istanza e fornisce un punto di accesso globale a quella istanza.
- **Factory Method**: Definisce un'interfaccia per creare un oggetto, ma lascia che le sottoclassi decidano quale classe istanziare.
- **Abstract Factory**: Fornisce un'interfaccia per creare famiglie di oggetti correlati senza specificare le loro classi concrete.
- **Builder**: Separa la costruzione di un oggetto complesso dalla sua rappresentazione, in modo che lo stesso processo di costruzione possa creare diverse rappresentazioni.
- **Prototype**: Crea nuovi oggetti clonando un prototipo.

## 3. **Riflessione**

- **Valuta il Contesto**: Non tutti i pattern sono adatti per ogni situazione. Considera i pro e i contro di ciascun pattern.
- **Combinazione con Altri Pattern**: A volte, combinare diversi pattern può portare a soluzioni più robuste.

## Caratteristiche generali

## 1. Singleton

- **Scopo**:
  - Garantire che una classe abbia una sola istanza e fornire un punto di accesso globale a tale istanza.
- **Caratteristiche**:
  - Costruttore privato per prevenire l'istanziazione diretta.
  - Un metodo statico che restituisca l'unica istanza esistente della classe.

    ```java
    public class Singleton {
        private static Singleton instance;

        private Singleton() {}

        public static Singleton getInstance() {
            if (instance == null) {
                instance = new Singleton();
            }
            return instance;
        }
    }
    ```

## 2. Factory Method

- **Scopo**:
  - Definire un'interfaccia per creare un oggetto, ma lasciare che le sottoclassi decidano quale classe istanziare.
- **Caratteristiche**:
  - Definisci un'interfaccia o una classe astratta con un metodo astratto (factory) senza implementazione.
  - Lascia che le sottoclassi implementino questo metodo per creare oggetti di classi appropriate.
  - Usalo per delegare la responsabilità della creazione dell'oggetto a sottoclassi, promuovendo il **loose coupling**.

    ```java
    public abstract class Animal {
        public abstract String makeSound();
    }

    public class Dog extends Animal {
        @Override
        public String makeSound() {
            return "Bark";
        }
    }

    public class AnimalFactory {
        public Animal createAnimal(String type) {
            if ("dog".equals(type)) {
                return new Dog();
            }
            // ... altri tipi di animali
            return null;
        }
    }

    ```

## 3. Abstract Factory

- **Scopo**:
  - Fornire un'interfaccia per creare famiglie di oggetti correlati o dipendenti senza specificarne le classi concrete.
- **Caratteristiche**:
  - Crea interfacce astratte per ogni tipo di oggetto che desideri creare.
  - Implementa queste interfacce in classi concrete raggruppate in "famiglie".
  - Assicurati che il codice che utilizza queste fabbriche operi solo con le interfacce, non con le implementazioni concrete.

    ```java
    interface Button {
        void paint();
    }

    class WinButton implements Button {
        public void paint() {
            System.out.println("Windows Button");
        }
    }

    class MacButton implements Button {
        public void paint() {
            System.out.println("Mac Button");
        }
    }

    interface GUIFactory {
        Button createButton();
    }

    class WinFactory implements GUIFactory {
        public Button createButton() {
            return new WinButton();
        }
    }

    class MacFactory implements GUIFactory {
        public Button createButton() {
            return new MacButton();
        }
    }

    ```

## 4. Builder

- **Scopo**:
  - Separare la costruzione di un oggetto complesso dalla sua rappresentazione, in modo che lo stesso processo di costruzione possa creare diverse rappresentazioni.
- **Caratteristiche**:
  - Differenzia tra il processo di costruzione (Builder) e la rappresentazione finale (Product).
  - Il Builder è di solito una classe astratta o un'interfaccia che definisce i passi per costruire il prodotto finale.
  - Permette la costruzione di un oggetto passo dopo passo, spesso attraverso una fluent interface.
  - Isola il codice cliente dalla costruzione interna dell'oggetto.

    ```java
    public class Car {
        private final String engine;
        private final int wheels;

        private Car(Builder builder) {
            this.engine = builder.engine;
            this.wheels = builder.wheels;
        }

        public static class Builder {
            private String engine;
            private int wheels;

            public Builder engine(String engine) {
                this.engine = engine;
                return this;
            }

            public Builder wheels(int wheels) {
                this.wheels = wheels;
                return this;
            }

            public Car build() {
                return new Car(this);
            }
        }
    }

    ```

## 5. Prototype

- **Scopo**:
  - Usare un oggetto prototipico per specificare i tipi di oggetti da creare e creare nuovi oggetti copiando questo prototipo.
- **Caratteristiche**:
  - Implementa un'interfaccia che consente agli oggetti di essere clonati.
  - L'oggetto originale (prototipo) deve essere in grado di creare una copia completa di se stesso.
  - È utile quando la creazione di un'istanza è più costosa che clonarne una esistente.

    ```java
    public abstract class Shape implements Cloneable {
        private String id;
        protected String type;

        abstract void draw();

        public String getType(){
            return type;
        }

        public String getId() {
            return id;
        }

        public void setId(String id) {
            this.id = id;
        }

        public Object clone() {
            Object clone = null;
            try {
            clone = super.clone();
            } catch (CloneNotSupportedException e) {
            e.printStackTrace();
            }
            return clone;
        }
    }

    public class Rectangle extends Shape {
        public Rectangle() {
            type = "Rectangle";
        }

        @Override
        void draw() {
            System.out.println("Inside Rectangle::draw() method.");
        }
    }

    ```

## Considerazioni Generali

- **Scegli il pattern adeguato in base alle esigenze** del tuo progetto, considerando fattori come la complessità dell'oggetto da creare, la necessità di estensioni future, il grado di accoppiamento desiderato, e altri requisiti specifici del dominio.
- **Attenzione alla violazione dei principi SOLID**, specialmente:
  - Single Responsibility Principle.
  - Open/Closed Principle.
- **Ricorda che l'uso eccessivo di pattern può portare a una complessità non necessaria**.
  - Utilizzali solo quando offrono un chiaro vantaggio in termini di manutenibilità, estensibilità e comprensione del codice.
