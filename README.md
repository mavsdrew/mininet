# Mininet

O **Mininet** é uma ferramenta poderosa para a emulação de redes e é amplamente utilizada em pesquisas e experimentos com **Redes Definidas por Software (SDN)**.

Este repositório contém um tutorial detalhado para a instalação do **Mininet** em uma máquina virtual (VM) rodando **[Ubuntu](https://ubuntu.com/)** no **[VirtualBox](https://www.virtualbox.org/)**.

Aqui você encontrará um passo a passo com todos os comandos necessários para realizar a instalação e verificação de funcionamento do **Mininet**, além de exemplos de topologias e integração com **OpenFlow**.

# Configuração do Ambiente com VirtualBox e Ubuntu

Nesta seção, descreveremos como configurar um ambiente de virtualização usando o **[VirtualBox](https://www.virtualbox.org/)** e a imagem do **[Ubuntu Desktop](https://ubuntu.com/)**.

## Download

Certifique-se de realizar o download dos seguintes itens (versões relacionadas) antes de prosseguir:

- Microsoft Visual Studio C++: **[Download Microsoft Visual Studio C++ 2015-2022 Redistributable (x64) - 14.40.33810](https://aka.ms/vs/17/release/vc_redist.x64.exe)**
- VirtualBox: **[Download VirtualBox 7.0.20](https://download.virtualbox.org/virtualbox/7.0.20/VirtualBox-7.0.20-163906-Win.exe)**
- Pacote de Extensão do VirtualBox: **[Download Extension Pack 7.0.20](https://download.virtualbox.org/virtualbox/7.0.20/Oracle_VM_VirtualBox_Extension_Pack-7.0.20.vbox-extpack)**
- Imagem do Ubuntu Desktop: **[Download Ubuntu Desktop 22.04.4 LTS](https://ubuntu.com/download/desktop/thank-you?version=22.04.4&architecture=amd64&lts=true)**

## Instalação e Configuração

### **Microsoft Visual Studio C++:**

- Caso esteja executando um host Windows, instale o Microsoft Visual Studio C++. Após a instalação, reincie o host.
    
### **VirtualBox e Pacote de Extensão:**

- Realize a instalação padrão do VirtualBox.
- Instale o Pacote de Extensão através do VirtualBox:

    ```bash
    Arquivo -> Ferramentas -> Gerenciador de Pacotes de Extensão: Instalar.
    ```

### **Ubuntu Desktop 22.04 LTS:**
    
#### Configuração mínima:

- Sistema Operacional Host: `Qualquer sistema com suporte ao VirtualBox`.
- Sistema Operacional da VM: `Ubuntu 22.04 LTS`.
- Memória RAM da VM: Pelo menos `2 GB`.
- Disco da VM: `10 GB ou mais de armazenamento.`

#### Configuração adotada:

- Criação de uma nova VM:
    - **Nome**: `mininet`
    - **Tipo**: `Linux`
    - **Versão**: `Ubuntu 22.04 LTS (Jammy Jellyfish) (64-bit)`
    - **Memória Base (RAM)**: `8 GB`
    - **Processador (Núcleos)**: `2 CPU`
    - **Disco**: 50 GB

- Configuração da VM:
    - **Arrastar e Soltar**: `Desabilitado`
    - **Aceleração 3D**: `Habilitado`
    - **Rede**: `NAT`
    
#### Instalação do Ubuntu:
- **Idioma**: `Português do Brasil`
- **Layout do Teclado**: `Portuguese (Brazil)`
- **Tipo de Instalação**: `Instalação Normal` - marque a opção para baixar atualizações durante a instalação e instalar software de terceiros (como drivers gráficos).
- **Particionamento do Disco**: `Apagar disco e reinstalar o Ubuntu`
- **Fuso Horário**: `São Paulo`
- **Criar um Usuário**: Insira seus dados.
- **Iniciar a instalação**: Quando a instalação estiver concluída, o instalador solicitará que você reinicie o sistema.

#### Instalação do CD dos Adicionais para Convidado:
- A instalação permitirá:
    - O redimensionamento automático da tela.
    - O compartilhamento de arquivos entre o sistema host e a VM.
    - Melhor suporte para aceleração gráfica.

- Para isso, instale algumas dependências e demais procedimentos através da execução de comandos pelo terminal (`Ctrl + Alt + T`):

    ```bash
    sudo apt install build-essential dkms linux-headers-$(uname -r)
    ```

- **Executar Script**:

    ```bash
    cd /media/username
    sudo ./VBox_GAs_7.0.20/VBoxLinuxAdditions.run
    ```

- **Reiniciar**:

    ```bash
    sudo reboot
    ```

- **Atualização do Ubuntu**: Após a instalação, atualize o sistema.

    ```bash
    sudo apt update
    sudo apt upgrade -y
    ```

## Mininet - Preparando o ambiente

Instale pacotes essenciais para a compilação e o funcionamento do Mininet:

    ```bash
    sudo apt install -y git build-essential
    ```

## Mininet - Instalação

1. Clone o repositório oficial do Mininet:

    ```bash
    git clone https://github.com/mininet/mininet
    ```

2. Entre no diretório do Mininet clonado:

    ```bash
    cd mininet
    ```

3. Execute o script de instalação completa (o parâmetro `-a` garante que todos os pacotes recomendados sejam instalados):

    ```bash
    sudo ./util/install.sh -a
    ```

## Mininet - Verificação da Instalação

Após a instalação, verifique se o Mininet está funcionando corretamente com o seguinte comando:

bash
Copiar código
sudo mn --test pingall
O teste cria uma rede simples e verifica se os hosts conseguem se comunicar via ping. O resultado esperado é:

bash
Copiar código
*** Ping: testing ping reachability
h1 -> h2
h2 -> h1
*** Results: 0% dropped (2/2 received)