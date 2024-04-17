package it.unical.ingsw;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

/**
 * Questa classe contiene i test per la classe PhoneBookService.
 * Viene utilizzato il framework Mockito per simulare il comportamento della classe PhoneBookRegistry.
 */
class PhoneBookServiceTest {
    @Mock
    private PhoneBookRegistry registry;

    private PhoneBookService service;

    /**
     * Inizializza il framework Mockito e crea un'istanza di PhoneBookService.
     */
    @BeforeEach
    void setUp() {
        MockitoAnnotations.initMocks(this);
        service = new PhoneBookService(registry);
    }

    /**
     * Verifica che il metodo addContact di PhoneBookService aggiunga un contatto correttamente.
     * Viene simulato il comportamento del metodo contains di PhoneBookRegistry.
     */
    @Test
    void testAddContact() {
        when(registry.contains("John")).thenReturn(false);
        service.addContact("John", "1234567890");
        verify(registry).addContact("John", "1234567890");
    }

    /**
     * Verifica che il metodo removeContact di PhoneBookService rimuova un contatto correttamente.
     * Viene simulato il comportamento del metodo contains di PhoneBookRegistry.
     */
    @Test
    void testRemoveContact() {
        when(registry.contains("John")).thenReturn(true);
        service.removeContact("John");
        verify(registry).removeContact("John");
    }
}