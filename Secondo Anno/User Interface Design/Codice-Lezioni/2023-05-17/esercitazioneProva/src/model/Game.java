package model;

public class Game {
    private SantaCharacter character = new SantaCharacter();
    private static Game instance = new Game();
    private Game() {

    }

    public static Game getInstance(){
        return instance;
    }
    public void startMovement(){
        character.startMovement();

    }
    public void stopMovement(){
        character.stopMovement();
    }
    public void update(){
        if(character.isMoving())
            character.move();
        if(character.isJumping())
            character.jump();
    }
}
