document.addEventListener("DOMContentLoaded", function() {

  $('#payment-form').on('submit',function(){
    var firstname = $('#firstname').val();
    var lastname = $('#lastname').val();
    if(firstname ===''|| lastname === ''){
      alert('First name and last name cannot be left blank');
      return;
    }

    var cvc = $('#cvc').val();
    if(cvc.length !==3){
      alert('Please enter a valid cvc');
    }
    var cardNum = $('#credit-card').val();
    if(cardNum.length !==16){
      alert('Please enter at valid credit card');
      return;
    }

    var exp = document.getElementById('expiration').value;
    if (exp != /^\/[\d]{2}\/[\d]{2}/){
      alert('Please enter the correct format MM/DD');
    }

  });

});
