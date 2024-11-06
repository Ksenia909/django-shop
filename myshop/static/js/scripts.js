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

    setTimeout(() => {
        const messages = document.querySelector('.messages');
        if (messages) {
            messages.style.opacity = "0";
            setTimeout(() => {
                messages.style.display = 'none';
                    }, 500);
                }
            }, 3000);
        });



