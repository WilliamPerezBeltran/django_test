import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { Emission } from '../models/emission.model';

@Injectable({
  providedIn: 'root',
})
export class EmissionsService {
  private apiUrl = 'http://localhost:8000/api/emissions/';

  constructor(private http: HttpClient) {}

  getEmissions(filters?: {
    country?: string;
    activity?: string;
    emission_type?: string;
  }): Observable<Emission[]> {
    let params = new HttpParams();
    if (filters) {
      Object.keys(filters).forEach((key) => {
        if (filters[key as keyof typeof filters]) {
          params = params.set(key, filters[key as keyof typeof filters]!);
        }
      });
    }

    return this.http.get<Emission[]>(this.apiUrl, { params }).pipe(
      catchError((err) => {
        console.error('Error fetching emissions:', err);
        return throwError(() => new Error('Failed to fetch emissions'));
      }),
    );
  }
}
