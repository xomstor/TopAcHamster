tinymce.init({
    selector: '#mytextarea',
    height: 500,
    "plugins": [
        "advlist","autolink", "lists", "link","image","charmap","preview","anchor","searchreplace","visualblocks","code","fullscreen","insertdatetime","media","table","help","wordcount"
      ],
     "toolbar": "undo redo | a11ycheck casechange blocks | bold italic backcolor | alignleft aligncenter alignright alignjustify | " +
        "bullist numlist checklist outdent indent | removeformat | code table help"
});

$(document).ready(function() {
    $('#form_content').submit(function(e) {
        e.preventDefault();
        // tinymce.triggerSave();
        let form = $(this);
        $.ajax({
            type : 'POST',
            data : {
                csrfmiddlewaretoken : form.find('input[name="csrfmiddlewaretoken"]').val(),
                content : form.find('#mytextarea').val(),
            },
            success : function(response) {
                if (response['status'] === 'ok') {
                    alert('Сохранено');
                    // let div = document.querySelector('.story-links');
                    // let a = document.createElement('a');
                    // let p = document.createElement('p');
                    // a.href = response['url'];
                    // a.textContent = `Ссылка на публикацию: ${response.url}`
                    // div.appendChild(a);
                    let div = $('.story-links');
                    let a = $('<a></a>').attr('href', response['url']).text(`Ссылка на публикацию: ${response.url}`);
                    div.append(a);
                    let p = $('<p></p>');
                    div.append(p);
                    // form[0].reset();
                }
                if (response['status'] === 'error') {
                    alert('Произошла ошибка, ссылка на публикацию не доступна');
                }
            },
            error : function(response) {
                alert('Произошла ошибка');
            }
        });
    });

})