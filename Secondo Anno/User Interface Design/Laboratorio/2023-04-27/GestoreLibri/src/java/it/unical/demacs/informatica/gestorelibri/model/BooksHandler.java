package it.unical.demacs.informatica.gestorelibri.model;

import it.unical.demacs.informatica.gestorelibri.Message;
import it.unical.demacs.informatica.gestorelibri.view.SceneHandler;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class BooksHandler {
    private User user;
    private final String path = "files" + File.separator + "books.txt";
    private static BooksHandler instance = null;
    private BooksHandler(){
        user = null;
    }
    public static BooksHandler getInstance(){
        if(instance==null)
            instance = new BooksHandler();
        return instance;
    }
    public List<Book> login(User user){
        Objects.requireNonNull(user, "User cannot be null");
        logout();
        List<Book> books = new ArrayList<>();
        this.user = user;
        try{
            List<String> lines = Files.readAllLines(Path.of(path));
            for(String line:lines){
                String[] res = line.split(";");
                if(res[0].equals(this.user.username()))
                    books.add(new Book(res[1], res[2], res[3], res[4], res[5]));
            }
        } catch (Exception ignored){
            SceneHandler.getInstance().showError(Message.LOGIN_ERROR);
        }
        return books;
    }
    public void logout(){
        this.user = null;
    }
    public boolean addBook(Book b){
        if(user == null)
            return false;
        try{
            BufferedWriter writer = new BufferedWriter(new FileWriter(path, true));
            writer.append(user.username()).append(";").append(b.toString()).append(System.lineSeparator());
            writer.close();
        } catch (IOException e){
            return false;
        }
        return true;
    }
}
