import { createSlice } from "@reduxjs/toolkit";

import { persistReducer } from "redux-persist";
import storage from "redux-persist/lib/storage/session";

const authSlice = createSlice({
  name: "auth",

  initialState: {
    currentUser: null,
    id: null,
    email: "",
    first_name: "",
    last_name: "",
    bio: "",
    loading: false,
    error: false,
    image: "",
    token: null,
  },

  reducers: {
    fetchStart: (state) => {
      state.loading = true;
      state.error = false;
    },
    loginSuccess: (state, { payload }) => {
      state.loading = false;
      state.error = false;
      state.currentUser = payload?.user?.username;
      state.id = payload?.user?.id;
      state.email = payload?.user?.email;
      state.first_name = payload?.user?.first_name;
      state.last_name = payload?.user?.last_name;
      state.bio = payload?.user?.bio;
      state.image = payload?.user?.image;
      state.token = payload?.key;
    },
    logoutSuccess: (state) => {
      state.currentUser = null;
      state.id = null;
      state.email = "";
      state.first_name = "";
      state.last_name = "";
      state.bio = "";
      state.loading = false;
      state.error = false;
      state.image = "";
      state.token = null;
    },
    registerSuccess: (state, { payload }) => {
      state.loading = false;
      state.currentUser = payload?.username;
      state.id = payload?.id;
      state.email = payload?.email;
      state.first_name = payload?.first_name;
      state.last_name = payload?.last_name;
      state.bio = payload?.bio;
      state.image = payload?.image;
      state.token = payload?.token;
      state.error = false;
    },
    fetchFail: (state, { payload }) => {
      state.loading = false;
      state.error = payload;
    },
    fetchSuccess: (state, { payload }) => {
      state.loading = false;
      state.error = false;
    },
  },
  extraReducers: (builder) => {
    builder.addCase("auth/resetLoading", (state) => {
      state.loading = false;
      state.error = false;
    });
  },
});

const persistConfig = {
  key: "auth",
  storage,
};

const persistedAuthReducer = persistReducer(persistConfig, authSlice.reducer);

export const {
  fetchStart,
  loginSuccess,
  logoutSuccess,
  registerSuccess,
  fetchFail,
  fetchSuccess,
} = authSlice.actions;
export const resetLoading = { type: "auth/resetLoading" };
export default persistedAuthReducer;
