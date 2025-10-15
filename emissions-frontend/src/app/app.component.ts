import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { EmissionsService } from './services/emissions.service';
import { Emission } from './models/emission.model';
import { EmissionsChartComponent } from './components/emissions-chart/emissions-chart.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, HttpClientModule, EmissionsChartComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {
  public emissions: Emission[] = [];
  public loading = true;
  public error: string | null = null;

  constructor(private emissionsService: EmissionsService) {}

  ngOnInit(): void {
    this.loadEmissions();
  }

  private loadEmissions(): void {
    this.loading = true;
    this.error = null;

    this.emissionsService.getEmissions().subscribe({
      next: (data: Emission[]) => {
        this.emissions = data;
        this.loading = false;
      },
      error: (err) => {
        console.error(err);
        this.error = 'The broadcasts could not be loaded.';
        this.loading = false;
      },
    });
  }
}
