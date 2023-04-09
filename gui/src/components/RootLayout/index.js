import { Outlet } from "react-router-dom";
import MainNavigation from "../../components/MainNavigation";
import { Container } from "react-bootstrap";

export default function RootLayout() {
  return (
    <>
      <MainNavigation />
      <main>
        <Container>
          <Outlet />
        </Container>
      </main>
    </>
  );
}
