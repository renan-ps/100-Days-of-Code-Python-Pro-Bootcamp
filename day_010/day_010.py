def format_name(name, lastname):
    """
    Formata o nome corretamente, colocando a primeira letra de cada nome maúscula e deixando o restante minúsculo
    """
    formated_name = name.title() + " " + lastname.title()
    return formated_name


formated_name = format_name("renan", "pErEiRA")

print(formated_name)

