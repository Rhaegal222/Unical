package Es02.view;
import java.awt.Graphics;

import javax.swing.JPanel;

public class SelectedImagePanel extends JPanel {
    private ImageView img = null;
    public void changeBackground(ImageView i){
        img = i;
        repaint();
    }

    @Override
    public void paintComponent(Graphics g){
        super.paintComponents(g);
        if(img!=null){
            g.drawImage(img.getImage(),0,0,this.getWidth(),this.getHeight(),null);
        }
    }

}
