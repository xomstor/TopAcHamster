$(document).ready(function() {
    $('.send-btn').click(function() {
        $.ajax({
            type : 'POST',
            url : '/api',
            data : {
                csrfmiddlewaretoken : $('meta[name="csrf-token"]').attr('content'),
                gen_length : $('#gen_length').val(),
                gen_amount : $('#gen_amount').val(),
            },
            success : function(data) {
                for (let i = 0; i < data.data.length; i++) {
                    let section = document.querySelector('#passwords');
                    let p = document.createElement('p');
                    p.textContent = data.data[i];
                    section.appendChild(p);
                }
                
            },
            error : function(data) {
                alert('error1')
                console.log(data)
            }
        })
        prompt("hello", "WORLD!")
    })
})