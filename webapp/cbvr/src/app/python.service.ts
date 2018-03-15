import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import 'rxjs/add/operator/map'

@Injectable()
export class PythonService {

  constructor( private http: HttpClient) {
   }

   getRelatedVideoFileNames() {
    return this.http.get('localhost:4300/video').map((res: Response) => {
      return res.json();
    })
   }

}
