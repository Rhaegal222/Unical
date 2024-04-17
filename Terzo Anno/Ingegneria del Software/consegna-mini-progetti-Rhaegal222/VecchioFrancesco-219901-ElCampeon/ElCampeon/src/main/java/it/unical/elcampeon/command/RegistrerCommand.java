package it.unical.elcampeon.command;

import it.unical.elcampeon.model.User;

import java.time.LocalDate;

public class RegistrerCommand implements Command{

    private final User user;


    public RegistrerCommand(String username, String password, String name, String surname, String email, LocalDate birthday){
        this.user = new User(username, password, name, surname, email, birthday);
    }

    @Override
    public void execute() {
        user.performRegister();
    }
}
