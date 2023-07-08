import Button from "@mui/material/Button";
import useBlogCall from "../../hooks/useBlogCall";
import { useNavigate } from "react-router-dom";
import { Modal, Paper, Stack, Typography } from "@mui/material";

const deleteModalStyle = {
  position: "absolute",
  top: "50vh",
  left: "50vw",
  transform: "translate(-50%, -50%)",
  minWidth: "270px",
  width: "50%",
  maxWidth: "768px",
  p: 2,
};

const DeleteModal = ({ id, deleteModalOpen, setDeleteModalOpen }) => {
  const { deleteBlogData } = useBlogCall();
  const navigate = useNavigate();

  const handleClose = () => {
    setDeleteModalOpen(false);
  };

  const handleDelete = async () => {
    await deleteBlogData(id);
    handleClose();
    navigate("/");
  };

  return (
    <div>
      <Modal
        open={deleteModalOpen}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Paper sx={deleteModalStyle} elevation={5}>
          <Stack spacing={2}>
            <Typography variant="h5">
              Would you like to delete this blog?
            </Typography>
            <Typography variant="h6">
              This action cannot be revertable.
            </Typography>
            <Stack direction="row" justifyContent="flex-end" spacing={2}>
              <Button onClick={handleClose}>No</Button>
              <Button onClick={handleDelete}>Yes</Button>
            </Stack>
          </Stack>
        </Paper>
      </Modal>
    </div>
  );
};

export default DeleteModal;
