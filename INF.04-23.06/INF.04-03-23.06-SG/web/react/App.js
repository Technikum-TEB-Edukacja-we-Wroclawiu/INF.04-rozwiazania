import './App.css';
import "bootstrap/dist/css/bootstrap.css";

function App() {
  function onSubmit(event) {
    event.preventDefault();

    const title = event.target.elements.filmTitle.value;
    const type = event.target.elements.filmType.value;
    console.log(`tytul: ${title}, rodzaj: ${type}`);
  }

  return (
    <>
      <form onSubmit={onSubmit} method="post">
        <div className="form-group">
          <label htmlFor="filmTitle">Tytuł filmu</label>
          <input
            type="text"
            name="filmTitle"
            id="filmTitle"
            className="form-control"
          />
        </div>
        <div className="form-group">
          <label htmlFor="filmType">Rodzaj</label>
          <select name="filmType" id="filmType" className="form-control">
            <option></option>
            <option value="1">Komedia</option>
            <option value="2">Obyczajowy</option>
            <option value="3">Sensacyjny</option>
            <option value="4">Horror</option>
          </select>
        </div>
        <div className="form-group">
          <button type="submit" className="btn btn-primary">
            Dodaj
          </button>
        </div>
      </form>
    </>
  );
}

export default App;
