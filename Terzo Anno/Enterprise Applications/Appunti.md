# Enterprise Applications

## Cosa vedremo

1. Docker
2. Annotation, reflection, lombok
3. ORM, JPA
4. Spring Repository
5. Service, paging sorting, coaching, scheduler, auditing
6. DTO e Controller
7. Input validation, audit logging, i18n
8. OAuth2, JWT, keycloak o auth0 + https
9. Microservices and Spring Cloud
10. Dockerizzazione di un'applicazione Spring Boot e Spring Cloud
11. AOP, logging, swagger e auth, Rate Limiting

## Cosa serve

- Java
  - Annotation
  - Stream e lambda
  - Lib Datetime
  - Logging
  - JUnit
- Sql e progettazione DB
- Angular

## Java Logging

### Cos'è il logging?

Il logging è un'attività che consiste nel registrare in un file o in un database le attività di un'applicazione. Questo permette di avere un tracciamento delle attività svolte dall'applicazione e di poter risalire a eventuali errori.

### Java Logging Framework

Java fornisce un framework per il logging, chiamato `java.util.logging`. Questo framework permette di registrare i log in un file o in un database.

#### Esempio di utilizzo di `java.util.logging`

```java
import java.util.logging.Logger;

public class MyClass {
    private static final Logger LOGGER = Logger.getLogger(MyClass.class.getName());

    public void myMethod() {
        LOGGER.info("This is a log message");
    }
}
```

### Messaggio di logging

Un messaggio di logging è una stringa che viene registata durante l'esecuzione di un metodo.

### Logger

Il logger è il componente responsabile della registrazione dei messaggi di logging. All'interno della stessa apllicazzione è possibile utilizzare più logger; ad esempio, un logger per package p un logger per classe.

### Handler (o Appender)

Il handler è il componente responsabile della registrazione dei messaggi di logging prodotti da un logger su un flusso o dispositivo; con un formato specificato. Ad esempio, un handler può scrivere i messaggi di logging su un file, su un database o sulla console. A ciascuna categoria di logger può essere associato uno o più handler.

Java fornisce un handler di default, chiamato `ConsoleHandler`, che scrive i messaggi di logging sulla console.

`FileHandler` è un altro handler che scrive i messaggi di logging su un file.

### Formatter

Il formatter è il componente responsabile della formattazione dei messaggi di logging. Si può personalizzare il formato dei messaggi di logging per includere timestamp, nomi dei thread, nomi dei logger, ecc. Ad esempio, un formatter può formattare i messaggi di logging in formato JSON.

Gli handler determinano dove i messaggi di logging vengono scritti, mentre i formatter determinano come i messaggi di logging vengono scritti.

Java fornisce un formatter di default, chiamato `SimpleFormatter`, che formatta i messaggi di logging in modo semplice.

### Livelli di logging

I livelli di logging sono una serie di costanti che rappresentano la gravità dei messaggi di logging.

I livelli di logging sono:

- `SEVERE`: utilizzato per errori gravi che impediscono il corretto funzionamento dell'applicazione.
- `WARNING`: utilizzato per avvisi che indicano potenziali problemi ma che non impediscono il corretto funzionamento dell'applicazione.
- `INFO`: utilizzato per informazioni generiche sull'esecuzione dell'applicazione.
- `CONFIG`: utilizzato per informazioni di configurazione dell'applicazione.
- `FINE`: utilizzato per informazioni di debugging più dettagliate.
- `FINER` e `FINEST`: utilizzati per informazioni di debugging molto dettagliate.

La scelta del livello di logging dipende dal tipo di informazioni che si vogliono registrare, in base alla gravità degli eventi e alla necessità di debug.

#### Esempio di logging

```java
import java.util.logging.Logger;

public class MyClass {
    private static final Logger LOGGER = Logger.getLogger(MyClass.class.getName());

    public void myMethod() {
        LOGGER.severe("This is a severe log message");
        LOGGER.warning("This is a warning log message");
        LOGGER.info("This is an info log message");
        LOGGER.config("This is a config log message");
        LOGGER.fine("This is a fine log message");
        LOGGER.finer("This is a finer log message");
        LOGGER.finest("This is a finest log message");
    }
}
```

### Configurazione del logging

La configurazione del logging in Java può essere fatta tramite un file di configurazione `logging.properties` o tramite codice.

#### Configurazione tramite file `logging.properties`

Un esempio di file di configurazione `logging.properties`:

```properties
# File di configurazione del logging

# Impostazioni globali
.level=INFO

# Impostazioni del formatter
java.util.logging.ConsoleHandler.formatter=java.util.logging.SimpleFormatter

# Configurazione dei logger pere una classe specifica
com.example.MyClass.level=FINE
com.example.MyClass.handlers=java.util.logging.FileHandler

# Impostazioni del file di output per il FileHandler
java.util.logging.FileHandler.pattern=%h/java%u.log
java.util.logging.FileHandler.limit=50000
java.util.logging.FileHandler.count=1
java.util.logging.FileHandler.formatter=java.util.logging.SimpleFormatter
```

