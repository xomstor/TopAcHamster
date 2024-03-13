let status_server = false;
let search = "";

document.querySelector('.search-input').addEventListener('input', (e) => {
    console.log(e.target.value)
    search = e.target.value
    if (status_server == false) {
        status_server = true
        if (search == "") {
            document.querySelector('.search ul').innerHTML = ""
        }
        setTimeout(() => {
            status_server = false
            $.ajax({
                url: '/search',
                type: 'POST',
                data: {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'search': search,
                },
                success: function (response) {
                    console.log(response)
                    let section = document.querySelector(".search ul")
                    document.querySelector('.search ul').innerHTML = ""
                    for (let i = 0; i < response.product.length; i++) {
                        let product = response.product[i]
                        let li = document.createElement('li')
                        li.innerHTML = `<a href="${product.id}">${product.title}</a>`
                        section.appendChild(li)
                        // section.innerHTML += `
                        //     <li>
                        //         <a href="${response[i]}">${response[i]}</a>
                        //     </li>
                        // `
                    }
                }
            })
        }, 1000)
    }
    
})