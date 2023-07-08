import Box from "@mui/material/Box";
import { useEffect } from "react";
import useBlogCall from "../../hooks/useBlogCall";
import { LoadingButton } from "@mui/lab";
import { MenuItem, Modal, Paper, TextField } from "@mui/material";
import { useSelector } from "react-redux";
import { object, string } from "yup";
import { Form, Formik } from "formik";

const UpdateModal = ({
  blog,
  id,
  updateModalOpen,
  setUpdateModalOpen,
  onDataChange,
}) => {
  const handleClose = () => setUpdateModalOpen(false);
  const { loading } = useSelector((state) => state.auth);
  const { categories } = useSelector((state) => state.blog);
  const { getBlogCategories, editBlogData } = useBlogCall();

  const updateModalStyle = {
    position: "absolute",
    top: "50vh",
    left: "50vw",
    transform: "translate(-50%, -50%)",
    minWidth: "270px",
    width: "50%",
    maxWidth: "768px",
    p: 2,
  };

  const isValidUrl = (url) => {
    try {
      new URL(url);
    } catch (e) {
      return false;
    }
    return true;
  };

  const createCategorySchema = (categoriesArr) =>
    object().shape({
      title: string()
        .min(5, "Title must be at least 5 characters.")
        .max(50, "Title must be at most 50 characters.")
        .required("You must enter the title."),
      image: string().test("is-url-valid", "URL is not valid", (value) =>
        isValidUrl(value)
      ),
      category: string().required("Category required"),
      status: string()
        .oneOf(["d", "p"], "Invalid status type")
        .required("Status type required"),
      content: string().required("Content required"),
    });

  useEffect(() => {
    const fetchCategories = async () => {
      await getBlogCategories();
    };
    fetchCategories();
  }, []);

  return (
    <div>
      <Modal
        open={updateModalOpen}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Formik
          initialValues={blog}
          validationSchema={createCategorySchema}
          onSubmit={(values, actions) => {
            editBlogData(id, values);
            onDataChange();

            actions.resetForm();
            actions.setSubmitting(false);
            setUpdateModalOpen(false);
          }}
        >
          {({
            values,
            errors,
            touched,
            handleChange,
            handleBlur,
            handleSubmit,
            isSubmitting,
          }) => (
            <Paper sx={updateModalStyle} elevation={5}>
              <Form className="forms">
                <Box sx={{ display: "flex", flexDirection: "column", gap: 2 }}>
                  <TextField
                    label="Title"
                    name="title"
                    id="title"
                    type="text"
                    variant="outlined"
                    value={values.title}
                    error={touched?.title && Boolean(errors?.title)}
                    helperText={touched?.title && errors?.title}
                    onChange={handleChange}
                    onBlur={handleBlur}
                    required
                  />

                  <TextField
                    label="Image URL"
                    name="image"
                    id="image"
                    type="url"
                    variant="outlined"
                    value={values.image}
                    error={touched?.image && Boolean(errors?.image)}
                    helperText={touched?.image && errors?.image}
                    onChange={handleChange}
                    onBlur={handleBlur}
                    required
                  />

                  <TextField
                    margin="dense"
                    select
                    fullWidth
                    label="Category"
                    id="category"
                    name="category"
                    value={values.category || ""}
                    error={touched?.category && Boolean(errors?.category)}
                    helperText={touched?.category && errors?.category}
                    onChange={(event) => {
                      handleChange(event);
                      if (event.target.value) {
                      }
                    }}
                    onBlur={handleBlur}
                    required
                  >
                    <MenuItem selected disabled>
                      Please choose...
                    </MenuItem>
                    {categories?.map((category) => {
                      return (
                        <MenuItem key={category.id} value={category.id}>
                          {category.name}
                        </MenuItem>
                      );
                    })}
                  </TextField>

                  <TextField
                    margin="dense"
                    select
                    fullWidth
                    label="Status"
                    id="status"
                    name="status"
                    value={values.status || ""}
                    error={touched?.status && Boolean(errors?.status)}
                    helperText={touched?.status && errors?.status}
                    onChange={handleChange}
                    onBlur={handleBlur}
                    required
                  >
                    <MenuItem selected disabled>
                      Please choose...
                    </MenuItem>
                    <MenuItem value="d">Draft</MenuItem>
                    <MenuItem value="p">Published</MenuItem>
                  </TextField>

                  <TextField
                    label="Content"
                    name="content"
                    id="content"
                    variant="outlined"
                    multiline
                    rows={2}
                    value={values.content}
                    error={touched?.content && Boolean(errors?.content)}
                    helperText={touched?.content && errors?.content}
                    onChange={handleChange}
                    onBlur={handleBlur}
                    required
                  />

                  <LoadingButton
                    variant="contained"
                    type="submit"
                    loading={loading}
                  >
                    Edit Blog
                  </LoadingButton>
                </Box>
              </Form>
            </Paper>
          )}
        </Formik>
      </Modal>
    </div>
  );
};

export default UpdateModal;
