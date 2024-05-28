const deleteAddressModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteAddressButtons = document.getElementsByClassName("address-delete");
const deleteAddressConfirm = document.getElementById("deleteConfirm");

/**
 * Initializes delete functionality for the provided delete post buttons.
 * 
 * For each button in the `deleteAddressButtons` collection:
 * - Retrieves the associated address's ID upon click.
 * - Updates the `deleteAddressConfirm` link's href to point to the 
 * deletion endpoint for the specific comment.
 * - Displays a confirmation modal (`deleteModal`) to prompt 
 * the user for confirmation before deletion.
 */

for (let button of deleteAddressButtons) {
  button.addEventListener("click", (e) => {
    let addressId = button.getAttribute("address_id");
    console.log(addressId);
    document.getElementById("deleteModalLabel").innerHTML = "Delete Address?";
    document.getElementById("modalBodyContent").innerHTML = "Are you sure you want to delete your address? This action cannot be undone."
    deleteAddressConfirm.href = `address/delete/${addressId}`;
    deleteAddressModal.show();
  });
}