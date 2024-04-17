import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SezioneRistoranteVetrinaComponent } from './sezione-ristorante-vetrina.component';

describe('SezioneRistoranteVetrinaComponent', () => {
  let component: SezioneRistoranteVetrinaComponent;
  let fixture: ComponentFixture<SezioneRistoranteVetrinaComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [SezioneRistoranteVetrinaComponent]
    });
    fixture = TestBed.createComponent(SezioneRistoranteVetrinaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
