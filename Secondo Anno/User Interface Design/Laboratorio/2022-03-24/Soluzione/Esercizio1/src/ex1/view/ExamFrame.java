package ex1.view;

import java.awt.Dimension;
import java.io.File;

import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.JScrollPane;
import javax.swing.filechooser.FileNameExtensionFilter;

import ex1.Settings;
import ex1.model.QuestionReader;

public class ExamFrame extends JFrame {

	private static final long serialVersionUID = 8087969647206236005L;

	private JMenuBar createMenuBar() {
		JMenuBar menubar = new JMenuBar();
		JMenu file = new JMenu("File");
		JMenuItem newexam = new JMenuItem("New exam");
		JMenuItem loadexam = new JMenuItem("Load exam");
		file.add(newexam);
		file.add(loadexam);
		menubar.add(file);
		JMenu exam = new JMenu("Exam");
		JMenuItem suggestion = new JMenuItem("Suggestion");
		JMenuItem check = new JMenuItem("Check answers");
		exam.add(suggestion);
		exam.add(check);
 		menubar.add(exam);		
		JMenu help = new JMenu("Help");
		JMenuItem about = new JMenuItem("About");
		help.add(about);
		menubar.add(help);
		return menubar;
	}
	
	public ExamFrame() {
		setTitle("Exam test");		
		setSize(Settings.WIDTH, Settings.HEIGHT);
		setMaximumSize(new Dimension(Settings.WIDTH, Settings.HEIGHT));
		setJMenuBar(createMenuBar());		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	
	public void startApplication() {
		FileNameExtensionFilter filter = new FileNameExtensionFilter("Text files", "txt");		
		JFileChooser chooser = new JFileChooser();
		chooser.setFileFilter(filter);
		chooser.showOpenDialog(this);		
		File file = chooser.getSelectedFile();		
		if (file != null) {
			try {
				add(new JScrollPane(new ExamView(new QuestionReader().readExam(file))));
			} catch (Exception e) {
				JOptionPane.showMessageDialog(this, "Error while processing the file", "Error", JOptionPane.ERROR_MESSAGE);
				System.exit(ABORT);
			}
		}
		setVisible(true);
	}

}
