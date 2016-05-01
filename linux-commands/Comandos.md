DICAS PARA COMANDOS LINUX
=========================


Disk/Files
----------

#Editar Tabelas de Partição
sudo vim /etc/fstab

#Ver partições em /
sudo fdisk -l

#Ver partições em dispositivo (ex. /dev/sda)
sudo lsblk /dev/sda

#Ver partições montadas
df -Th

#Ver tamanho de arquivo
du -sh

#Montar Partição/Pendrive (Se pasta estiver cheia ele esconde os arquivos até desmontar o dispositivo)
sudo mkdir /mnt/pendrive
sudo mount -t vfat /dev/sdb1 /mnt/pendrive/

#Desmontar Partição/Pendrive
sudo umount /dev/sdb1
sudo umount /mnt/pendrive

#Formatar Pendrive[Ex: sdb (Dispositivo), sdb1 (Primeira partição do dispositivo)]
#Obs:Desmontar primeiro
mkfs.vfat -n "LABEL" -F 32 /dev/sdb1

#Formatar Partição
mkfs.ext4 /dev/sdaX

#Criar imagem iso a partir de um cd [Copia direto do device para um arquivo]
dd if=/dev/sr0 of=/my/dir/image.iso

#Montar arquivo de imagem como file system [Dispositivo de loopback (falso block device)]
mount -o loop image.iso /my/dir

#Gravar Distro no pendrive[Ex: Arch Linux - Copiar para sdb (dispositivo) ]
#Formatar primeiro
sudo dd if=/home/guilherme/Desktop/pendrive/archlinux-2015.04.01-dual.iso of=/dev/sdb bs=8M

#Gravar Iso em disco
cdrecord -v -f=16m speed=16 dev=/dev/hdc -data nomedaiso.iso



Kernel
-----------------

#Limpar memória cache
echo 3 > /proc/sys/vm/drop_caches

#Ver módulos
lsmod

#Adicionar módulo *
insmod *.ko

#remover módulo
rmmod *

#Ver info Hardware
cat /proc/meminfo
free -m
lscpu
lspci
lshw


ANDROID
--------------

#Habilitar Galaxy no Android (Ubuntu)
#Criar regra no udev
chmod a+r /etc/udev/rules.d/51-android.rules

#Indicar na regra: 
SUBSYSTEM=="usb", ATTR{idVendor}=="04e8", ATTRS{idProduct}==”6860″, MODE="0666", GROUP="plugdev"

#Ver Produto ID: 
lsusb

MAC ADDRESS Galaxy S2 lite
bc851fd9e96e


Modelo INITD LINUX
------------------

RunLevel - Utilizar update-rc.d
rc0.d = Desliga
rc1.d = Inicialização mínima
rc2.d - rc5.d = MultiUsuário 

-> Pasta rcX.d contém links simbólicos para executar serviços em init.d
- SXXscript (O XX serviço a ser iniciado) - $1 = start
- KXXscript (O XX serviço a ser encerrado) - $1 = stop

#Ver runlevel default
cat /etc/init/rc-sysinit.conf (Ubuntu)
cat /etc/inittab (Fedora)


APT-GET (Ordenação Topológica + dpkg)
-------------------------------------

#Lista dos repositórios oficiais [deb(pacotes debian) link-repositório precise(nome-distro) main universe(diretorios) ]
cat /etc/apt/sources.list

#Lista de PPA
cat /etc/apt/sources.list.d

#Adicionar repositório extra (p.e. SVN)
sudo echo -e "deb http://ppa.launchpad.net/svn/ppa/ubuntu precise main\ndeb-src http://ppa.launchpad.net/svn/ppa/ubuntu precise main" > svn.list

#Adicionar Chave para svn
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EAA903E3A2F4C039

#Adicionar PPA *
add-apt-repository ppa:*

#Corrigir pacotes quebrados
apt-get update ou aptitude update
dpkg --configure -a
apt-get -f install

#Instalar pacote dpkg *
dkpg -i *

#Verificar se pacote está instalado
dpkg -s <PACOTE>

#Verificar todos os pacotes instalados
dpkg --get-selections

#Ver opções para instalação de um determinado pacote
apt-cache policy <PACOTE>


CRON
----

#Criar/Editar crontab
crontab -l
crontab -e


BLUETOOTH
---------

#Ver bluetooth devices
hciconfig

#Configurar nome 
sudo hciconfig hci0 name "guilherme-ubuntu"

#scannear rede
hcitool scan

#criar porta serial para rfcomm
mknod --mode=666 /dev/rfcomm0 c 216 0

#conectar com device (hci0 em canal 1)
rfcomm connect 0 <ADDRESS> 1

#ver canais disponíveis no cel
sdptool records <ADDRESS>
sdptool browse <ADDRESS>

