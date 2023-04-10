const API_URL = "http://" + process.env.REACT_APP_API_URL;  // for development

export const ROUTES = Object.freeze({
  token: API_URL + "/token",
  logout: API_URL + "/logout",
  profile: API_URL + "/profile",
  ticker: API_URL + "/ticker",
});
