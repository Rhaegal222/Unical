//    Aprire una finestra con allegro

/* per compilare:
  g++ prova1.cpp -o prova1 -lallegro -lallegro_main -lallegro_image */

#include "stdio.h"
#include "allegro5/allegro.h"
#include "allegro5/allegro_image.h"
#include <iostream>
using namespace std;

#define A_Display  400
#define L_Display   650
#define TITOLO  "finestra allegro"
#define ICONA   "algr-icon.bmp"

int GestErrori(int e){
  const char* msg="";
  switch(e) {
    case 1:  msg ="Errore Inizializzazione Allegro!\n";
             break;
    case 2:  msg ="Errore Creazione Display!\n";
             break;
    case 3:  msg ="Errore Lettura Icona!\n";
             break;
    case 4:  msg ="Errore Lettura Font!\n";
             break;
  }
  fprintf(stderr, "%s", msg);
  return -1;
}

int main() {

  al_init();
	al_install_keyboard();

	ALLEGRO_DISPLAY *display;
	ALLEGRO_BITMAP *icona;
	ALLEGRO_EVENT_QUEUE *queue;
	ALLEGRO_EVENT event;

  if(!al_init()) 
			return GestErrori(1);
			
			//creazione display
			display = al_create_display(L_Display, A_Display);
			
			if(!display)  
				return GestErrori(2);
			
			// set titolo
			al_set_window_title(display, TITOLO);
			
			// aggiunta icona 
			if (!icona) 
				return GestErrori(3);

			al_init_image_addon();
			icona = al_load_bitmap(ICONA);
			al_set_display_icon(display, icona);  
			al_flip_display();

			queue = al_create_event_queue(); 
			al_register_event_source(queue, al_get_display_event_source(display));
			al_register_event_source(queue, al_get_keyboard_event_source());
			al_clear_to_color(al_map_rgb(255, 255, 255)); // colore sfondo	
  
  while (true) { 
    
    //registra eventi
    al_peek_next_event(queue, &event);

    //chiusura finestra
    if((event.type == ALLEGRO_EVENT_KEY_DOWN) || (event.type == ALLEGRO_EVENT_DISPLAY_CLOSE))
      break;

  }

  al_clear_to_color(al_map_rgb(50,100,100));
  al_set_window_title(display, TITOLO);
  
  al_destroy_display(display);
  return 0;
}


