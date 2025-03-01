const buttonsBuy = document.querySelectorAll('#buy');
const main = document.querySelector('main');
const form = document.querySelector(".form-container");
const subscriptionInput = document.querySelector(".hidden-input");
const desktopNumberInput = document.createElement("input");

console.log(buttonsBuy, form);
buttonsBuy.forEach((buttonBuy) => {
    buttonBuy.addEventListener('click', () => {
        main.style.display = "None";
        form.style.display = "block";
        const buttonChild = buttonBuy.children[0];
        console.log("buttonChild id =", buttonChild.id);
        const subscription = buttonChild.id.split("sub")[1];
        console.log(subscription);
        if (subscription != "Desktop"){
            subscriptionInput.value = subscription;
        }else{
            desktopNumberInput.type = "number";
            desktopNumberInput.classList = "form-input";
        }
    })
})