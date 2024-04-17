package it.unical.elcampeon.model;

import it.unical.elcampeon.handler.AlertHandler;
import it.unical.elcampeon.handler.LoggedHandler;
import it.unical.elcampeon.handler.SettingsHandler;
import it.unical.elcampeon.service.EmailService;
import it.unical.elcampeon.service.SqlService;

import java.time.LocalDate;

public class User {
    // Attributi
    private String username;
    private String password;
    private String name;
    private String surname;
    private String email;
    private LocalDate birthday;
    private final boolean stayLogged;

    AlertHandler alertHandler = AlertHandler.getInstance();
    SqlService sqlService = SqlService.getInstance();
    EmailService emailService = EmailService.getInstance();
    LoggedHandler loggedHandler = LoggedHandler.getInstance();
    SettingsHandler settingsHandler = SettingsHandler.getInstance();

    // Costruttore per la creazione di un utente
    public User(String username, String password, String name, String surname, String email, LocalDate birthday) {
        this.username = username;
        this.password = password;
        this.name = name;
        this.surname = surname;
        this.email = email;
        this.birthday = birthday;
        this.stayLogged = false;
    }

    // Costruttore per la creazione di un utente
    public User(String username, String password, Boolean stayLogged) {
        this.username = username;
        this.password = password;
        this.stayLogged = stayLogged;
    }

    // Getters
    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }

    public String getName() {
        return name;
    }

    public String getSurname() {
        return surname;
    }

    public String getEmail() {
        return email;
    }

    public LocalDate getBirthday() {
        return birthday;
    }

    // Setters
    public void setUsername(String username) {
        this.username = username;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public void setName(String name) {
        this.name = name;
    }
    public void setSurname(String surname) {
        this.surname = surname;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setBirthday(LocalDate birthday) {
        this.birthday = birthday;
    }

    // Override di equals e hashCode per la gestione degli utenti
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof User user)) return false; // Se l'oggetto non è un utente ritorna false
        return username.equals(user.username);
    }

    @Override
    public int hashCode() {
        return username.hashCode();
    }

    // Override di toString per la stampa degli utenti
    @Override
    public String toString() {
        return "User{" +
                "username='" + username + '\'' +
                ", password='" + password +
                ", name='" + name + '\'' +
                ", surname='" + surname + '\'' +
                ", email='" + email + '\'' +
                ", birthday='" + birthday + '\'' +
                '}';
    }

    // Metodo per la creazione di un utente
    public static User createUser(String username, String password, String name, String surname, String email, LocalDate birthday) {
        return new User(username, password, name, surname, email, birthday);
    }

    public void performLogin() {
        if (sqlService.authenticateUser(this.username, this.password) == 0) {
            loggedHandler.setUsername(username);
            if (stayLogged) loggedHandler.stayLoggedWriting(username);
            else loggedHandler.stayLoggedWriting("null");
            settingsHandler.updateSettings(sqlService.getUserSettings(username));
            alertHandler.createLoginSuccessAlert();
        } else {
            alertHandler.createWrongCredentialsAlert();
        }
    }

    public void performRegister() {
        if (sqlService.createUserAccount(this.username, this.password, this.name, this.surname, this.email, this.birthday)) {
            alertHandler.createRegistrationSuccessAlert();
        } else {
            alertHandler.createAlreadyUsedAlert();
        }
        emailService.sendWelcomeEmail(this.email, "El Campeon - Registrazione",
                    "Ciao " + this.name + ", ti ringraziamo per aver effettuato la registrazione!");
    }
}
