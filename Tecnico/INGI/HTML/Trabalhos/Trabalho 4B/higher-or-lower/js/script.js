// ===== Projeto Prático — Higher or Lower: The Mountain Guessing Game =====
// Dupla: (escreva aqui o nome dos integrantes)
//
// O index.html e o css/style.css já estão prontos. Vocês escrevem só este arquivo.
// Sigam as seções abaixo, na ordem, testando cada passo no navegador com o Console aberto (F12).
//
// ----- IDs disponíveis no index.html -----
//   new-round-btn   botão "New Round"
//   guess-btn       botão "Guess"
//   restart-btn     botão "Restart Game"
//   theme-btn       botão "Dark mode / Light mode"
//   guess-input     campo do palpite
//   message         parágrafo das mensagens
//   lives           <div> onde ficam os pinhões (começa vazia)
//   game-box        área do jogo (recebe o fundo verde ou vermelho)
//   wins / losses   números do placar
//   history-list    <ul> do histórico (começa vazia)
//   greeting        parágrafo da saudação, no cabeçalho
//   year            ano, no rodapé
//
// ----- Classes prontas no style.css (ligue e desligue com classList) -----
//   no #message:      high, low, correct, wrong, warning   (cores das mensagens)
//   no #guess-input:  invalid                             (borda vermelha)
//   no #game-box:     win, lose                           (fundo verde / vermelho)
//   em cada <li>:     won, lost                           (texto verde / vermelho)
//   em cada pinhão:   pine-nut                            (o <span> com o emoji 🌰)
//   no body:          dark-mode                           (tema escuro)


// ----- 1) Elementos da página -----
// Guarde em constantes os elementos que serão usados várias vezes (getElementById).
const arduino = document.getElementById("arduino");

const newRoundBtn = document.getElementById("new-round-btn");
const guessBtn = document.getElementById("guess-btn");
const restartBtn = document.getElementById("restart-btn");
const themeBtn = document.getElementById("theme-btn");

// ----- 2) Variáveis do jogo -----
// Use let para o que muda durante o jogo. Sugestões:
//   secretNumber (número sorteado), lives (pinhões restantes), roundNumber (rodada atual),
//   wins e losses (placar), roundActive (true enquanto a rodada está em andamento)
let secretNumber;
let lives;
let roundActive;
let wins = 0;
let losses = 0;

// ----- 3) Saudação e ano -----
// Saudação conforme a hora (Good morning / Good afternoon / Good evening) e ano atual no rodapé.
const ano = new Date().getFullYear();
const hour = new Date().getHours();

document.getElementById("year").textContent = ano;

if (hour < 12) {
    document.getElementById("greeting").textContent = "Good morning";
} else if (hour < 18) {
    document.getElementById("greeting").textContent = "Good afternoon";
} else {
    document.getElementById("greeting").textContent = "Good evening";
}

// ----- 4) Funções do jogo -----

// Botão "New Round": sorteia o número, recria os 5 pinhões e mostra uma mensagem

function newRound() {
    // Linha pronta: número inteiro aleatório de 1 a 50
    secretNumber = Math.floor(Math.random() * 50) + 1;
    console.log(secretNumber);
    lives = 5;
    roundActive = true;

}

// Botão "Guess": lê o palpite, valida (1 a 50) e compara com o número secreto
function checkGuess(guessInput) {
    arduino.src = "img/arduino.png";
    arduino.alt = "Arduino";
    arduino.classList.add("arduino");
    function createLives() {
        livesContainer.innerHTML = "";
        for (let i = 0; i < 5; i++) {
        const arduino = document.createElement("arduininho");
        livesContainer.appendChild(arduino); 
    }
}

    if (guessInput === secretNumber && roundActive === true && lives >= 0) {
        wins++;
        roundActive = false;

    }else if (guessInput > secretNumber && roundActive === true && lives >= 0) {
        lives--;
        
    }else if (guessInput < secretNumber && roundActive === true && lives >= 0) {
        lives--;

    }else if (lives === 0) {
        losses++;
        roundActive = false;
    }
}
// Botão "Restart Game": zera o placar, apaga o histórico e os pinhões
function restartGame() {
    losses = 0;
    wins = 0;
    lives = 5
}

// Botão de tema: liga e desliga a classe dark-mode no body
function toggleTheme() {
    document.body.classList.toggle("dark-mode");
     const themeButton = document.getElementById("theme-btn");
    if (document.body.classList.contains("dark-mode")) {
        themeButton.textContent = "Light mode";
    } else {
        themeButton.textContent = "Dark mode";
    }
}


// ----- 5) Eventos -----
// Ligue cada botão à sua função com addEventListener (não use onclick no HTML)

if (newRoundBtn) {newRoundBtn.addEventListener("click", newRound);}
if (guessBtn) {guessBtn.addEventListener("click", checkGuess);}
if (restartBtn) {restartBtn.addEventListener("click", restartGame);}
if (themeBtn) {themeBtn.addEventListener("click", toggleTheme);}