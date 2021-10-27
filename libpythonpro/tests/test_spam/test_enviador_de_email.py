from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido
import pytest



def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'geovanipaz7@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()

    resultado = enviador.enviar(
        destinatario,
        'luciano@gmail.com',
        'teste de email',
        'primeiro teste de email'
    )
    assert destinatario in resultado





@pytest.mark.parametrize(
    'destinatario',
    ['', 'geovanipaz7']
)
def test_remetente_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            destinatario,
            'luciano@gmail.com',
            'teste de email',
            'primeiro teste de email'
        )
