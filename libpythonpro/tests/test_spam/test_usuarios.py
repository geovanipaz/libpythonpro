from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Renzo', email='renzo@mail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)



def test_listar_usuario(conexao):
    sessao = conexao.gerar_sessao()
    usuarios = [
        Usuario(nome='Renzo', email='renzo@mail.com'),
        Usuario(nome='Geovani', email='renzo@mail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
