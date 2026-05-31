def funcao(texto, deslocamento):
    texto_codificado = ""
    for char in texto:
        if 'A' <= char <= 'Z':
            original_0_a_25 = ord(char) - ord('A')

            novo_0_a_25 = (original_0_a_25 + deslocamento) % 26

            novo_codigo_ascii = novo_0_a_25 + ord('A')

            nova_letra = chr(novo_codigo_ascii)

            texto_codificado = texto_codificado + nova_letra

        else:
            texto_codificado = texto_codificado + char

    return texto_codificado
