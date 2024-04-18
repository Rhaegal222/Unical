module it.unical.elcampeon {
    requires javafx.controls;
    requires javafx.fxml;
    requires javafx.web;
    requires java.sql;
    requires com.jfoenix;
    requires org.controlsfx.controls;
    requires org.kordamp.ikonli.javafx;
    requires org.kordamp.bootstrapfx.core;
    requires spring.boot.autoconfigure;
    requires spring.boot;
    requires spring.context;
    requires spring.beans;
    requires spring.core;
    requires spring.context.support;
    requires jakarta.mail;
    requires org.apache.commons.codec;
    requires spring.security.crypto;
    requires org.xerial.sqlitejdbc;
    requires com.fasterxml.jackson.databind;
    requires com.google.gson;
    requires okhttp3;
    requires annotations;
    requires com.rometools.rome;
    requires java.desktop;

    exports it.unical.elcampeon.controller;
    opens it.unical.elcampeon.controller to javafx.fxml;
    exports it.unical.elcampeon;
    opens it.unical.elcampeon.model to javafx.base;
    opens it.unical.elcampeon.handler to javafx.base;
    opens it.unical.elcampeon.service to javafx.base;
}