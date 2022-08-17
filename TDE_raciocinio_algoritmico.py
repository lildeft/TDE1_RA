
def retorna_mais1_menos1(numero):
    print("Antecessor: {numero-1}, Sucessor: {numero+1}")

def retorna_idade_2032(ano_nascimento):
    idade = 2032 - ano_nascimento
    print(idade)

def retorna_salario_minimo(salario):
    salario_minimo = 1212 #procurei no google e ta isso ae
    quantidade_salarios_minimos = salario/salario_minimo
    print(quantidade_salarios_minimos)

def retorna_area_circulo(diametro):
    raio = diametro/2
    pi = 3.1415
    area = pi * (raio ** 2)
    print(area)

def retorna_preços_produto(preco):
    preco3x = (preco*1.05)/3
    preco2x = preco/2
    preco1x = preco*0.95
    print(f'Preço em 3x (por parcela): {preco3x}')
    print(f'Preço em 2x (por parcela): {preco2x}')
    print(f'Preço a vista: {preco1x}')
    
def retorna_hipotenusa(cateto1, cateto2):
    hipotenusa_ao_quadrado = (cateto1 ** 2) + (cateto2 ** 2)
    hipotenusa = hipotenusa_ao_quadrado ** 0.5
    print(hipotenusa)

def retorna_segundos_minutos(hora, minuto, segundo):
    total_de_minutos_passados = (hora*60) + minuto
    total_de_segundos_passados = (hora*60*60) + (minuto*60) + segundo
    print(f"Minutos passados: {total_de_minutos_passados}")
    print(f"Segundos passados: {total_de_segundos_passados}")

def retorna_latas_e_preco(altura, raio):
    pi = 3.1415
    area_cilindro_base = pi*(raio ** 2)
    area_cilindro_lateral = (2*pi)*raio*altura
    area_cilindro_total = (area_cilindro_base*2) + area_cilindro_lateral
    custo_lata_de_tinta = 50.00
    litro_da_lata = 5
    metros_quadrados_pintados = 3*litro_da_lata
    quantidade_latas = area_cilindro_total/metros_quadrados_pintados
    custo_total = quantidade_latas * custo_lata_de_tinta
    print(f'Quantidade de latas: {quantidade_latas}')
    print(f'Custo total: {custo_total}')

def meunome(nome, sobrenome):
    print(nome)
    print(sobrenome)


retorna_mais1_menos1(10)
retorna_idade_2032(2022)
retorna_salario_minimo(2424)
retorna_area_circulo(10)
retorna_preços_produto(10)
retorna_hipotenusa(10, 10)
retorna_segundos_minutos(10,10,10)
retorna_latas_e_preco(10, 10)

