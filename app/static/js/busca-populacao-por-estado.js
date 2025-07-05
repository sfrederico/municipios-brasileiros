// Busca municípios por nome via AJAX
function buscarPopulacaoPorUF(uf) {
    if (uf.length < 1) {
        alert('Digite pelo menos 2 caracteres');
        return;
    }

    const url = `/buscar-populacao-por-estado/${encodeURIComponent(uf)}`;

    $.ajax({
        url: url,
        type: 'GET',
        success: function (html) {
            $('#resultado-busca').html(html);
        },
        error: function (xhr, status, error) {
            console.error('Erro na busca:', xhr.status, error);
        }
    });
}

// Inicializa eventos quando página carrega
$(document).ready(function () {
    $('#form-busca-populacao-por-estado').on('submit', function (e) {
        e.preventDefault();

        // Pega valor do input e chama busca
        const uf = $(this).find('input[type="text"]').val().trim().toUpperCase();
        buscarPopulacaoPorUF(uf);
    });
});
