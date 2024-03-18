// Function to check if the user name was entered 
function validateForm() {
  var number = document.getElementById('number').value;

  if (number === '') { 
    alert('Please enter a number before submition');
    return false
  }
  return true; // Allow form submission
}