import { TestBed, inject } from '@angular/core/testing';

import { PythonService } from './python.service';

describe('PythonService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [PythonService]
    });
  });

  it('should be created', inject([PythonService], (service: PythonService) => {
    expect(service).toBeTruthy();
  }));
});
