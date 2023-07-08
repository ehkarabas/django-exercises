import { BrowserRouter, Outlet, Route, Routes } from "react-router-dom";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import { Box } from "@mui/material";
import Dashboard from "../pages/Dashboard";
import About from "../pages/About";
import Login from "../pages/Login";
import Register from "../pages/Register";
import PrivateRouter from "./PrivateRouter";
import Detail from "../pages/Detail";
import NewBlog from "../pages/NewBlog";
import Profile from "../pages/Profile";
import NotFound from "../pages/NotFound";
import MyBlogs from "../pages/MyBlogs";
import PwResetRequest from "../pages/PwResetRequest";

const PageLayout = () => {
  return (
    <>
      <Box sx={{ flexGrow: 1 }}>
        <Navbar />
        <Outlet />
      </Box>
      <Footer />
    </>
  );
};

const AppRouter = () => {
  return (
    <BrowserRouter>
      <Box className="flex flex-col min-h-screen">
        <Routes>
          <Route element={<PageLayout />}>
            <Route path="/" element={<Dashboard />} />
            <Route path="/about" element={<About />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/password/reset/" element={<PwResetRequest />} exact />
            <Route element={<PrivateRouter />}>
              <Route path="/detail/:id" element={<Detail />} />
              <Route path="/new-blog" element={<NewBlog />} />
              <Route path="/my-blogs" element={<MyBlogs />} />
              <Route path="/profile" element={<Profile />} />
            </Route>
          </Route>
          <Route path="*" element={<NotFound />} />
        </Routes>
      </Box>
    </BrowserRouter>
  );
};

export default AppRouter;
