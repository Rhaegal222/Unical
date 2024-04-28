# Guida per la creazione di un backend

## Introduzione

Un backend è la parte di un'applicazione che si occupa di elaborare i dati e di fornire le risposte alle richieste provenienti dal frontend. Questa guida illustra i passaggi necessari per creare un backend utilizzando Java, Sping Boot, Spring Data JPA e Postgres.

## Creazione di un progetto Spring Boot

Per creare un progetto Spring Boot, è possibile utilizzare [Spring Initializr](https://start.spring.io/). In questo caso, è necessario selezionare le dipendenze `Spring Boot DevTools`, `Lombok`, `Spring Web`, `Spring Security`, `JDBC API`, `Spring Data JPA`, `PostgreSQL Driver` e `Validation`.

## Configurazione di un database

Per configurare un database Postgres, è necessario aggiungere le seguenti proprietà al file `application.properties`:

```properties
spring.application.name=backend

# application.properties
spring.datasource.url=jdbc:postgresql://localhost:5432/postgres
spring.datasource.username=postgres
spring.datasource.password=postgres

spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true

# Se usi un dialetto specifico di PostgreSQL
spring.jpa.database-platform=org.hibernate.dialect.PostgreSQLDialect
```

## Creazione di un'entità, un repository, un servizio e un controller

### Creazione di un'entità

Il passo successivo consiste nella creazione delle entità. Un'entità rappresenta una tabella del database. Ad esempio, la seguente classe rappresenta un'entità `User` nel package `com.example.backend.data.entity`:

```java
package com.example.backend.data.entity;

import lombok.Data;

import jakarta.persistence.*; // Importa le annotazioni di JPA
import lombok.Data; // Importa Data da Lombok che genera i getter e i setter
import lombok.NoArgsConstructor; // Importa NoArgsConstructor da Lombok che genera un costruttore vuoto
import org.springframework.data.jpa.domain.support.AuditingEntityListener; // Importa AuditingEntityListener che permette di registrare le modifiche alle entità nel database
import com.example.backend.core.entityAuditTrailListener.UserListener; // Importa UserListener che permette di registrare le modifiche alle entità User nel database

@Entity // Indica che la classe è un'entità
@Data // Genera i getter e i setter
public class User {
    @Id // Indica che il campo è la chiave primaria
    // Genera un valore univoco per la chiave primaria
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String username;
    private String password;
}
```

### Creazione di un listener per le entità (opzionale)

Per registrare le modifiche alle entità nel database, è possibile creare un listener. Ad esempio, la seguente classe rappresenta un listener `UserListener` nel package `com.example.backend.core.entityAuditTrailListener`:

```java
package com.example.backend.core.entityAuditTrailListener;

import com.example.backend.data.entity.User; // Importa l'entità User
import jakarta.persistence.*; // Importa le annotazioni di JPA
import org.apache.commons.logging.Log; // Importa Log da Apache Commons Logging che permette di registrare le modifiche alle entità nel database
import org.apache.commons.logging.LogFactory; // Importa LogFactory da Apache Commons Logging che permette di creare un logger

public class UserListener {
    private static final Log log = LogFactory.getLog(UserListener.class);

    @PrePersist // Indica che il metodo viene eseguito prima di persistere l'entità
    public void prePersist(User user) {
        log.info("User " + user.getUsername() + " is being persisted");
    }

    @PostPersist // Indica che il metodo viene eseguito dopo aver persistito l'entità
    public void postPersist(User user) {
        log.info("User " + user.getUsername() + " has been persisted");
    }

    @PreUpdate // Indica che il metodo viene eseguito prima di aggiornare l'entità
    public void preUpdate(User user) {
        log.info("User " + user.getUsername() + " is being updated");
    }

    @PostUpdate // Indica che il metodo viene eseguito dopo aver aggiornato l'entità
    public void postUpdate(User user) {
        log.info("User " + user.getUsername() + " has been updated");
    }

    @PreRemove // Indica che il metodo viene eseguito prima di rimuovere l'entità
    public void preRemove(User user) {
        log.info("User " + user.getUsername() + " is being removed");
    }

    @PostRemove // Indica che il metodo viene eseguito dopo aver rimosso l'entità
    public void postRemove(User user) {
        log.info("User " + user.getUsername() + " has been removed");
    }
}
```

### Creazione di un DTO (Data Transfer Object)

Un DTO (Data Transfer Object) è un oggetto che trasporta i dati tra il frontend e il backend. Un DTO può contenere solo i campi necessari per la visualizzazione dei dati e non deve contenere i campi sensibili come la password. Ad esempio, la seguente classe rappresenta un DTO `UserDto` nel package `com.example.backend.data.dto`:

```java
package com.example.backend.data.dto;

import lombok.Data;
import lombok.NoArgsConstructor;
import jakarta.validation.constraints.*;

@Data
@NoArgsConstructor
public class UserDto {
    private Long id;

    @NotBlank
    @Size(min = 3, max = 50)
    private String username;

    @NotBlank
    @Size(min = 6, max = 100)
    private String password;
}
```

### Creazione di un repository

Una volta creata l'entità, è necessario creare un repository per interagire con il database.

Con Spring Data JPA, è possibile creare un repository estendendo l'interfaccia `JpaRepository`. I metodi di base come `save`, `findById`, `findAll`, `delete` e `count` sono già implementati in `JpaRepository`. Inoltre, è possibile definire query personalizzate utilizzando l'annotazione `@Query`.

Quindi ci spostiamo nel package `com.example.backend.data.dao` e creiamo un'interfaccia `UserDao`:

```java
package com.example.backend.data.dao;

import com.example.backend.data.entity.User; // Importa User che rappresenta un'entità User
import org.springframework.data.jpa.repository.JpaRepository; // Importa JpaRepository da Spring Data JPA che permette di interagire con il database
import org.springframework.data.jpa.repository.Query; // Importa Query da Spring Data JPA che permette di definire query personalizzate
import org.springframework.stereotype.Repository; // Importa Repository da Spring Framework che indica che l'interfaccia è un repository

@Repository
public interface UserDao extends JpaRepository<User, Long> {
    // Query personalizzata per cercare un utente per username
    @Query("SELECT u FROM User u WHERE u.username = ?1")
    User findByUsername(String username);

    // Non è necessario definire i metodi di base come save, findById, findAll, delete e count
}
```

### Creazione di un servizio

Successivamente, è necessario creare un servizio per gestire le operazioni sulle entità. Le operazioni possono includere la ricerca, l'aggiornamento e la rimozione delle entità.

#### Creazione di un'interfaccia per il servizio

Quindi ci spostiamo nel package `com.example.backend.service` e creiamo un'interfaccia `UserService`:

```java
package com.example.backend.service;

import com.example.backend.data.entity.User; // Importa User che rappresenta un'entità User

public interface UserService {
    void save(User user);
    User findByUsername(String username);
}
```

#### Creazione dell'implementazione del servizio

Poi dentro al package `com.example.backend.service.impl` creiamo una classe `UserServiceImpl` che implementa l'interfaccia `UserService`:

```java
package com.example.backend.service.impl;

import com.example.backend.data.dao.UserDao; // Importa UserDao che permette di interagire con il database
import com.example.backend.data.entity.User; // Importa User che rappresenta un'entità User
import com.example.backend.service.UserService; // Importa UserService che rappresenta un servizio per gestire le operazioni sulle entità
import lombok.RequiredArgsConstructor; // Importa RequiredArgsConstructor da Lombok che genera un costruttore con i parametri richiesti
import org.springframework.stereotype.Service; // Importa Service da Spring Framework che indica che la classe è un servizio
import org.springframework.beans.factory.annotation.Autowired; // Importa Autowired da Spring Framework che permette di iniettare le dipendenze

@Service
@RequiredArgsConstructor
public class UserServiceImpl implements UserService {
    @Autowired
    private UserDao userDao;

    @Override
    public void save(User user) {
        userDao.save(user);
    }

    @Override
    public User findByUsername(String username) {
        return userDao.findByUsername(username);
    }
}
```

### Creazione di un controller

Successivamente, è necessario creare un controller per gestire le richieste HTTP provenienti dal frontend. Un controller può includere metodi per gestire le richieste di tipo `GET`, `POST`, `PUT` e `DELETE`.

Quindi ci spostiamo nel package `com.example.backend.controller` e creiamo una classe `UserController`:

```java
package com.example.backend.controller;

import com.example.backend.data.entity.User; // Importa User che rappresenta un'entità User
import com.example.backend.service.UserService; // Importa UserService che rappresenta un servizio per gestire le operazioni sulle entità
import lombok.RequiredArgsConstructor; // Importa RequiredArgsConstructor da Lombok che genera un costruttore con i parametri richiesti
import org.springframework.http.HttpStatus; // Importa HttpStatus da Spring Framework che rappresenta lo stato HTTP
import org.springframework.http.ResponseEntity; // Importa ResponseEntity da Spring Framework che rappresenta una risposta HTTP
import org.springframework.web.bind.annotation.*; // Importa RequestMapping da Spring Framework che permette di mappare le richieste HTTP ai metodi

@RestController
@RequestMapping("/api/users")
@RequiredArgsConstructor
public class UserController {
    private final UserService userService;

    @PostMapping
    public ResponseEntity<Void> save(@RequestBody User user) {
        userService.save(user);
        return new ResponseEntity<>(HttpStatus.CREATED);
    }

    @GetMapping("/{username}")
    public ResponseEntity<User> findByUsername(@PathVariable String username) {
        User user = userService.findByUsername(username);
        return new ResponseEntity<>(user, HttpStatus.OK);
    }
}
```

## Configurazione dell'applicazione Spring Boot

Il package `com.example.backend.config` contiene le classi di configurazione dell'applicazione. Queste classi possono includere la configurazione di Spring Security, la configurazione di Spring Data JPA, la configurazione di ModelMapper e la configurazione della cache di Spring.

In questo caso specifico, il package `com.example.backend.config` deve contenere le seguenti classi e package:

- il package `audit` che contiene le classi per l'audit delle entità.
- il package `i18n` che contiene le classi per la localizzazione delle risorse.
- il package `security` che contiene le classi per la sicurezza dell'applicazione.
- la classe `ModelMapperConfig` che configura ModelMapper per mappare le entità ai DTO.
- la classe `CacheConfig` che configura la cache di Spring.

### Configurazione di `security`

Il package `com.example.backend.config.security` contiene le classi per la sicurezza dell'applicazione. Queste classi possono includere la configurazione di Spring Security, la configurazione di JWT e la configurazione di OAuth2.

Nell'esempio seguente, la classe `SecurityConfig` configura Spring Security per richiedere l'autenticazione per tutte le richieste e per consentire l'accesso a determinati endpoint solo agli utenti autenticati con un ruolo specifico.




### Configurazione di `audit`

Il package `com.example.backend.config.audit` contiene le classi per l'audit delle entità. Queste classi possono includere un listener per le entità e un interceptor per le richieste HTTP.

Nell'esempio seguente, la classe `UserAuditorAware` implementa l'interfaccia `AuditorAware` per restituire il nome dell'utente correntemente autenticato. Questo nome può essere utilizzato per registrare le modifiche alle entità nel database.

```java
package com.example.backend.config.auditor;

import org.springframework.data.domain.AuditorAware;

import java.util.Optional;

public class UserAuditorAware implements AuditorAware<String> {
    @Override
    public Optional<Long> getCurrentAuditor() {
        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        if (authentication == null || !authentication.isAuthenticated()) {
            return Optional.empty();
        }

        if (authentication.getPrincipal() instanceof UserDetailsImpl) {
            UserDetails userDetails = (UserDetails) authentication.getPrincipal();
            return Optional.of(userDetails.getUsername());
        }

        return Optional.empty();
    }
}
```


