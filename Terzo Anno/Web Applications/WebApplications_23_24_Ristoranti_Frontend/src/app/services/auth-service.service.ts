import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AuthToken, Utente } from '../model/utente';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthServiceService {
  private backendUrl = "http://localhost:8080";
  public token?:string | null;

  getToken(){
    if (this.token == undefined){
      this.token = localStorage.getItem("ristoranti_token");
    }
    return this.token;
  }

  setToken(token:string){
    this.token = token;
    localStorage.setItem("ristoranti_token", token);

  }

  removeToken(){
    this.token = undefined;
    localStorage.removeItem("ristoranti_token");
  }

  constructor(private http:HttpClient, private router:Router) { }

  checkAuthentication(){    
    this.http.post<AuthToken>(this.backendUrl + "/isAuthenticated", 
    {"Authorization":"Basic " + this.token}, {withCredentials: true}).subscribe(
      res => {
        if (!res){
          this.removeToken();
        }
      }
    );    
  }

  isAuthenticated(){
    return this.getToken() != undefined;
  }

  login(username:string, password:string){
    var utente:Utente = {"username": username, "password": password};
    this.http.post<AuthToken>(this.backendUrl + "/login",utente,{withCredentials: true})
    .subscribe(response => {
      this.setToken(response.token);
      this.router.navigate(["/"]);
    });
  }
  logout(){
    this.http.post<AuthToken>(this.backendUrl + "/logout", 
    {"Authorization":"Basic " + this.token}, {withCredentials: true}).subscribe(
      res => {
        if (res){
          this.removeToken();
        }
        this.router.navigate(["/"]);
      }
    );    
  }
}
