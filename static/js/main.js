const exit = document.querySelector(".exit")
const elModal = document.querySelector(".modal")
const btnSim = document.querySelectorAll(".botaoResposta")[0]
const btnNao = document.querySelectorAll(".botaoResposta")[1]
const overlay = document.querySelector(".overlay")
const botaoAbrir = document.querySelector(".botao_abrir")
const botaoparagrafo = document.querySelector(".desc")
const abrirbotoes = document.querySelector(".desc_botao")
// const logar = document


//Função criada para sair da pagina através do "X"

let esconder = false


btnSim.addEventListener("click", resposta, 'true')
btnNao.addEventListener("click", resposta, 'false')
exit.addEventListener("click", sairdapagina)


function sairdapagina() {
    if (esconder) {
        esconder = false
        overlay.style.display = 'none'
        elModal.style.display = 'none'
    } else {
        esconder = true
        elModal.style.display = 'flex'
        overlay.style.display = 'flex'
    }
}

function resposta(e) {
    if (e.target.innerHTML == 'Sim') {
        sairdapagina()
        window.location.href = '/index.html'

    } else {
        esconder = true
        sairdapagina()
    }
}

//Função criada para abrir a descrição do livro

let esconderdescricao = false


botaoAbrir.addEventListener("click", abrirdesc)

function abrirdesc() {
    if (esconderdescricao) {
        esconderdescricao = false
        botaoparagrafo.style.display = 'none'

        botaoAbrir.style.background = 'url(/assets/fechado.png)'
        botaoparagrafo.style.transition = '2s'
        // botaoAbrir.style.backgroundRepeat = 'no-repeat'

    } else {
        esconderdescricao = true
        botaoparagrafo.style.display = 'flex'
        botaoAbrir.style.background = 'url(/assets/aberto.png)'
        botaoparagrafo.style.transition = '2s'
        // botaoAbrir.style.backgroundRepeat = 'no-repeat'
    }
}


function getCep(cep) {
    fetch(`https://viacep.com.br/ws/${cep}/json/`)
        .then((response) => response.json())
        .then(data => {
            console.log(data)
        })

}


getCep('05790310')