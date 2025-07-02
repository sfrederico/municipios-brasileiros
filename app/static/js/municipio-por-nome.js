// Busca municípios por nome via AJAX
function buscarMunicipioPorNome(nome) {
    if (nome.length < 2) {
        alert('Digite pelo menos 2 caracteres');
        return;
    }

    const url = `/municipios-por-nome/${encodeURIComponent(nome)}`;

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
    $('#form-busca-municipio-por-nome').on('submit', function (e) {
        e.preventDefault();

        // Pega valor do input e chama busca
        const nome = $(this).find('input[type="text"]').val().trim();
        buscarMunicipioPorNome(nome);
    });
});
