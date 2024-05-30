// use the service to get the booking details
$(document).ready(function() {
    // parse the js data from html
    const bookingDescription =JSON.parse($('#descriptionForbooking').html())
    $('#taskDescription').text(bookingDescription)

    // Check which payment method is clicked and update it
    $('#bookingForm').on('click', function() {
        const form = $(this);
        const online_payment = form[0][1]['checked']
        const cash_payment = form[0][2]['checked']
        const onlinePaymentValue = 'Online payment at job completion'     //(form[0][1]['value'])
        const cashPaymentValue = 'Cash payment at job completion'   //(form[0][2]['value'])

        if (online_payment == true) {
            $('#thePaymentType').val(onlinePaymentValue)
        } else if ( cash_payment == true) {
            $('#thePaymentType').val(cashPaymentValue)
        }
          
        

    })
});
