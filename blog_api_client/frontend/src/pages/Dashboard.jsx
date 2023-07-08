import { useEffect, useState } from "react";
import useBlogCall from "../hooks/useBlogCall";
import {
  Stack,
  Box,
  TablePagination,
  Typography,
  CircularProgress,
} from "@mui/material";
import BlogCard from "../components/blog/BlogCard";
import { useSelector } from "react-redux";
import { Helmet } from "react-helmet";

const Dashboard = () => {
  const { isDark } = useSelector((state) => state.theme);
  const { blogList, likeCommentChange } = useSelector((state) => state.blog);
  const { getAllBlogsData } = useBlogCall();
  const [isLoading, setIsLoading] = useState(true);
  const [page, setPage] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(10);
  const [totalCount, setTotalCount] = useState(0);

  useEffect(() => {
    const fetchData = async () => {
      setIsLoading(true);
      const data = await getAllBlogsData(page + 1);
      setTotalCount(data.count);
      setIsLoading(false);
    };
    fetchData();
  }, [page, likeCommentChange]);

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  if (isLoading) {
    return (
      <Stack
        direction="row"
        alignItems="center"
        justifyContent="center"
        mt={2}
        sx={{
          width: "100%",
        }}
      >
        <CircularProgress color="success" />
      </Stack>
    );
  }

  return (
    <>
      <Helmet>
        <title>BlogApp - Dashboard</title>
      </Helmet>

      <Stack
        direction="row"
        alignItems="center"
        justifyContent="space-evenly"
        flexWrap="wrap"
        sx={{ minHeight: "70vh" }}
      >
        {blogList.length === 0 ? (
          <Typography>No blogs to show</Typography>
        ) : (
          blogList.map((blog) => <BlogCard key={blog.id} blog={blog} />)
        )}
      </Stack>

      <Box display="flex" justifyContent="center" padding="2em">
        <TablePagination
          component="div"
          count={totalCount}
          page={page}
          onPageChange={handleChangePage}
          rowsPerPage={rowsPerPage}
          onRowsPerPageChange={(event) =>
            setRowsPerPage(parseInt(event.target.value, 10))
          }
          rowsPerPageOptions={[10]}
          sx={{ textAlign: "center", color: isDark ? "yellow" : "black" }}
        />
      </Box>
    </>
  );
};

export default Dashboard;
