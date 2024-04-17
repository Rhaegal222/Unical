package model;

public class SantaCharacter {
    private int x = 0;
    private int y = 200;
    private boolean movement = false;
    private int jump = 0;
    void startMovement(){
        movement = true;
    }
    void stopMovement(){
        movement = false;
    }
    boolean isJumping(){
        return jump!=0;
    }
    boolean isMoving(){
        return jump!=0;
    }
    public void move(){
        x+=10;
    }
    public void jump(){
        if(jump == 0)
            return;
        int jumpSize = 15;
        jump++;
        if(jump >= 2 && jump <= 9){
            y -= jumpSize;
        }
        else if(jump >= 10 && jump <= 17){
            y += jumpSize;
        }
        else{
            jump = 0;
        }
    }

}
