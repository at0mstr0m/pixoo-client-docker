import logo from "./logo.svg";
import "./App.css";

export default function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <button
          onClick={() => {
            fetch("http://192.168.188.69:1337/draw_number?num=1");
          }}
        >
          Click me! 1
        </button>
        <button
          onClick={() => {
            fetch("http://192.168.188.69:1337/draw_number?num=10");
          }}
        >
          Click me! 10
        </button>
      </header>
    </div>
  );
}
