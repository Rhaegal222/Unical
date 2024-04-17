package snake.view;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;

import javax.swing.JPanel;

import snake.config.Settings;
import snake.model.Block;
import snake.model.Game;
import snake.model.Position;
import snake.model.World;

public class SnakePanel extends JPanel {

	private static final long serialVersionUID = -2623791009785894161L;

	private void drawEnd(Graphics g, String message) {
		this.setBackground(Color.DARK_GRAY);
		g.setFont(new Font("arial", Font.PLAIN, 20));
		g.setColor(Color.WHITE);
		g.drawString(message, Settings.WINDOW_SIZE / 20, Settings.WINDOW_SIZE / 2);
	}

	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);
		this.setBackground(Color.WHITE);
		Game game = Game.getGame();
		if (!game.isAlive()) {
			drawEnd(g, "Game over! Press n to start a new game");
			return;
		} else if (game.win()) {
			drawEnd(g, "You win! Press n to start a new game");
			return;
		}

		World world = game.getWorld();
		for (int i = 0; i < world.getDim(); i++) {
			for (int j = 0; j < world.getDim(); j++) {
				switch (world.getBlock(new Position(i, j))) {
				case Block.GRASS -> {
					g.setColor(Color.GREEN);
					g.fillRect(i * Settings.BLOCK_SIZE, j * Settings.BLOCK_SIZE, Settings.BLOCK_SIZE,
							Settings.BLOCK_SIZE);
				}
				case Block.SNAKE_HEAD -> {
					g.setColor(Color.BLACK);
					g.fillOval(i * Settings.BLOCK_SIZE, j * Settings.BLOCK_SIZE, Settings.BLOCK_SIZE,
							Settings.BLOCK_SIZE);
				}
				case Block.SNAKE_BODY -> {
					g.setColor(Color.BLACK);
					g.fillRect(i * Settings.BLOCK_SIZE, j * Settings.BLOCK_SIZE, Settings.BLOCK_SIZE,
							Settings.BLOCK_SIZE);
				}
				case Block.APPLE -> {
					g.setColor(Color.RED);
					g.fillRect(i * Settings.BLOCK_SIZE, j * Settings.BLOCK_SIZE, Settings.BLOCK_SIZE,
							Settings.BLOCK_SIZE);					
				}
				}
			}
		}
	}
}
