import { Paper, Stack, Typography } from "@mui/material";

const CommentCard = ({ comment }) => {
  return (
    <Paper
      sx={{
        width: "100%",
        m: "10px auto",
        ml: 0,
        height: "auto",
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-evenly",
        alignItems: "flex-start",
      }}
      elevation={2}
    >
      <Stack sx={{ order: 0 }} alignItems="flex-start" spacing={1} p={2}>
        <Typography>{comment?.user ?? "No author"}</Typography>
        <Typography sx={{ opacity: "0.6" }}>
          {comment?.time_stamp
            ? new Date(comment?.time_stamp).toLocaleString("en-US")
            : "No date"}
        </Typography>
        <Typography
          sx={{
            my: 1,
            pt: 2,
          }}
        >
          {comment?.content ?? "No content"}
        </Typography>
      </Stack>
    </Paper>
  );
};

export default CommentCard;
