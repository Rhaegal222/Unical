package application.controller;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.JFileChooser;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.filechooser.FileFilter;
import javax.swing.filechooser.FileNameExtensionFilter;

import application.view.ImageView;
import application.view.SelectedImagePanel;

public class ChooseImageListener implements ActionListener {

	private JPanel leftPanel;
	private SelectedImagePanel selectedImagePanel;
	public ChooseImageListener(JPanel leftPanel, SelectedImagePanel selectedImagePanel) {
		this.leftPanel = leftPanel;
		this.selectedImagePanel = selectedImagePanel;
	}
	
	@Override
	public void actionPerformed(ActionEvent e) {
		FileFilter imageFilter = new FileNameExtensionFilter(
			    "Image files", ImageIO.getReaderFileSuffixes());
		JFileChooser f = new JFileChooser();
		f.setFileFilter(imageFilter);
		int res = f.showOpenDialog(null);
		if (res == JFileChooser.APPROVE_OPTION) {
			File file = f.getSelectedFile();
			String name = JOptionPane.showInputDialog("Insert a name for the image");
			if (name == null || name.equals(""))
				name = "No name";
			try {
				BufferedImage img = ImageIO.read(file);
				ImageView i = new ImageView(name, img);
				i.addMouseListener(new MouseAdapter() {
					@Override
					public void mousePressed(MouseEvent e) {
						selectedImagePanel.changeBackground(i);
					}
				});
				leftPanel.add(i);
				leftPanel.repaint();
				leftPanel.revalidate();
			} catch (IOException e1) {
				JOptionPane.showMessageDialog(null, "Error while processing the image", "Error", JOptionPane.ERROR_MESSAGE);
			}
		}
		
		
	}	
}
