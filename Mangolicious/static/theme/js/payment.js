$(document).ready(function () {
    $('.paywithRazorpay').click(function (e){
        e.preventDefault();
        $.ajax({
            method: "GET",
            url: "proceed-to-pay",
            success: function (response){
                var options = {
                    "key": "rzp_test_DuofX8F7J4lvMj", // Enter the Key ID generated from the Dashboard
                    "amount": response.total_price * 100, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                    "currency": "INR",
                    "name": "Mangolicious", //your business name
                    "description": "Test Transaction",
                    "image": "https://example.com/your_logo",
                    // "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                    "handler": function (response){
                        alert(response.razorpay_payment_id);
                        window.location.href = '/';
                    },
                    // "prefill": { //We recommend using the prefill parameter to auto-fill customer's contact information, especially their phone number
                    //     "name": "Gaurav Kumar", //your customer's name
                    //     "email": "gaurav.kumar@example.com", 
                    //     "contact": "9000090000"  //Provide the customer's phone number for better conversion rates 
                    // },
                    "notes": {
                        "address": "Razorpay Corporate Office"
                    },
                    "theme": {
                        "color": "#3399cc"
                    },
                };
                var rzp1 = new Razorpay(options);
                rzp1.open();
            },
        });
    });
    
});