import { Component, Input, OnInit } from '@angular/core';
import { RistorantiServiceService } from '../ristoranti-service.service';
import { Ristorante } from '../model/ristorante';


@Component({
  selector: 'app-sezione-ristorante-vetrina',
  templateUrl: './sezione-ristorante-vetrina.component.html',
  styleUrls: ['./sezione-ristorante-vetrina.component.css']
})
export class SezioneRistoranteVetrinaComponent implements OnInit {
  @Input()stato?:string
  ristoranti?:Ristorante[]

  constructor(private ristServise:RistorantiServiceService){}

  ngOnInit(){
    this.getRistoranti();
  }

  getRistoranti(){
    if (this.stato == "migliori"){
      this.ristServise.dammiRistorantiMigliori().subscribe
                  (rists => this.ristoranti = rists);
    }
    
  }


}
