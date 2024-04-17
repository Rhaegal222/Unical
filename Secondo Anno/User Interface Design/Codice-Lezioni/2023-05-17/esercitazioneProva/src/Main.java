import view.GraphicPanel;

import javax.swing.*;

public class Main {
    public static void main(String[] args){
        JFrame frame = new JFrame("Animation Swing");
        GraphicPanel panel = new GraphicPanel();
        frame.add(panel);
        GameController controller = new GameController(panel);
        panel.addKeyListener(controller);
        panel.setFocusable(true);
        panel.requestFocus();
    }
}