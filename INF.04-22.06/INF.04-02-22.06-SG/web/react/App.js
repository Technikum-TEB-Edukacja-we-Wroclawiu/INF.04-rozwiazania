import { useRef } from "react";
import "./App.css";
import "bootstrap/dist/css/bootstrap.css";

function App() {
  const kursy = [
    "Programowanie w C#",
    "Angular dla początkujących",
    "Kurs Django",
  ];

  const imieNazwiskoRef = useRef();
  const numerKursuRef = useRef();

  function handleSubmit(event) {
    event.preventDefault();

    const imienazwisko = imieNazwiskoRef.current.value;
    console.log(imienazwisko);

    const numerkursu = numerKursuRef.current.value;
    const kurs = kursy[numerkursu - 1];
    if (kurs !== undefined) {
      console.log(kurs);
    } else {
      console.log("Nieprawidłowy numer kursu");
    }
  }

  return (
    <>
      <h2>Liczba kursów: {kursy.length}</h2>
      <ol>
        {kursy.map((kurs, index) => (
          <li key={index}>{kurs}</li>
        ))}
      </ol>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="imienazwisko">Imię i nazwisko:</label>
          <input
            type="text"
            id="imienazwisko"
            name="imienazwisko"
            className="form-control"
            ref={imieNazwiskoRef}
          />
        </div>
        <div className="form-group">
          <label htmlFor="numerkursu">Numer kursu:</label>
          <input
            type="number"
            id="numerkursu"
            name="numerkursu"
            className="form-control"
            ref={numerKursuRef}
          />
        </div>
        <div className="form-group mt-3">
          <button type="submit" className="btn btn-primary">
            Zapisz do kursu
          </button>
        </div>
      </form>
    </>
  );
}

export default App;
