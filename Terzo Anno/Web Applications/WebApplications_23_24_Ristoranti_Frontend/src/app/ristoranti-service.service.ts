import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from  '@angular/common/http';
import { Observable } from 'rxjs';
import { Ristorante } from './model/ristorante';
import { AuthServiceService } from './services/auth-service.service';
import { Recensione } from './model/recensione';

@Injectable({
  providedIn: 'root'
})
export class RistorantiServiceService {
  private backendUrl = "http://localhost:8080"

  constructor(private http:HttpClient,private auth:AuthServiceService) {}
  dammiRistorantiMigliori():Observable<Ristorante[]>{
    
    var header = {
      headers: new HttpHeaders().set('Authorization', 'Basic ' + this.auth.token)
    }

    return this.http.get<Ristorante[]>(this.backendUrl + "/ristorantiMigliori", 
                  header)
  }

  recensioni():Observable<Recensione[]>{
    var header = {
      headers: new HttpHeaders().set('Authorization', 'Basic ' + this.auth.getToken())
    
    }
    return this.http.get<Recensione[]>(this.backendUrl + "/recensioni", {withCredentials: true});
  }

}
