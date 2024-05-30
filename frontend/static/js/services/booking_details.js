$(document).ready(function() {

    // Get all the LGA datas
    const lgas = JSON.parse($('#LGAData').html());
    //console.log(lgas)
    console.log('Abia'[lgas])

    $('#inputState').change(function() {
        // get the selected value
        var selectedValue = $(this).val();
        const selectedLGA = $('#inputLGA');

        selectedLGA.empty();
        selectedLGA.append('<option value="">Choose...</option>');

        // get the LGAs for the selected state
        if (lgas[selectedValue]) {
            lgas[selectedValue].forEach(function(lga) {
                selectedLGA.append(new Option(lga, lga));
            });
        }

        
    })
});