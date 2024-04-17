package snake.view;

import java.awt.Dimension;
import java.awt.Toolkit;

import javax.swing.JFrame;
import javax.swing.JOptionPane;

import snake.config.Settings;
import snake.controller.SnakeListener;

public class MainWindow {

	public static void launch() {
		JFrame f = new JFrame();
		f.setSize(Settings.WINDOW_SIZE, Settings.WINDOW_SIZE);
		// Set location of JFrame
		Dimension dim = Toolkit.getDefaultToolkit().getScreenSize();
		f.setLocation(dim.width / 2 - f.getSize().width / 2, dim.height / 2 - f.getSize().height / 2);
		SnakePanel panel = new SnakePanel();
		f.add(panel);
		f.setUndecorated(true); // Remove title bar
		panel.addKeyListener(new SnakeListener(panel));
		panel.setFocusable(true);
		JOptionPane.showMessageDialog(f, "Use arrow keys to move" + System.lineSeparator()
		+ "Press n to start a new game" + System.lineSeparator() + "Press q to quit", "Instructions", JOptionPane.INFORMATION_MESSAGE);		
		f.setVisible(true);
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
}
