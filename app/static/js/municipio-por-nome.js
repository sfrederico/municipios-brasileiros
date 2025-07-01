function buscarMunicipioPorNome(nome) {
    if (nome.length < 2) {
        alert('Digite pelo menos 2 caracteres');
        return;
    }

    try {
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

    } catch (error) {
        console.error('Erro na requisição:', error);
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('form-busca-municipio-por-nome');

    if (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();

            // Pegar o valor do input
            const input = this.querySelector('input[type="text"]');
            const nome = input.value.trim();

            // Chamar a função de busca
            buscarMunicipioPorNome(nome);
        });
    }
});
