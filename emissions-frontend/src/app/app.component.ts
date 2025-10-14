import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { EmissionsChartComponent } from './components/emissions-chart/emissions-chart.component';
import { EmissionsService } from './services/emissions.service';
import { Emission } from './models/emission.model';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  standalone: true,
  imports: [CommonModule, HttpClientModule, EmissionsChartComponent],
})
export class AppComponent implements OnInit {
  emissions: Emission[] = [];
  errorMessage = '';

  constructor(private emissionsService: EmissionsService) {}

  ngOnInit() {
    this.loadEmissions({ country: 'Canada', emission_type: 'CO2' });
  }

  loadEmissions(filters?: { country?: string; activity?: string; emission_type?: string }) {
    this.emissionsService.getEmissions(filters).subscribe({
      next: (data) => {
        this.emissions = data;
        this.errorMessage = '';
      },
      error: (err) => {
        this.emissions = [];
        this.errorMessage = err.message;
      },
    });
  }
}
