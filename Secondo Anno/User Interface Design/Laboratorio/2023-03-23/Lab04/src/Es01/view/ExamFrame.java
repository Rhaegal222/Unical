package Es01.view;

import Es01.Settings;
import Es01.model.ExamTest;
import Es01.view.ExamFrame;

import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;
import java.awt.*;
import java.io.File;

public class ExamFrame extends JFrame {
	private JMenuBar createMenuBar() {
		JMenuBar menuBar = new JMenuBar();
		JMenu file = new JMenu("File");
		JMenuItem newExam = new JMenuItem("New exam");
		JMenuItem loadExam = new JMenuItem("Load exam");
		file.add(newExam);
		file.add(loadExam);
		menuBar.add(file);
		JMenu exam = new JMenu("Exam");
		JMenuItem suggestion = new JMenuItem("Suggestion");
		JMenuItem check = new JMenuItem("Check answers");
		exam.add(suggestion);
		exam.add(check);
 		menuBar.add(exam);
		JMenu help = new JMenu("Help");
		JMenuItem about = new JMenuItem("About");
		help.add(about);
		menuBar.add(help);
		return menuBar;
	}
	public ExamFrame() {
		setTitle("Exam test");		
		setSize(Settings.WIDTH, Settings.HEIGHT);
		setMaximumSize(new Dimension(Settings.WIDTH, Settings.HEIGHT));
		setJMenuBar(createMenuBar());		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	public File selectFile() {
		FileNameExtensionFilter filter = new FileNameExtensionFilter("Text files", "txt");
		JFileChooser chooser = new JFileChooser();
		chooser.setFileFilter(filter);
		chooser.showOpenDialog(this);
		return chooser.getSelectedFile();
	}
	public void showExam(ExamTest examTest) {
		add(new JScrollPane(new ExamView(examTest)));
		setVisible(true);
	}
	public void showErrorMessageAndTerminate() {
		JOptionPane.showMessageDialog(this, "Error while processing the file", "Error", JOptionPane.ERROR_MESSAGE);
		System.exit(ABORT);
	}
}
