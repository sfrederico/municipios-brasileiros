// Busca os dez municípios mais populosos que não são capitais
function buscarDezMunicipiosMaisPopulosos() {
    console.log('Buscando os dez municípios mais populosos...');

    const url = '/dez-municipios-mais-populosos';

    $.ajax({
        url: url,
        type: 'GET',
        success: function (html) {
            $('#resultado-busca').html(html);
        },
        error: function (xhr, status, error) {
            console.error('Erro na busca:', xhr.status, error);
            alert('Erro ao buscar municípios. Tente novamente.');
        }
    });
}

// Inicializa eventos quando página carrega
$(document).ready(function () {
    $('#form-dez-municipios-mais-populosos').on('submit', function (e) {
        e.preventDefault();
        buscarDezMunicipiosMaisPopulosos();
    });
});