Il livello di logging globale è impostato a `INFO`, il che significa che verranno registrati solo i messaggi di logging di livello `INFO` e superiori.

Viene utilizzato un `ConsoleHandler` con un `SimpleFormatter` per scrivere i messaggi di logging sulla console.

Per la classe `com.example.MyClass` viene impostato il livello di logging a `FINE` e viene utilizzato un `FileHandler` per scrivere i messaggi di logging su un file. Il FileHandler scrive i messaggi di logging su un file chiamato `java.log` nella directory home dell'utente, limitando la dimensione del file a 50.000 byte e mantenendo un solo file di log.

Il file di configurazione `logging.properties` deve essere posizionato nella directory `src/main/resources` del progetto.

#### Configurazione tramite codice

Un esempio di configurazione del logging tramite codice:

```java
import java.util.logging.ConsoleHandler;
import java.util.logging.FileHandler;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

public class LoggingExample {
    private static final Logger LOGGER = Logger.getLogger(LoggingExample.class.getName());

    public static void main(String[] args) {
        LOGGER.setLevel(Level.FINE);

        ConsoleHandler consoleHandler = new ConsoleHandler();
        consoleHandler.setLevel(Level.FINE);
        consoleHandler.setFormatter(new SimpleFormatter());
        LOGGER.addHandler(consoleHandler);

        try {
            FileHandler fileHandler = new FileHandler("%h/java%u.log", 50000, 1, true);
            fileHandler.setLevel(Level.FINE);
            fileHandler.setFormatter(new SimpleFormatter());
            LOGGER.addHandler(fileHandler);
        } catch (IOException e) {
            LOGGER.log(Level.SEVERE, "Error creating file handler", e);
        }

        LOGGER.severe("This is a severe log message");
        LOGGER.warning("This is a warning log message");
        LOGGER.info("This is an info log message");
        LOGGER.config("This is a config log message");
        LOGGER.fine("This is a fine log message");
        LOGGER.finer("This is a finer log message");
        LOGGER.finest("This is a finest log message");
    }
}
```

In questo esempio, viene creato un logger con livello di logging `FINE`. Viene aggiunto un `ConsoleHandler` con livello di logging `FINE` e un `SimpleFormatter`. Viene creato un `FileHandler` con le stesse impostazioni del file di configurazione precedente.

### Logback

Logback è un framework di logging per Java che fornisce funzionalità avanzate rispetto a `java.util.logging`. Logback può essere integrato facilmente nelle applicazioni Java tramite Maven o Gradle.

Le principali caratteristiche di Logback sono:

- Flessibilità: Logback offre una vasta gamma di configurazioni per adattarsi alle esigenze specifiche dell'applicazione.

- Performance: Logback è progettato per essere veloce ed efficiente, riducendo al minimo l'impatto sulle prestazioni dell'applicazione.

- Modularità: Logback è composto da diversi moduli che possono essere utilizzati in modo indipendente o combinati per ottenere funzionalità avanzate.

- Ampiamente utilizzato: Logback è ampiamente utilizzato nell'industria del software ed è supportato da una vasta comunità di sviluppatori.

Per integrare Logback in un progetto Maven, è sufficiente aggiungere la dipendenza `logback-classic` nel file `pom.xml`:

```xml
<dependency>
    <groupId>ch.qos.logback</groupId>
    <artifactId>logback-classic</artifactId>
    <version>1.2.3</version>
</dependency>
```

### Appender di Logback

Nell'architettura di Logback, gli appender sono responsabili della scrittura dei messaggi di logging su un output specifico, come un file, una console o un database. Tutti gli appender di Logback implementano l'interfaccia `ch.qos.logback.core.Appender`.

Inoltre, ogni appender corrisponde a un certo tipo di output o modalità di scrittura dei log.

I principali appender di Logback sono:

- `ConsoleAppender`: scrive i messaggi di logging sulla console del sistema.
- `FileAppender`: scrive i messaggi di logging su un file di log.
- `RollingFileAppender`: scrive i messaggi di logging su un file di log rotante, che viene diviso in segmenti di dimensioni specificate.
- `SMTPAppender`: invia i messaggi di logging via email, per impostazione predefinita solo per i messaggi di livello `ERROR`.
- `DBAppender`: aggiunge i messaggi di logging a un database.
- `SiftingAppender`: indirizza i messaggi di logging a diversi appender in base a determinate condizioni.

### Layout ed Encoder di Logback

I componenti responsabili della trasformazione di un messaggio di registro nel formato di output desiderato sono il `Layout` e l'`Encoder`. Alcuni dei layout e encoder più comuni sono:

- `PatternLayout`: formatta i messaggi di logging utilizzando un pattern specificato.
- `HTMLLayout`: formatta i messaggi di logging in formato HTML.
- `JSONLayout`: formatta i messaggi di logging in formato JSON.
- `XMLLayout`: formatta i messaggi di logging in formato XML.

