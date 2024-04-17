package Es02.view;

import java.awt.Image;

import javax.swing.ImageIcon;
import javax.swing.JLabel;

public class ImageView extends JLabel {

    private String name;
    private Image img;
    private Image imgScaled;

    public ImageView(String name, Image img){
        super();
        this.name = name;
        this.img = img;
        this.imgScaled = img.getScaledInstance(50,50,Image.SCALE_SMOOTH);
        this.setIcon(new ImageIcon(this.imgScaled));
        this.setText(this.name);
    }

    public Image getImage(){
        return img;
    }
}
