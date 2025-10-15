import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { Emission } from '../models/emission.model';
import { AppConfig } from '../app.config';

@Injectable({
  providedIn: 'root',
})
export class EmissionsService {
  private apiUrl = `${AppConfig.apiUrl}/emissions/`;

  constructor(private http: HttpClient) {}

  getEmissions(filters?: {
    country?: string;
    activity?: string;
    emission_type?: string;
  }): Observable<Emission[]> {
    let params = new HttpParams();

    if (filters?.country) params = params.set('country', filters.country);
    if (filters?.activity) params = params.set('activity', filters.activity);
    if (filters?.emission_type) params = params.set('emission_type', filters.emission_type);

    return this.http.get<Emission[]>(this.apiUrl, { params }).pipe(
      catchError((err) => {
        console.error('Error fetching emissions:', err);
        return throwError(() => new Error('Failed to fetch emissions'));
      }),
    );
  }
}
