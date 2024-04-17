#include <allegro5/allegro.h>
#include <allegro5/allegro_ttf.h>
#include <allegro5/allegro_font.h>
#include <allegro5/allegro_primitives.h>
#include <cstdio> // Aggiunto per includere <cstdio>

int main()
{
    al_init();
    al_init_font_addon();
    al_init_ttf_addon();
    al_install_keyboard();

    ALLEGRO_DISPLAY *display;

    ALLEGRO_FONT *font = al_load_ttf_font("./YARDSALE.ttf", 30, 0);
    if (!font) {
        std::fprintf(stderr, "Impossibile caricare il font.\n"); // Usando std::fprintf
        return 1; // Uscire con un errore
    }

    ALLEGRO_EVENT_QUEUE *queue;
    ALLEGRO_EVENT event;

    al_init();	
    display = al_create_display(600, 400);
    al_flip_display();

    queue = al_create_event_queue(); 
    al_register_event_source(queue, al_get_display_event_source(display));
    al_register_event_source(queue, al_get_keyboard_event_source());
    al_clear_to_color(al_map_rgb(102, 204, 255)); // colore sfondo	

    while (true) {

        al_peek_next_event(queue, &event);
        if((event.type == ALLEGRO_EVENT_KEY_DOWN) || (event.type == ALLEGRO_EVENT_DISPLAY_CLOSE))
            break;
        
        al_clear_to_color(al_map_rgb(143, 180, 240)); // colore sfondo
        al_draw_text(font, al_map_rgb(213, 255, 179), 0, 0, ALLEGRO_ALIGN_LEFT, "Hello World"); //font, colore font coord x coord y, allineamento  , 'testo'    
        al_flip_display();
    }

    // Al termine del programma, rilascia le risorse
    al_destroy_font(font);
    al_destroy_event_queue(queue);
    al_destroy_display(display);

    return 0;
}
