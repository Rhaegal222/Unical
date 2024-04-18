package it.unical.elcampeon.service;

import it.unical.elcampeon.handler.AlertHandler;
import javafx.application.Platform;
import org.springframework.security.crypto.bcrypt.BCrypt;

import java.sql.*;
import java.time.LocalDate;

public class SqlQuery {

    private static final AlertHandler alertHandler = AlertHandler.getInstance();
    private SqlQuery() {}
    private static SqlQuery instance;
    public static SqlQuery getInstance() {
        if (instance == null)
            instance = new SqlQuery();
        return instance;
    }

    private Connection con;

    public Connection openConnection() {
        try {
            String url = "jdbc:sqlite:progettouid.db";
            con = DriverManager.getConnection(url);
        } catch (SQLException e) {
            Platform.runLater(alertHandler::createDatabaseConnectionErrorAlert);
        }
        return con;
    }

    public void closeConnection(Connection con){
        try {
            con.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    // Metodo per il controllo della password
    public boolean checkPassword(String username,String password) {
        try {
            con = openConnection();
            PreparedStatement stmt = con.prepareStatement("SELECT password FROM users WHERE username = ?");
            stmt.setString(1, username);
            ResultSet rs = stmt.executeQuery();
            if (BCrypt.checkpw(password, rs.getString(1))) {
                rs.close();
                stmt.close();
                closeConnection(con);
                return true;
            } else {
                rs.close();
                stmt.close();
                closeConnection(con);
                return false;
            }
        } catch (SQLException e) {
            throw new RuntimeException();
        }
    }


    public byte authenticateUser(String username, String password) {
        // Esegue una query per il login di un utente.
        try {
            if (checkUsernameLogin(username)) {
                con = openConnection();
                PreparedStatement stmt1 = con.prepareStatement("SELECT password FROM users WHERE username = ?");
                stmt1.setString(1, username);
                ResultSet rs1 = stmt1.executeQuery();
                if(BCrypt.checkpw(password, rs1.getString(1))) {
                    rs1.close();
                    stmt1.close();
                    closeConnection(con);
                    return 0;
                }
                else {
                    rs1.close();
                    stmt1.close();
                    closeConnection(con);
                    return 2;
                }
            }else{
                closeConnection(con);
                return 1;
            }
        } catch (SQLException e) {
            throw new RuntimeException();
        }
    }

    public boolean createUserAccount(String username, String password, String name, String surname, String email, LocalDate birthday) {
        // Esegue una query per la registrazione di un utente.
        if(checkEmail(email) || checkUsername(username)) return false;
        else
            try {
                con = openConnection();
                PreparedStatement stmt = con.prepareStatement("INSERT INTO users values (?, ?, ?, ?, ?, ?)");
                stmt.setString(1, username);
                stmt.setString(2, BCrypt.hashpw(password, BCrypt.gensalt(12)));
                stmt.setString(3, email);
                stmt.setObject(4, birthday);
                stmt.setString(5, name);
                stmt.setString(6, surname);
                stmt.executeUpdate();
                insertAccountSettings(username);
                stmt.close();
                closeConnection(con);
                return true;
            } catch (SQLException e) {
                throw new RuntimeException();
            }
    }

    private void insertAccountSettings(String username) {
        // Esegue una query per l'inserimento delle impostazioni di default di un utente.
        try{
            con = openConnection();
            PreparedStatement s = con.prepareStatement(
                    "INSERT INTO settings (username, theme, language, logged) VALUES (?,?,?,?)");
            s.setString(1, username);
            s.setString(2, "en");
            s.setString(3, "blue.css");
            s.setInt(4, 0);
            s.executeUpdate();

            s.close();
            closeConnection(con);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    public boolean checkUsernameLogin(String username){
        // Esegue una query per vedere se l'username inserito esiste nel database.
        try{
            con = openConnection();
            PreparedStatement stmt = con.prepareStatement("SELECT username From users");
            ResultSet rs = stmt.executeQuery();
            while (rs.next())
                if (rs.getString(1).equals(username)){
                    rs.close();
                    stmt.close();
                    closeConnection(con);
                    return true;
                }
            rs.close();
            stmt.close();
            closeConnection(con);
        }catch(SQLException e){
            throw new RuntimeException();
        }
        return false;
    }

    public boolean checkEmail(String email){
        // Esegue una query per vedere se la mail inserita esiste nel database. Questo metodo viene sfruttato
        // qualora un utente si fosse dimenticato la password

        try{
            con = openConnection();
            PreparedStatement stmt = con.prepareStatement("SELECT email From users");
            ResultSet rs = stmt.executeQuery();
            while (rs.next())
                if (rs.getString(1).equals(email)){
                    stmt.close();
                    rs.close();
                    closeConnection(con);
                    return true;
                }

            rs.close();
            stmt.close();
            closeConnection(con);
        }catch(SQLException e){
            throw new RuntimeException();
        }
        return false;
    }

    public boolean resetUserPassword(String email, String newPassword) {
        // Esegue una query per il cambio password
        if(checkEmail(email)){
            try {
                con = openConnection();
                PreparedStatement stmt1 = con.prepareStatement("UPDATE users SET Password = ? WHERE Email = ?");
                stmt1.setString(1,BCrypt.hashpw(newPassword, BCrypt.gensalt(12)));
                stmt1.setString(2,email);
                stmt1.executeUpdate();
                stmt1.close();
                closeConnection(con);
                return true;
            }catch(SQLException e){
                throw new RuntimeException();
            }
        }
        return false;
    }

    public String[] getNameSurname(String username){
        // Esegue una query per prendere il nome e il cognome di un utente
        try{
            con = openConnection();
            String [] array = new String[2];
            PreparedStatement stmt = con.prepareStatement("SELECT name, surname FROM users WHERE username = ?");
            stmt.setString(1,username);
            ResultSet rs = stmt.executeQuery();

            while(rs.next()){
                array[0] = rs.getString(1);
                array[1] = rs.getString(2);
            }

            rs.close();
            stmt.close();
            closeConnection(con);
            return array;

        }catch(SQLException e){
            throw new RuntimeException();
        }
    }

    public boolean checkUsername(String username) {
        try {
            con = openConnection();
            PreparedStatement stmt = con.prepareStatement("SELECT username From users");
            ResultSet rs = stmt.executeQuery();
            while (rs.next())
                if (rs.getString(1).equals(username)) {
                    stmt.close();
                    rs.close();
                    closeConnection(con);
                    return true;
                }

            stmt.close();
            rs.close();
            closeConnection(con);
        } catch (SQLException e) {
            throw new RuntimeException();
        }
        return false;
    }




    public boolean changeUserName(String newName,String username){
        try{
            con = openConnection();
            PreparedStatement stm = con.prepareStatement("UPDATE users SET name = ? WHERE username = ?");
            stm.setString(1, newName );
            stm.setString(2,username);
            if(stm.executeUpdate() == 1){
                stm.close();
                closeConnection(con);
                return true;
            }

            if(stm.executeUpdate() == 0){
                stm.close();
                closeConnection(con);
                return false;
            }
            stm.close();
            closeConnection(con);
            return true;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
    public boolean changeUserSurname(String surname,String username){
        try{
            con = openConnection();
            PreparedStatement stm = con.prepareStatement("UPDATE users SET surname = ? WHERE username = ?");
            stm.setString(1, surname );
            stm.setString(2,username);
            if(stm.executeUpdate() == 1){
                stm.close();
                closeConnection(con);
                return true;
            }

            if(stm.executeUpdate() == 0){
                stm.close();
                closeConnection(con);
                return false;
            }
            stm.close();
            closeConnection(con);
            return true;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    public boolean changeUserPassword(String password, String username) {
        try{
            con = openConnection();
            PreparedStatement stm = con.prepareStatement("UPDATE users SET password = ? WHERE username = ?");
            stm.setString(1, BCrypt.hashpw(password, BCrypt.gensalt(12)) );
            stm.setString(2,username);
            if(stm.executeUpdate() == 1){
                closeConnection(con);
                stm.close();
                return true;
            }

            if(stm.executeUpdate() == 0){
                closeConnection(con);
                stm.close();
                return false;
            }
            stm.close();
            closeConnection(con);
            return true;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    public String [] getUserSettings(String username){
        try{
            con = openConnection();
            String [] settings = new String[3];
            PreparedStatement s = con.prepareStatement("SELECT theme, language FROM settings WHERE username = ?");
            s.setString(1, username);

            ResultSet rs = s.executeQuery();

            settings [0] = rs.getString(1); // theme
            settings [1] = rs.getString(2); // language

            rs.close();
            closeConnection(con);
            return settings;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    public void updateUserSettings(String username, String theme, String language)  {
        try {
            con = openConnection();
            PreparedStatement s = con.prepareStatement("UPDATE settings SET theme = ?, language = ? WHERE username = ? ");
            s.setString(1, theme);
            s.setString(2, language);
            s.setString(3, username);
            s.executeUpdate();
            closeConnection(con);
        } catch (Exception e) {
            alertHandler.createGenericErrorAlert();
        }
    }

    public boolean verifyEmailAvailability(String email) {
        try{
            con = openConnection();
            PreparedStatement s = con.prepareStatement("SELECT email FROM users");
            ResultSet rs = s.executeQuery();
            while(rs.next()){
                if(rs.getString(1).equals(email)){
                    rs.close();
                    s.close();
                    closeConnection(con);
                    return true;
                }
            }
            rs.close();
            s.close();
            return false;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    public String[] getProfileInfo(String username){
        try{
            con = openConnection();
            String [] array = new String[4];
            PreparedStatement stmt = con.prepareStatement("SELECT name, surname, email, birthday FROM users WHERE username = ?");
            stmt.setString(1,username);
            ResultSet rs = stmt.executeQuery();
            while (rs.next()){
                array[0] = rs.getString(1);
                array[1] = rs.getString(2);
                array[2] = rs.getString(3);
                array[3] = rs.getString(4);
            }
            rs.close();
            stmt.close();
            closeConnection(con);
            return array;
        }catch(SQLException e){
            throw new RuntimeException();
        }
    }
}