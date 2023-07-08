import { useDispatch, useSelector } from "react-redux";
import useAxios from "./useAxios";
import {
  blogFail,
  blogSuccess,
  resetLoading,
  categoryFail,
  categorySuccess,
  fetchStart,
  likeCommentChange,
  toggleComments,
  userBlogsSuccess,
} from "../features/blogSlice";
import { toastErrorNotify, toastSuccessNotify } from "../helper/ToastNotify";
import useAuthCall from "./useAuthCall";
import { useEffect, useState } from "react";

const useBlogCall = () => {
  const dispatch = useDispatch();
  const { axiosWithToken, axiosPublic } = useAxios();
  let currentUser = useSelector((state) => state.auth);

  const getAllBlogsData = async (page = 1) => {
    dispatch(fetchStart());
    try {
      const { data } = await axiosPublic(`api/blogs/?status=p&page=${page}`);

      dispatch(blogSuccess(data.results));
      return data;
    } catch (error) {
      const err = `Error ${error.response.status}: ${
        error.response?.data[Object.keys(error.response?.data)[0]]
      }`;
      dispatch(blogFail(err));
      toastErrorNotify(err);
    }
  };

  const getBlogData = async (id) => {
    dispatch(fetchStart());
    try {
      const { data } = await axiosWithToken(`api/blogs/${id}/`);

      return data;
    } catch (error) {
      const err = `Error ${error.response.status}: ${
        error.response?.data[Object.keys(error.response?.data)[0]]
      }`;
      dispatch(blogFail(err));
      toastErrorNotify(err);
    }
  };

  const postBlogData = async (blogData) => {
    dispatch(fetchStart());
    try {
      await axiosWithToken.post(`api/blogs/`, blogData);
      getAllBlogsData();
      toastSuccessNotify(`Blog posted successfully.`);
    } catch (error) {
      const err = `Error ${error.response.status}: ${
        error.response?.data[Object.keys(error.response?.data)[0]]
      }`;
      dispatch(blogFail(err));
      toastErrorNotify(err);
    }
  };

  const editBlogData = async (id, editedBlogData) => {
    dispatch(fetchStart());
    try {
      await axiosWithToken.put(`api/blogs/${id}/`, editedBlogData);
      getBlogData(id);
      toastSuccessNotify(`Blog posted successfully.`);
    } catch (error) {
      const err = `Error ${error.response.status}: ${
        error.response?.data[Object.keys(error.response?.data)[0]]
      }`;
      dispatch(blogFail(err));
      toastErrorNotify(err);
    }
  };

  const deleteBlogData = async (id) => {
    dispatch(fetchStart());
    try {
      await axiosWithToken.delete(`api/blogs/${id}/`);
      getAllBlogsData();
      toastSuccessNotify(`Blog deleted successfully.`);
    } catch (error) {
      const err = `Error ${error.response.status}: ${
        error.response?.data[Object.keys(error.response?.data)[0]]
      }`;
      dispatch(blogFail(err));
      toastErrorNotify(err);
    }
  };

  const getUserBlogsData = async (page = 1) => {
    dispatch(fetchStart());

    try {
      const { data } = await axiosWithToken(
        `api/blogs/?author=${currentUser?.id}&page=${page}`
      );

      dispatch(userBlogsSuccess(data.results));
      return data;
    } catch (error) {
      const err = `Error ${error.response.status}: ${
        error.response?.data[Object.keys(error.response?.data)[0]]
      }`;
      dispatch(blogFail(err));
      toastErrorNotify(err);
    }
  };

  const getBlogCategories = async () => {
    dispatch(fetchStart());
    try {
      const { data } = await axiosWithToken(`api/categories/`);
      const filteredData = data.filter(
        (blog) => blog.name !== "administration"
      );
      dispatch(categorySuccess(filteredData));
      return filteredData;
    } catch (error) {
      const err = `Error ${error.response.status}: ${
        error.response?.data[Object.keys(error.response?.data)[0]]
      }`;
      dispatch(categoryFail(err));
      toastErrorNotify(err);
    }
  };

  const likeCreate = async (id) => {
    dispatch(fetchStart());
    try {
      await axiosWithToken.post(`api/likes/${id}/`);
      const data = getBlogData(id);
      dispatch(likeCommentChange());
      return data;
    } catch (error) {
      const err = `Error ${error.response.status}: ${
        error.response?.data[Object.keys(error.response?.data)[0]]
      }`;
      dispatch(blogFail(err));
      toastErrorNotify(err);
    }
  };

  const commentCreate = async (id, comment) => {
    dispatch(fetchStart());
    try {
      await axiosWithToken.post(`api/comments/${id}/`, comment);
      const data = getBlogData(id);
      dispatch(likeCommentChange());
      return data;
    } catch (error) {
      const err = `Error ${error.response.status}: ${
        error.response?.data[Object.keys(error.response?.data)[0]]
      }`;
      dispatch(blogFail(err));
      toastErrorNotify(err);
    }
  };

  const commentsToggler = (bool) => {
    dispatch(toggleComments(bool));
  };

  return {
    getAllBlogsData,
    getBlogData,
    postBlogData,
    editBlogData,
    deleteBlogData,
    getBlogCategories,
    likeCreate,
    commentCreate,
    commentsToggler,
    getUserBlogsData,
  };
};

export default useBlogCall;
