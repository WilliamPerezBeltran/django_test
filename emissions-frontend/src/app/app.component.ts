import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { EmissionsService } from './services/emissions.service';
import { Emission } from './models/emission.model';
import { EmissionsChartComponent } from './components/emissions-chart/emissions-chart.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, HttpClientModule, FormsModule, EmissionsChartComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {
  public emissions: Emission[] = [];
  public filteredEmissions: Emission[] = [];
  public loading = true;
  public error: string | null = null;

  public filters = {
    country: '',
    activity: '',
    emission_type: '',
  };

  public allCountries: string[] = [];
  public allActivities: string[] = [];
  public allEmissionTypes: string[] = [];

  public countries: string[] = [];
  public activities: string[] = [];
  public emissionTypes: string[] = [];

  constructor(private emissionsService: EmissionsService) {}

  ngOnInit(): void {
    this.loadEmissions();
  }

  loadEmissions(): void {
    this.loading = true;
    this.error = null;

    this.emissionsService.getEmissions().subscribe({
      next: (data: Emission[]) => {
        this.emissions = data;
        this.filteredEmissions = [...data]; 

        this.allCountries = Array.from(new Set(data.map(e => e.country))).sort();
        this.allActivities = Array.from(new Set(data.map(e => e.activity))).sort();
        this.allEmissionTypes = Array.from(new Set(data.map(e => e.emission_type))).sort();

        this.countries = [...this.allCountries];
        this.activities = [...this.allActivities];
        this.emissionTypes = [...this.allEmissionTypes];

        this.loading = false;
      },
      error: (err) => {
        console.error(err);
        this.error = 'The broadcasts could not be loaded.';
        this.loading = false;
      },
    });
  }

  updateFilters(): void {
    this.filteredEmissions = this.emissions.filter(e =>
      (this.filters.country ? e.country === this.filters.country : true) &&
      (this.filters.activity ? e.activity === this.filters.activity : true) &&
      (this.filters.emission_type ? e.emission_type === this.filters.emission_type : true)
    );

    this.countries = Array.from(new Set(this.filteredEmissions.map(e => e.country))).sort();
    this.activities = Array.from(new Set(this.filteredEmissions.map(e => e.activity))).sort();
    this.emissionTypes = Array.from(new Set(this.filteredEmissions.map(e => e.emission_type))).sort();
  }
}
