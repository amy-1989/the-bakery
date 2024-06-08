const deleteReplyModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteReplyButtons = document.getElementsByClassName("comment-delete");
const deleteReplyConfirm = document.getElementById("deleteConfirm");

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

for (let button of deleteReplyButtons) {
    button.addEventListener("click", (e) => {
        let replyId = button.getAttribute("reply_id");
        document.getElementById("deleteModalLabel").innerHTML = "Delete Reply?";
        document.getElementById("modalBodyContent").innerHTML = "Are you sure you want to delete this reply? This action cannot be undone."
        deleteReplyConfirm.href = `delete/${replyId}`;
        deleteReplyModal.show();
    });
}