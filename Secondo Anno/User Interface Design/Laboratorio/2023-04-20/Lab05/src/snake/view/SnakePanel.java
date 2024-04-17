package snake.view;

import snake.config.Settings;
import snake.model.Game;
import snake.model.Position;
import snake.model.World;

import javax.swing.*;
import java.awt.*;

public class SnakePanel extends JPanel {

    public SnakePanel() {
        reset();
    }

    public void reset() {
        this.setBackground(Color.WHITE);
    }

    private void drawEnd(Graphics g, String message) {
        this.setBackground(Color.DARK_GRAY);
        g.setFont(new Font("arial", Font.PLAIN, 20));
        g.setColor(Color.WHITE);
        g.drawString(message, Settings.WINDOW_SIZE/20, Settings.WINDOW_SIZE/2);
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Game game = Game.getGame();
        if (!game.isAlive()) {
            drawEnd(g, "Game over! Press n to start a new game");
            return;
        } else if (game.win()) {
            drawEnd(g, "You win! Press n to start a new game");
            return;
        }

        World world = game.getWorld();
        for (int i = 0; i < world.getSize(); i++) {
            for (int j = 0; j < world.getSize(); j++) {
                Position p = new Position(i, j);
                if(world.isEmpty(p))
                    continue;
                Color c = Color.BLACK;
                boolean drawOval = false;
                if(world.isGrass(p)) c = Color.GREEN;
                else if (world.isSnakeHead(p)) drawOval = true;
                else if(world.isApple(p)) c = Color.RED;
                g.setColor(c);
                if(drawOval)
                    g.fillOval(i * Settings.BLOCK_SIZE, j * Settings.BLOCK_SIZE, Settings.BLOCK_SIZE,
                            Settings.BLOCK_SIZE);
                else
                    g.fillRect(i * Settings.BLOCK_SIZE, j * Settings.BLOCK_SIZE, Settings.BLOCK_SIZE,
                            Settings.BLOCK_SIZE);
            }
        }
    }
}