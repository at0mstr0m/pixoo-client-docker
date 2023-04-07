import { useState } from "react";
import { Form, Button } from "react-bootstrap";
import axios from "axios";
import { useContext } from "react";
import { AuthContext } from "../../context/AuthContext";
import { Navigate } from "react-router-dom";
import { API_URL } from "../../constants/backendUrl";

export default function Login(props) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const { saveToken, isLoggedIn } = useContext(AuthContext);

  async function handleSubmit(event) {
    event.preventDefault();
    try {
      const response = await axios({
        method: "POST",
        url: API_URL + "/token",
        data: {
          username: username,
          password: password,
        },
      });
      saveToken(response.data.access_token);
      setUsername("");
      setPassword("");
    } catch (error) {
      console.error(error);
    }
  }

  if (isLoggedIn()) {
    return <Navigate replace to="/" />;
  }

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group controlId="formBasicUsername">
        <Form.Label>Benutzername</Form.Label>
        <Form.Control
          type="text"
          placeholder="Benutzername"
          value={username}
          autoComplete="on"
          onChange={(event) => setUsername(event.target.value)}
        />
      </Form.Group>

      <Form.Group controlId="formBasicPassword">
        <Form.Label>Passwort</Form.Label>
        <Form.Control
          type="password"
          placeholder="Passwort"
          autoComplete="on"
          value={password}
          onChange={(event) => setPassword(event.target.value)}
        />
      </Form.Group>

      <Button variant="primary" type="submit">
        Einloggen
      </Button>
    </Form>
  );
}
