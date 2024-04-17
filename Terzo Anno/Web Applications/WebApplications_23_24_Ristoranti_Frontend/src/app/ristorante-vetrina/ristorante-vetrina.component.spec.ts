import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RistoranteVetrinaComponent } from './ristorante-vetrina.component';

describe('RistoranteVetrinaComponent', () => {
  let component: RistoranteVetrinaComponent;
  let fixture: ComponentFixture<RistoranteVetrinaComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [RistoranteVetrinaComponent]
    });
    fixture = TestBed.createComponent(RistoranteVetrinaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
