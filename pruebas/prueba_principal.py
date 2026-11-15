from agendalo.__main__ import principal


def prueba_principal_imprime_nombre(capsys):
    principal()
    assert capsys.readouterr().out == "Agéndalo\n"
