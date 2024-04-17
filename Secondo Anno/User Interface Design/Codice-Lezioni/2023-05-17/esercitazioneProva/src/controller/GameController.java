package controller;

import model.Game;
import view.GraphicPanel;

import java.awt.event.KeyEvent;

public class GameController {
    private final GraphicPanel panel;

    public GameController(GraphicPanel panel){
        this.panel= panel;
    }
    @Override
    public void KeyPressed(KeyEvent e){
        switch (e.getKeyCode()){
            case KeyEvent.VK_UP -> Game.getInstance().jump();
            case KeyEvent.VK_RIGHT -> Game.getInstance().startMovement();
        }
    }
    @Override
    public void KeyTyped(KeyEvent e){}
    public void KeyReleased(KeyEvent e) {
        if (e.getKeyCode() == KeyEvent.VK_RIGHT)
            Game.getInstance().stopMovement();
    }
    public void update(){
        Game.getInstance().update();
        panel.update();
    }
}