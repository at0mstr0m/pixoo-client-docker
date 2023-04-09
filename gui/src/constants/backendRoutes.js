const API_URL = "http://"; // insert URL to Backend
export const ROUTES = Object.freeze({
  token: API_URL + "/token",
  logout: API_URL + "/logout",
  profile: API_URL + "/profile",
  ticker: API_URL + "/ticker",
});
