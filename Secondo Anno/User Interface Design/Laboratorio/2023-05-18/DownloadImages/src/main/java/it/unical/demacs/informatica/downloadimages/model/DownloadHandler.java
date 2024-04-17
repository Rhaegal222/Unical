package it.unical.demacs.informatica.downloadimages.model;

import it.unical.demacs.informatica.downloadimages.view.SceneHandler;
import javafx.stage.DirectoryChooser;
import javafx.stage.Stage;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;

import javax.imageio.*;

public class DownloadHandler {
    private static String chooseDirectory(){
        Stage stage = SceneHandler.getInstance().getStage();
        DirectoryChooser directoryChooser = new DirectoryChooser();
        File selectedDirectory = directoryChooser.showDialog(stage);
        if(selectedDirectory == null){
            return null;
        }else{
            String path = selectedDirectory.getAbsolutePath()+"saved.jpg";
            return path;
        }

    }
    public static void download(String link){
        try{
            URL url = new URL(link);
            try{
                BufferedImage img = ImageIO.read(url);
                System.out.println(img.getPropertyNames());
                ImageIO.write(img, "jpg", new File(chooseDirectory()));
            } catch (IOException e){
                System.out.println(e);
            }
        }
        catch (MalformedURLException e1){
            System.out.println(e1);
        }
    }
}
