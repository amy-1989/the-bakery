const deleteRatingModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteRatingButtons = document.getElementsByClassName("rating-delete");
const deleteRatingConfirm = document.getElementById("deleteConfirm");

/**
 * Initializes delete functionality for the provided delete post buttons.
 * 
 * For each button in the `deleteProductsButtons` collection:
 * - Retrieves the associated rating's ID upon click.
 * - Updates the `deleteRatingConfirm` link's href to point to the 
 * deletion endpoint for the specific comment.
 * - Displays a confirmation modal (`deleteModal`) to prompt 
 * the user for confirmation before deletion.
 */

for (let button of deleteRatingButtons) {
    button.addEventListener("click", (e) => {
        let ratingId = button.getAttribute("rating_id");
        document.getElementById("deleteModalLabel").innerHTML = "Delete Product Rating?";
        document.getElementById("modalBodyContent").innerHTML = "Are you sure you want to delete this product rating? This action cannot be undone.";
        deleteRatingConfirm.href = `delete/${ratingId}`;
        deleteRatingModal.show();
    });
}