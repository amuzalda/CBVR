import { Component } from '@angular/core';
import { PythonService } from './python.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  videoname: string;
  title = 'app';

  constructor(private pythonService: PythonService) {

  }

  public sendName() {
    console.log("Calling server", this.videoname);
    this.pythonService.getRelatedVideoFileNames().subscribe((response) => {
        console.log("First ", response);
    })
    console.log("second");
  }
}
