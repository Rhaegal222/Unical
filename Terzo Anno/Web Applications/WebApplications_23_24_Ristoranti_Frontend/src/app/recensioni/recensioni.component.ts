import { Component, OnInit } from '@angular/core';
import { Recensione } from '../model/recensione';
import { RistorantiServiceService } from '../ristoranti-service.service';

@Component({
  selector: 'app-recensioni',
  templateUrl: './recensioni.component.html',
  styleUrls: ['./recensioni.component.css']
})
export class RecensioniComponent implements OnInit {
  recensioni?:Recensione[]
  
  constructor(private ristService:RistorantiServiceService){}

  ngOnInit(): void {
    this.ristService.recensioni().subscribe(rec => this.recensioni = rec);
  }

}
