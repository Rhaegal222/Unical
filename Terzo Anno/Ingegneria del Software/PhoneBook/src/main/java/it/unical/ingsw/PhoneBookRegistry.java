package it.unical.ingsw;

/**
 * Questa interfaccia definisce i metodi per aggiungere, rimuovere e verificare la presenza di un contatto nella rubrica telefonica.
 */
public interface PhoneBookRegistry {

    /**
     * Aggiunge un nuovo contatto alla rubrica telefonica.
     * @param name il nome del contatto da aggiungere
     * @param number il numero di telefono del contatto da aggiungere
     */
    void addContact(String name, String number);

    /**
     * Rimuove un contatto dalla rubrica telefonica.
     * @param name il nome del contatto da rimuovere
     */
    void removeContact(String name);

    /**
     * Verifica se un contatto è presente nella rubrica telefonica.
     * @param name il nome del contatto da cercare
     * @return true se il contatto è presente, false altrimenti
     */
    boolean contains(String name);
}
