import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import axios from "axios";

export const fetchBlogDetail = createAsyncThunk(
  "blog/fetchBlogDetail",
  async (id, thunkAPI) => {
    const BASE_URL = process.env.REACT_APP_API_URL;
    const { token } = thunkAPI.getState().auth;

    const axiosWithToken = axios.create({
      baseURL: BASE_URL,
      headers: { Authorization: `Token ${token}` },
    });

    try {
      const { data } = await axiosWithToken.get(`api/blogs/${id}/`);
      return data;
    } catch (error) {
      let message;
      if (error.response) {
        message = `Error ${error.response.status}: ${
          error.response.data[Object.keys(error.response.data)[0]]
        }`;
      } else if (error.request) {
        message =
          "No response received from server. Check your network connection.";
      } else {
        message = "Error in setting up the request: " + error.message;
      }

      return thunkAPI.rejectWithValue({
        error: message,
      });
    }
  }
);

const blogSlice = createSlice({
  name: "blog",

  initialState: {
    loading: false,
    blogList: [],
    blogDetail: null,
    categories: [],
    error: false,
    likeCommentChange: false,
    commentsToggle: false,
    userBlogs: [],
  },

  reducers: {
    fetchStart: (state) => {
      state.loading = true;
    },
    blogSuccess: (state, { payload }) => {
      state.blogList = payload;
      state.error = false;
      state.loading = false;
    },
    categorySuccess: (state, { payload }) => {
      state.categories = payload;
      state.error = false;
      state.loading = false;
    },
    blogFail: (state, { payload }) => {
      state.blogList = [];
      state.error = payload;
      state.loading = false;
    },
    categoryFail: (state, { payload }) => {
      state.categories = [];
      state.error = payload.error;
      state.loading = false;
    },
    likeCommentChange: (state) => {
      state.likeCommentChange = !state.likeCommentChange;
      state.error = false;
      state.loading = false;
    },
    toggleComments: (state, { payload }) => {
      state.commentsToggle = payload ?? !state.commentsToggle;
    },
    userBlogsSuccess: (state, { payload }) => {
      state.userBlogs = payload;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase("blog/resetLoading", (state) => {
        state.loading = false;
        state.error = false;
      })
      .addCase(fetchBlogDetail.pending, (state) => {
        state.loading = true;
      })
      .addCase(fetchBlogDetail.fulfilled, (state, action) => {
        state.loading = false;
        state.error = false;
        state.blogDetail = action.payload;
      })
      .addCase(fetchBlogDetail.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload.error;
      });
  },
});

export const {
  fetchStart,
  blogSuccess,
  categorySuccess,
  blogFail,
  categoryFail,
  likeCommentChange,
  toggleComments,
  userBlogsSuccess,
} = blogSlice.actions;
export const resetLoading = { type: "blog/resetLoading" };
export default blogSlice.reducer;
