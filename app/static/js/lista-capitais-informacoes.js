// Busca todas as capitais via AJAX
function buscarTodasCapitais() {
    $.ajax({
        url: '/capitais', // Ajuste para o endpoint correto do seu backend
        type: 'GET',
        success: function (html) {
            $('#resultado-busca').html(html); // Ou outro elemento para exibir os dados
        },
        error: function (xhr, status, error) {
            console.error('Erro ao buscar capitais:', xhr.status, error);
        }
    });
}

// Inicializa eventos quando página carrega
$(document).ready(function () {
    $('#form-lista-capitais-informacoes').on('submit', function (e) {
        e.preventDefault();
        // Chama a função para buscar todas as capitais
        buscarTodasCapitais();
});
});