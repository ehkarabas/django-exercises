import Typography from "@mui/material/Typography";
import AccountCircle from "@mui/icons-material/AccountCircle";
import FavoriteIcon from "@mui/icons-material/Favorite";
import IconButton from "@mui/material/IconButton";
import ChatBubbleOutlineOutlinedIcon from "@mui/icons-material/ChatBubbleOutlineOutlined";
import { useNavigate } from "react-router-dom";
import RemoveRedEyeOutlinedIcon from "@mui/icons-material/RemoveRedEyeOutlined";
import { useSelector } from "react-redux";
import { Box, Button, Paper, Stack } from "@mui/material";
import useBlogCall from "../../hooks/useBlogCall";
import { toastWarnNotify } from "../../helper/ToastNotify";

const BlogCard = ({ blog }) => {
  const { isDark } = useSelector((state) => state.theme);
  const { currentUser, id: currentUserID } = useSelector((state) => state.auth);
  const { likeCreate, commentsToggler } = useBlogCall();
  const navigate = useNavigate();

  const listStyles = {
    overflow: "hidden",
    textOverflow: "ellipsis",
    display: "-webkit-box",
    WebkitLineClamp: "2",
    WebkitBoxOrient: "vertical",
    m: 2,
  };

  const handleLikeAndDirect = (e) => {
    if (e.currentTarget.id === `like-button-${blog?.id}`) {
      if (currentUser) {
        likeCreate(blog?.id);
      } else {
        toastWarnNotify(
          "You must login first to send a like/comment or access whole blog."
        );
      }
    } else if (e.currentTarget.id === `comment-button-${blog?.id}`) {
      if (currentUser) {
        commentsToggler(true);
        navigate(`/detail/${blog?.id}/`);
      } else {
        toastWarnNotify(
          "You must login first to send a like/comment or access whole blog."
        );
      }
    } else {
      commentsToggler(false);
      navigate(`/detail/${blog?.id}/`);
    }
  };

  return (
    <Paper
      sx={{
        minWidth: "270px",
        width: "auto",
        maxWidth: "350px",
        m: "10px",
        height: "500px",
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-evenly",
        alignItems: "flex-start",
      }}
      elevation={10}
    >
      <Stack
        direction="row"
        alignItems="center"
        justifyContent="center"
        mt={2}
        sx={{
          width: "100%",
        }}
      >
        <img
          src={
            blog?.image ||
            "https://thumbs.dreamstime.com/b/no-image-icon-vector-available-picture-symbol-isolated-white-background-suitable-user-interface-element-205805243.jpg"
          }
          alt="img"
          className="h-48 object-cover object-center"
          onError={(e) => {
            e.currentTarget.src =
              "https://thumbs.dreamstime.com/b/no-image-icon-vector-available-picture-symbol-isolated-white-background-suitable-user-interface-element-205805243.jpg";
          }}
        />
      </Stack>
      <Box sx={{ m: 0, mt: 1, width: "100%" }}>
        <Typography
          gutterBottom
          variant="h5"
          sx={{ textAlign: "center", color: isDark ? "red" : "green" }}
        >
          {blog?.title?.toUpperCase()}
        </Typography>
        <Typography sx={listStyles}>{blog?.content ?? "No Content"}</Typography>
      </Box>

      <Stack>
        <Typography sx={{ textAlign: "left", m: 2, mb: 0 }}>
          {blog?.publish_date
            ? new Date(blog?.publish_date).toLocaleString("en-US")
            : "No date"}
        </Typography>
        <Stack
          direction="row"
          alignItems="center"
          sx={{
            textAlign: "left",
            m: 2,
            my: 1,
            color: "black",
          }}
        >
          <AccountCircle />
          <span>{blog?.author ?? "No author"}</span>
        </Stack>
      </Stack>

      <Stack
        direction="row"
        justifyContent="space-between"
        alignItems="center"
        sx={{ p: 2, pt: 0, width: "100%" }}
      >
        <Box>
          <IconButton
            aria-label="add to favorites"
            sx={{ textAlign: "left", alignItems: "left" }}
            id={`like-button-${blog?.id}`}
            onClick={(e) => {
              handleLikeAndDirect(e);
            }}
          >
            <FavoriteIcon
              sx={{
                color: `${
                  blog?.likes_n?.filter(
                    (like) => like.user_id === currentUserID
                  ).length > 0
                    ? "red"
                    : "gray"
                }`,
              }}
            />
            <span>{blog?.likes ?? "0"}</span>
          </IconButton>

          <IconButton
            aria-label="add comment"
            id={`comment-button-${blog?.id}`}
            sx={{ textAlign: "left", alignItems: "left" }}
            onClick={(e) => {
              handleLikeAndDirect(e);
            }}
          >
            <ChatBubbleOutlineOutlinedIcon />
            <span>{blog?.comment_count ?? "0"}</span>
          </IconButton>

          <IconButton
            aria-label="view"
            onClick={(e) => {
              e.preventDefault();
            }}
            sx={{
              "&:hover": {
                cursor: "auto",
              },
            }}
            disableRipple={true}
          >
            <RemoveRedEyeOutlinedIcon />
            <span>{blog?.post_views}</span>
          </IconButton>
        </Box>
        <Button
          variant="contained"
          color="success"
          onClick={(e) => {
            handleLikeAndDirect(e);
          }}
        >
          READ MORE
        </Button>
      </Stack>
    </Paper>
  );
};

export default BlogCard;
