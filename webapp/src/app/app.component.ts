import { Component } from '@angular/core';
import { PythonService } from './python.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  videoname;
  responseFiles = [];
  constructor(private pythonService: PythonService) {

  }

  // public sendName(file) {
  //   console.log("Calling server", this.videoname, file);
  //   this.pythonService.getRelatedVideoFileNames(this.videoname).subscribe((response) => {
  //       console.log("First ", response);
  //   })
  //   console.log("second");
  // }

  onChange(event) {
    let file = event.srcElement.files;
    let postData = { field1: "field1", field2: "field2" }; // Put your form data variable. This is only example.
    this.pythonService.getRelatedVideoFileNames(file).subscribe(result => {
      console.log(" After service call", result);
      this.responseFiles = result as any[];
    });
  }
}
