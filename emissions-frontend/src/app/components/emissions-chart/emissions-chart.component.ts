import { Component, Input, OnChanges, SimpleChanges } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NgxChartsModule, Color, ScaleType } from '@swimlane/ngx-charts';
import { Emission } from '../../models/emission.model';

@Component({
  selector: 'app-emissions-chart',
  templateUrl: './emissions-chart.component.html',
  styleUrls: ['./emissions-chart.component.scss'],
  standalone: true,
  imports: [CommonModule, NgxChartsModule],
})
export class EmissionsChartComponent implements OnChanges {
  @Input() emissions: Emission[] = [];

  public chartData: { name: string; series: { name: string; value: number }[] }[] = [];

  public colorScheme: Color = {
    name: 'greenScheme',
    selectable: true,
    group: ScaleType.Ordinal,
    domain: ['#5AA454'],
  };

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['emissions']) {
      this.buildChart();
    }
  }

  private buildChart(): void {
    if (!this.emissions?.length) {
      this.chartData = [];
      return;
    }

    const grouped: { [year: string]: number } = {};

    this.emissions.forEach((e) => {
      if (e?.year != null && e.emissions != null && !isNaN(e.emissions)) {
        grouped[e.year.toString()] = (grouped[e.year.toString()] || 0) + Number(e.emissions);
      }
    });

    const series = Object.keys(grouped)
      .map((year) => ({ name: year, value: grouped[year] }))
      .sort((a, b) => Number(a.name) - Number(b.name));

    this.chartData = series.length ? [{ name: 'Emisiones Anuales', series }] : [];
  }
}
