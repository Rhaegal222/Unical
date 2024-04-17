package snake.model;

import java.util.LinkedList;

public class Snake {

	private LinkedList<Position> body;
	private Position head;
	
	public Snake() {
		body = new LinkedList<Position>();
		head = new Position(1,1);		
	}
		
	public Position getHead() {
		return head;
	}
	
	public void updateHead(Position newHead) {
		head = newHead;
	}
	
	public boolean hasBody() {
		return !body.isEmpty();
	}
	
	public Position getBodyStart() {
		return body.getFirst();
	}
	
	public Position getTail() {
		return body.getLast();
	}
	
	public void addBodyBlock(Position p) {		
		body.add(p);
	}
	
	public void moveBody(Position p) {
		body.removeLast();
		body.addFirst(p);
	}
}
