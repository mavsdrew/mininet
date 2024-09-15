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
    - Regras de Encaminhamento para Topologia de Árvore (Profundidade 3, Fanout 2): A topologia é organizada da seguinte forma:

                     s1
                 /        \
               s2         s3
             /   \       /  \
            s4    s5    s6   s7
           / \   / \   / \   / \
          h1 h2 h3 h4 h5 h6 h7 h8


    - Os **switches** estão organizados em três níveis. O **switch raiz (`s1`)** se conecta a **switches intermediários (`s2` e `s3`)**, que por sua vez se conectam a **switches folha** (`s4`, `s5`, `s6`, e `s7`). Cada switch de nível folha se conecta a dois hosts.
    
    1. Regras para o Switch `s1` (Switch Raiz): O switch `s1` conecta-se aos switches `s2` e `s3`. As regras de encaminhamento permitem o tráfego entre `s2` e `s3`.
        ```bash
        # Regras de s1
        sudo ovs-ofctl add-flow s1 in_port=1,actions=output:2  # De s2 para s3
        sudo ovs-ofctl add-flow s1 in_port=2,actions=output:1  # De s3 para s2
        ```

    2. Regras para o Switch `s2` (Switch Intermediário): O switch `s2` conecta `s1` a `s4` e `s5`, que por sua vez conectam aos hosts `h1`, `h2`, `h3`, e `h4`.
        ```bash
        # Regras de s2
        sudo ovs-ofctl add-flow s2 in_port=1,actions=output:2  # De s1 para s4
        sudo ovs-ofctl add-flow s2 in_port=2,actions=output:1  # De s4 para s1
        sudo ovs-ofctl add-flow s2 in_port=1,actions=output:3  # De s1 para s5
        sudo ovs-ofctl add-flow s2 in_port=3,actions=output:1  # De s5 para s1
        ```

    3. Regras para o Switch `s3` (Switch Intermediário): O switch `s3` conecta `s1` a `s6` e `s7`, que por sua vez conectam aos hosts `h5`, `h6`, `h7`, e `h8`.
        ```bash
        # Regras de s3
        sudo ovs-ofctl add-flow s3 in_port=1,actions=output:2  # De s1 para s6
        sudo ovs-ofctl add-flow s3 in_port=2,actions=output:1  # De s6 para s1
        sudo ovs-ofctl add-flow s3 in_port=1,actions=output:3  # De s1 para s7
        sudo ovs-ofctl add-flow s3 in_port=3,actions=output:1  # De s7 para s1

        ```

    4. Regras para o Switch `s4` (Switch de Nível Folha): O switch `s4` conecta `s2` aos hosts `h1` e `h2`.
        ```bash
        # Regras de s4
        sudo ovs-ofctl add-flow s4 in_port=1,actions=output:2  # De s2 para h1
        sudo ovs-ofctl add-flow s4 in_port=2,actions=output:1  # De h1 para s2
        sudo ovs-ofctl add-flow s4 in_port=1,actions=output:3  # De s2 para h2
        sudo ovs-ofctl add-flow s4 in_port=3,actions=output:1  # De h2 para s2

        ```

    5. Regras para o Switch `s5` (Switch de Nível Folha): O switch `s5` conecta `s2` aos hosts `h3` e `h4`.
        ```bash
        # Regras de s5
        sudo ovs-ofctl add-flow s5 in_port=1,actions=output:2  # De s2 para h3
        sudo ovs-ofctl add-flow s5 in_port=2,actions=output:1  # De h3 para s2
        sudo ovs-ofctl add-flow s5 in_port=1,actions=output:3  # De s2 para h4
        sudo ovs-ofctl add-flow s5 in_port=3,actions=output:1  # De h4 para s2
        ```

    6. Regras para o Switch `s6` (Switch de Nível Folha): O switch `s6` conecta `s3` aos hosts `h5` e `h6`.
        ```bash
        # Regras de s6
        sudo ovs-ofctl add-flow s6 in_port=1,actions=output:2  # De s3 para h5
        sudo ovs-ofctl add-flow s6 in_port=2,actions=output:1  # De h5 para s3
        sudo ovs-ofctl add-flow s6 in_port=1,actions=output:3  # De s3 para h6
        sudo ovs-ofctl add-flow s6 in_port=3,actions=output:1  # De h6 para s3
        ```

    7. Regras para o Switch `s7` (Switch de Nível Folha): O switch `s7` conecta `s3` aos hosts `h7` e `h8`.
        ```bash
        # Regras de s7
        sudo ovs-ofctl add-flow s7 in_port=1,actions=output:2  # De s3 para h7
        sudo ovs-ofctl add-flow s7 in_port=2,actions=output:1  # De h7 para s3
        sudo ovs-ofctl add-flow s7 in_port=1,actions=output:3  # De s3 para h8
        sudo ovs-ofctl add-flow s7 in_port=3,actions=output:1  # De h8 para s3
        ```

    - Todas as regras de encaminhamento:
        ```bash
        sudo ovs-ofctl add-flow s1 in_port=1,actions=output:2  # De s2 para s3
        sudo ovs-ofctl add-flow s1 in_port=2,actions=output:1  # De s3 para s2
        sudo ovs-ofctl add-flow s2 in_port=1,actions=output:2  # De s1 para s4
        sudo ovs-ofctl add-flow s2 in_port=2,actions=output:1  # De s4 para s1
        sudo ovs-ofctl add-flow s2 in_port=1,actions=output:3  # De s1 para s5
        sudo ovs-ofctl add-flow s2 in_port=3,actions=output:1  # De s5 para s1
        sudo ovs-ofctl add-flow s3 in_port=1,actions=output:2  # De s1 para s6
        sudo ovs-ofctl add-flow s3 in_port=2,actions=output:1  # De s6 para s1
        sudo ovs-ofctl add-flow s3 in_port=1,actions=output:3  # De s1 para s7
        sudo ovs-ofctl add-flow s3 in_port=3,actions=output:1  # De s7 para s1
        sudo ovs-ofctl add-flow s4 in_port=1,actions=output:2  # De s2 para h1
        sudo ovs-ofctl add-flow s4 in_port=2,actions=output:1  # De h1 para s2
        sudo ovs-ofctl add-flow s4 in_port=1,actions=output:3  # De s2 para h2
        sudo ovs-ofctl add-flow s4 in_port=3,actions=output:1  # De h2 para s2
        sudo ovs-ofctl add-flow s5 in_port=1,actions=output:2  # De s2 para h3
        sudo ovs-ofctl add-flow s5 in_port=2,actions=output:1  # De h3 para s2
        sudo ovs-ofctl add-flow s5 in_port=1,actions=output:3  # De s2 para h4
        sudo ovs-ofctl add-flow s5 in_port=3,actions=output:1  # De h4 para s2
        sudo ovs-ofctl add-flow s6 in_port=1,actions=output:2  # De s3 para h5
        sudo ovs-ofctl add-flow s6 in_port=2,actions=output:1  # De h5 para s3
        sudo ovs-ofctl add-flow s6 in_port=1,actions=output:3  # De s3 para h6
        sudo ovs-ofctl add-flow s6 in_port=3,actions=output:1  # De h6 para s3
        sudo ovs-ofctl add-flow s7 in_port=1,actions=output:2  # De s3 para h7
        sudo ovs-ofctl add-flow s7 in_port=2,actions=output:1  # De h7 para s3
        sudo ovs-ofctl add-flow s7 in_port=1,actions=output:3  # De s3 para h8
        sudo ovs-ofctl add-flow s7 in_port=3,actions=output:1  # De h8 para s3
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
