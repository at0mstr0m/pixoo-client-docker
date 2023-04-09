import { useState } from "react";
import axios from "axios";
import { useContext } from "react";
import { AuthContext } from "../../context/AuthContext";
import { ROUTES } from "../../constants/backendRoutes";

function Profile(props) {
  const [profileData, setProfileData] = useState(null);
  const { token } = useContext(AuthContext);

  async function getData() {
    try {
      const response = await axios({
        method: "GET",
        url: ROUTES.profile,
        headers: {
          Authorization: "Bearer " + token,
        },
      });
      console.log('response', response);

      setProfileData({
        profile_name: response.data.name,
        about_me: response.data.about,
      });
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div className="Profile">
      <p>To get your profile details: </p>
      <button onClick={getData}>Click me</button>
      {profileData && (
        <div>
          <p>Profile name: {profileData.profile_name}</p>
          <p>About me: {profileData.about_me}</p>
        </div>
      )}
    </div>
  );
}

export default Profile;
