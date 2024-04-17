import { Ristorante } from "./ristorante";
import { Utente } from "./utente";

export interface Recensione{
    id:number,
    titolo:string,
    testo:string;
    numeroMiPiace:number;
    numeroNonMiPiace:number;
    ristorante:Ristorante;
    scrittaDa:Utente;
}