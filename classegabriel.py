class futebol:
    def __init__(self,homem_bandeira,homemquechuta,homemdogol):
        self.homem_bandeira = homem_bandeira
        self.homemquechuta = homemquechuta
        self.homemdogol = homemdogol
        self.torcida = []
    def adicionar_torcida(self, torc1, torc2, torc3):
        self.torcida.extend([torc1, torc2, torc3])
    def mostrar_jogadores(self):
        print(f'Jogadores: ')
        print(self.homem_bandeira, self.homemquechuta, self.homemdogol)
    def mostrar_torcida(self):
        print(f'Torcida: ')
        print(f" , ".join(self.torcida))
campo = futebol('jorge1', 'jorge2', 'jorge3')
campo.adicionar_torcida('torcedor1', 'torcedor2', 'torcedor3')
campo.mostrar_jogadores()
campo.mostrar_torcida()

class bolo:
    def __init__(self, recheio, sabor, tematico):
        self.recheio = recheio
        self.sabor = sabor
        self.tematico = tematico
        self.fotos = []
    def adicionar_poses(self, pose1, pose2, pose3):
        self.fotos.extend([pose1, pose2, pose3])
    def mostrar_bolo(self):
        print(f'Caracteristicas do bolo: ')
        print(self.recheio,self.sabor,self.tematico)
    def mostrar_poses(self):
        print(f'Poses: ')
        print(f' , '.join(self.fotos))
pedido = bolo('maracuja', 'chocolate', 'Virgínia Fonseca')
pedido.adicionar_poses('beijinho', 'abraçando o vini', 'tentando abraçar a propria filha')
pedido.mostrar_bolo()
pedido.mostrar_poses()