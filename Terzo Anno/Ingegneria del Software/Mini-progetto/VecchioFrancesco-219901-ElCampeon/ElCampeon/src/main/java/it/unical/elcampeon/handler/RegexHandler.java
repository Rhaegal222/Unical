package it.unical.elcampeon.handler;

// Classe per la gestione delle regex
public class RegexHandler {
    private static RegexHandler instance;
    private RegexHandler() {}
    public static RegexHandler getInstance() {
        if(instance == null)
            instance = new RegexHandler();
        return instance;
    }


    public final String regexEmail =
            "^[a-zA-Z0-9.!#$%&’*+/=?^_{|}~-]+@(?:gmail\\.com|yahoo\\.com|hotmail\\.com|libero\\.it|icloud\\.com|gmx\\.com|aol\\.com)";

    public final String regexPassword =
            "^(?=.*[A-Z])(?=.*[0-9])(?=.*[@!%~&£°#'?*=.])[a-zA-Z0-9@!%&£°#'?*=.]{8,}";

    public final String regexFirstLast =
            "^(?=.{2,20}$)[a-zA-Z]+(?:[-'\\s][a-zA-Z]+)*$";
}
