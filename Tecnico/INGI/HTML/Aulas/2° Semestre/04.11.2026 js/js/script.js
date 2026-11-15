//alert("Welcome to Campos do Jordão!"); 

console.log("Welcome to the Campos do Jordão Travel Guide!");

//declaração de variaveis
let temperatureC = 12;

//declaração constant
const cityName = "Campos do Jordão";
const altitude = 1628;

console.log("Temperature in "+ cityName + ": " + temperatureC + " Celsius degree(s).");
// metros -> pés 
altitude * 3.28; 
// Celsius -> Fahrenheit 
temperatureC * 9 / 5 + 32;

console.log(`${cityName} is ${altitude} meters above sea level.`);

let isTouristCity = true;

console.log(typeof altitude);  
console.log(typeof cityName);
console.log(typeof isTouristCity);

//operações aritméticas
const altitudeFeet = Math.ceil(altitude * 3.28);
console.log(altitudeFeet);

const TemperatureF = temperatureC * 9 / 5 + 32;
console.log(TemperatureF);

// entrada de dados simples
const visitorName = prompt("What is your name?");
if (visitorName) {
    alert(`Hello, ${visitorName}`);
}

//objeto Date: data e hora
const now = new Date();
const hour = now.getHours(); // 0 a 23
const month = now.getMonth() + 1; // 1 a 12

//estrutura condicional - if - else
let greeting;

if(hour < 12){
    greeting = "Good morning";
}else if(hour < 18){
    greeting = "Good afternoon";
}else{
    greeting = "Good evening";
}

//operadores lógicos
let season;
if(month >= 6 && month <= 8){
    season = "Winter (high season)";
} else if(month >= 9 && month <= 11){
    season = "Spring"; 
} else if (month === 12 || month <= 2){
    season = "Summer";
} else {
    season = "Autumn"; // Corrigido de "Autum"
}

console.log("Current season: " + season);
if(temperatureC < 10){
    console.log("It is cold. Bring a coat!");
}else{
    console.log("The weather is nice today.");
}

//array com as atrações
const attractions = ["Vila Capivari", "Elephant Hill", "Amantikir Park"]; 
console.log(attractions.length);  // quantidade de itens
console.log(attractions[0]);   // primeiro item  

// repetição com for (corrigido de attractions[1] para attractions[i])
for(let i = 0; i < attractions.length; i++){
    console.log(`${i + 1}. ${attractions[i]}`);
}
    
// repetição for...of
for(const attraction of attractions){
    console.log(attraction.toLocaleUpperCase());
}

//array com os meses
const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]; 

// Ano atual no rodapé
const yearElement = document.getElementById("year");
if (yearElement) {
    yearElement.textContent = now.getFullYear();
}

const seasonElement = document.getElementById("season");
if (seasonElement) {
    seasonElement.innerHTML = `<strong>Current season:</strong> ${season}`;
}

const celsiusInput = document.getElementById("celsius");
if (celsiusInput) {
    celsiusInput.value = temperatureC;
}

// Função chamada pelo botão de conversão
function convertTemperature() {
    const celsius = Number(celsiusInput.value);
    const fahrenheit = celsius * 9 / 5 + 32;

    const resultElement = document.getElementById("result");
    if (resultElement) {
        resultElement.textContent = `${celsius} °C = ${fahrenheit.toFixed(1)} °F`;
    }
}

// Associa o evento de clique ao botão do conversor
const convertBtn = document.getElementById("convert-btn");
if (convertBtn) {
    convertBtn.addEventListener("click", convertTemperature);
}

// Tamanho da fonte da página: valor dinâmico, bom caso de uso para o style
let fontSize = 16;   // tamanho atual, em pixels

function changeFontSize(amount) {
    const newSize = fontSize + amount;

    // Limites: a fonte não fica menor que 12px nem maior que 24px
    if (newSize >= 12 && newSize <= 24) {
        fontSize = newSize;
        document.body.style.fontSize = fontSize + "px";
    }
}
   // toggle: adiciona a classe se ela não existe, remove se ela existe
    document.body.classList.toggle("dark-mode");

    // contains: verifica se a classe está no elemento (true ou false)
    const themeButton = document.getElementById("theme-btn");
    if (document.body.classList.contains("dark-mode")) {
        themeButton.textContent = "Light mode";
    } else {
        themeButton.textContent = "Dark mode";
    }
    // Aula 35: a cor do resultado depende da temperatura (classes .cold e .hot do CSS)
    resultElement.classList.remove("cold");
    resultElement.classList.remove("hot");
    if (celsius < 15) {
        resultElement.classList.add("cold");
    } else {
        resultElement.classList.add("hot");
    }
function toggleTheme() {
    // toggle: adiciona a classe se ela não existe, remove se ela existe
    document.body.classList.toggle("dark-mode");

    // contains: verifica se a classe está no elemento (true ou false)
    const themeButton = document.getElementById("theme-btn");
    if (document.body.classList.contains("dark-mode")) {
        themeButton.textContent = "Light mode";
    } else {
        themeButton.textContent = "Dark mode";
    }
}