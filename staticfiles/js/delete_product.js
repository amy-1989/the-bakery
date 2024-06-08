const deleteProductModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteProductButtons = document.getElementsByClassName("product-delete");
const deleteProductConfirm = document.getElementById("deleteConfirm");

/**
 * Initializes delete functionality for the provided delete post buttons.
 * 
 * For each button in the `deleteProductsButtons` collection:
 * - Retrieves the associated address's ID upon click.
 * - Updates the `deleteProductConfirm` link's href to point to the 
 * deletion endpoint for the specific comment.
 * - Displays a confirmation modal (`deleteModal`) to prompt 
 * the user for confirmation before deletion.
 */

for (let button of deleteProductButtons) {
    button.addEventListener("click", (e) => {
        let productId = button.getAttribute("product_id");
        document.getElementById("deleteModalLabel").innerHTML = "Delete Product?";
        document.getElementById("modalBodyContent").innerHTML = "Are you sure you want to delete this product? This action cannot be undone."
        deleteProductConfirm.href = `delete/${productId}`;
        deleteProductModal.show();
    });
}