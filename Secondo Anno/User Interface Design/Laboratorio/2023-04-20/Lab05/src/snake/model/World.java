package snake.model;

import java.util.ArrayList;
import java.util.Random;

import snake.config.Settings;

public class World {

    private enum Block { EMPTY, GRASS, SNAKE_HEAD, SNAKE_BODY, APPLE }
    private final Block[][] blocks;
    private final Snake snake;

    public World() {
        blocks = new Block[Settings.WORLD_SIZE][Settings.WORLD_SIZE];
        for (int i = 0; i < blocks.length; i++) {
            for (int j = 0; j < blocks.length; j++) {
                if (i == 0 || i == blocks.length - 1 || j == 0 || j == blocks.length - 1)
                    blocks[i][j] = Block.GRASS;
                else
                    blocks[i][j] = Block.EMPTY;
            }
        }
        Position snakePosition = new Position(1, 1);
        snake = new Snake(snakePosition);
        blocks[snakePosition.x()][snakePosition.y()] = Block.SNAKE_HEAD;
        generateApple();
    }

    public boolean generateApple() {
        ArrayList<Position> emptyBlocks = new ArrayList<>();
        for (int i = 0; i < blocks.length; i++) {
            for (int j = 0; j < blocks.length; j++) {
                if (blocks[i][j] == Block.EMPTY)
                    emptyBlocks.add(new Position(i, j));
            }
        }
        if (emptyBlocks.isEmpty()) {
            return false;
        } else {
            Position p = emptyBlocks.get(new Random().nextInt(emptyBlocks.size()));
            setType(p, Block.APPLE);
        }
        return true;
    }

    private boolean isType(Position p, Block block) {
        if(isInvalidPosition(p))
            throw new IllegalArgumentException("Invalid position " + p);
        return blocks[p.x()][p.y()] == block;
    }

    private void setType(Position p, Block type) {
        if(isInvalidPosition(p))
            throw new IllegalArgumentException("Invalid position " + p);
        blocks[p.x()][p.y()] = type;
    }

    public boolean isSnakeHead(Position p) {
        return isType(p, Block.SNAKE_HEAD);
    }

    public boolean isSnakeBody(Position p) {
        return isType(p, Block.SNAKE_BODY);
    }

    public boolean isApple(Position p) {
        return isType(p, Block.APPLE);
    }

    public boolean isGrass(Position p) {
        return isType(p, Block.GRASS);
    }

    public boolean isEmpty(Position p) {
        return isType(p, Block.EMPTY);
    }

    public int getSize() {
        return blocks.length;
    }

    private boolean isInvalidPosition(Position p) {
        return p.x() < 0 || p.x() >= blocks.length || p.y() < 0 || p.y() >= blocks.length;
    }

    void moveSnake(Position p) {
        // Update the position of the head
        setType(snake.getHead(), Block.EMPTY);
        // Move the body of the snake
        moveBody(snake.getHead());
        // Move the head of the snake
        snake.updateHead(p);
        // Update the world
        setType(snake.getHead(), Block.SNAKE_HEAD);
    }

    private void moveBody(Position p) {
        if (snake.hasBody()) {
            // The tail of the snake is now empty
            setType(snake.getTail(), Block.EMPTY);
            // The first position is updated
            snake.moveBody(p);
            // Update the world
            setType(snake.getBodyStart(), Block.SNAKE_BODY);
        }
    }

    Snake getSnake() {
        return snake;
    }
}