// Function to check if the user name was entered 
function validateForm() {
    var firstName = document.getElementById('firstName').value;
    var lastName = document.getElementById('lastName').value;
  
    if (firstName.trim() === '' || lastName.trim() === '') { // Trim function is used to remove whitespace characters  
      alert('Please enter both first and last name.');
    //   window.history.back();
    return false
    }
    return true; // Allow form submission
}
  