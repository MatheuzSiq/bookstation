const endForm = document.querySelector("#endForm")
const cepInput = document.querySelector("#cep")
const endereco = document.querySelector("#endereco")
const bairro = document.querySelector("#bairro")
const cidade = document.querySelector("#cidade")
// input para manipular em massa
const formInputs = document.querySelector("[data-input]")
const closeButton = document.querySelector("#close-message")

const fadeElement = document.querySelector("#fade")

// validar CEP input
cepInput.addEventListener("keypress", (e) => {
    const apenasNumeros = /[0-9]/;
    const tecla = String.fromCharCode(e.keyCode);

    // permitir apenas numeros
    if(!apenasNumeros.test(tecla)){
        e.preventDefault();
        return;
    }
});

// evento para pegar o cep
cepInput.addEventListener("keyup", (e) =>{

    const valorInput = e.target.value

    // verifica se tem o tamanho correto
    if(valorInput.length === 8){
        pegarEndereco(valorInput);
    }

})

// Pegar o endereco da API
const pegarEndereco = async (cep) => {
    // tira o cursor do campo cep
    cepInput.blur();

    const apiURL = `https://viacep.com.br/ws/${cep}/json/`

    const response = await fetch(apiURL);

    const data = await response.json();

    // mostrar erro e resetar o form
    if(data.erro === true){
        endForm.reset();
        mudarLoader();
        // mostrar mensagem
        mostrarMensagem("CEP invalido, tente novamente!")
        return;
    }

    endereco.value = data.logradouro;
    bairro.value = data.bairro;
    cidade.value = data.localidade + "-" + data.uf;
}

const mudarLoader = () => {

    const loaderElement = document.querySelector("#loader")

    fadeElement.classList.toggle("hide")
    loaderElement.classList.toggle("hide")

}

const mostrarMensagem = (msg) => {

    const messageElement = document.querySelector("#message");

    const messageElementText = document.querySelector("#message p")

    messageElementText.innerText = msg;

    fadeElement.classList.toggle("hide");
    messageElement.classList.toggle("hide");

}

// Close message modal
closeButton.addEventListener("click", () => mostrarMensagem());




