# 01

Crie uma rede simples, com no mínimo dois hosts, usando o comando `mn` (por exemplo, `mn --controller remote`).    

Criação da rede através do comando:
```bash
mn --controller remote
```
Figura 01.

---

1. Execute o comando `ping` entre dois hosts dessa rede. Descreva o resultado.
    - Aparentemente o controlador não está ativo pois foi obtido como resposta `Destination Host Unreachable`.
    - Foi executado o comando `net`, demonstrando que a topologia foi criada corretamente e que os hosts (`h1` e `h2`) estão conectados ao switch (`s1`):
        ```bash
        mininet> net
        h1 h1-eth0:s1-eth1
        h2 h2-eth0:s1-eth2
        s1 lo:  s1-eth1:h1-eth0 s1-eth2:h2-eth0
        c0
        ```
    - Foi validado os endereços IP dos hosts (`h1` e `h2`) com o comando `ifconfig`, estando corretamente configurados (`10.0.0.1/8` e `10.0.0.2/8`):
        ```bash
        mininet> h1 ifconfig
        h1-eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.0.1  netmask 255.0.0.0  broadcast 10.255.255.255
        inet6 fe80::b034:74ff:fe10:9391  prefixlen 64  scopeid 0x20<link>
        ether b2:34:74:10:93:91  txqueuelen 1000  (Ethernet)
        RX packets 27  bytes 3164 (3.1 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 29  bytes 1622 (1.6 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

        lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Loopback Local)
        RX packets 17  bytes 1904 (1.9 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 17  bytes 1904 (1.9 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

        mininet> h2 ifconfig
        h2-eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.0.2  netmask 255.0.0.0  broadcast 10.255.255.255
        inet6 fe80::a8cb:aaff:fe54:95fb  prefixlen 64  scopeid 0x20<link>
        ether aa:cb:aa:54:95:fb  txqueuelen 1000  (Ethernet)
        RX packets 27  bytes 3164 (3.1 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 11  bytes 866 (866.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

        lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Loopback Local)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        ```

    - Existe a possibilidado do controlador não está ativo, e portanto, foi executado o comando `exit` e reiniciado a rede com o controlador padrão do Mininet através do comando:
        ```bash
        exit
        sudo mn --topo minimal --controller=default
        ```
        Figura 02.
    
    - Executado o comando `ping`:
        ```bash
        h1 ping h2
        ```
    
    - Obtido sucesso no comando.
        ```bash
        mininet> h1 ping h2
        PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
        64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=1.56 ms
        64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=0.163 ms
        64 bytes from 10.0.0.2: icmp_seq=3 ttl=64 time=0.037 ms
        64 bytes from 10.0.0.2: icmp_seq=4 ttl=64 time=0.036 ms
        ```

    Figura 03.
---

2. Crie regras utilizando o comando `ovs-ofctl` para que os hosts possam estabelecer qualquer troca de dados. Descreva as regras instaladas.

    - Abra uma nova janela do `Terminal` para que esteja fora da interface do Mininet. Crie as seguintes regras:
        ```bash
        sudo ovs-ofctl add-flow s1 in_port=1,actions=output:2
        sudo ovs-ofctl add-flow s1 in_port=2,actions=output:1
        ````
    
    - Explicação das regras:
        - `ovs-ofctl`: Comando para manipular switches Open vSwitch.
        - `add-flow`: Adiciona uma regra de fluxo ao switch.
        - `in_port`: Define a porta de entrada.
        - `actions=output:<porta>`: Define a porta de saída para encaminhar os pacotes.
        
    - Resumo das regras:
        - A primeira regra define que todo tráfego que entra pela porta 1 (`h1`) será encaminhado para a porta 2 (`h2`).
        - A segunda regra faz o inverso, encaminhando o tráfego de `h2` (porta 2) para `h1` (porta 1).

    - Retornemos à interface do Mininet e testamos novamente com o comando `ping` entre os hosts (`h1` e `h2`):
        ```bash
        h1 ping h2
        ```
    
    - Verificamos as regras de fluxo instaladas:
        ```bash
        sudo ovs-ofctl dump-flows s1
        ```
    
    - Exibição das regras que foram aplicadas ao switch:  
    Figura 4.

3. Após, faça com que o switch por onde passam os pacotes altere o endereço MAC de origem dos pacotes de resposta do comando `ping` (i.e., `ICMP reply`). Descreva as regras instaladas.

    - Instalado uma regra no switch `s1` para modificar o endereço MAC de origem dos pacotes de resposta do ping (`ICMP reply`):
        ```bash
        sudo ovs-ofctl add-flow s1 in_port=2,icmp,actions=mod_dl_src:aa:bb:cc:dd:ee:ff,output:1
        ```

    - Explicação: Essa regra define que todo o tráfego ICMP que chega à porta 2 (`h2`) terá seu endereço MAC de origem modificado para `aa:bb:cc:dd:ee:ff` antes de ser encaminhado para a porta 1 (`h1`).

4. Verifique, usando o software `wireshark`, que o switch está, de fato, alterando os pacotes. Ilustre o resultado.

    - Instale o Wireshark:
        ```bash
        sudo apt install wireshark
        ```

    - Inicie o Wireshark com o seu usuário (não sendo o `root`):
        ```bash
        wireshark &
        ```
    
    - Reconfigure o `wireshark` para permitir captura de pacotes para usuários não root através do comando abaixo (aceite `Sim` para as perguntas):
        ```bash
        sudo dpkg-reconfigure wireshark-common
        ```
    
    - Adicione seu usuário ao grupo `wireshark`. Substitua `{your username}` pelo seu nome de usuário no sistema (você pode verificar com `whoami`).
        ```bash
        sudo usermod -aG wireshark $(whoami)
        ```
    
    - Reinicie o sistema.

    - Caso tenha problemas, realize os seguintes passos. Remova as regras existentes:
        ```bash
        sudo ovs-ofctl del-flows s1
        ```
    
    - Adicione a regra de modificação de endereço MAC para pacotes que entram pela porta 2 (interface s1-eth2):
        ```bash
        sudo ovs-ofctl add-flow s1 priority=32768,in_port=2,icmp,actions=mod_dl_src:aa:bb:cc:dd:ee:ff,output:1
        ```

    - Reaplique as regras de encaminhamento para garantir a comunicação entre os hosts:
        ```bash
        sudo ovs-ofctl add-flow s1 priority=100,in_port=1,actions=output:2
        sudo ovs-ofctl add-flow s1 priority=100,in_port=2,actions=output:1
        ```

    Figura 05.
    Figura 06.


5. O comando `ping` continua funcionando normalmente?
6. Apague a regra criada anteriormente. Crie, agora, uma regra que altere o endereço MAC de destino dos pacotes de resposta.
7. Verifique, usando o software `wireshark`, que o switch está, de fato, alterando os pacotes.
8. O comando `ping` continua funcionando normalmente?