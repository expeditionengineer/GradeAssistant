import React, { useEffect, useState } from "react";
import logo from "./logo.svg";
import "./App.css";
import Login from "./Login.js"
import Dashboard from "./Dashboard.js"
import axios from "axios";
import Container from "react-bootstrap/Container";
import Navbar from "react-bootstrap/Navbar";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";

axios.defaults.xsrfCookieName = "csrftoken";
axios.default.xsrdHeaderName = "X-CSRFToken";
axios.defaults.withCredentials = true;

const client = axios.create({
  baseURL: "http://127.0.0.1:8000"
});


function App() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState();
  const [login, setLogin] = useState(false);
  const [user, setUser] = useState();
  const [token, setToken] = useState("");
  function submitLogin(e) {
    e.preventDefault();
    client.post(
      "/login/",
      {
        username: username,
        password: password
      }
    ).then(function(res) {
      setUser(true);
      console.log("User: " + user)
      console.log(res.data.token)
      setToken(res.data.token);
    });
  }
  // useEffect(() => {
  //   fetch("/login")
  //     .then(res => res.json())
  //     .then(res => {
  //       setMessage(res.message);
  //       if (res.Login === true) {
  //         window.location.href = "http://localhost:3000";
  //         setLogin(true);
  //       }
  //       console.log("Login: " + res.Login)
  //     })
  //     .catch(console.error);
  // });
  if (user) {
    return (
      <div className="App">
        <Dashboard token={token} />
        {/* <Container>
          <Navbar bg="light" expand="lg">
            <Navbar.Brand href="#home">Django React Demo</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav"></Navbar.Collapse>
            <Form inline>
              <Button variant="outline-success">Logout</Button>
            </Form>
          </Navbar>
          <header className="App-header">
            <img src={logo} className="App-logo" alt="logo" />
            <p>{message || "Loading..."}</p>
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
          </header>
        </Container> */}
      </div>
    );
  }
  else {
    return (
      <div className="center">
      <form onSubmit={e => submitLogin(e)}>
          <input type="text" placeholder="Enter email" value={username} onChange={e => setUsername(e.target.value)} id="username" />

          <input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} id="password" />
        <button variant="primary" type="submit" id="submit">
          Submit
        </button>
      </form>
    </div>
    );
  }
}

export default App;
