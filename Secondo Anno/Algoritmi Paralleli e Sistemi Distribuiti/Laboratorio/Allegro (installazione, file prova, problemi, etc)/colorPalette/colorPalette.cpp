#include <allegro5/allegro.h>
#include <allegro5/allegro_primitives.h>
#include <iostream>

using namespace std;

int main() {
    // Inizializzazione di Allegro
    if (!al_init()) {
        cerr << "Errore durante l'inizializzazione di Allegro." << endl;
        return 1;
    }

    // Inizializzazione dell'input da tastiera
    if (!al_install_keyboard()) {
        cerr << "Errore durante l'installazione della tastiera." << endl;
        return 1;
    }

    // Creazione di un display di 256x256 pixel
    ALLEGRO_DISPLAY *display = al_create_display(256, 256);
    if (!display) {
        cerr << "Errore durante la creazione del display." << endl;
        return 1;
    }

    // Disegno sul display
    al_clear_to_color(al_map_rgb(0, 0, 0)); // Sfondo nero
    for (int row = 0; row < 255; row++) {
        for (int column = 0; column < 255; column++) {
            al_draw_pixel(column, row, al_map_rgb(row, column, 128));
        }
    }

    // Attendi un evento per chiudere la finestra
    ALLEGRO_EVENT_QUEUE *event_queue = al_create_event_queue();
    al_register_event_source(event_queue, al_get_keyboard_event_source());

    al_flip_display(); // Aggiorna la finestra
    bool running = true;

    while (running) {
        ALLEGRO_EVENT ev;
        al_wait_for_event(event_queue, &ev);

        if (ev.type == ALLEGRO_EVENT_KEY_DOWN) {
            running = false; // Esci dal ciclo quando viene premuto un tasto
        }
    }

    // Pulizia e uscita
    al_destroy_display(display);
    al_destroy_event_queue(event_queue);

    return 0;
}
