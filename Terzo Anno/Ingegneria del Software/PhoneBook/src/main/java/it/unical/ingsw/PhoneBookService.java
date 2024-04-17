package it.unical.ingsw;

/**
 * Questa classe rappresenta un servizio per la gestione di una rubrica telefonica.
 * Implementa l'interfaccia PhoneBookRegistry e fornisce i metodi per verificare la presenza di un contatto,
 * aggiungere un nuovo contatto e rimuovere un contatto esistente.
 */
public class PhoneBookService implements PhoneBookRegistry {
    private final PhoneBookRegistry registry;

    /**
     * Costruttore della classe PhoneBookService.
     * @param registry l'istanza di PhoneBookRegistry da utilizzare per la gestione della rubrica telefonica
     */
    public PhoneBookService(PhoneBookRegistry registry) {
        this.registry = registry;
    }

    /**
     * Verifica se il nome del contatto è presente nella rubrica.
     * @param name il nome del contatto da cercare
     * @return true se il contatto è presente, false altrimenti
     */
    @Override
    public boolean contains(String name) {
        return registry.contains(name);
    }

    /**
     * Aggiunge un nuovo contatto alla rubrica.
     * @param name il nome del nuovo contatto
     * @param number il numero di telefono del nuovo contatto
     */
    @Override
    public void addContact(String name, String number) {
        if(!registry.contains(name))
            registry.addContact(name, number);
    }

    /**
     * Rimuove un contatto esistente dalla rubrica.
     * @param name il nome del contatto da rimuovere
     */
    @Override
    public void removeContact(String name) {
        if(registry.contains(name))
            registry.removeContact(name);
    }
}
