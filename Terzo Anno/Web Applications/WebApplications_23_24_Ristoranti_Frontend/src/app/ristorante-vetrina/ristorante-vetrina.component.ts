import { Component, Input } from '@angular/core';
import { Ristorante } from '../model/ristorante';

declare function jsonFlickrApi():void;

@Component({
  selector: 'app-ristorante-vetrina',
  templateUrl: './ristorante-vetrina.component.html',
  styleUrls: ['./ristorante-vetrina.component.css']
})
export class RistoranteVetrinaComponent {
  @Input()ristorante?:Ristorante;
  farmid?:string;
  serverid?:string
  id?:string;
  secret?:string;
  
}
