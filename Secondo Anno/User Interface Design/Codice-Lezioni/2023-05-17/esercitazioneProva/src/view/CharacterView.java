package view;

import java.awt.*;

public class CharacterView {
    private CharacterAnimation runAnimation = new CharacterAnimation("run");
    private CharacterAnimation jumpAnimation = new CharacterAnimation("jump");
    private Image currentImage;
    public CharacterView(){
        currentImage = runAnimation.getDefaultImage();
    }
}
