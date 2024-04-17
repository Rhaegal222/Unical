package snake.model;

public class Game {

	public final static int MOVE_RIGHT = 0;
	public final static int MOVE_LEFT = 1;
	public final static int MOVE_UP = 2;
	public final static int MOVE_DOWN = 3;

	private static Game game = null;
	private boolean alive;
	private Snake snake;
	private boolean win;
	private World world;

	private Game() {
		alive = true;
		win = false;
		snake = new Snake();
		world = new World(snake.getHead());
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
		return alive;
	}

	public boolean win() {
		return win;
	}

	public void move(int direction) {
		// Aggiorniamo la posizione della testa
		Position newHead = switch (direction) {
		case MOVE_RIGHT -> new Position(snake.getHead().x() + 1, snake.getHead().y());
		case MOVE_LEFT -> new Position(snake.getHead().x() - 1, snake.getHead().y());
		case MOVE_UP -> new Position(snake.getHead().x(), snake.getHead().y() - 1);
		case MOVE_DOWN -> new Position(snake.getHead().x(), snake.getHead().y() + 1);
		default -> null;
		};
		if (newHead == null)
			return;
		// Se la testa del serpente va sull'erba o sul proprio corpo il gioco finisce
		if (world.getBlock(newHead) == Block.GRASS || world.getBlock(newHead) == Block.SNAKE_BODY)
			alive = false;
		else {
			// Cancelliamo la posizione del serpente dal mondo
			world.setBlock(snake.getHead(), Block.EMPTY);
			// Spostiamo il corpo del serpente nel punto dove prima c'era la testa
			moveBody(snake.getHead());
			// Se il serpente ha mangiato una mela aggiorniamo ne creiamo una nuova
			if (world.getBlock(newHead) == Block.APPLE) {
				snake.addBodyBlock(newHead);
				// Se non è possibile generare un nuovo blocco il gioco termina
				win = !world.generateBlock();
			}
			// Spostiamo la testa del serpente
			snake.updateHead(newHead);
			// Aggiorniamo il mondo
			world.setBlock(snake.getHead(), Block.SNAKE_HEAD);
		}
	}

	private void moveBody(Position p) {
		if (snake.hasBody()) {
			// nella posizione della coda del serpente si mette un blocco vuoto
			world.setBlock(snake.getTail(), Block.EMPTY);
			// la prima posizione va nella nuova posizione x,y
			snake.moveBody(p);
			// si aggiorna il mondo
			world.setBlock(snake.getBodyStart(), Block.SNAKE_BODY);
		}
	}
}
