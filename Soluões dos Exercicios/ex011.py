largura = float(input('largura da parede: '))
altura = float(input('altura da parede: '))
area = largura * altura
tinta = area / 2
print('sua parede tem a dimensão de {}x{} e sua area é de {}m²'.format(largura, altura, area))
print('para pintar essa parede vc precisa de {}l de tinta'.format(tinta))
