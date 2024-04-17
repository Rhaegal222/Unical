package it.unical.demacs.informatica.completejavafxinterface.model;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.*;

public record Conversation(String sender, String receiver, String subject, List<Email> emails) {

    public Conversation {
        Objects.requireNonNull(sender);
        Objects.requireNonNull(receiver);
        Objects.requireNonNull(subject);
        Objects.requireNonNull(emails);
        if (emails.isEmpty())
            throw new IllegalArgumentException("Email list cannot be empty");
    }

    public Email getLastEmail() {
        return emails.get(0);
    }

    public static List<Conversation> createFromJsonFile(String jsonText) {
        List<Conversation> conversations = new ArrayList<>();
        JSONObject o = new JSONObject(jsonText);
        JSONArray conv = o.getJSONArray("conversations");
        for(int i = 0; i < conv.length(); i++) {
            JSONObject conversation = conv.getJSONObject(i);
            String sender = conversation.getString("sender");
            String receiver = conversation.getString("receiver");
            String subject = conversation.getString("subject");
            JSONArray emails = conversation.getJSONArray("emails");
            Stack<Email> emailStack = new Stack<>();
            for(int j = 0; j < emails.length(); j++) {
                JSONObject email = emails.getJSONObject(j);
                String date = email.getString("date");
                String text = email.getString("text");
                emailStack.add(new Email(date, text));
            }
            conversations.add(new Conversation(sender, receiver, subject, emailStack));
        }
        return Collections.unmodifiableList(conversations);
    }
}