``` xml
<encoder>
    <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
</encoder>
```

### Logger di Logback

I logger sono il terzo componente principale di Logback e sono responsabili della registrazione dei messaggi di logging a un certo livello. Ogni logger è associato a un nome univoco e a un livello di logging specifico.

La libreria Logback definisce cinque livelli di logging standard:

- `TRACE`: il livello di logging più dettagliato, utilizzato per messaggi di debug molto dettagliati.
- `DEBUG`: utilizzato per messaggi di debug dettagliati.
- `INFO`: utilizzato per messaggi informativi sull'esecuzione dell'applicazione.
- `WARN`: utilizzato per messaggi di avviso che indicano potenziali problemi.
- `ERROR`: utilizzato per messaggi di errore gravi che impediscono il corretto funzionamento dell'applicazione.

Ognuno di questi ha un metodo di registrazione corrispondente nel logger: `trace()`, `debug()`, `info()`, `warn()` e `error()`. I messaggi di logging vengono registrati solo se il livello del logger è uguale o superiore al livello del messaggio.

Se non si definisce esplicitamente un livello di log, il logger eredita il livello del suo predecessore o del root logger.

#### Esempio di configurazione di Logback

Un esempio di configurazione di Logback tramite un file `logback.xml`:

``` xml
<configuration>
  # Console appender
  <appender name="stdout" class="ch.qos.logback.core.ConsoleAppender">
    <layout class="ch.qos.logback.classic.PatternLayout">
      # Formato del messaggio di log per l'appender della console
      <pattern>%d{yyyy-MM-dd HH:mm:ss} %-5p %m%n</pattern>
    </layout>
  </appender>

  # File appender
  <appender name="fout" class="ch.qos.logback.core.FileAppender">
    <file>logger.log</file>
    <append>false</append>
    <encoder>
      # Formato del messaggio di log per l'appender del file
      <pattern>%d{yyyy-MM-dd HH:mm:ss} %-5p %m%n</pattern>
    </encoder>
  </appender>

  # Override del livello di log per un package specifico
  <logger name="com.baeldung.log4j" level="TRACE"/>

  <root level="INFO">
    <appender-ref ref="stdout" />
    <appender-ref ref="fout" />
  </root>
</configuration>
```

#### Esempio di RollingFileAppender di Logback

Un esempio di configurazione di un `RollingFileAppender` in Logback:

``` xml
<property name="LOG_FILE" value="LogFile" />
<appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
    <file>${LOG_FILE}.log</file>
    <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
        <!-- Rollover giornaliero -->
        <fileNamePattern>${LOG_FILE}.%d{yyyy-MM-dd}.gz</fileNamePattern>

        <!-- Mantieni 30 giorni di log -->
        <maxHistory>30</maxHistory>
        <!-- Dimensione massima del file di log -->
        <totalSizeCap>3GB</totalSizeCap>
    </rollingPolicy>
    <encoder>
        <pattern>%-4relative [%thread] %-5level %logger{35} - %msg%n</pattern>
    </encoder>
</appender>
```

## Java Annotations

### Cos'è un'annotazione?

Un'annotazione in Java è una forma di metadati che fornisce informazioni supplementari su classi, metodi, variabili e altri elementi del codice. Consentono di aggiungere marcatori o istruzioni speciali al codice sorgente che possono essere letti tramite reflection o utilizzati da strumenti di analisi del codice.

Le annotazioni possono essere utlizzate per vari scopi, come la documentazione, la gestione dei test, l'iniezione di dipendenze (es. Spring Framework), la validazione dei dati, ecc.

Per esempio `@Override` è un'annotazione che indica che un metodo sta sovrascrivendo un metodo della superclasse.

In Java le annotazioni sono dichiarate con l'annotazione `@`. Ad esempio: `@Override`, `@Deprecated`, `@SuppressWarnings`. Si possono anche creare annotazioni personalizzate definendo una nuova interfaccia annotata con `@interface`.

Le annotazioni possono essere lette tramite reflection consentendo al programma di esaminare e modificare il comportamento di un'applicazione in base alle annotazioni presenti. Ad esempio, si possono creare annotazioni per definire regole di validazione dei dati e utilizzarle per controllare i dati in input.

Questo permette di scrivere codice più flessibile e dinamico, in quanto le annotazioni possono essere lette a runtime per modificare il comportamento dell'applicazione.

#### Annotazioni di Marker

Le annotazioni di marker sono annotazioni che non richiedono alcuna informazione aggiuntiva e sono utilizzate solo per marcare un elemento del codice, per indicare la presenza di una determinata caratteristica. Ad esempio, `@Override`, `@Deprecated`, `@SuppressWarnings`.

#### Annotazioni di Singolo Valore

Le annotazioni di singolo valore sono annotazioni che richiedono un singolo valore come parametro e sono spesso utilizzate per configurare il comportamento di un elemento del codice o per fornire informazioni specifiche.

```java
@Column(name = "first_name")
@RequestMapping("/home")
```

#### Annotazioni di Array di Valori

