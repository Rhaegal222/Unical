package Es02.view;

import Es02.controller.ChooseImageController;

import java.awt.Dimension;

import javax.swing.*;

public class MainWindow {
    public static void launch(){
        JFrame f = new JFrame("Image Viewer");
        JPanel leftPanel = new JPanel();
        SelectedImagePanel selectedImagePanel = new SelectedImagePanel();
        JButton chooseImage = new JButton("Load Image");
        leftPanel.setLayout(new BoxLayout(leftPanel, BoxLayout.PAGE_AXIS));
        leftPanel.add(chooseImage);
        chooseImage.addActionListener(new ChooseImageController(leftPanel, selectedImagePanel));
        JScrollPane scroll = new JScrollPane(leftPanel);
        JSplitPane splitPane = new JSplitPane(JSplitPane.HORIZONTAL_SPLIT, scroll, selectedImagePanel);
        splitPane.setDividerSize(0);
        splitPane.setDividerLocation(200);
        f.add(splitPane);
        f.setSize(800,800);
        f.setMinimumSize(new Dimension(400,400));
        f.setVisible(true);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}