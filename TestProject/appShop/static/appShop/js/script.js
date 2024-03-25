let addBack = document.querySelectorAll('#addback');
addBack.forEach((btn) => {
    btn.addEventListener('click', () => {
        let elements = btn.closest('.card');
        let title = elements.querySelector('h1').textContent;
        let price = elements.querySelector('h3').textContent;
        let product_id = btn.getAttribute('data-product-id');
        
        // let productCount = parseInt(elements.querySelector('.count').textContent);
        // if (productCount <= 0) {
        //     return;
        // }
        let back = document.querySelector('.back');
        let content = document.createElement('div');
        content.innerHTML = `<p>${title}</p><p>${price}</p><button class="delete-from-cart" data-product-id="${product_id}">Удалить</button>`;
        back.appendChild(content);

        $.ajax({
            type: 'POST',
            url: '/shop/add_to_cart/',
            data: {
                product_id: product_id, 
                csrfmiddlewaretoken: $('meta[name="csrf-token"]').attr('content'),
            },
            success: function(response) {
                backed = response.backed;
                console.log(backed);
            },
            error: function(xhr, status, error) {
                // console.error('Error in POST request:', error);
            }
        });

        content.querySelector('.delete-from-cart').addEventListener('click', () => {
            content.remove();
        })
    })
})

$('#form').submit(function(event) {
    event.preventDefault();

    var formData = {
        janr: $('input[name=janr]').val(),
        title: $('input[name=title]').val(),
        price: $('input[name=price]').val()
    };

    $.ajax({
        type: 'POST',
        url: '/shop/',
        data: formData,
        success: function(response) {
            // Handle the successful response
        },
        error: function(xhr, status, error) {
            // Handle the error response
        }
    });

    $('input[name=janr]').val('');
    $('input[name=title]').val('');
    $('input[name=price]').val('');

    return false;
})

document.querySelector("#formAjax").addEventListener("submit", function(event) {
    event.preventDefault();
    let form = document.querySelector("#formAjax");
    let text = form.querySelector("textarea").value;
    let csrf = form.querySelector("input[name=csrfmiddlewaretoken]").value;
    $.ajax({
        type: "POST",
        url: form.getAttribute("action"),
        data: {
            csrfmiddlewaretoken: csrf,
            text: text
        },
        success: function(response) {
            console.log(response);
        },
        error: function(xhr, status, error) {
            console.error("Error:", error);
        }
    });

})