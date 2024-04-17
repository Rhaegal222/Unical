package snake.controller;

import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

import snake.model.Game;
import snake.view.SnakePanel;

public class SnakeListener extends KeyAdapter {

    private final SnakePanel snakePanel;
    public SnakeListener(SnakePanel snakePanel) {
        this.snakePanel = snakePanel;
    }

    @Override
    public void keyPressed(KeyEvent e) {
        if(e.getKeyCode() == KeyEvent.VK_Q)
            System.exit(0);

        if(e.getKeyCode() == KeyEvent.VK_N) {
            Game.restartGame();
            snakePanel.reset();
            snakePanel.repaint();
            return;
        }

        if(Game.getGame().isAlive() && !Game.getGame().win()) {
            switch(e.getKeyCode()) {
                case KeyEvent.VK_LEFT -> Game.getGame().move(Game.MOVE_LEFT);
                case KeyEvent.VK_RIGHT -> Game.getGame().move(Game.MOVE_RIGHT);
                case KeyEvent.VK_DOWN -> Game.getGame().move(Game.MOVE_DOWN);
                case KeyEvent.VK_UP -> Game.getGame().move(Game.MOVE_UP);
            }
            snakePanel.repaint();
        }
    }
}