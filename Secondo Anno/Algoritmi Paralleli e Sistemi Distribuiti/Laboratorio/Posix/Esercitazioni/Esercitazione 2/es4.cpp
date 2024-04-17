/*

Si consideri il traffico di macchine in prossimità di un quadrivio. Implementare le 
macchine come thread paralleli e gestire il transito delle macchine in base alle 
seguenti regole: 
- una macchina appare inizialmente, dopo certo tempo random, in una delle strade 
che compongono il quadrivio. Se vi sono altre macchine in attesa nella stessa strada, essa si mette in coda ad esse. 
- solo una macchina alla volta può transitare l'incrocio. 
- una macchina può transitare l’incrocio solo se ha la destra libera. Se nessuna 
macchina ha la destra libera, una macchina a caso transiterà l'incrocio.

*/