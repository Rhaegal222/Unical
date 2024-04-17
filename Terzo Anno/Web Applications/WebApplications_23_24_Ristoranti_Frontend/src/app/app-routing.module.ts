import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ChiSiamoComponent } from './chi-siamo/chi-siamo.component';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { RecensioniComponent } from './recensioni/recensioni.component';
import { AuthGuardService } from './auth-guard.service';

const routes: Routes = [
  {"path" : "", component:HomeComponent},
  {"path" : "chi_siamo", component:ChiSiamoComponent},
  {"path" : "login", component:LoginComponent},  
  {"path" : "recensioni", component:RecensioniComponent, canActivate:[AuthGuardService]},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { 

}
