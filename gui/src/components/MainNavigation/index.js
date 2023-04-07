import Navbar from "react-bootstrap/Navbar";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import { LinkContainer } from "react-router-bootstrap";
import { useContext } from "react";
import { AuthContext } from "../../context/AuthContext";

export default function MainNavigation() {
  const { isLoggedIn } = useContext(AuthContext);

  const navBarItems = isLoggedIn() ? (
    <>
      <LinkContainer to="/">
        <Nav.Link>Home</Nav.Link>
      </LinkContainer>
      <LinkContainer to="/profile">
        <Nav.Link>Profile</Nav.Link>
      </LinkContainer>
      <LinkContainer to="/logout">
        <Nav.Link>Logout</Nav.Link>
      </LinkContainer>
    </>
  ) : (
    <LinkContainer to="/login">
      <Nav.Link>Login</Nav.Link>
    </LinkContainer>
  );

  return (
    <Navbar bg="dark" expand="lg" variant="dark">
      <Container>
        <LinkContainer to="/">
          <Navbar.Brand>API</Navbar.Brand>
        </LinkContainer>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">{navBarItems}</Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}
