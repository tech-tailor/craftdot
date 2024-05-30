// jquery for interaction
$(document).ready(function() {
    $('#openModalBtn').click(function() {
        // Open modal by dynamically loading its content
        $.get('/booking/schedule/', function(data) {
            $('#modalContainer').html(data);
            $('#modalContainer').show();
        });
      });
    
    // Close modal when close button is clicked
      $('#modalContainer').on('click', '#closeModalBtn', function() {
        $('#modalContainer').hide();
        // Navigate back to the original page
        window.history.back();
    });

});
