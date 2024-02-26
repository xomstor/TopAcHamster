// $(document).ready(()=>(
//     $("#id_title").input(() => (
//         $("#id_description").val($("#id_title").val())
//         ))
// ))

document.addEventListener("DOMContentLoaded", function(event) {
    document.getElementById("id_title").addEventListener("input", function() {
        let a = document.querySelector("#id_title").value.replace(/ /g, "-")
        console.log(a)
        document.getElementById("id_name_url").value = a;
    });
    document.getElementById("id_content").addEventListener("input", function() {
        let b = document.querySelector("#id_content").value
        console.log(b)
    })
})