Le annotazioni di array di valori sono annotazioni che richiedono un array di valori come parametro e sono utilizzate per specificare più valori per un'annotazione, quindi, più azioni o configurazioni.

```java
@RolesAllowed({"ADMIN", "USER"})
@Order({1, 2, 3})
```

#### Annotazioni di Meta-Annotazioni

Le meta-annotazioni sono annotazioni che vengono utilizzate per definire altre annotazioni e specificarne il comportamento. Ad esempio, `@Retention`, `@Target`, `@Documented`, `@Inherited`.

```java
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
```

### Meta Annotazioni

#### @Retention

L'annotazione `@Retention` specifica come l'annotazione annotata deve essere conservata. Ci sono tre tipi di politiche di conservazione:

- `RetentionPolicy.SOURCE`: l'annotazione è conservata solo nel codice sorgente e non è inclusa nel file di classe, quindi scarta al momento della compilazione.
- `RetentionPolicy.CLASS`: l'annotazione è conservata nel file di classe, ma non è disponibile in fase di esecuzione.
- `RetentionPolicy.RUNTIME`: l'annotazione è conservata nel file di classe e disponibile in fase di esecuzione tramite reflection.

#### @Target

L'annotazione `@Target` specifica i tipi di elementi del codice a cui può essere applicata un'annotazione. I tipi di elementi includono:

- `ElementType.TYPE`: annotazione applicabile a una classe, interfaccia o enumerazione.
- `ElementType.METHOD`: annotazione applicabile a un metodo.
- `ElementType.FIELD`: annotazione applicabile a un campo o variabile di istanza.
- `ElementType.PARAMETER`: annotazione applicabile a un parametro di un metodo o costruttore.
- `ElementType.CONSTRUCTOR`: annotazione applicabile a un costruttore.
- E così via per altri tipi di elementi.

#### @Documented

L'annotazione `@Documented` è utilizzata per indicare che un'annotazione personalizzata deve essere inclusa nella documentazione generata automaticamente. Questo significa che quando si utilizza un'annotazione contrassegnata con `@Documented`, gli elementi annotati con tale annotazione verrano inclusi nella documentazione generata tramite strumenti come Javadoc. Ad esempio, se definiamo un'annotazione personalizzata `@MyAnnotation` e la contrassegniamo con `@Documented`, allora i metodi, classi o campi annotati con `@MyAnnotation` verranno inclusi nella documentazione generata.

#### @Inherited

L'annotazione `@Inherited` è utilizzata per indicare che un'annotazione personalizzata deve essere ereditata dalle sottoclassi. se non è esplicitamente sovrascritta.  Questo significa che se una classe annotata con un'annotazione contrassegnata con `@Inherited` viene estesa da una sottoclasse, la sottoclasse eredita l'annotazione a meno che non venga sovrascritta nella sottoclasse stessa. Questo è utile per definire comportamenti comuni che devono essere ereditati da tutte le sottoclassi. Ha effetto solo sulle annotazioni quando applicate a classi, non a metodi o altri elementi.

#### @Repeatable

L'annotazione `@Repeatable` consente di annotare più volte lo stesso elemento con la stessa annotazione. Consente di definire un contenitore di annotazioni (chiamato "container annotation") che consente di specificare più volte la stessa annotazione. Questo rende il codice più leggibile in situazioni in cui è necessario applicare più volte la stessa annotazione a un singolo elemento. Ad esempio, se definiamo un'annotazione `@MiaAnnotazione` contrassegnata con `@Repeatable`, possiamo applicare `@MiaAnnotazione` più volte allo stesso elemento senza dover creare un contenitore esterno per raggruppare le annotazioni.

## Lombok

### Cos'è Lombok?

Lombok è una libreria Java che consente di ridurre la quantità di codice boilerplate necessario per la scrittura di classi Java. Lombok fornisce delle annotazioni che generano automaticamente codice per metodi getter e setter, costruttori, metodi `equals()`, `hashCode()`, `toString()`, ecc. Questo permette di scrivere codice più conciso e leggibile, eliminando la necessità di scrivere manualmente il codice ripetitivo.

## New Date and Time API

### Importazione di java.time

Per utilizzare le classi del nuovo API di data e ora di Java, è necessario importare il pacchetto `java.time`.

```java
import java.time.*;
```

### LocalDate

`LocalDate` rappresenta una data senza un fuso orario specifico. È composta da anno, mese e giorno.

```java
LocalDate date = LocalDate.now();
```

### Current Date and Time

Per ottenere la data e l'ora correnti, è possibile utilizzare i metodi statici `now()` delle classi `LocalDate`, `LocalTime` e `LocalDateTime`.

```java
LocalDateTime dateTime = LocalDateTime.now();
```

### Precise Instant

`Instant` rappresenta un istante preciso nel tempo, misurato in millisecondi da un punto di riferimento specifico chiamato "epoch". È utile per rappresentare timestamp e durate.

```java
LocalDate may = LocalDate.of(2022, Month.MAY, 1);
```

