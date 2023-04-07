import { createContext, useState, useEffect } from "react";

export const AuthContext = createContext({
  token: null,
  saveToken: (userToken) => {},
  removeToken: () => {},
  getToken: () => {},
  isLoggedIn: () => {},
});

export function AuthContextProvider({ children }) {
  const [token, setToken] = useState(null);

  useEffect(() => {
    setToken(getToken());
  }, [])
    
  function getToken() {
    const userToken = localStorage.getItem("token");
    return userToken && userToken;
  }

  function saveToken(userToken) {
    localStorage.setItem("token", userToken);
    setToken(userToken);
  }

  function removeToken() {
    localStorage.removeItem("token");
    setToken(null);
  }

  function isLoggedIn() {
    return !!token;
  }

  const value = {
    token: token,
    getToken: getToken,
    saveToken: saveToken,
    removeToken: removeToken,
    isLoggedIn: isLoggedIn,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}
