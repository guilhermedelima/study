Sistema de Arquivos - ROOTFS - Day 2
------------------------------------

Mount
	- Monta um dispositivo em um diretório.
	- Para jffs2 é necessário informar parametro '-t'

Obs: No Kernel, operações de I/O em disco usam buffers na memória para obter performance. Por isso, nem sempre após um 'write' é garantia do dado estar em disco. Para ter certeza é necessário um 'sync'.

Obs: Um dos papéis do kernel é montar o root file system. Por isso, é preciso passar para ele como parametro a partição que sera montada, caso contrário, ocorrerá um kernel panic.

Obs: Uma forma de bootar um file system é comprimi-lo em disco / flash, e quando o kernel subir, dizer a ele para carregar este file system comprimido na memória ram, através do "randisk". A vantagem é que o boot é rápido e é útil para sistemas com poucos recursos de disco / flash. Porém, as alterações no randisk não são persistidas. Nas distros atuais, é usada como passo intermediário para montagem do verdadeiro file system, pois o kernel carrega uma partição com os módulos na randisk, assim a imagem do kernel não precisa ser muito grande e ainda sim tem um boot rápido.


Arquivos que representam dispositivos no linux:
	- Dispositivos de caracteres possuem o label especial "c" (ls -lah). [Porta serial, byte a byte].
	- Dispositivos de blocos possuem o label especial "b". [Disco, informação endereçável].
	- Major number (Indica categoria do dispositivo) e minor number (Indica o número do dispositivo) de um dispositivo indicam qual o driver que será usado em operações com este dispositivo.


Criar dispositivo:
$ mknod /dev/<DEVICE> [c|b] major minor

Obs: Em sistemas atuais, deamons fazem o trabalho de adicionar dispositos automaticamente. Ex: udev.


PROCFS
------

	- /proc possui informações de processos e do sistema em geral. Ex: /proc/[ID] possui as informações do processo com pid ID.
	- Em /proc/sys é possível alterar configurações do kernel em tempo de execução. (sysctl escreve em /proc/sys).
	- Para montar o proc é necessário "mount -t proc none /proc". None não significa nada, já que o proc é apenas um lugar onde o kernel irá colocar e ler informações.


SYSFS
-----

	- Exportar informações do hardware.
	- Ambos /dev e /sys interagem com dispositivos. Diferença: 
		- /dev é utilizado para trocar dados com dispositivos (Ex: leitura e escrita em disco).
		- /sys é utilizado para controlar status de um dispositivo.
	- Montar sys: "mount -t sysfs none /sys"


BUILDROOT
--------

Ferramenta para automatizar a criação de uma distribuição linux. Responsável por criar os componentes:
	- Toolchain
	- Bootloader
	- Kernel
	- Rootfs
