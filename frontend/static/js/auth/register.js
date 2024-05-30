$( document ).ready(function() {
  $('#signup').on('click', function() {
    event.preventDefault();
    let formData = $('#signupForm').serializeArray()

    phone_number = formData[0].value
    password = formData[1].value
    

    phoneNumberRegex = /^\d*$/;

    // validate the forms
    if (phone_number.length === 0) {
      $('#messageError').text('Please enter your phone number').show()
    } else if (!phoneNumberRegex.test(phone_number)) {
      $('#messageError').text('Please enter a valid phone number').show()
    } else if (password.length === 0) {
      $('#messageError').text('Please enter your password').show()
    } else if (password.length < 8 ) {
      $('#messageError').text('Please enter a password of 8 minimum characters').show()
    } else {
      // verify phone number and genearate token
      $.ajax({
        url: '/auth/register',
        type: 'POST',
        data: JSON.stringify({
          phone_number: phone_number,
          password: password,
        }),
        contentType: 'application/json',
        dataType: 'json',
        success: function(token) {
          // pop modal to take the otp for verificaton
          $('#otpModal').modal('show')
          // call the function to verify the otp and token
          verifyCode(token)
        },
        error: function( jqXHR, textStatus, errorThrown ) {
          let m = jqXHR.responseText
          pText = getPElement(m)
          $('#messageError').text(pText).show()
        }
      })
    }
  })

  // submit the otp and token to backend for verification
  verifyCode = function (token) {
    $('#otpForm').submit(function() {
      event.preventDefault();

      let otp = $('#otpInput').val();
      if (otp.length == 0) {
        $('#otpMSG').text('Enter the otp to verify your phone number').show()
      } else if (otp.length < 6) {
        $('#otpMSG').text('Please, enter the complete otp').show()
      } else {
        $.ajax({
          url: '/auth/verify/otp',
          type: 'POST',
          data: JSON.stringify({
            otp: otp,
            token: token,
          }),
          contentType: 'application/json',
          dataType: 'json',
          // Create user when otp verification succeeds
          success: function() {
            $('#otpMSG').text('Success').show()
            createuser();
          },
          error: function( jqXHR, textStatus, errorThrown ) {
            let response = jqXHR.responseText
            pText = getPElement(response)
            $('#otpMSG').text(pText + ", " + 'Try again').show()
            // Reload the web when otp verification failed
            setTimeout(function() {
              window.location.reload()
            }, 6000)
            
          }
        })
      }
    });
  }

  // Create user
  createuser = function () {
    $.ajax({
      url: 'http://127.0.0.1:8000/api/v1/users',
      type: 'POST',
      data: JSON.stringify({
        phone_number: phone_number,
        password: password,
      }),
      contentType: 'application/json',
      dataType: 'json',
      success: function(data, textStatus, jqXHR) {
        data = (data[0])
        userId = data.id
        console.log(userId)
        loginUser()
        window.location.href = '/account/profile'
      },

      error: function( jqXHR, textStatus, errorThrown ) {
        let response = jqXHR.responseText
        pText = getPElement(response)
        $('#messageError').text(pText + ", " + 'Try again').show()
        window.location.reload()
      }
    })
  }

  // Parse the html response to get the p tag element
  let getPElement = function (htmlstring) {
    // temporal div to parse the html string
    let tempDiv = document.createElement('div')
    tempDiv.innerHTML = htmlstring
    // get the p element in the parsed html
    let pElement = tempDiv.querySelector('p')
    if (pElement) {
      return pElement.textContent;
    }
  }

  // handler to always return ajax response
  let responseHandler = function(response) {
    return response
  }


  // Login the user
  loginUser = function () {
    $.ajax({
      url: '/auth/login',
      type: 'POST',
      data: JSON.stringify({
        phone_number: phone_number,
        password: password,
      }),
      contentType: 'application/json',
      dataType: 'json',
      success: function(data, textStatus, jqXHR) {
        window.location.href = '/account/profile'
      },
      error: function( jqXHR, textStatus, errorThrown ) {
        window.location.reload()
      }
    })
  }













    
});