### Adding a day

Per aggiungere o sottrarre giorni, mesi o anni a una data, è possibile utilizzare i metodi `plusDays()`, `plusMonths()`, `plusYears()`, `minusDays()`, `minusMonths()`, `minusYears()`.

```java
LocalDate date = LocalDate.now().plusDays(1);
```

### Stampare una data in un formato specifico

```java
System.out.println(LocalDate.now());
    2024-04-24

System.out.println(LocalTime.now());
    15:30:00.123456789

System.out.println(LocalDateTime.now());
    2024-04-24T15:30:00.123456789

System.out.println(ZonedDateTime.now());
    2024-04-24T15:30:00.123456789+02:00[Europe/Rome]
```

### Gestione delle date e degli orari in Java utilizzando le classi LocalDate, LocalTime, LocalDateTime e ZonedDateTime

```java
LocalDate date1 = LocalDate.of(2015, Month.JANUARY, 20);
LocalDate date2 = LocalDate.of(2015, 1, 20);

LocalTime time1 = LocalTime.of(6, 15); // hour and minute
LocalTime time2 = LocalTime.of(6, 15, 30); // + seconds
LocalTime time3 = LocalTime.of(6, 15, 30, 200); // + nanoseconds

LocalDateTime dateTime1 = LocalDateTime.of(2015, Month.JANUARY, 20, 6, 15, 30);
LocalDateTime dateTime2 = LocalDateTime.of(date1, time1);

ZoneId zone = ZoneId.of("US/Eastern");
ZonedDateTime zoned1 = ZonedDateTime.of(2015, 1, 20, 6, 15, 30, 200, zone);
ZonedDateTime zoned2 = ZonedDateTime.of(date1, time1, zone);
ZonedDateTime zoned3 = ZonedDateTime.of(dateTime1, zone);

LocalDate date = LocalDate.of(2014, Month.JANUARY, 20);
System.out.println(date); // 2014–01–20

date = date.plusDays(2); //.minusDays(1);
System.out.println(date); // 2014–01–22

date = date.plusWeeks(1); // .minusWeeks(1);
System.out.println(date); // 2014–01–29

date = date.plusMonths(1); // .minusMonths(1);
System.out.println(date); // 2014–02–28

date = date.plusYears(5); // .minusYears(1);
System.out.println(date); // 2019–02–28

LocalDate.parse("1942-07-22", DateTimeFormatter.ISO_LOCAL_DATE);

DateTimeFormatter.ISO_LOCAL_DATE.format(LocalDate.now());

LocalDate.now().format(DateTimeFormatter.ISO_LOCAL_DATE);

DateTimeFormatter dtf=DateTimeFormatter.ofLocalizedDate(FormatStyle.LONG).withLocale(Locale.FRENCH);
System.out.println(dtf.format(LocalDate.now());

DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy-MM-dd");
      String s = dtf.format(LocalDateTime.now());
```

### Metodi di Conversione tra LocalDate, LocalDateTime e Date in Java

```java
public class DateUtils
{
    public static Date asDate(final LocalDate localDate)
    {
        return Date.from(localDate.atStartOfDay().atZone(ZoneId.systemDefault()).toInstant());
    }

    public static Date asDate(final LocalDateTime localDateTime)
    {
        return Date.from(localDateTime.atZone(ZoneId.systemDefault()).toInstant());
    }

    public static LocalDate asLocalDate(final Date date)
    {
        return Instant.ofEpochMilli(date.getTime()).atZone(ZoneId.systemDefault()).toLocalDate();
    }

    public static LocalDateTime asLocalDateTime(final Date date)
    {
        return Instant.ofEpochMilli(date.getTime()).atZone(ZoneId.systemDefault()).toLocalDateTime();
    }
}
```

## Functional programming

Il paradigma della programmazione funzionale è stato creato espressamente per supportare un approccio funzionale puro alla programmazione dichiarativa.

Con un approccio imperativo lo sviluppatore scrive codice in cui vengono descritti in dettagglio i passaggi esatti che devono essere eseguiti dal computer per raggiungere l'obiettivo. Ci si concentra su COME FARE;

Un approccio funzionale implica la composizione del problema come set di funzioni da eseguire. È necessario definire con attenzione l'input e l'output di ogni funzione. Ci si concentra su COSA FARE e si delegano i dettagli a librerie di funzioni;

### Functional interface

Le interfacce funzionali sono delle interface che definiscono un solo metodo astratto (SAM, Single Abstract Method) e nessuno o più metodi di default o statici. Grazie a questa particolarità possono essere implementate con espressioni lambda.

Sono definite usando l'annotazione `@FunctionalInterface` (opzionale).

```java
@FunctionalInterface
public interface MyFunctionalInterface {
    void myMethod();
}
```

In Java esistono già delle interfacce funzionali, ad esempio `Runnable`, `Callable`, `Comparator`, `Function`, `Predicate`, `Supplier`, `Consumer`. Queste possono essere usate sia con le Anonymous Inner Classes che con le Lambda Expressions.

