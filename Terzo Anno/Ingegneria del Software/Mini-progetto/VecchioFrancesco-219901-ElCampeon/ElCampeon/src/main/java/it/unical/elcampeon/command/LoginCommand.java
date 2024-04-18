package it.unical.elcampeon.command;

import it.unical.elcampeon.model.User;

public class LoginCommand implements Command {

    String username;
    String password;
    Boolean stayLogged;

    public LoginCommand(String username, String password, boolean stayLogged) {
        this.username = username;
        this.password = password;
        this.stayLogged = stayLogged;
    }

    @Override
    public void execute() {
        User user = new User(username, password, stayLogged);
        user.performLogin();
    }
}
