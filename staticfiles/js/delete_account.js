const deleteAccountModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteAccountButtons = document.getElementsByClassName("account-delete");
const deleteAccountConfirm = document.getElementById("deleteConfirm");

/**
 * Initializes delete functionality for the provided delete post buttons.
 * 
 * For each button in the `deleteAccountButtons` collection:
 * - Retrieves the associated account's ID upon click.
 * - Updates the `deleteAccountConfirm` link's href to point to the 
 * deletion endpoint for the specific comment.
 * - Displays a confirmation modal (`deleteModal`) to prompt 
 * the user for confirmation before deletion.
 */

for (let button of deleteAccountButtons) {
    button.addEventListener("click", (e) => {
        let accountId = button.getAttribute("user_id");
        console.log(accountId);
        document.getElementById("deleteModalLabel").innerHTML = "Delete Account?";
        document.getElementById("modalBodyContent").innerHTML = "Are you sure you want to delete your account? This action cannot be undone.";
        deleteAccountConfirm.href = `account/delete/${accountId}`;
        deleteAccountModal.show();
    });
}