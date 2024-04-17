package it.unical.elcampeon.service;

import it.unical.elcampeon.handler.AlertHandler;
import it.unical.elcampeon.model.Settings;

import java.time.LocalDate;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

// Executor service per l'esecuzione delle query
public class SqlService {
    private static final AlertHandler alertHandler = AlertHandler.getInstance();
    private static final SqlQuery sqlQuery = SqlQuery.getInstance();

    private static SqlService instance;
    public static SqlService getInstance() {
        if(instance == null)
            instance = new SqlService();
        return instance;
    }

    // Metodi per l'esecuzione delle query

    public byte authenticateUser(String username, String password) {
        byte[] res = new byte[1];
        ExecutorService queryExe = Executors.newSingleThreadExecutor();
        Future<?> future = queryExe.submit(() -> res[0] = sqlQuery.authenticateUser(username, password));

        try { future.get(); }
        catch (InterruptedException | ExecutionException e) { alertHandler.createGenericErrorAlert(); }
        finally { queryExe.shutdown(); }
        return res[0];
    }

    public boolean createUserAccount(String username, String password, String name, String surname, String email, LocalDate birthday){
        final boolean[] c = new boolean[1];
        ExecutorService queryExe = Executors.newSingleThreadExecutor();
        Future<?> future = queryExe.submit(() -> c[0] = sqlQuery.createUserAccount(username, password, name, surname, email, birthday));

        try { future.get(); }
        catch (InterruptedException | ExecutionException e) { alertHandler.createGenericErrorAlert();}
        finally { queryExe.shutdown(); }
        return c[0];
    }

    public boolean resetUserPassword(String email, String password){
        boolean[] res = new boolean[1];
        ExecutorService queryExe = Executors.newSingleThreadExecutor();
        Future<?> future = queryExe.submit(() -> res[0] = sqlQuery.resetUserPassword(email, password));

        try { future.get(); }
        catch (InterruptedException | ExecutionException e) { alertHandler.createGenericErrorAlert(); }
        finally { queryExe.shutdown(); }
        return res[0];
    }

    public boolean changeUserName( String newName,String username){
        boolean[] res = new boolean[1];
        ExecutorService queryExe = Executors.newSingleThreadExecutor();
        Future<?> future = queryExe.submit(() -> res[0] = sqlQuery.changeUserName(newName,username));

        try { future.get(); }
        catch (InterruptedException | ExecutionException e) { alertHandler.createGenericErrorAlert();}
        finally { queryExe.shutdown(); }
        return res[0];
    }
    public boolean changeUserSurname( String newSurName,String username){
        boolean[] res = new boolean[1];
        ExecutorService queryExe = Executors.newSingleThreadExecutor();
        Future<?> future = queryExe.submit(() -> res[0] = sqlQuery.changeUserSurname(newSurName,username));

        try { future.get(); }
        catch (InterruptedException | ExecutionException e) { alertHandler.createGenericErrorAlert();}
        finally { queryExe.shutdown(); }
        return res[0];
    }

    public boolean changeUserPassword(String newPassword, String username) {
        boolean[] res = new boolean[1];
        ExecutorService queryExe = Executors.newSingleThreadExecutor();
        Future<?> future = queryExe.submit(() -> res[0] = sqlQuery.changeUserPassword(newPassword,username));

        try { future.get(); }
        catch (InterruptedException | ExecutionException e) { alertHandler.createGenericErrorAlert();}
        finally { queryExe.shutdown(); }
        return res[0];
    }

   public Settings getUserSettings(String username){
        var ref = new Object() {
           String[] settings = new String[2];
        };
        ExecutorService queryExe = Executors.newSingleThreadExecutor();
        Future<?> future = queryExe.submit(() -> ref.settings = sqlQuery.getUserSettings(username));

        try { future.get(); }
        catch (InterruptedException | ExecutionException e) { alertHandler.createGenericErrorAlert();}
        finally { queryExe.shutdown(); }
        return new Settings(ref.settings[1], ref.settings[0]);
   }

   public void updateUserSettings(String username, String theme, String language){
        ExecutorService queryExe = Executors.newSingleThreadExecutor();
        Future<?> future = queryExe.submit(() -> sqlQuery.updateUserSettings(username, theme, language));

        try { future.get(); }
        catch (InterruptedException | ExecutionException e) { alertHandler.createGenericErrorAlert();}
        finally { queryExe.shutdown(); }
   }

    public boolean verifyEmailAvailability(String email) {
        boolean[] res = new boolean[1];
        ExecutorService queryExe = Executors.newSingleThreadExecutor();
        Future<?> future = queryExe.submit(() -> res[0] = sqlQuery.verifyEmailAvailability(email));

        try { future.get(); }
        catch (InterruptedException | ExecutionException e) { alertHandler.createGenericErrorAlert();}
        finally { queryExe.shutdown(); }
        return res[0];
    }
}
