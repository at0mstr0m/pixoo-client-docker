import { useState } from "react";
import { useContext } from "react";
import { AuthContext } from "../../context/AuthContext";
import { Form } from "react-bootstrap";
import Spinner from "react-bootstrap/Spinner";
import axios from "axios";
import { ROUTES } from "../../constants/backendRoutes";

export default function Ticker(props) {
  const { token } = useContext(AuthContext);
  const [text, setText] = useState("");
  const [isBusy, setIsBusy] = useState(false);

  async function handleSubmit(event) {
    event.preventDefault();
    if (!text) return;
    setIsBusy(true);
    try {
      const response = await axios({
        method: "POST",
        url: ROUTES.ticker,
        headers: {
          Authorization: "Bearer " + token,
        },
        data: {
          text: text,
        },
      });
      console.log("response", response);
    } catch (error) {
      console.error(error);
    }
    setIsBusy(false);
  }

  return (
    <>
      <h1>Ticker</h1>
      <Form onSubmit={handleSubmit}>
        {isBusy ? (
          <Spinner animation="border" variant="primary" />
        ) : (
          <>
            <Form.Label>Ticker Text</Form.Label>
            <Form.Control
              type="text"
              placeholder="anzuzeigender Text"
              value={text}
              autoComplete="on"
              onChange={(event) => setText(event.target.value)}
            />
          </>
        )}
      </Form>
    </>
  );
}
