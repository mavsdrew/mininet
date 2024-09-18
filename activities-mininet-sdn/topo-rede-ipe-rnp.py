from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.node import RemoteController
from mininet.cli import CLI

class RedeIpeRNPTopo(Topo):
    def build(self):
        # Criando switches representando as cidades (28 switches)
        s_porto_alegre = self.addSwitch('s1')
        s_florianopolis = self.addSwitch('s2')
        s_curitiba = self.addSwitch('s3')
        s_sao_paulo = self.addSwitch('s4')
        s_rio_janeiro = self.addSwitch('s5')
        s_campo_grande = self.addSwitch('s6')
        s_vitoria = self.addSwitch('s7')
        s_belo_horizonte = self.addSwitch('s8')
        s_goiania = self.addSwitch('s9')
        s_brasilia = self.addSwitch('s10')
        s_salvador = self.addSwitch('s11')
        s_cuiaba = self.addSwitch('s12')
        s_aracaju = self.addSwitch('s13')
        s_palmas = self.addSwitch('s14')
        s_porto_velho = self.addSwitch('s15')
        s_rio_branco = self.addSwitch('s16')
        s_maceio = self.addSwitch('s17')
        s_recife = self.addSwitch('s18')
        s_campina_grande = self.addSwitch('s20')
        s_joao_pessoa = self.addSwitch('s19')
        s_natal = self.addSwitch('s21')
        s_teresina = self.addSwitch('s22')
        s_manaus = self.addSwitch('s23')
        s_fortaleza = self.addSwitch('s24')
        s_sao_luis = self.addSwitch('s25')
        s_belem = self.addSwitch('s26')
        s_macapa = self.addSwitch('s27')
        s_boa_vista = self.addSwitch('s28')
        
        # Criando hosts (56 hosts)
        for i in range(1, 29):
            host1 = self.addHost(f'h{i*2-1}')
            host2 = self.addHost(f'h{i*2}')
            switch = f's{i}'
            self.addLink(switch, host1)
            self.addLink(switch, host2)

        # Criando links de acordo com o mapa (em Gbps e Mbps)
        # Notação: bw = largura de banda (bandwidth)
        
        # 10 Gbps (19 links)
        self.addLink(s_porto_alegre, s_florianopolis, bw=10)
        self.addLink(s_porto_alegre, s_curitiba, bw=10)
        self.addLink(s_florianopolis, s_sao_paulo, bw=10)
        self.addLink(s_curitiba, s_sao_paulo, bw=10)
        self.addLink(s_sao_paulo, s_rio_janeiro, bw=10)
        self.addLink(s_sao_paulo, s_belo_horizonte, bw=10)
        self.addLink(s_rio_janeiro, s_vitoria, bw=10)
        self.addLink(s_rio_janeiro, s_brasilia, bw=10)
        self.addLink(s_vitoria, s_salvador, bw=10)
        self.addLink(s_belo_horizonte, s_brasilia, bw=10)
        self.addLink(s_belo_horizonte, s_salvador, bw=10)
        self.addLink(s_belo_horizonte, s_fortaleza, bw=10)
        self.addLink(s_salvador, s_aracaju, bw=10)
        self.addLink(s_aracaju, s_maceio, bw=10)       
        self.addLink(s_maceio, s_recife, bw=10)
        self.addLink(s_recife, s_campina_grande, bw=10)
        self.addLink(s_campina_grande, s_joao_pessoa, bw=10)
        self.addLink(s_joao_pessoa, s_natal, bw=10)
        self.addLink(s_natal, s_fortaleza, bw=10)
        
        # 3 Gbps (07 links)
        self.addLink(s_curitiba, s_campo_grande, bw=3)
        self.addLink(s_campo_grande, s_cuiaba, bw=3)
        self.addLink(s_goiania, s_brasilia, bw=3)
        self.addLink(s_goiania, s_cuiaba, bw=3)
        self.addLink(s_goiania, s_palmas, bw=3)
        self.addLink(s_cuiaba, s_porto_velho, bw=3)
        self.addLink(s_porto_velho, s_rio_branco, bw=3)

        # 200 Mbps (01 link)
        self.addLink(s_brasilia, s_manaus, bw=0.2)

        # 20 Mbps (02 links)
        self.addLink(s_brasilia, s_macapa, bw=0.02)
        self.addLink(s_brasilia, s_boa_vista, bw=0.02)

# Criando a rede e iniciando o controlador
def run():
    topo = RedeIpeRNPTopo()
    
    # Adicionando o r2q para ajustar o quantum dos links mais lentos
    net = Mininet(topo=topo, controller=RemoteController, link=TCLink, autoSetMacs=True, autoStaticArp=True)
    
    # Iniciar a rede
    net.start()
    
    # Abrir CLI para interagir com a rede
    CLI(net)
    
    # Parar a rede
    net.stop()

if __name__ == '__main__':
    run()
