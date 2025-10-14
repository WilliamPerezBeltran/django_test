import { Component, Input, OnChanges } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NgxChartsModule } from '@swimlane/ngx-charts';
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

  public chartData: { name: string; value: number }[] = [];

  public colorScheme = 'vivid';

  ngOnChanges(): void {
    this.updateChart();
  }

  private updateChart() {
    if (!this.emissions || this.emissions.length === 0) {
      this.chartData = [];
      return;
    }

    const dataMap: { [year: string]: number } = {};
    this.emissions.forEach((e) => {
      const year = e.year.toString();
      dataMap[year] = (dataMap[year] || 0) + e.value;
    });

    this.chartData = Object.keys(dataMap).map((year) => ({
      name: year,
      value: dataMap[year],
    }));
  }
}
