package snake.model;

public record Block(int type) {

	public final static int EMPTY = 0;
	public final static int GRASS = 1;
	public final static int SNAKE_HEAD = 2;
	public final static int SNAKE_BODY = 3;
	public final static int APPLE = 4;
	
	public Block(int type) {
		if(type < 0 || type > 5)
			throw new IllegalArgumentException("Unexpected block value");
		this.type = type;
	}
}
