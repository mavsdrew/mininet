# Mininet

Ir para a [Home](https://github.com/mavsdrew/mininet) do projeto.

- [Preparando o ambiente](https://github.com/mavsdrew/mininet/blob/main/docs/mininet.md#preparando-o-ambiente)
- [Instalação](https://github.com/mavsdrew/mininet/blob/main/docs/mininet.md#instala%C3%A7%C3%A3o)
- [Verificação da Instalação](https://github.com/mavsdrew/mininet/blob/main/docs/mininet.md#verifica%C3%A7%C3%A3o-da-instala%C3%A7%C3%A3o)

Nesta seção, descreveremos como preparar o ambiente, instalar e verificar a instalação do Mininet.

# Preparando o ambiente

Antes de instalar o Mininet, é necessário garantir que seu sistema esteja pronto, instalando alguns pacotes essenciais para a compilação e o funcionamento do Mininet. No terminal, execute o seguinte comando:

```bash
sudo apt install -y git build-essential
```

Esses pacotes incluem o `git` para clonar o repositório do Mininet, além de ferramentas de compilação (`build-essential`).

# Instalação

1. **Instale o Git**: Execute o comando abaixo para instalar o Git e validar a sua versão:

    ```bash
    sudo apt install git -y
    git --version
    ```

2. **Clone o repositório oficial do Mininet**: Execute o comando abaixo para clonar o repositório do Mininet no GitHub:

    ```bash
    git clone https://github.com/mininet/mininet
    ```

3. **Entre no diretório do Mininet clonado**: Navegue até o diretório clonado com o seguinte comando:

    ```bash
    cd mininet
    ```

4. **Execute o script de instalação completa**: O script de instalação completa vai configurar o Mininet com todos os pacotes necessários. Execute o comando abaixo:

    ```bash
    sudo ./util/install.sh -a
    ```

# Verificação da Instalação

Após a instalação, é importante verificar se o Mininet foi instalado corretamente e está funcionando. Para isso, execute o seguinte comando para rodar um teste básico:

```bash
sudo mn --test pingall
```

Esse comando cria uma rede simples e verifica se os hosts conseguem se comunicar via ping. O resultado esperado é algo semelhante a isto:

O teste cria uma rede simples e verifica se os hosts conseguem se comunicar via ping. O resultado esperado é:

```bash
*** Ping: testing ping reachability
h1 -> h2
h2 -> h1
*** Results: 0% dropped (2/2 received)
```

Se esse resultado for obtido, significa que o Mininet está funcionando corretamente e sua instalação foi bem-sucedida.