In Java 8 sono state introdotte nuove interfacce funzionali nel package `java.util.function`, come `Function`, `Predicate`, `Supplier`, `Consumer`, `UnaryOperator`, `BinaryOperator`.

#### Esempio di utilizzo di un'interfaccia funzionale

```java
/*
 * Interfaccia con un solo metodo
 * Una sola funzione da implemetare
 * Legate ai lambda
 * 
 * @FunctionalInterface: non obbligatoria
*/

@FunctionalInterface
public interface MyFunctionalInterface {
    // SAM: Single Abstract Method
    public void doWork();
}

@FunctionalInterface
public interface Runnable {
    public abstract void run();
}
```

### Lambda expressions

Le espressioni lambda sono una delle tecniche più popolari usate nella programmazione funzionale in Java 8. Con il loro uso è possibile definire e chiamare un metodo, senza necessariamente dichiarare una classe che lo contiene.

Il termine lambda indica un insieme di istruzioni che possono essere salvate come variabili, passate a un programma ed eseguite successivamente. Rappresenta un modo più sintetico per esprimere il concetto di anonynous inner class.

Può essere assegnata ad una variabile, passata come argomento ad un metodo o manipolata come qualsiasi altro valore.

La definizioned i un'espressione lambda è formata da tre parti:

- elenco di parametri formali, input, tra (), separati da virgole, se c'è sono un input le parentesi si possono omettere.
- operatore lambda `->`, separa i parametri formali dal corpo della lambda; è chiamato operatore freccia.
- corpo della lambda, tra {}, contiene l'espressione o il blocco di codice da eseguire; se il corpo è composto da una sola istruzione, le parentesi graffe e il punto e virgola possono essere omessi.

```java
// Un'espressione lambda senza parametri che stampa "Hello, World!" quando viene eseguita
() -> System.out.println("Hello, World!");

// Un'espressione lambda senza parametri passata come argomento al metodo doSomething
doSomething(() -> System.out.println("Hello, World!"));

// Un'espressione lambda con due parametri che restituisce la loro somma
doSomething((a, b) -> a + b);

// Un'espressione lambda con due parametri di tipo Integer che restituisce la loro somma
doSomething((Integer a, Integer b) -> a + b);

// Un'espressione lambda con due parametri che restituisce la loro somma, utilizzando la parola chiave 'return'
doSomething((a, b) -> return a + b);

// Un'espressione lambda con due parametri che restituisce la loro somma, utilizzando la parola chiave 'return' e le parentesi graffe
doSomething((a, b) -> { return a + b; });

// Un'espressione lambda con un parametro che incrementa il valore del parametro di 2 e poi lo restituisce
doSomething(x -> {x += 2; return x;});

// Un'espressione lambda assegnata a una variabile di tipo Predicate<String>. Questa espressione lambda prende una stringa come argomento e restituisce true se la stringa non è null e la sua lunghezza è maggiore di 0
Predicate<String> notBlank = s -> s != null && s.length() > 0;
```

### java.util.function

Il package `java.util.function` contiene una serie di interfacce funzionali predefinite che possono essere utilizzate con le espressioni lambda. Queste interfacce definiscono metodi che possono essere utilizzati per eseguire operazioni comuni come trasformazioni, filtraggi, aggregazioni, ecc.

- `FUNCTION<T, R>`: definisce una funzione che accetta un argomento di tipo T e restituisce un risultato di tipo R; il suo metodo astratto è apply, che applica la funzione definita all’oggetto t passato come argomento.
- `BIFUNCTION<T,U,R>`: specializzazione di Function, definisce una funzione che accetta 2 argomenti, di tipo T e U, e restituisce un risultato di tipo R, il suo metodo astratto è apply.
- `SUPPLIER<T>`: definisce un’operazione che non riceve input e restituisce un risultato di tipo T, il suo metodo astratto è get, che restituisce il risultato calcolato dall’operazione.
- `CONSUMER<T>`: Definisce un’operazione che accetta un solo input di tipo T e non restituisce risultati, il suo metodo astratto è accept, che esegue l’operazione sull’input.
- `BICONSUMER<T,U>`: Specializzazione di Consumer, definisce un’operazione che accetta due argomenti di tipo T e U e non restituisce risultati, il suo metodo astratto è accept;
- `PREDICATE<T>`: Rappresenta un predicato, cioè una funzione booleana, che riceve un solo argomento; il suo metodo astratto è test, che valuta il predicato definito sull’argomento passato.
- `BIPREDICATE<T,U>`: Specializzazione di Predicate, rappresenta un predicato, cioè una funzione booleana, che riceve due argomenti; il suo metodo astratto è test, che valuta il predicato definito sui due argomenti passati
- Vengono inoltre definite interfacce funzionali per i tipi primitivi int, long e double.

### Method references (slide 40)

I riferimenti ai metodi sono un'alternativa più concisa alle espressioni lambda per chiamare un metodo esistente. Possono essere utilizzati per riferirsi a metodi statici, metodi di istanza e costruttori.

