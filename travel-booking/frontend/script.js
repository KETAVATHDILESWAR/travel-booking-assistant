document.getElementById("bookingForm").addEventListener("submit", function(event){

    event.preventDefault();

    const bookingData = {

        name: document.getElementById("name").value,

        source: document.getElementById("source").value,

        destination: document.getElementById("destination").value,

        date: document.getElementById("date").value

    };

    fetch("http://YOUR-EC2-IP:5000/book", {

        method: "POST",

        headers: {
            "Content-Type":"application/json"
        },

        body: JSON.stringify(bookingData)

    })

    .then(response => response.json())

    .then(data => {

        document.getElementById("message").innerHTML = data.message;

    });

});
