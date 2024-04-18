package it.unical.elcampeon.handler;

import javax.crypto.Cipher;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.spec.SecretKeySpec;
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;
import java.util.Base64;

// Classe per gestire il mantieni accesso
public class LoggedHandler {

    private static final AlertHandler alertHandler = AlertHandler.getInstance();

    private String username = "null";

    private static LoggedHandler instance;

    public static LoggedHandler getInstance() {
        if(instance == null)
            try {
                instance = new LoggedHandler();
                return instance;
            } catch (NoSuchPaddingException | NoSuchAlgorithmException e) {
                alertHandler.createGenericErrorAlert();
            }
        return instance;
    }
    private LoggedHandler() throws NoSuchPaddingException, NoSuchAlgorithmException {}

    private  SecretKeySpec secretKey;
    byte [] key;

    // Trasforma la chiave in una SecretKeySpec (con l'algoritmo di hashing SHA-512)
    public void setKey(String myKey) throws NoSuchAlgorithmException {

        key = myKey.getBytes(StandardCharsets.UTF_8);
        MessageDigest sha = MessageDigest.getInstance("SHA-512");
        key = sha.digest(key);
        key = Arrays.copyOf(key, 32);
        secretKey = new SecretKeySpec(key, "AES");
    }

    // Crypta l'username
    private String encryptUsername(String username){
        try {
            setKey("ElCampeon");
            Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
            cipher.init(Cipher.ENCRYPT_MODE, secretKey);
            return Base64.getEncoder().encodeToString(cipher.doFinal(username.getBytes(StandardCharsets.UTF_8)));
        }catch (Exception e){
            System.out.println("Error in LoggedHandler.java (rows: 44-51) " + e);
        }
        return null;
    }

    // Decrypta username
    private void decryptUsername(String usernameCrypyted, String sec){
        try {
            setKey(sec);
            Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
            cipher.init(Cipher.DECRYPT_MODE, secretKey);
            this.username = new String(cipher.doFinal(Base64.getDecoder().decode(usernameCrypyted)));
        }catch (Exception e){
            System.out.println("Error in LoggedHandler.java (rows: 57-64) "+ e);
        }
    }

    // Legge sul file di testo su cui è salvato l'username
    public String stayLoggedReading(){
        try {
            // Se il file di testo non esiste lo crea
            File file = new File("stayLogged.txt");
            if(!file.exists()){
                setNullUser();
            }
            // Legge il file di testo
            FileReader stream = new FileReader("stayLogged.txt");
            BufferedReader buff = new BufferedReader(stream);
            String username = buff.readLine();
            if(username == null){
                setNullUser();
                stayLoggedReading();
            } else if(username.equals("null")) {
                stream.close();
                buff.close();
                return username;
            }
            else {
                stream.close();
                buff.close();
                String myKey = "ElCampeon";
                decryptUsername(username, myKey);
                return this.username;
            }

        }catch (IOException e){
            alertHandler.createGenericErrorAlert();
        }
        return null;
    }

    private void setNullUser(){
        try{
            FileWriter stream = new FileWriter("stayLogged.txt", false);
            PrintWriter file = new PrintWriter(stream);
            file.println("null");
            stream.close();
            file.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    // Scrive sul file di testo in cui verrà salvato il nome
    public void stayLoggedWriting(String username){
        try {
            FileWriter stream = new FileWriter("stayLogged.txt", false);
            PrintWriter file = new PrintWriter(stream);
            if(username.equals("null")) file.println(username);
            else file.println(encryptUsername(username));
            stream.close();
            file.close();
        }catch (IOException e){
            System.out.println("Error in LoggedHandler.java (rows: 82-91) " + e);
        }
    }

    public void setUsername(String username){
        this.username = username;
    }

    public String getUsername(){
        return username;
    }
}