#Arch linux - Instalar bluez e bluez-utils [hcitools, etc.]
# usar serviço em systemd
systemctl start bluetooth.service


TOMCAT
------

#Modo debug
./bin/catalina.sh jpda start
tailf logs/catalina.out


JAVA
----

#Trocat JVM default
sudo update-alternatives --config java

#Ajustar layout dos applets no arch linux
#Adicionar linha em arquivo /etc/profile.d/jre.sh
export _JAVA_OPTIONS='-Dawt.useSystemAAFontSettings=on -Dswing.aatext=true -Dswing.defaultlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel'

GREP
----

Utilizando OU
ls /etc/rc* | grep 'apache\|rc[0-9]'

Utilizando AND
ls /etc/rc* | grep 'K.*apache\|rc[0-9]'


ABNTEX2
-------

#Remover versão texlive anterior (Caso esteja instalada)
sudo apt-get purge texlive*
rm -rf /usr/local/texlive/2012 and rm -rf ~/.texlive2012
rm -rf /usr/local/share/texmf
rm -rf /var/lib/texmf
rm -rf /etc/texmf
sudo apt-get remove tex-common --purge
rm -rf ~/.texlive

1.	Instalar Tex
Adicionar repositório Ubuntu 13.10 (Usar aptpinning com prioridade negativa para não permitir pacotes saucy)
Criar arquivo /etc/apt/preferences

adicionar repositório em sources.list
echo "deb http://br.archive.ubuntu.com/ubuntu/ saucy main universe" >> /etc/apt/sources.list

sudo apt-get update && sudo apt-get install -y -t saucy texlive-full

2.	Instalar abntex2
Adicionar repositório abntex2
echo "deb http://distrib.abntex2.googlecode.com/hg/debian/ testing main" >> /etc/apt/sources.list 

Adicionar chave gpg
wget -O - http://distrib.abntex2.googlecode.com/hg/debian/89C55467.asc | sudo apt-key add - 

sudo apt-get update && sudo apt-get install abntex2

Converter imagens para eps
convert *.png -set filename:fname '%t' +adjoin '%[filename:fname].eps'


POSTGRESQL
----------

#Instalar Postgresql
yum install postgresql-server

#Alterar postgresql.conf - Descomentar linhas:
listen_addresses = 'localhost'
port = 5432

#Alterar pg_hba.conf - Verificar se método de autenticação é o md5:
# IPv4 local connections:
host    all             all             127.0.0.1/32            md5

#Alterar password do usuário postgres
su postgres
psql
alter user postgres with password 'root';

#Utilizar psql
psql -h localhost -U postgres -W database


Ubuntu
----------------------

#Alterar Nome de Desktop no ubuntu
vim ~/.config/user-dirs.dirs

#Corrigir bug do mouse
sudo modprobe -r psmouse
sudo modprobe psmouse proto=imps


SUPER USUARIO
-------------

#Editar arquivo /etc/sudoers
visudo

#incluir linha
<USERNAME> ALL=(ALL) ALL


RSYNC
-----

#Copiar arquivos de um computador para outro usando ssh e ignorando repetidos
rsync -avz -e "ssh -p 10122" user@server:/dir/ dir/

* Obs: Deve ser adicionada barra ao fim do nome do diretório, se não criará um diretório dir/dir

-C = Ignora uma lista de arquivos especificados na regra da flag --filter
-u = copia apenas novos arquivos ou arquivos modificados
--ignore-existing = copia apenas novos arquivos, ignorando os que existem com mesmo nome
-r = recursive
-a = Mantém permissões dos diretórios
-v = verbose imprimindo informações de execução
-z = transfere compactando arquivos
-e = indicar parametros do SSH


FONTES
------

#Configurar teclado e fonte. Arquivo /etc/vconsole.conf mantém configurações
loadkeys br-abnt2
setfont Lat2-Terminus16

#Ver status da fonte atual
localectl status

#Arquivo /etc/locale.conf mantém variável LANG
#Gerar idiomas usados pela glibc e localizados em /etc/locale-gen
locale-gen


GRUB2
-----

#Instalar grub e módulo para reconhecer outros SOs
pacman -S grub os-prober

#Instalar GRUB2 em arch linux sem sobrescrever MBR (Partição de boot = sda5)
grub-install --target=i386-pc --grub-setup=/bin/true --recheck --debug /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg


SSH
---

#Instalar pacote ssh
pacman -S openssh

#Editar arquivo /etc/ssh/sshd_config

# Aceitar conexões de IPs remotos na porta 10122, e liberar utilização do X11
Port 10122
ListenAddress 0.0.0.0
X11Forwarding yes

#Não permitir Logar como Root
PermitRootLogin no

#Para permitir autenticação apenascom chaves
PasswordAuthentication no
ChallengeResponseAuthentication no

