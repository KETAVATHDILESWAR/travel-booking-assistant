document.getElementById("bookingForm").addEventListener("submit", function(e){

    e.preventDefault();

    fetch("/book",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            name:document.getElementById("name").value,
            email:document.getElementById("email").value,
            phone:document.getElementById("phone").value

        })

    })

    .then(response=>response.json())

    .then(data=>{

        document.getElementById("message").innerHTML=data.message;

    });

});
