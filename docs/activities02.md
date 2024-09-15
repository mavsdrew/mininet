# 02

Encerre a instância anterior do Mininet e crie uma rede mais complexa (por exemplo, uma árvore com profundidade 3 e fanout 2 – i.e., `mn --topo=tree,depth=3,fanout=2 --controller=remote`

Criação da rede através do comando `Default`:
```bash
mn --topo=tree,depth=3,fanout=2 --controller=default
```

1. Crie regras utilizando o comando ovs-ofctl para que os hosts possam estabelecer qualquer troca de dados. Descreva as regras instaladas.

    - Identificar os switches na rede: Execute o seguinte comando:
        ```bash
        net
        ```
    
    - Instalado as seguintes regras encaminhamento:
        ```bash
        sudo ovs-ofctl add-flow s1 in_port=1,actions=output:2
        ```
        ```bash
        sudo ovs-ofctl add-flow s1 in_port=2,actions=output:1
        ```

2. Execute, por no mínimo 10 segundos, o comando iperf entre dois host conectados a diferentes dispositivos de encaminhamento
    - Em um dos host execute `”iperf -s”` (host servidor). Escolhido o `h1` para executar o comando:
        ```bash
        h1 iperf -s
        ```
    - No outro host execute `”iperf -c ipHostServidor”`. Escolhido o host `h8` para executar o comando:
        ```bash
        h8 iperf -c 10.0.0.1
        ```

    - Excutado o `iperf` por no mínimo 10 segundos.
        ```bash
        h8 iperf -c 10.0.0.1 -t 10
        ```

3. Verifique qual é vazão obtida em cada host.

    - Após a execução do comando `iperf`, teremos a vazão em ambos os hosts (cliente e servidor).

    - No host servidor (`h1`), o resultado é :
        ```bash
        [  4]  0.0-10.0 sec   112 MBytes   94.0 Mbits/sec
        ```

    - No host cliente (`h8`), o resultado é semelhante e mostra a taxa de transferência (vazão) alcançada entre os dois hosts.