#Iniciar/Habilitar no boot
systemctl start sshd.service
systemctl enable sshd.service


Multicast
---------

#habilitar nat no kernel
modprobe ip_tables
modprobe iptables_nat

#remover nat
modprobe -r iptables_nat

#Liberar roteador
echo 1 > /proc/sys/net/ipv4/ip_forward

Desabilitar ipv6 - cat /proc/sys/net/ipv6/conf/all/disable_ipv6 (0=Habilitado)
adicionar linhas em /etc/sysctl.conf
# IPv6
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1

#Nat - eth0 ligada a internet (Atualiza tabela NAT, onde todos os IPs que saem de eth0 são mascarados)
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

#Liberar Multicast
ifconfig eth0 multicast

#Ver se o Kernel suporta multicast
grep IP_MROUTE /boot/config-3.2.0-45-generic

#Rota para multicast
route add -net 224.0.0.0 netmask 240.0.0.0 dev eth0

#Tabela de rotas
netstat -nr
netstat -g

#Ver Portas
netstat -an
netstat -tulnap

-l = portas em "listening"
-t = portas TCP
-u = portas UDP
-a = todos os sockets
-n = usar números ao invés de nomes

#Olhar pid dos processos que utilizam determinada porta (matá-los para liberar)
sudo fuser port/tcp

#Configurar Rede com rotas (Configurar ip para gateway jogar na Internet)
ifconfig eth0 192.168.0.10 netmask 255.255.255.0
route add -net 0.0.0.0 netmask 0.0.0.0 gw 192.168.0.1 eth0


WIRELESS
--------

#Instalando pacotes necessários [iw ou wireless_tools]
pacman -S iw
pacman -S wireless_tools

#Instalando pacote necessário para autenticar rede com segurança WPA
pacman -S wpa_supplicant

#Ativar interface de rede
ifconfig wlp2s0 up
ip link set wlp2s0 up

#Listar redes disponíveis
iwlist wlp2s0 scan
iw dev wlp2s0 scan

Obs:
Signal Level: [-100 - 0] - Quanto mais próximo de zero melhor o sinal
ESSID: Nome da rede

# Informação de uma interface
iw dev wlp2s0 link

#Conectar a uma rede sem segurança
iwconfig wlp2s0 essid <ESSID>
iw dev wlp2s0 connect <ESSID>

#Conectar a uma rede com segurança WEP
iwconfig wlp2s0 essid <ESSID> key s:<SENHA>
iw dev wlp2s0 connect <ESSID> key 0:<SENHA>

#Gerar uma PSK (pre shared key) usada no protocolo WAP
wpa_passphrase "<ESSID>" "<SENHA>"

#Conectar a uma rede com segurança WPA
wpa_supplicant -B -i wlp2s0 -c <(wpa_passphrase "<ESSID>" "<SENHA>")

Obs:
-B = rodar em background
-i = interface de rede
-c = arquivo de configuração com os parametros da rede (ESSID e PSK)

Obs: Um arquivo .conf pode ter um ou mais blocos com configurações de rede válida.
     wpa_supplicant seleciona a rede de acordo com a prioridade
       1) Ordem do bloco dentro do arquivo
       2) Nível de segurança (WPA2 - WPA)
       3) Qualidade do Sinal


Modelo SYSTEMD Linux
--------------------

Um serviço, de acordo com o systemd, é denominado unidade e pode ser do tipo:
 - ".socket"
 - ".service" 
 - ".mount"
 - ".device"

Os antigos runlevels agora são definidos como targets. Porém, targets possuem nome e servem para um propósito específico, podendo existir multiplos targets rodando simultaneamente. Alguns targets possuem mapeamento 1:1 com antigos runlevels do sysvinit, porém, outros targets podem existir em mais de um runlevel.

#Listar todos os targets do sistema
systemctl list-units --type=target

#Visualizar Target (runlevel) default
systemctl get-default

Arquivos com unidades são escritos no formato de entrada de desktop inspiradas no XDG. Eles estão localizados nos diretórios:
 - /usr/lib/systemd/system/ [Instalados por pacotes]
 - /etc/systemd/system/     [Serviços do administrador do sistema]

#Gerenciar uma unidade
systemctl status|start|stop|restart <SERVICO>

#Mostrar unidades com falha
systemctl --failed

#Mostrar todos as unidades
systemctl --all

Obs: Alguns podem ser mostrados como not found (Ex: auditd, display-manager, syslog, plymouth)
     Isso ocorre por que eles estão sendo referenciados por outros serviços.

#Checar quem referencia um determinado serviço (Ex. syslog.service)
systemctl show -p WantedBy -p RequiredBy -p Before -p After syslog.service

#Mascarar serviços que não existem, mas são referenciados por outros. Causando falha em "systemctl -all"
systemctl mask <SERVICO>

