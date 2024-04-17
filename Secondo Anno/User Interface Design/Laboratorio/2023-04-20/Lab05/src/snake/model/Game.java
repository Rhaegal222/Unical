package snake.model;

public class Game {

    public final static int MOVE_RIGHT = 0;
    public final static int MOVE_LEFT = 1;
    public final static int MOVE_UP = 2;
    public final static int MOVE_DOWN = 3;

    private static Game game = null;

    private boolean win;
    private final World world;

    private Game() {
        win = false;
        world = new World();
    }

    public World getWorld() {
        return world;
    }

    public static Game getGame() {
        if (game == null)
            game = new Game();
        return game;
    }

    public static void restartGame() {
        game = new Game();
    }

    public boolean isAlive() {
        return world.getSnake().isAlive();
    }

    public boolean win() {
        return win;
    }

    public void move(int direction) {
        // Update the position of the head
        Position newHead = switch (direction) {
            case MOVE_RIGHT -> new Position(world.getSnake().getHead().x() + 1, world.getSnake().getHead().y());
            case MOVE_LEFT -> new Position(world.getSnake().getHead().x() - 1, world.getSnake().getHead().y());
            case MOVE_UP -> new Position(world.getSnake().getHead().x(), world.getSnake().getHead().y() - 1);
            case MOVE_DOWN -> new Position(world.getSnake().getHead().x(), world.getSnake().getHead().y() + 1);
            default -> null;
        };
        if (newHead == null)
            return;

        // If the head hits the grass or the body then the game is over.
        if(world.isGrass(newHead) || world.isSnakeBody(newHead))
            world.getSnake().setDead();
        else {
            boolean hitApple = world.isApple(newHead);
            if(hitApple) {
                // If it's not possible to generate a new apple, then user won
                if(!world.generateApple())
                    win = true;
                else
                    world.getSnake().addBodyBlock(newHead);
            }
            world.moveSnake(newHead);
        }
    }
}