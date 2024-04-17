package snake.model;

import java.util.LinkedList;

public class Snake {

    private final LinkedList<Position> body;
    private Position head;

    private boolean alive;

    public Snake(Position p) {
        body = new LinkedList<>();
        head = p;
        alive = true;
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

    public boolean isAlive() {
        return alive;
    }

    public void moveBody(Position p) {
        body.removeLast();
        body.addFirst(p);
    }

    public void setDead() {
        alive = false;
    }
}