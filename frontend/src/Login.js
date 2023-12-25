import React, { useState } from 'react';
import Dashboard from "./Dashboard.js"

export default function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleEmailChange = (e) => {
        setUsername(e.target.value);
    };

    const handlePasswordChange = (e) => {
        setPassword(e.target.value);
    };
    const [login, setLogin] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        // Perform login logic here
        try {
            const response = await fetch('http://localhost:8000/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            });
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
    
            const data = await response.json();
            console.log(data);
            if (data.Login === true) {
                // window.location.href = "http://localhost:3000";
                setLogin(true);
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };
    React.useEffect(() => {
        fetch("/login")
          .then(res => res.json())
          .then(res => {
            if (res.Login === true) {
            //   window.location.href = "http://localhost:3000";
              setLogin(true);
            }
            console.log("Login: " + res.Login)
          })
          .catch(console.error);
      })
    return (
            <div>
            {login && <Dashboard />}
            {!login && (<div><h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Username:
                    <input type="text" value={username} onChange={handleEmailChange} id="username" />
                </label>
                <br />
                <label>
                    Password:
                    <input type="password" value={password} onChange={handlePasswordChange} id="password" />
                </label>
                <br />
                <button type="submit" onClick={handleSubmit} id="submit">Login</button>
            </form></div>)}
            </div>
            
    );
};