```java
// Lambda che consiste solamente in un'invoazione di metodo già esistente
Consumer<String> c = System.out.println(s);
BiPredicate<String, String> eqstr = (s1, s2) -> s1.equals(s2);
```

In casi come quello sopra, in cui il corpo della lambda consiste solo in una chiamata a un metodo esistente, è possibile utilizzare un riferimento al metodo per riferirsi direttamente al metodo stesso.

```java
Consumer<String> c = System.out::println;
BiPredicate<String, String> eqstr = String::equals;
```

Nella chiamata al metodo si sostituisce `.`, `::` e non vengono passati i parametri. Il compilatore si occupa di fare il binding dei parametri; inferisce che il primo parametro è l'oggetto su cui si chiama il metodo, il secondo parametro è il parametro del metodo. In generale la sintassi di un riferimento a un metodo può essere una della seguenti:

- object::instanceMethod (es. System.out::println)
- Class::staticMethod (es. Integer::parseInt)
- Class::instanceMethod (es. String::length)
- Object::new (es. ArrayList::new)

## Stream API

### Iterazioni sulle collection - metodo forEach()

Introdotto come metodo di default in Java 8; prende in input un oggetto di tipo Consumer (esegue operazioni su oggetti di solito per modificare lo stato o per effettuare operazioni di output).

Ogni collezione può iterare sui suoi elementi tramite il metodo forEach() e passando in input un'espressione lambda per fare operazioni sugli elementi.

```java
list.forEach(s -> System.out.println(s));
```

### Stream API

Lo Stream API è una nuova libreria di alto livello che semplifica l'uso delle collezioni e offre supporto alla programmazione parallela; porta Java alla pari di altri linguaggi che puntano su nuove architetture basate su multi-core e cluster di computer che gestiscono grandi quantità di dati.

Un concetto fondamentale è lo Stream inteso come un flusso di dati che nasce da una collection e sul quale è possibile eseguire operazioni complicate con codice semplice basato su espressioni lambda e reference method.

#### Come ottenere oggetti Stream

**Stream finiti:**

```java
Stream<String> stream = Stream.of("a", "b", "c");
Stream<String> stream = Arrays.stream(new String[] {"a", "b", "c"});
Stream<String> stream = list.stream();
```

**Stream infiniti:**

```java
Stream<Integer> stream = Stream.iterate(2, n -> n * 2);
Stream<Double> stream = Stream.generate(() -> Math.random());
Stream.iterate(1, element -> element + 1).filter(element -> element % 5 == 0).limit(5).forEach(System.out::println);
```

Utilizzando i metodi dei sottotipi `IntStream`, `LongStream` e `DoubleStream` è possibile creare stream di interi, long e double.

```java
IntStream intStream = IntStream.range(1, 10);
LongStream longStream = LongStream.rangeClosed(1, 10);
DoubleStream doubleStream = DoubleStream.of(1.0, 2.0, 3.0);
```

A partire dalle collezioni è possibile ottenere uno stream tramite il metodo `stream()`.

```java
list.stream();
set.stream();
map.entrySet().stream();
```

### Definizione di Stream e Pipeline

Uno stream è una sequenza di elementi che si può iterare una sola volta (una volta terminato, lo stream non può essere riutilizzato). Uno stream non immagazzina i dati, ma permette di concatenare una serie di operazioni sugli elementi dello stream tramite un'operazione di pipeline.

Una pipeline è una sequenza di operazioni di aggregazione costituita da tre parti:

- Sorgente: origine degli elementi dello stream (es. una collezione, un array, un generatore, ecc.). Una sorgente mette a disposizione un metodo per ottenere un oggetto Stream.

- Zero o più operazioni aggregazione (o intermedie): trasformano uno stream in un altro stream. Queste operazioni sono lazy, cioè non vengono eseguite fino a quando non viene chiamata un'operazione terminale. Es.: `filter()`, `map()`, `sorted()`, `distinct()`, `limit()`, `skip()`.

- Operazione terminale: è un metodo che restituisce un risultato non di tipo Stream. Quando viene chiamata un'operazione terminale, tutte le operazioni intermedie vengono eseguite. Es.: `forEach()`, `collect()`, `reduce()`, `count()`, `min()`, `max()`.

```java
double average = product.stream().filter(p -> p.getName().length() < 10).mapToDouble(Product::getPrice).average().getAsDouble();
```

## Operazioni intermedie

### Filtering

Lo Stream API di Java 8 fornisce vari metodi che possono essere utilizzati per interrogare gli Stream (come si fa con una SELECT per interrogare un database).

- `filter()`: restituisce un nuovo stream contenente solo gli elementi che soddisfano il predicato specificato.

```java
products.stream().filter(p -> p.getName().length() < 10).collect(Collectors.toList());
```

- `distinct()`: restituisce un nuovo stream contenente solo gli elementi unici. Utilizza il metodo `equals()` per confrontare gli elementi.

```java
products.stream().map(Product::getName).distinct().collect(Collectors.toList());
```

