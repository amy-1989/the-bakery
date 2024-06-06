const deleteCommentModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteCommentButtons = document.getElementsByClassName("comment-delete");
const deleteCommentConfirm = document.getElementById("deleteConfirm");

/**
 * Initializes delete functionality for the provided delete post buttons.
 * 
 * For each button in the `deleteCommentsButtons` collection:
 * - Retrieves the associated address's ID upon click.
 * - Updates the `deleteCommentConfirm` link's href to point to the 
 * deletion endpoint for the specific comment.
 * - Displays a confirmation modal (`deleteModal`) to prompt 
 * the user for confirmation before deletion.
 */

for (let button of deleteCommentButtons) {
    button.addEventListener("click", (e) => {
        let commentId = button.getAttribute("comment_id");
        document.getElementById("deleteModalLabel").innerHTML = "Delete Comment?";
        document.getElementById("modalBodyContent").innerHTML = "Are you sure you want to delete this comment? This action cannot be undone."
        deleteCommentConfirm.href = `delete/${commentId}`;
        deleteCommentModal.show();
    });
}