import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ChiSiamoComponent } from './chi-siamo.component';

describe('ChiSiamoComponent', () => {
  let component: ChiSiamoComponent;
  let fixture: ComponentFixture<ChiSiamoComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ChiSiamoComponent]
    });
    fixture = TestBed.createComponent(ChiSiamoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
