Treinamento Linux DAY 1 - Linux Embarcado.
------------------------------------------

Os 3 Marcos:
	- 1970: Criacao do Unix (Engenheiros Bell Labs - Ken Thompso, Dennis Ritchie).
	- 1983: Inicio do projeto GNU e software livre (Stallman).
	- 1991: Criacao do Kernel Linux (Torvalds).


Componentes:

1 - Hardware:
	- Processador (x86, arm, PPC).
	- CPUs de 32/64 bits não foram feitas para micro controladores.
	- CPUs feitas originalmente para funcionar com MMU (Memória virtual).
	- Obs: Priorizar hardwares que sao suportados por novas releases do kernel.

2 - Toolchain
	- Conjuntos de ferramentas para gerar código de máquina (nativo ou cross compilação).
	- Compilador / Linker

3 - Bootloader:
	- Função: Inicializar o hardware e carregar o kernel.
	- Recursos: Passar parametros para o kernel, 
	- Ex: x86 (Grub); Arm (U-Boot).

4 - Kernel:
	- Abstrai hardware para aplicações (Escalonador / MMU).

	Funcoes:
		- Inicializa CPU, memória e barramento.
		- Configura MMU.
		- Inicializa Device drivers.
		- Inicializa Escalonador.
		- Inicia threads do kernel.
		- Inicia sistema de arquivos, rootfs e inicia "init".

	- Chamdas de sistemas:
		- Aplicações usam bibliotecas (glibc) que implementam system call (nao sao portáveis), que chamam direto funções do kernel.

5 - Rootfs
	- Conjunto de aplicações para utilizar um kernel (Papal de uma distribuição).
	- Componentes: bibliotecas (glibc, ...) + ferramentas.


Toolchains
----------

- Compilação:
	- 1: Pre compilação (Gera codigo intermediário em C). Expansão das macros, otimizações, etc.
	- 2: Compilação (Gera codigo em assembly).
	- 3: Assembler (Gera código de Máquina).
	- 4: Linker (Gera executável "ELF").

Obs: Compilação cruzada faz referencia a hardware E "softwares" diferentes. (x86 / arm ; Ubuntu / Arch).

- Componentes:
	- Compilador (GCC).
	- Biblioteca C (glibc): Interface entre aplicações e o kernel.
	- Binutils (Ferramentas para manipular binarios para uma arquitetura específica: as, ar, ld, strip, etc.).
	- Headers do kernel (Geralmente, Kernel mantem retro compatibilidade entre syscalls de versões anteriores).
	- Debugger (GDB).

Obs: Utilizar o mesmo toolchain que gerou uma distribuição para cross compilar aplicações para ela (Kernel e libs iguais).

Obs: glibc for feita com foco em performance, nao se preocupando muito com economia de recursos.


- Utilizando Toolchains.

	1) Toolchain do fabricante:
		- Simples e conveniente.
		- Inflexível a mudanças. Torna-se limitado as libs e rootfs disponibilizados pelo fabricante.
		- Compilar aplicação com toolchains baseados em gcc. Ex: "PREFIX-gcc -o prog prog.cpp".

	2) Construir o próprio toolchain:
		- Tarefa complicada. Linux from scratch.

	3) Usar ferramentas que automatizam a geração de toolchains:
		- Crosstool-ng
		- Buildroot
		- Yocto


Obs: Toolchain com prefixo: arm-cortexa9-linux-gnuabihf
	arm = arquitetura
	cortexa9 = sub arquitetura
	linux = suporte ao kernel linux
	gnuabi = suporte a glibc
	hf = suporte a ponto flutuante em hardware

Obs: Pasta sysroot do toolchain possui as libs da máquina "target", necessárias para cross compilação.


Bootloader
----------

Funções:
	- Inicializar o Hardware (CPU, GPIO, Controladora de RAM, etc.).
	- Carregar outro binário (geralmente o próprio SO) na RAM.
	- Passar o controle para este outro binário

Processo Boot x86:
	- Estágio 0: Carregar código da BIOS, que inicia o Hardware e procura um dispositivo para realizar o boot.
	- Estágio 1: Le os primeiros 512 bytes (MBR + tabela de partições) do disco e executa o código da MBR (Bootloader de 1 estágio).
	- Estágio 2: O MBR carrega um bootlader de estágio 2 (grub, lilo, windows boot, etc.) na memória e executa, o qual é mais complexo, podendo carregar um sistema operacional (kernel), por exemplo.

Processo Boot ARM:
	- Estagio 0: Cada chip ARM tem uma memória ram interna bem pequena (max 64K). O procesador carrega um bootloader primário SPL nesta RAM interna e em seguida o executa. O programa que carrega o SPL reside em uma ROM interna no chip.
	- Estagio 1: :
	-

Obs:
	- Diretório arch da suporte ao código do específico do processador
	- Diretório board da suporte ao código específico das placas de desenvolvimento
