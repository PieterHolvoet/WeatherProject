async function getWeather() {
    const city = document.getElementById('city').value;
    const response = await fetch(`http://localhost:5000/weather?city=${city}`);
    const data = await response.json();
    document.getElementById('result').innerHTML =
        `Temperature in ${data.city}: ${data.temperature}, Condition: ${data.condition}`;
}
