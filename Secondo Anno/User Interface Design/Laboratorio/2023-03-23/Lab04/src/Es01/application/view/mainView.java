package Es01.application.view;

import javax.swing.*;
import java.awt.*;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class mainView {
    public static void createInterface() throws IOException {
        JFrame f = new JFrame("Exam test");
        f.setSize(800, 600);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.getContentPane().setLayout(new FlowLayout());

        JMenuBar menuBar = new JMenuBar();

        JMenu file = new JMenu("File");
        JMenu exam = new JMenu("Exam");
        JMenu help = new JMenu("Help");

        menuBar.add(file);
        menuBar.add(exam);
        menuBar.add(help);

        JMenuItem newItem = new JMenuItem("New");
        JMenuItem loadItem = new JMenuItem("Load");
        JMenuItem aboutItem = new JMenuItem("About");
        JMenuItem checkItem = new JMenuItem("Check answer");
        JMenuItem suggestionsItem = new JMenuItem("Suggestions");

        file.add(newItem);
        file.add(loadItem);
        exam.add(checkItem);
        exam.add(suggestionsItem);
        help.add(aboutItem);

        JPanel p = new JPanel(new GridBagLayout());

        GridBagConstraints constraints = new GridBagConstraints();
        constraints.anchor = GridBagConstraints.WEST;
        constraints.gridx = 0;

        List<String> der = Files.readAllLines(Path.of(fileChooser.getFile(f)));

        for(int i = 0; i < der.size(); i++){
            constraints.gridy = i;
            if(i % 2 == 0){
                JLabel question = new JLabel(der.get(i));
                p.add(question, constraints);
            }
            else{
                String[] a = der.get(i).split(";");
                JPanel r = new JPanel(new GridLayout(1,4));
                for (String s : a) {
                    JCheckBox checks = new JCheckBox(s);
                    r.add(checks);
                }
                p.add(r, constraints);
            }
        }

        constraints.gridy = der.size();
        JButton submit = new JButton("Submit");
        p.add(submit, constraints);


        JScrollPane scrollPane = new JScrollPane(p);
        scrollPane.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
        scrollPane.setHorizontalScrollBarPolicy(JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED);
        scrollPane.setBounds(0, 0, f.getWidth(), f.getHeight());

        f.setContentPane(scrollPane);
        f.setJMenuBar(menuBar);
        f.setVisible(true);
    }
}
