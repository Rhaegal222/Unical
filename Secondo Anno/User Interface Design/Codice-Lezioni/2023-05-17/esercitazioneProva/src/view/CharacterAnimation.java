package view;

import javax.imageio.ImageIO;
import java.awt.*;
import java.util.ArrayList;

public class CharacterAnimation {
    private ArrayList<Image> images = new ArrayList<>();
    public CharacterAnimation(String action, int numberOfElements){
        try {
            for (int i = 0; i <= numberOfElements; i++) {
                Image img = ImageIO.read(getClass().getResourceAsStream("application/resources" + action + i + ".png"));
                images.add(img);
            }
        }
        catch ()
    }
    public Image getDefaultImage(){
        return images.get(0);
    }
    public void update(){
        index = (index+1) % images.size();
        return images.get(index);
    }
}