- `limit()`: restituisce un nuovo stream contenente solo i primi n elementi dello stream originale. Prende in input un long che rappresenta il numero massimo di elementi da restituire.

```java
products.stream().filter(p -> p.getName().length() < 10).map(Product::getName).limit(3).collect(Collectors.toList());
```

### Mapping

Il mapping è un'operazione che trasforma gli elementi di uno stream in un altro tipo di dato. La funzione `map()` è un'operazione che prende in input un'altra funzione come argomento e applica questa funzione a ciascun elemento dello stream, restituendo un nuovo stream contenente i risultati della funzione. È utile per trasformare gli elementi di uno stream in un altro tipo di dato.

```java
products.stream().map(Product::getName).collect(Collectors.toList());
IntStream mapToInt = products.stream().mapToInt(value -> value.getId());
```

Lo stream iniziale estratto dalla Collection è uno stream di oggetti Product. La funzione `map()` viene utilizzata per trasformare ogni oggetto Product in una stringa contenente il nome del prodotto. Il risultato è uno stream di stringhe.

### Sorting

L'operazione `sorted()` viene utilizzata per ordinare gli elementi di uno stream in base a un criterio specificato. Può essere utilizzata con o senza un comparatore personalizzato.

```java
products.stream().map(Product::getName).sorted().collect(Collectors.toList());

products.stream().sorted(Comparator.comparing(Product::getName))
                 .collect(Collectors.toList());

products.stream().sorted(Comparator.comparing(Product::getName).reversed())
                 .collect(Collectors.toList());

products.stream().sorted(Comparator.comparing(Product::getName)
                 .thenComparing(Product::getPrice)).collect(Collectors.toList());
```

## Operazioni terminali

### Match condizionali e ricerche

Le operazioni terminali di match sono utilizzate per verificare se uno stream soddisfa una determinata condizione. Queste operazioni restituiscono un valore booleano.

```java
// Verifica se almeno un elemento soddisfa il predicato specificato
boolean match = products.stream().anyMatch(p -> p.getName().length() < 10);
// Verifica se tutti gli elementi soddisfano il predicato specificato
boolean match = products.stream().allMatch(p -> p.getName().length() < 10);
// Verifica se nessun elemento soddisfa il predicato specificato
boolean match = products.stream().noneMatch(p -> p.getName().length() < 10);
```

Lo Stream API fornisce due metodi per le ricerche negli stream:

- `findFirst()`: restituisce il primo elemento dello stream. Se lo stream è vuoto, restituisce un Optional vuoto.

```java
Optional<Product> res = products.stream().filter(p -> p.getName().length() < 10).findFirst();
```

- `findAny()`: restituisce un qualsiasi elemento dello stream. È utile per ottenere un elemento qualsiasi da uno stream parallelo.

```java
Optional<Product> res = products.stream().filter(p -> p.getName().length() < 10).findAny();
```

### Reduction

L'operazione di riduzione è un'operazione terminale che combina gli elementi di uno stream in un singolo risultato. È utile per eseguire operazioni di aggregazione come somma, media, conteggio, ecc.

Esistono operazioni di riduzione che ritornano collezioni, come `collect()`, e operazioni di riduzione che ritornano un singolo valore, come `reduce()`.

- `reduce()`: combina gli elementi di uno stream in un singolo risultato. Prende in input un'operazione binaria (funzione che prende due argomenti e restituisce un risultato) e un valore iniziale.

```java
// Somma dei prezzi dei prodotti con nome più corto di 10 caratteri
products.stream().filter(p -> p.getName().length() < 10).mapToDouble(p -> p.getPrice()).reduce(0, (p1, p2) -> p1 + p2);
```

- `collect()`: combina gli elementi di uno stream in una collezione. Prende in input un `Collector` che specifica come combinare gli elementi. Collectors è una classe di utilità che fornisce metodi statici per creare vari tipi di collector come `toList()`, `toCollection()`, `reducing()`, `joining()`, `groupingBy()`, `partitioningBy()`.

```java
// Restituisce una lista di nomi dei prodotti
TreeSet<String> s = products.stream().map(p -> p.getName()).collect(Collectors.toCollection(TreeSet::new));

String c = products.stream().map(p -> p.getName()).collect(Collectors.joining("; "));

Map<Float, List<Product>> m = products.stream().collect(Collectors.groupingBy(p -> p.getPrice()));

DoubleSummaryStatistics stat = products.stream().collect(Collectors.summarizingDouble(Product::getPrice));
```

### Parallel Stream

Lo Stream API di Java 8 supporta l'esecuzione parallela di operazioni sugli stream. Gli stream paralleli sono utili per eseguire operazioni su grandi quantità di dati in modo più efficiente, sfruttando i multi-core e i cluster di computer.

Per creare uno stream parallelo, è possibile utilizzare il metodo `parallelStream()` invece di `stream()`.

```java
products.parallelStream().filter(p -> p.getName().length() < 10).collect(Collectors.toList());
```

