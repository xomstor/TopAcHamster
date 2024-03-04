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
                console.log(response);
                alert('Сохранено');
            },
            error : function(response) {
                alert('Произошла ошибка');
            }
        });
    });

})