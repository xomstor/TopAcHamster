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
    $('#form_reg').submit(function(e) {
        e.preventDefault();
        let form = $(this);
        let csrftoken = form.find('input[name="csrfmiddlewaretoken"]').val();
        let login = form.find('input[name="login"]').val();
        let name = form.find('input[name="name"]').val();
        let surname = form.find('input[name="surname"]').val();
        let email = form.find('input[name="email"]').val();
        let password = form.find('input[name="password"]').val();
        let password2 = form.find('input[name="password2"]').val();
        if (password != password2) {
            $('#Error').text('Пароли не совпадают');
        } else if (login === '' || email === '' || password === '' || password2 === '') {
            $('#Error').text('Заполните все поля');
        } else if (!email.includes('@') || !email.includes('.')) {
            $('#Error').text('Неверная почта');
        } else {
            alert('Регистрация прошла успешно');
        }
        $.ajax({
            type : 'POST',
            url : '/auth/reg/',
            data : {
                "login" : login,
                "name" : name,
                "surname" : surname,
                "email" : email,
                "password" : password,
                csrfmiddlewaretoken : csrftoken,
            },
            success : function(response) {
                if (response.status === 'ok') {
                    $.('#result').text("Регистрация прошла успешно");
                } else if (response.status === 'error') {
                    $.('#result').text("Регистрация не прошла, фиговый логин или почта");
                } else {
                    $.('#result').text("Регистрация не прошла");
                }
                }
        })
    })
})