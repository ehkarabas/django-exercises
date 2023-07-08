import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import {
  fetchFail,
  fetchStart,
  fetchSuccess,
  loginSuccess,
  logoutSuccess,
  registerSuccess,
} from "../features/authSlice";
import { toastErrorNotify, toastSuccessNotify } from "../helper/ToastNotify";
import useAxios from "./useAxios";

const useAuthCall = () => {
  const { axiosPublic, axiosWithToken } = useAxios();
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const login = async (userInfo) => {
    dispatch(fetchStart());
    try {
      const { data } = await axiosPublic.post(`users/auth/login/`, userInfo);
      dispatch(loginSuccess(data));
      toastSuccessNotify("Logged in successfully.");
      navigate("/");
    } catch (error) {
      const err = `Error ${error.response.status}: ${
        error.response?.data[Object.keys(error.response?.data)[0]]
      }`;
      dispatch(fetchFail(err));
      toastErrorNotify(err);
    }
  };

  const logout = async () => {
    dispatch(fetchStart());
    try {
      await axiosWithToken.post(`users/auth/logout/`);
      dispatch(logoutSuccess());
      navigate("/");
      toastSuccessNotify("Logged out.");
    } catch (error) {
      const err = `Error ${error.response.status}: ${
        error.response?.data[Object.keys(error.response?.data)[0]]
      }`;
      dispatch(fetchFail(err));
      toastErrorNotify(err);
    }
  };

  const register = async (newUser) => {
    dispatch(fetchStart());
    try {
      const { data } = await axiosPublic.post(`users/register/`, newUser);

      dispatch(registerSuccess(data));
      toastSuccessNotify("Registration successful!");
      navigate("/");
    } catch (error) {
      const err = `Error ${error.response.status}: ${
        error.response?.data[Object.keys(error.response?.data)[0]]
      }`;
      dispatch(fetchFail(err));
      toastErrorNotify(err);
    }
  };

  const pwReset = async (email) => {
    dispatch(fetchStart());
    try {
      const { data } = await axiosPublic.post(
        `users/auth/password/reset/`,
        email
      );

      console.log(data);

      dispatch(fetchSuccess());
      toastSuccessNotify(
        "If you entered your account's email correct, an email has sent to you. Check your email."
      );
      navigate("/login");
    } catch (error) {
      const err = `Error ${error.response.status}: ${
        error.response?.data[Object.keys(error.response?.data)[0]]
      }`;
      console.log(error);
      dispatch(fetchFail(err));
      toastErrorNotify(err);
    }
  };

  const pwResetConfirm = async (obj) => {
    dispatch(fetchStart());
    try {
      const { data } = await axiosPublic.post(
        `users/auth/password/reset/confirm/${obj.uid}/${obj.token}/`,
        obj
      );

      console.log(data);

      dispatch(fetchSuccess());
      toastSuccessNotify("Your password has been successfully reset!");
      navigate("/login");
    } catch (error) {
      const err = `Error ${error.response.status}: ${
        error.response?.data[Object.keys(error.response?.data)[0]]
      }`;
      dispatch(fetchFail(err));
      toastErrorNotify(err);
    }
  };

  return { login, logout, register, pwReset, pwResetConfirm };
};

export default useAuthCall;