#Visualizar árvore de processos
systemd-cgls


NETCTL
------

Gerenciador de interfaces de rede. Perfis com configurações de uma interface podem ser escritos e devel ser colocados na pasta '/etc/netctl'

#Iniciar um perfil
netctl status <NOME_PERFIL>

Obs: Netctl disponibiliza um serviço no systemd que permite iniciar/parar um perfil de uma interface se o cabo de rede/rede wireless forem conectados/desconectados. 

#Ethernet: Instalar ifplugd
pacman -S ifplugd
systemctl enable nectl-ifplugd@enp4s0

#Wireless: Instalar wpa_actiond
pacman -S wpa_actiond
systemctl enable netctl-auto@wlp2s0

Obs: Se mais de uma rota default estiver configurada, será usada a com o menor valor do parâmetro "metric".

#Checar rotas
ip route

#Checar qual rota será usada para determinado IP
ip route get <IP>


PACMAN
------

1. R [Remover]

#Remover pacote e dependencias que não são utilizadas por mais ninguém [Forma segura]
pacman -Rs <PACKAGE>


2. S [Sync]

#Instalar um pacote dos repositórios
pacman -S <PACKAGE>

#Pesquisar um pacote nos repositórios
pacman -Ss <TEXT>

#Consultar informações de um pacote nos repositórios
pacman -Si <PACKAGE>


3. Q [Query]

#Lista todos os pacotes instalados
pacman -Q

#Verificar se um pacote está instalado
pacman -Q <PACKAGE>

#Verificar informações de um pacote já instalado
pacman -Qi <PACKAGE>

#Verificar pacotes que foram instalados como dependencias [-d] e não são utilizados por nenhum outro pacote [-t]
#Util para remover pacotes órfãos que podem ser removidos
pacman -Qdt

#Obs: opção -q deixa o output mais limpo, útil para concatenar comandos
#Ex: Remover pacotes órfãos
pacman -Rs $(pacman -Qdtq)

#Lista pacotes que foram instalados e não estão nos repositórios oficiais (útil para ver pacotes do aur)
pacman -Qm

#Lista pacotes instalados explicitamente
pacman -Qe

#Verifica a qual pacote determinado arquivo pertence
pacman -Qo <FILE>

#Verifica arquivos que pertecem a um determinado pacote
pacman -Ql <PACKAGE>


4. U [Update]

#Instalar pacote de uma arquivo local
pacman -U <PACKAGE_FILE>


AUR
---

#Reposítorio de usuário com pacotes alternativos.
#É necessário para todos os pacotes fazer o download do fonte, construir o pacote utilizando makepkg e instalar o pacote localmente com pacman -U

#Instalar auxiliador de pacotes do AUR packer [semelhante ao pacman].
#Após downlaod do fonte do pacote no aur, construir pacote packer
makepkg -sc[i]

-s = instala dependencias utilizando pacman
-c = limpa arquivos temporários após a construção do pacote
-i = instala pacote construído utilizando pacman -U

#Instala pacote construído. [Necessário apenas se a opção -i não for utilizada]
pacman -U <PACKER-PACKAGE>

#Upgrade do sistema apenas com pacotes do aur
packer -Syu --auronly


X11
---

#Driver Intel
pacman -S xf86-video-intel

#Xorg
pacman -S xorg-server xorg-server-utils xorg-apps

#Xinit para iniciar x manualmente
pacman -S xorg-xinit

#Instalando Windows Manager e Emulador de terminal basicos
pacman -S xorg-twm xorg-xclock xterm

#Testar X [Copiar arquivo default /etc/X11/xinit/xinitrc para ~.xinitrc]
#Executar com usuário normal
startx

#Criar diretorios default para usuários do X
#Instalar xdg-user-dirs 
pacman -S xdg-user-dirs

#Criar pastas default em inglês. [Caso script em /etc/X11/xinit/xinitrc.d/$(script) não tenha sido executado]
LC_ALL=C xdg-user-dirs-update

#Reconhecer touchpad
pacman -S xf86-input-synaptics


KDE
---

#Instalar KDE
pacman -S plasma-meta

#Gerenciador de login oficial [Slim é mais simples]
pacman -S sddm

#Ferramenta para controle das configurações do sddm [/etc/sddm.conf]
pacman -S sddm-kcm

#Iniciar sddm em tty1 [Adicionar linha em /etc/sddm.conf]
[XDisplay]
MinimumVT=7

#Iniciar console [getty] no tty1, com sddm
#Alterar servico sddm [/etc/systemd/system/display-manager.service] *Se sddm for o display manager atual
#Comentar linha
Conflicts=getty@tty1.service

#Ferramentas
pacman -S konsole
pacman -S dolphin dolphin-plugins
