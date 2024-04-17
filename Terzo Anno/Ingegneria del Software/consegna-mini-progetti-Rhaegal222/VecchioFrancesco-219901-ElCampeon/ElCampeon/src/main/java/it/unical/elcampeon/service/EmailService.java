package it.unical.elcampeon.service;

import it.unical.elcampeon.handler.AlertHandler;

import org.jetbrains.annotations.NotNull;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSenderImpl;

import java.util.Properties;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

// Service per l'invio delle mail
public class EmailService {
    private static final AlertHandler alertHandler = AlertHandler.getInstance();
    private EmailService(){}
    private static EmailService instance;
    public static EmailService getInstance(){
        if(instance == null)
            instance = new EmailService();
        return instance;
    }

    @NotNull
    private static JavaMailSenderImpl getJavaMailSender() {
        JavaMailSenderImpl mailSender = new JavaMailSenderImpl();
        mailSender.setHost("smtp.libero.it");
        mailSender.setPort(587);
        mailSender.setUsername("ateyoaraton@libero.it");
        mailSender.setPassword("Avatar3121.");

        Properties properties = mailSender.getJavaMailProperties();
        properties.put("mail.transport.protocol", "smtp");
        properties.put("mail.smtp.auth", "true");
        properties.put("mail.smtp.starttls.enable", "true");
        properties.put( "mail.debug", "true");
        return mailSender;
    }

    private void queueWelcomeEmail(String toEmail, String subject, String body){
        try {
            JavaMailSenderImpl mailSender = getJavaMailSender();
            SimpleMailMessage message = new SimpleMailMessage();
            message.setFrom("ateyoaraton@libero.it");
            message.setTo(toEmail);
            message.setText(body);
            message.setSubject(subject);
            mailSender.send(message);
        } catch (Exception e) {
            alertHandler.createGenericErrorAlert();
        }
    }

    private void queuePasswordRecoveryEmail(String toEmail, String subject, String body, String newPass){
        // Codice per l'invio di una mail
        try{
            JavaMailSenderImpl mailSender = getJavaMailSender();
            SimpleMailMessage message = new SimpleMailMessage();
            message.setFrom("ateyoaraton@libero.it");
            message.setTo(toEmail);
            message.setText(body + newPass);
            message.setSubject(subject);
            mailSender.send(message);
        }catch(Exception e){
            alertHandler.createGenericErrorAlert();
        }
    }

    public void sendWelcomeEmail(String toEmail, String subject, String body){
        ExecutorService emailExecutor = Executors.newSingleThreadExecutor();
        emailExecutor.execute(() -> queueWelcomeEmail(toEmail, subject, body));
        emailExecutor.shutdown();
    }

    public void sendEmailPasswordRecover(String toEmail, String subject, String body, String token){
        ExecutorService emailExecutor = Executors.newSingleThreadExecutor();
        emailExecutor.execute(() -> queuePasswordRecoveryEmail(toEmail, subject, body, token));
        emailExecutor.shutdown();
    }
}
