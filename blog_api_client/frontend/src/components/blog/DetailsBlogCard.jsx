import Typography from "@mui/material/Typography";
import AccountCircle from "@mui/icons-material/AccountCircle";
import FavoriteIcon from "@mui/icons-material/Favorite";
import IconButton from "@mui/material/IconButton";
import ChatBubbleOutlineOutlinedIcon from "@mui/icons-material/ChatBubbleOutlineOutlined";
import RemoveRedEyeOutlinedIcon from "@mui/icons-material/RemoveRedEyeOutlined";
import { useSelector } from "react-redux";
import { Box, Button, Paper, Stack } from "@mui/material";
import { useState } from "react";
import useBlogCall from "../../hooks/useBlogCall";
import CommentForm from "./CommentForm";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import DeleteModal from "./DeleteModal";
import UpdateModal from "./UpdateModal";
import BlogActions from "./BlogActions";

const DetailsBlogCard = ({ detailBlog, onDataChange }) => {
  const [deleteModalOpen, setDeleteModalOpen] = useState(false);
  const [updateModalOpen, setUpdateModalOpen] = useState(false);

  const { isDark } = useSelector((state) => state.theme);
  const currentUser = useSelector((state) => state.auth);
  const { commentsToggle } = useSelector((state) => state.blog);
  const { likeCreate, commentsToggler } = useBlogCall();

  const detailStyles = {
    overflow: "hidden",
    textOverflow: "ellipsis",
    m: 2,
  };

  const handleLikeAndComments = (e) => {
    if (e.currentTarget.id === `detail-like-button-${detailBlog?.id}`) {
      likeCreate(detailBlog?.id);
      onDataChange();
    }
    if (e.currentTarget.id === `detail-comment-button-${detailBlog?.id}`) {
      commentsToggler();
    }
  };

  return (
    <Paper
      sx={{
        minWidth: "270px",
        width: "50%",
        maxWidth: "768px",
        m: "10px auto",
        height: "auto",
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-evenly",
        alignItems: "flex-start",
      }}
      elevation={0}
    >
      <Stack
        direction="row"
        alignItems="center"
        justifyContent="center"
        mt={2}
        sx={{
          width: "100%",
          order: 0,
        }}
      >
        <img
          src={
            detailBlog?.image ||
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
      <Box sx={{ m: 0, mt: 1, width: "100%", order: 2 }}>
        <Typography
          gutterBottom
          variant="h5"
          sx={{ textAlign: "center", color: isDark ? "red" : "green" }}
        >
          {detailBlog?.title?.toUpperCase()}
        </Typography>
        <Typography sx={detailStyles}>
          {detailBlog?.content ?? "No Content"}
        </Typography>
      </Box>

      <Stack sx={{ order: 1 }}>
        <Typography sx={{ textAlign: "left", m: 2, mb: 0 }}>
          {detailBlog?.publish_date
            ? new Date(detailBlog?.publish_date).toLocaleString("en-US")
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
          <span>{detailBlog?.author ?? "No author"}</span>
        </Stack>
      </Stack>

      <Stack
        direction="row"
        justifyContent="space-between"
        alignItems="center"
        sx={{ p: 2, pt: 0, width: "100%", order: 3 }}
      >
        <BlogActions currentUser={currentUser} />

        {/* <Box>
          <IconButton
            aria-label="add to favorites"
            sx={{ textAlign: "left", alignItems: "left" }}
            id={`detail-like-button-${detailBlog?.id}`}
            onClick={(e) => {
              handleLikeAndComments(e);
            }}
          >
            <FavoriteIcon
              sx={{
                color: `${
                  detailBlog?.likes_n?.filter(
                    (like) => like.user_id === currentUser?.id
                  ).length > 0
                    ? "red"
                    : "gray"
                }`,
              }}
            />
            <span>{detailBlog?.likes ?? "0"}</span>
          </IconButton>

          <IconButton
            aria-label="add to favorites"
            id={`detail-comment-button-${detailBlog?.id}`}
            sx={{ textAlign: "left", alignItems: "left" }}
            onClick={(e) => {
              handleLikeAndComments(e);
            }}
          >
            <ChatBubbleOutlineOutlinedIcon />
            <span>{detailBlog?.comment_count ?? "0"}</span>
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
            <span>{detailBlog?.post_views}</span>
          </IconButton>
        </Box> */}

        {detailBlog?.author === currentUser?.currentUser && (
          <Stack direction="row" justifyContent="flex-end" spacing={1}>
            <Button
              variant="contained"
              color="warning"
              onClick={(e) => {
                setUpdateModalOpen(true);
              }}
            >
              <EditIcon />
            </Button>

            <Button
              variant="contained"
              color="error"
              onClick={(e) => {
                setDeleteModalOpen(true);
              }}
            >
              <DeleteForeverIcon />
            </Button>
          </Stack>
        )}
      </Stack>

      {commentsToggle && (
        <Box mt={2} sx={{ width: "100% !important", order: 4 }}>
          <CommentForm id={detailBlog?.id} />
        </Box>
      )}

      <UpdateModal
        id={detailBlog?.id}
        setUpdateModalOpen={setUpdateModalOpen}
        updateModalOpen={updateModalOpen}
        onDataChange={onDataChange}
        blog={detailBlog}
      />

      <DeleteModal
        id={detailBlog?.id}
        setDeleteModalOpen={setDeleteModalOpen}
        deleteModalOpen={deleteModalOpen}
      />
    </Paper>
  );
};

export default DetailsBlogCard;
