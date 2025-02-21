let buttonsBuy = document.querySelectorAll('.button');
let main = document.querySelector('main');
let body = document.querySelector("body");
let newInput;
let newButton;
let newForm;

console.log(buttonsBuy);
buttonsBuy.forEach((buttonBuy) => {
    buttonBuy.addEventListener('click', () => {
        main.style.display = "None";
        newForm = document.createElement("form");
        newForm.method = "POST";
        console.log(newForm);
        body.appendChild(newForm);
        newInput = document.createElement('input');
        newInput.name = "subscription";
        newInput.type = "text";
        body.appendChild(newInput);
        newButton = document.createElement('button');
        newButton.type = "submit";
        body.appendChild(newButton);
    })
})