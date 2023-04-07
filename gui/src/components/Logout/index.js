import { useEffect } from "react";
import { Navigate } from "react-router-dom";
import axios from "axios";
import { useContext } from "react";
import { AuthContext } from "../../context/AuthContext";
import { API_URL } from "../../constants/backendUrl";

export default function Logout(props) {
  const { token, removeToken, isLoggedIn } = useContext(AuthContext);

  useEffect(() => {
    async function logout() {
      if (!isLoggedIn()) return;
      try {
        await axios({
          method: "POST",
          url: API_URL + "/logout",
          headers: {
            Authorization: "Bearer " + token,
          },
        });
        removeToken();
      } catch (error) {
          console.error(error);
      }
    }
    logout();
  }, [token, removeToken, isLoggedIn]);

  return isLoggedIn() ? <h1>Logging out...</h1> : <Navigate replace to="/" />;
}
