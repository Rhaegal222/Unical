import { TestBed } from '@angular/core/testing';

import { RistorantiServiceService } from './ristoranti-service.service';

describe('RistorantiServiceService', () => {
  let service: RistorantiServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RistorantiServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
