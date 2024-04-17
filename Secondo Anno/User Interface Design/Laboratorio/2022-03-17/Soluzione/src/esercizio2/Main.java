package esercizio2;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JSplitPane;
import javax.swing.JTabbedPane;
import javax.swing.JTextArea;

public class Main {
	public static void main(String[] args) {
		JFrame f = new JFrame();
		f.setSize(800, 400);		
		JPanel pleft = new JPanel();
		pleft.setBackground(Color.RED);
		JTabbedPane pright = new JTabbedPane();
		JPanel tab1 = new JPanel();
		tab1.setBackground(Color.BLUE);
		JTextArea areaNonResizable = new JTextArea();
		areaNonResizable.setPreferredSize(new Dimension(300,200));
		areaNonResizable.setLineWrap(true);
		tab1.add(areaNonResizable);		
		JPanel tab2 = new JPanel();		
		pright.addTab("Primo tab", tab1);
		pright.addTab("Secondo tab", tab2);
		JPanel north = new JPanel();
		north.setBackground(Color.CYAN);
		JPanel east = new JPanel();
		east.setBackground(Color.YELLOW);
		JPanel west = new JPanel();
		west.setBackground(Color.BLACK);
		JPanel south = new JPanel();
		south.setBackground(Color.MAGENTA);
		JTextArea areaResizable = new JTextArea();
		JScrollPane center = new JScrollPane(areaResizable);
		tab2.setLayout(new BorderLayout());
		tab2.add(north, BorderLayout.PAGE_START);
		tab2.add(south, BorderLayout.PAGE_END);
		tab2.add(west, BorderLayout.LINE_START);
		tab2.add(east, BorderLayout.LINE_END);
		tab2.add(center, BorderLayout.CENTER);
		
		JSplitPane splitPane = new JSplitPane(
				JSplitPane.HORIZONTAL_SPLIT,
				pleft,
				pright);
		splitPane.setDividerLocation(200);
		f.add(splitPane);
		f.setVisible(true);
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);		
	}
}