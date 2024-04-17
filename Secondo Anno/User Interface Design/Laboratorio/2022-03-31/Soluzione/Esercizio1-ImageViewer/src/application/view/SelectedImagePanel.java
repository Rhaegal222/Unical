package application.view;
import java.awt.Graphics;

import javax.swing.JPanel;

public class SelectedImagePanel extends JPanel {

	private static final long serialVersionUID = 8621502572507690366L;
	
	private ImageView img = null;
	
	public SelectedImagePanel() {		
	}
	
	public void changeBackground(ImageView i) {
		img = i;
		repaint();
	}
	
	@Override
	public void paintComponent(Graphics g) {		
		super.paintComponents(g);
		if(img != null)
			g.drawImage(img.getImage(), 0, 0, this.getWidth(), this.getHeight(), null);
	}	
}
