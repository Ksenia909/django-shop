// Эффект для кнопок при нажатии
document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll("button");

    buttons.forEach(button => {
        button.addEventListener("mousedown", () => {
            button.style.transform = "scale(0.95)";
        });

        button.addEventListener("mouseup", () => {
            button.style.transform = "scale(1)";
        });

        button.addEventListener("mouseout", () => {
            button.style.transform = "scale(1)";
        });
    });
});

function showAddToCartMessage() {
    const message = document.createElement("div");
    message.textContent = "Товар добавлен в корзину!";
    message.classList.add("cart-message");
    document.body.appendChild(message);

    setTimeout(() => {
        message.style.opacity = "0";
        setTimeout(() => {
            message.remove();
        }, 500);
    }, 1500);
}
