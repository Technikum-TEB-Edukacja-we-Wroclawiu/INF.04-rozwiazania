import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'courses';
  courses_names = [
    "Programowanie w C#",
    "Angular dla początkujących",
    "Kurs Django"
  ];

  nameAndSurname!: string;
  courseNumber!: number;

  status: string = "";
  status_newCourse: string = "";
  status_newCourse_success: boolean = false;

  newCourseName!: string;

  formSubmitted() {
    console.log(`${this.nameAndSurname}`);
    
    if(this.courseNumber <= 0 || this.courseNumber > this.courses_names.length) {
      console.log(`Nieprawidłowy numer kursu`);
      this.status = "Nieprawidłowy numer kursu";
    } else {
      console.log(`${this.courses_names[this.courseNumber - 1]}`);
      this.status = `Wybrany kurs: ${this.courses_names[this.courseNumber - 1]}`;
    }
  }

  resetStatus() {
    this.status = "";
  }

  addNewCourse() {
    if(this.newCourseName == "" || this.newCourseName == undefined) {
      this.status_newCourse = "Nazwa kursu nie może być pusta.";
      this.status_newCourse_success = false;
      return;
    } else if(this.courses_names.indexOf(this.newCourseName) !== -1) {
      this.status_newCourse = "Taki kurs już istnieje.";
      this.status_newCourse_success = false;
      return;
    }
    
    this.courses_names.push(this.newCourseName);
    this.status_newCourse = "";
    this.status_newCourse_success = true;
  }
}
