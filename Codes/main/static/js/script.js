let buttonsBuy = document.querySelectorAll('#buy');
let main = document.querySelector('main');
let body = document.querySelector("body");
let form = document.querySelector(".form-container");

console.log(buttonsBuy, form);
buttonsBuy.forEach((buttonBuy) => {
    buttonBuy.addEventListener('click', () => {
        main.style.display = "None";
        form.style.display = "block";
    })
})