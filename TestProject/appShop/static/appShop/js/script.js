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
                // console.log('POST request successful');
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