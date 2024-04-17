-- TABELLE PER IL PROGETTO DI BASI DI DATI

-- ok
CREATE TABLE Actor(
    actor_id   INT           NOT NULL PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50)   NOT NULL,
    last_name  VARCHAR(50)   NOT NULL
);

-- ok
CREATE TABLE Country(
    country_id     INT          NOT NULL PRIMARY KEY,
    country        VARCHAR(50)  NOT NULL
);

-- ok
CREATE TABLE Category(
    category_id INT          NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(30)  NOT NULL
);

-- ok
CREATE TABLE SpecialFeatures(
    feature_id INT         NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name       VARCHAR(30) NOT NULL
);

-- ok
CREATE TABLE Language(
    language_id INT         NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(30) NOT NULL
);

-- ok
CREATE TABLE Store(
    store_id         INT    NOT NULL PRIMARY KEY AUTO_INCREMENT,
    manager_staff_id INT    NOT NULL,
    address_id       INT    NOT NULL

    -- commentato queste 2 linee per evitare la dipendenza circolare
    -- verranno aggiunte dopo aver creato tutte le altre tabelle (guarda a fine file) 
    -- FOREIGN KEY (manager_staff_id) REFERENCES Staff(staff_id),
    -- FOREIGN KEY (address_id)       REFERENCES Address(address_id)    
);

-- ok
CREATE TABLE City(
    
    city_id    INT          NOT NULL PRIMARY KEY AUTO_INCREMENT,
    city       VARCHAR(50)  NOT NULL,
    country_id INT          NOT NULL,
    
    FOREIGN KEY (country_id) REFERENCES Country(country_id)   
);

-- ok
CREATE TABLE Address(
    
    address_id  INT         PRIMARY KEY AUTO_INCREMENT,
    address     VARCHAR(30) NOT NULL,
    address2    VARCHAR(30),
    district    VARCHAR(30) NOT NULL,
    city_id     INT         NOT NULL,
    postal_code INT         NOT NULL,
    phone       INT,
    location    VARCHAR(50),
  
    FOREIGN KEY (city_id)   REFERENCES City(city_id)
);

-- ok
CREATE TABLE Staff(
    
    staff_id    INT         NOT NULL PRIMARY KEY AUTO_INCREMENT,
    first_name  VARCHAR(50) NOT NULL,
    last_name   VARCHAR(50) NOT NULL,
    address_id  INT         NOT NULL,
    picture     VARCHAR(50) NOT NULL,
    email       VARCHAR(50) NOT NULL,
    store_id    INT         NOT NULL,
    active      BOOLEAN     NOT NULL,
    username    VARCHAR(30) NOT NULL,
    password    VARCHAR(30) NOT NULL,
    
    FOREIGN KEY (address_id) REFERENCES Address(address_id),
    FOREIGN KEY (store_id)   REFERENCES Store(store_id)
);

-- ok
CREATE TABLE Customer(
    
    customer_id INT             NOT NULL PRIMARY KEY AUTO_INCREMENT,
    store_id    INT             NOT NULL,
    first_name  VARCHAR(50),
    last_name   VARCHAR(50),
    email       VARCHAR(50),
    address_id  INT             NOT NULL,
    active      BOOLEAN,
    create_date DATETIME,
    
    FOREIGN KEY (store_id)   REFERENCES Store(store_id),
    FOREIGN KEY (address_id) REFERENCES Address(address_id)
);

-- ok
CREATE TABLE Film(
    film_id              INT            NOT NULL PRIMARY KEY AUTO_INCREMENT,
    title                VARCHAR(50)    NOT NULL,
    description          VARCHAR(1000)  NOT NULL,
    release_year         VARCHAR(4)     NOT NULL,
    language_id          INT,
    original_language_id INT,
    rental_duration      INT            NOT NULL,
    rental_rate          INT            NOT NULL,
    length               VARCHAR(3)     NOT NULL,
    replacement_cost     INT            NOT NULL,
    rating               INT            NOT NULL,
    FOREIGN KEY(language_id)            REFERENCES Language(language_id),
    FOREIGN KEY(original_language_id)   REFERENCES Language(language_id)
);

-- ok
CREATE TABLE CDFilm(
    cd_film_id INT      PRIMARY KEY AUTO_INCREMENT,
    film_id    INT,
    store_id   INT,

    FOREIGN KEY (film_id)      REFERENCES Film(film_id),
	FOREIGN KEY (store_id)     REFERENCES Store(store_id)
);

-- ok
CREATE TABLE FilmActor(
    
    actor_id    INT     NOT NULL,
    film_id     INT     NOT NULL,

    PRIMARY KEY(actor_id, film_id),
    FOREIGN KEY(actor_id)   REFERENCES Actor(actor_id),
    FOREIGN KEY(film_id)    REFERENCES Film(film_id)
);                                                     

-- ok                                         
CREATE TABLE  FilmCategory(                                
    film_id         INT     NOT NULL,
    category_id     INT     NOT NULL,
    
    PRIMARY KEY (film_id, category_id),
    FOREIGN KEY (film_id)     REFERENCES Film(film_id),
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
);

-- ok
CREATE TABLE Rental(
    rental_id   INT     NOT NULL    PRIMARY KEY AUTO_INCREMENT,
    rental_date DATE    NOT NULL,
    cd_film_id  INT     NOT NULL,
    customer_id INT     NOT NULL,
    return_date DATE    NOT NULL,
    staff_id    INT     NOT NULL,
    
    FOREIGN KEY(customer_id)     REFERENCES Customer(customer_id),
    FOREIGN KEY(cd_film_id)      REFERENCES CDFilm(cd_film_id),
    FOREIGN KEY(staff_id)        REFERENCES Staff(staff_id)
);

-- ok
CREATE TABLE Payment(
    payent_id    INT    NOT NULL    PRIMARY KEY AUTO_INCREMENT,
    customer_id  INT    NOT NULL,
    staff_id     INT    NOT NULL,
    rental_id    INT    NOT NULL,
    amount       INT    NOT NULL,
    payment_date DATE   NOT NULL,
    
    FOREIGN KEY(customer_id)    REFERENCES Customer(customer_id),
    FOREIGN KEY(staff_id)       REFERENCES Staff(staff_id),
    FOREIGN KEY(rental_id)      REFERENCES Rental(rental_id)
);

-- ok modified! :) 
-- DA INSERIRE DOPO AVER CREATO TUTTE LE ALTRE TABELLE
ALTER TABLE Store ADD ( 
    FOREIGN KEY (manager_staff_id) REFERENCES Staff(staff_id),
    FOREIGN KEY (address_id)       REFERENCES Address(address_id)    
);