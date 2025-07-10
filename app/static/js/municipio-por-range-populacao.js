// Busca municípios por range de população
function buscarMunicipioPorRangePopulacao(populacaoMin, populacaoMax) {
    // Validação dos parâmetros
    if (!populacaoMin || populacaoMin <= 0) {
        alert('Digite um valor válido para a população mínima');
        return;
    }

    if (!populacaoMax || populacaoMax <= 0) {
        alert('Digite um valor válido para a população máxima');
        return;
    }

    if (populacaoMin >= populacaoMax) {
        alert('A população mínima deve ser menor que a população máxima');
        return;
    }

    console.log('Buscando municípios com população entre:', populacaoMin, 'e', populacaoMax);

    const url = `/municipios-por-range-populacao/${populacaoMin}/${populacaoMax}`;

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
    $('#form-lista-municipios-range-populacao').on('submit', function (e) {
        e.preventDefault();

        // Pega os valores dos inputs de população
        const inputs = $(this).find('input.form-control');
        const populacaoMin = parseInt(inputs.eq(0).val().trim()) || 0;
        const populacaoMax = parseInt(inputs.eq(1).val().trim()) || 0;

        buscarMunicipioPorRangePopulacao(populacaoMin, populacaoMax);
    });
});
