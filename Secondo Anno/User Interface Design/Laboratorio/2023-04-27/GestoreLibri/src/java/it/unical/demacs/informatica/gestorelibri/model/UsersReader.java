package it.unical.demacs.informatica.gestorelibri.model;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashMap;
import java.util.List;

public class UsersReader {
    private final HashMap<String, String> users;
    private static UsersReader instance = null;
    private final static String RESOURCE_PATH = "/it/unical/demacs/informatica/gestorelibri/";
    private static final String path = RESOURCE_PATH + "files" + File.separator + "users.txt";
    private UsersReader(){
        users = new HashMap<>();
        try{
            List<String> allUsers = Files.readAllLines();
            allUsers.forEach(str -> {
                String[] res = str.split(";");
                users.put(res[0], res[1]);
            });
        } catch (IOException e) {
            System.out.println("FILE NON TROVATO");
            System.out.println(Path.of(path));
        }
    }
    public static UsersReader getInstance(){
        if(instance == null)
            instance = new UsersReader();
        return instance;
    }
    public boolean checkAccess(String user, String password){
        String pass = users.get(user);
        if(pass==null)
            return false;
        return pass.equals(password);
    }
}
