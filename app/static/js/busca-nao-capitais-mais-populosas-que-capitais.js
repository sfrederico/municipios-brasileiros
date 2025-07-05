// Busca cidades que não são capitais e têm população maior que capitais
function buscarNaoCapitaisMaisPopulosas() {
    $.ajax({
        url: '/cidades-nao-capitais-mais-populosas', // Endpoint que você vai criar no backend
        type: 'GET',
        success: function (html) {
            $('#resultado-busca').html(html); // Exibe o resultado na página
        },
        error: function (xhr, status, error) {
            console.error('Erro ao buscar cidades:', xhr.status, error);
        }
    });
}

$(document).ready(function () {
    $('#form-busca-nao-capitais-mais-populosas-que-capitais').on('submit', function (e) {
        e.preventDefault();
        buscarNaoCapitaisMaisPopulosas();
    });
});