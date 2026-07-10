import {useState} from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css'

function App() {
    const [generatePassword, setGeneratePassword] = useState(true);
    const [address, setAddress] = useState('');
    const [login, setLogin] = useState('');
    const [password, setPassword] = useState('');

    const [data, setData] = useState(['', '', '', true]);

    function handleSubmit(e) {
        e.preventDefault();
        setData([ address, login, password, generatePassword]);
    }


    return (
        <>
            <section>
                <h1>Menadżer haseł - wykonał 0000000000</h1>
                <form onSubmit={handleSubmit}>
                    <div className="form-group m-4">
                        <label htmlFor="address">Adres WWW:</label>
                        <input type="text" className="form-control" id="address" placeholder="Adres strony WWW"
                               value={address} onChange={(e) => setAddress(e.target.value)}/>
                    </div>
                    <div className="form-group m-4">
                        <label htmlFor="login">Login:</label>
                        <input type="text" className="form-control" id="login" placeholder="Twój login"
                               value={login} onChange={(e) => setLogin(e.target.value)}/>
                    </div>
                    <div className="form-group m-4">
                        <input className="form-check-input" type="checkbox"
                               checked={generatePassword} id="passwordGenerate"
                               onChange={() => setGeneratePassword(!generatePassword)}
                        />
                        <label className="form-check-label" htmlFor="passwordGenerate"> Wygeneruj hasło</label>
                    </div>
                    <div className="form-group m-4">
                        <label htmlFor="password">Hasło:</label>
                        <input type="password" className="form-control" id="password"
                               disabled={generatePassword}
                               value={password}
                               onChange={(e) => setPassword(e.target.value)}/>
                    </div>
                    <button type="submit" className="btn btn-primary m-2">Zapisz</button>
                </form>
            </section>
            <section>
                <p className="text-primary lead p-2">Adres: {data[0]} </p>
                <p className="p-2">Login: {data[1]}</p>
                <p className="p-2">{ data[3] ? "Hasło autmatycznie generowane" : `Hasło: ${data[2]}`}</p>


            </section>
        </>
    )
}

export default App
