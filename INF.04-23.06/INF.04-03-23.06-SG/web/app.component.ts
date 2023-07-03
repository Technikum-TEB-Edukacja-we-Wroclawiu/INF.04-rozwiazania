import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  film_title = '';
  film_type = '';

  wyslijFormularz() {
    console.log({
      "film_title": this.film_title,
      "film_type": this.film_type
    });
  }
}
