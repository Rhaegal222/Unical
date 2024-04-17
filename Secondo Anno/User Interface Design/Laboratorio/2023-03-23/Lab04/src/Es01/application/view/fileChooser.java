package Es01.application.view;

import javax.swing.*;
import java.io.File;

public class fileChooser {
    public static String getFile(JFrame f){
        String questions = null;
        JFileChooser c = new JFileChooser();
        File a = new File("src");
        c.setCurrentDirectory(a);
        int res = c.showOpenDialog(f);
        if(res == JFileChooser.APPROVE_OPTION) {
            a = c.getSelectedFile();
            questions = a.getPath();
        }
        return questions;
    }
}
