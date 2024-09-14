# Configuração do Ambiente com VirtualBox e Ubuntu

Ir para a [Home](https://github.com/mavsdrew/mininet) do projeto.

- [Download](https://github.com/mavsdrew/mininet/blob/main/docs/environment.md#download)
- [Microsoft Visual Studio C++](https://github.com/mavsdrew/mininet/blob/main/docs/environment.md#microsoft-visual-studio-C++)
- [VirtualBox e Pacote de Extensão](https://github.com/mavsdrew/mininet/blob/main/docs/environment.md#virtualbox-e-pacote-de-extensão)
- [Ubuntu Desktop 22.04 LTS](https://github.com/mavsdrew/mininet/blob/main/docs/environment.md#ubuntu-desktop-22.04-lts)
    - [Configuração mínima](https://github.com/mavsdrew/mininet/blob/main/docs/environment.md#configuração-mínima)
    - [Configuração adotada (recomendada)](https://github.com/mavsdrew/mininet/blob/main/docs/environment.md#configuração-adotada-(recomendada))
    - [Instalação Ubuntu](https://github.com/mavsdrew/mininet/blob/main/docs/environment.md#configuração-adotada-(recomendada))
    - [Instalação do CD dos Adicionais para Convidado](https://github.com/mavsdrew/mininet/blob/main/docs/environment.md#configuração-adotada-(recomendada))
    - [Atualização do Ubuntu](https://github.com/mavsdrew/mininet/blob/main/docs/environment.md#configuração-adotada-(recomendada))
    
Nesta seção, descreveremos como configurar um ambiente de virtualização usando o [VirtualBox](https://www.virtualbox.org/) e a imagem do [Ubuntu Desktop](https://ubuntu.com/).

## Download

Certifique-se de realizar o download dos seguintes itens (com as versões indicadas) antes de prosseguir:

- Microsoft Visual Studio C++: [Download Microsoft Visual Studio C++ 2015-2022 Redistributable (x64) - 14.40.33810](https://aka.ms/vs/17/release/vc_redist.x64.exe)
- VirtualBox: [Download VirtualBox 7.0.20](https://download.virtualbox.org/virtualbox/7.0.20/VirtualBox-7.0.20-163906-Win.exe)
- Pacote de Extensão do VirtualBox: [Download Extension Pack 7.0.20](https://download.virtualbox.org/virtualbox/7.0.20/Oracle_VM_VirtualBox_Extension_Pack-7.0.20.vbox-extpack)
- Imagem do Ubuntu Desktop: [Download Ubuntu Desktop 22.04.4 LTS](https://ubuntu.com/download/desktop/thank-you?version=22.04.4&architecture=amd64&lts=true)

## Instalação e Configuração

### Microsoft Visual Studio C++:

- Caso esteja executando um host Windows, instale o Microsoft Visual Studio C++. Após a instalação, reincie o host.
    
### VirtualBox e Pacote de Extensão:

- Realize a instalação padrão do VirtualBox.
- Instale o Pacote de Extensão através do VirtualBox:
    - No VirtualBox, vá em **Arquivo -> Ferramentas -> Gerenciador de Pacotes de Extensão** e selecione o pacote baixado para instalar.


### Ubuntu Desktop 22.04 LTS:
    
#### Configuração mínima:

- Sistema Operacional Host: `Qualquer sistema com suporte ao VirtualBox`.
- Sistema Operacional da VM: `Ubuntu 22.04 LTS`.
- Memória RAM da VM: Pelo menos `2 GB`.
- Disco da VM: `10 GB ou mais de armazenamento.`

#### Configuração adotada (recomendada):

- Criação de uma nova VM:
    - Nome: `mininet`
    - Tipo: `Linux`
    - Versão: `Ubuntu 22.04 LTS (Jammy Jellyfish) (64-bit)`
    - Memória Base (RAM): `8 GB`
    - Processador (Núcleos): `2 CPU`
    - Disco: 50 GB

- Configuração adicional da VM:
    - Área de Tranferência Compartilhada: `Hospedeiro para Convidado`
    - Arrastar e Soltar: `Desabilitado`
    - Aceleração 3D: `Habilitado`
    - Rede: `NAT`

---

#### Instalação do Ubuntu:
- Idioma: `Português do Brasil`.
- Layout do Teclado: `Portuguese (Brazil)`.
- Tipo de Instalação: Selecione a `Instalação Normal` e marque a opção para baixar atualizações durante a instalação e instalar software de terceiros (como drivers gráficos).
- Particionamento do Disco: Escolha a opção `Apagar disco e reinstalar o Ubuntu`.
- Fuso Horário: Defina como `São Paulo`.
- Criar um Usuário: Insira suas informações de usuário e senha.
- Iniciar a instalação: Ao finalizar a instalação, o instalador solicitará que você reinicie o sistema.

---

#### Instalação do CD dos Adicionais para Convidado:
- A instalação dos **Adicionais para Convidado** permitirá:
    - O redimensionamento automático da tela.
    - O compartilhamento de arquivos entre o sistema host e a VM.
    - Melhor suporte para aceleração gráfica.

##### Passo 1: Instalar Dependências

No terminal (`Ctrl + Alt + T`), instale as dependências necessárias para compilar os módulos de kernel:

```bash
sudo apt install build-essential dkms linux-headers-$(uname -r)
```

##### Passo 2: Executar o Script de Instalação

1. Monte o CD dos Adicionais para Convidado em sua VM no VirtualBox (vá em **Dispositivos > Inserir Imagem de CD dos Adicionais para Convidado**).

2. Em seguida, no terminal, execute:

```bash
cd /media/username
sudo ./VBox_GAs_7.0.20/VBoxLinuxAdditions.run
```
_Nota: Substitua `username` pelo nome de usuário da sua máquina._

##### Passo 3: Reiniciar a VM

Reinicie o sistema para aplicar as mudanças:
```bash
sudo reboot
```

---

#### Atualização do Ubuntu

Após a instalação, é recomendável atualizar o sistema para garantir que você tenha as últimas correções de segurança e melhorias:

```bash
sudo apt update
sudo apt upgrade -y
```
