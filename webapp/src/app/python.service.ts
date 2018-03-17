import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import 'rxjs/add/operator/map'
import { Observable } from 'rxjs/Observable';
@Injectable()
export class PythonService {

  constructor(private http: HttpClient) {
  }

  getRelatedVideoFileNames(file) {
    let headers = new Headers();
    let formData: FormData = new FormData();
    formData.append('file', file[0], file.name);
    console.log("FIle is ", file[0], file[0].name);
    return this.http.post('upload', formData).map((res) => {
      console.log("Reposne after proxy", res);
      return res;
    });
  }
}
