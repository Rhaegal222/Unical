package snake.model;

import java.util.ArrayList;
import java.util.Random;

import snake.config.Settings;

public class World {

	private Block[][] blocks;
	
	public World(Position snakePosition) {
		int dim = Settings.WINDOW_SIZE / Settings.BLOCK_SIZE;
		blocks = new Block[dim][dim];
		for (int i = 0; i < blocks.length; i++) {
			for (int j = 0; j < blocks.length; j++) {
				if (i == 0 || i == blocks.length - 1 || j == 0 || j == blocks.length - 1)
					blocks[i][j] = new Block(Block.GRASS);
				else
					blocks[i][j] = new Block(Block.EMPTY);				
			}
		}
		blocks[snakePosition.x()][snakePosition.y()] = new Block(Block.SNAKE_HEAD);
		generateBlock();
	}
	
	public boolean generateBlock() {
		ArrayList<Position> emptyBlocks = new ArrayList<>();
		for (int i = 0; i < blocks.length; i++) {
			for (int j = 0; j < blocks.length; j++) {
				if (blocks[i][j].type() == Block.EMPTY)
					emptyBlocks.add(new Position(i, j));
			}
		}
		if (emptyBlocks.isEmpty()) {
			return false;
		} else {
			Position p = emptyBlocks.get(new Random().nextInt(emptyBlocks.size()));
			setBlock(p, Block.APPLE);			
		}
		return true;
	}
	
	public int getBlock(Position p) {
		if(!isValidPosition(p))
			throw new IllegalArgumentException("Invalid position " + p);
		return blocks[p.x()][p.y()].type();
	}	
	
	void setBlock(Position p, int type) {
		if(!isValidPosition(p))
			throw new IllegalArgumentException("Invalid position " + p);
		blocks[p.x()][p.y()] = new Block(type);
	}
	
	public int getDim() {
		return blocks.length;
	}
	
	private boolean isValidPosition(Position p) {
		return p.x() >= 0 && p.x() < blocks.length && p.y() >= 0 && p.y() < blocks.length;
	}
}
