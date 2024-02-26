$(document).ready(function() {
    function submit_email(e) {
        e.preventDefault();
        let form = $(this)
        let len = form.find("input[name='len']").val()
        let csrftoken = form.find('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            type : 'POST',
            url : '/api',
            data : {
                csrfmiddlewaretoken : csrftoken,
                number_len : len,
                action : 'generate-email',
            },
            success : function(response) {
                for (let i = 0; i < response.data_email.length; i++) {
                    let section = document.querySelector('#emails');
                    let p = document.createElement('p');
                    p.textContent = response.data_email[i];
                    section.appendChild(p);
                }
            },
            error : function(response) {
                alert('error1')
            }
        })
    }
    $('#form_generate_email').submit(submit_email)
    $('.send-btn').click(function() {
        $.ajax({
            type : 'POST',
            url : '/api',
            data : {
                action : 'generate-password',
                csrfmiddlewaretoken : csrftoken,
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
            $('#form_generate_email').submit(submit_email(e))   
            },
            error : function(data) {
                alert('error1'),
                console.log(data)
            }
        })
        prompt("hello", "WORLD!")
        if (prompt("hello", "")) {
            alert("nihua")
        }
    })
})