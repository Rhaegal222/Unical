import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FooterComponent } from './footer/footer.component';
import { HeaderComponent } from './header/header.component';
import { HomeComponent } from './home/home.component';
import { ChiSiamoComponent } from './chi-siamo/chi-siamo.component';
import { RistoranteVetrinaComponent } from './ristorante-vetrina/ristorante-vetrina.component';
import { SezioneRistoranteVetrinaComponent } from './sezione-ristorante-vetrina/sezione-ristorante-vetrina.component';
import { CommonModule, NgFor } from '@angular/common';
import { RistorantiServiceService } from './ristoranti-service.service';
import { HttpClientModule } from '@angular/common/http';
import { LoginComponent } from './login/login.component';
import {FormBuilder, FormsModule, ReactiveFormsModule} from '@angular/forms';
import { RecensioniComponent } from './recensioni/recensioni.component';

@NgModule({
  declarations: [
    AppComponent,
    FooterComponent,
    HeaderComponent,
    HomeComponent,
    ChiSiamoComponent,
    RistoranteVetrinaComponent,
    SezioneRistoranteVetrinaComponent,
    LoginComponent,
    RecensioniComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    NgFor,
    FormsModule,
    CommonModule,
    ReactiveFormsModule
  ],
  providers: [RistorantiServiceService],
  bootstrap: [AppComponent]
})
export class AppModule { }
