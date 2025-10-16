import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { EmissionsService } from './emissions.service';
import { AppConfig } from '../app.config';
import { Emission } from '../models/emission.model';

describe('EmissionsService', () => {
  let service: EmissionsService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [EmissionsService]
    });
    service = TestBed.inject(EmissionsService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => httpMock.verify());

  it('should create service', () => expect(service).toBeTruthy());

  it('should fetch emissions', () => {
    const data: Emission[] = [
      { year: 2020, emissions: 100, emission_type: 'CO2', country: 'Canada', activity: 'Transport' }
    ];

    service.getEmissions().subscribe(res => expect(res).toEqual(data));

    const req = httpMock.expectOne(`${AppConfig.apiUrl}/emissions/`);
    req.flush(data);
  });

  it('should fetch with filters', () => {
    const data: Emission[] = [
      { year: 2020, emissions: 100, emission_type: 'CO2', country: 'Canada', activity: 'Transport' }
    ];

    service.getEmissions({ country: 'Canada' }).subscribe(res => expect(res).toEqual(data));

    const req = httpMock.expectOne(r => r.url === `${AppConfig.apiUrl}/emissions/` && r.params.get('country') === 'Canada');
    req.flush(data);
  });

  it('should handle error', () => {
    service.getEmissions().subscribe({
      next: () => fail('should fail'),
      error: err => expect(err.message).toBe('Failed to fetch emissions')
    });

    const req = httpMock.expectOne(`${AppConfig.apiUrl}/emissions/`);
    req.error(new ErrorEvent('Network error'));
  });
});
