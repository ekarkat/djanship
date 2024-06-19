document.addEventListener("DOMContentLoaded", function () {
    const stateSelect = document.getElementById('state-select');
    const citySelect = document.getElementById('city-select');

    stateSelect.addEventListener('change', function () {
        const stateId = this.value;

        if (stateId) {
            fetch(`http://localhost:8000/api/states/${stateId}/cities/`)
                .then(response => response.json())
                .then(data => {
                    // Clear the city select field
                    citySelect.innerHTML = '';

                    // Populate city select field with the retrieved cities
                    data.forEach(city => {
                        const option = document.createElement('option');
                        option.value = city.id;
                        option.textContent = city.name;
                        citySelect.appendChild(option);
                    });
                })
                .catch(error => {
                    console.error('Error fetching cities:', error);
                });
        } else {
            // Clear the city select field if no state is selected
            citySelect.innerHTML = '';
        }
    });
});
