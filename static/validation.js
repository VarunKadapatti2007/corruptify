function validateSize(input) {
    const sizeError = document.getElementById('size_error');
    const size = parseInt(input.value, 10);
    const downloadBtn = document.getElementById('download_btn');

    if (isNaN(size) || size < 0) {
        sizeError.textContent = 'Size must be a non-negative number.';
        input.setCustomValidity('');
        input.reportValidity();
        downloadBtn.setAttribute('disabled', true); // Disable the button
    } else {
        sizeError.textContent = '';
        input.setCustomValidity('');
        input.reportValidity();
        downloadBtn.removeAttribute('disabled'); // Enable the button
    }
}
