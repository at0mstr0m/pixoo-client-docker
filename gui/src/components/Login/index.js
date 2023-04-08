import { useState } from "react";
import { Container, Row, Col, Form, Button } from "react-bootstrap";
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
    <Container>
      <Row className="justify-content-md-center mt-5">
        <Col xs={12} md={6} lg={3}>
          <h1 className="text-center mb-4">Login</h1>
          <Form onSubmit={handleSubmit}>
            <Form.Group className="mt-3">
              <Form.Label>Benutzername</Form.Label>
              <Form.Control
                type="text"
                placeholder="Benutzername"
                value={username}
                autoComplete="on"
                onChange={(event) => setUsername(event.target.value)}
              />
            </Form.Group>
            <Form.Group className="mt-3">
              <Form.Label>Passwort</Form.Label>
              <Form.Control
                type="password"
                placeholder="Passwort"
                autoComplete="on"
                value={password}
                onChange={(event) => setPassword(event.target.value)}
              />
            </Form.Group>
            <Button variant="primary" type="submit" className="mt-3">
              Einloggen
            </Button>
          </Form>
        </Col>
      </Row>
    </Container>
  );
}
