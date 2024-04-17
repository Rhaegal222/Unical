package it.unical.demacs.informatica.completejavafxinterface.model;

import javafx.concurrent.Service;
import javafx.concurrent.Task;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;

public class MailDownloader extends Service<String> {
    @Override
    protected Task<String> createTask() {
        return new Task<>() {
            @Override
            protected String call() throws Exception {
                return null;
                //Download from URL: https://www.mat.unical.it/~dodaro/uid/emails.json
            }
        };
    }
}
