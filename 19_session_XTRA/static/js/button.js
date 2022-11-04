let svgCode = `
<svg class="hover-arrow" width="10" height="10" viewBox="0 0 10 10" aria-hidden="true">
    <g fill-rule="evenodd">
        <path class="hover-arrow-line-path" d="M0 5h7"></path>
        <path class="hover-arrow-tip-path" d="M1 1l4 4-4 4"></path>
    </g>
</svg>`

// Get each button with class "button"
let buttons = document.getElementsByClassName("button");
// Loop through each button
for (let i = 0; i < buttons.length; i++) {
    // Add SVG code to each button's innerHTML
    buttons[i].innerHTML += svgCode;
}