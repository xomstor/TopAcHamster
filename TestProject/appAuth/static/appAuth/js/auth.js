$(document).ready(function() {
    $('#form_auth').submit(function(e) {
        e.preventDefault();
        let form = $(this);
        let csrftoken = form.find('input[name="csrfmiddlewaretoken"]').val();
        let login = form.find('input[name="username"]').val();
        let password = form.find('input[name="password"]').val();
        
        $.ajax({
            type : 'POST',
            url : '/auth',
            data : {
                "юзернаме" : login,
                "pwd" : password,
                csrfmiddlewaretoken : csrftoken,
            },
            success : function(response) {
            if (response.status === 'ok') {
                var url = "auth";
                window.open(url, "_blank");
            } else {
                alert(response.message);
            }}
        })
    })
})

        //         $.ajax({
//             type : 'POST',
//             url : '/auth',
//             data : {
//                 username : form.find('input[name="username"]').val(),
//                 password : form.find('input[name="password"]').val(),
//                 csrfmiddlewaretoken : csrftoken,
//             },
//             success : function(response) {
//                 if (response.status === 'ok') {
//                     window.location.href = '/';
//                 } else {
//                     alert(response.message);
//                 }}
// })