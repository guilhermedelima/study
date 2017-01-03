DEVICE DRIVERS - DAY 3
----------------------

- Linux é um kernel monolitico. Módulos se comunicam através de chamadas de funções.
- Escrito em C, exceto no diretório "arch/", onde possuem algumas rotinas para inicialização, tratamento de exceções, otimizações.
- Kernel é uma aplicação standalone, que não pode depender de bibliotecas em espaço de usuário (glibc, etc.). O kernel tem ua própria biblioteca (memset, kmalloc, printk).
- Código deve ser portável, exceto diretório "arch/".
- API interna do kernel é altamente volátil, ao contrário da API disponibilizada para user space.

Obs: Importante ter ferramenta que consiga indexar o código do kernel para consulta. (Ex: vim, "LXR - html" - MUITO IMPORTANTE).

Diretórios:
	- arch/: suporte ao hardware. Ex: arch/arm:
		- plat/: código genérico para uma linha de chips.
		- mach/: código específico para uma linha de chips.
		Obs: Modelo antigo, desorganizado. Diretório x86, por exemplo, está mais organizado (x86 cresceu de forma organizada).
		
	- drivers/: todos os drivers genéricos

	- init/: Códigos de inicialização
		- arquivo main.c é o main do kernel.
		Obs: algumas funções tem usam o modificador __init, para o kernel liberar a memória após a função ser executada.

	- kernel/:
		- Implementação das syscalls.
		- Escalonador.

	- net/:
		- Protocolos de rede.

	- Documetation:/
		- Documentação de implementações que o kernel utiliza (Muito útil).
		- Arquivo CodingStyle contém o padrão de codificação do kernel.
		- Script scripts/checkpatch.pl verifica se seu código estáde acordo com o padrão.


Obs: Usar 'printenv bootcmd' para saber o que o u-boot está fazendo durante o boot

Kernel Monolítico:
	- Todo o sistema operacional roda em kernel space, com total acesso aos recursos da máquina.
	- Vantagens: Todo o kernel se comunica através de chamadas de funções (rápido e simples).
	- Desvantagens: Se algum código do kernel travar, todo o sistema para.

Micro Kernel:
	- Apenas uma parte do sistema operacional roda em kernel space. Outros módulos são executados em user space.
	- Vantagens: Sistema operacional mais seguro, pois se algum driver travar, por exemplo, o sistema continua funcionando.
	- Desvantagens: Perda muito grande de performance. Comunicação IPC entre módulos do sistema operacional.

Linux Kernel:
	- Kernel monolítico que possibilita incluir módulos em tempo de execução. O conceito de incluir novos módulos é parecido com conceitos do micro kernel, a diferença é que o módulo é executado em kernel space, ao contrário do micro kernel, onde novos componentes são executados em user space.


Modulos do Kernel
-----------------

Obs: diretório "/lib/modules/VERSAO-KERNEL/" contém os módulos que o kernel pode carregar:
	- Comando modprobe procura módulo pelo nome dentro do diretório /lib/modules/VERSAO-KERNEL/.
	- insmod carrega módulo recebendo como argumento o caminho completo do arquivo ".ko".

Obs: Em /sys/module/MODULO-NOME/ você consegue ver as informações de um móduo, inclusive de parâmetros habilitados pelo módulo com a função "module\_param".

A inclusão de um código no kernel (driver / "módulos") pode ser feita de duas formas:
	- Compilar o código junto ao kernel de forma estática, que irá dentro da imagem / como um módulo do kernel:
		- Alterar .Kconfig para incluir uma nova opção em algum menu existente.
		- Alterar Makefile do Kernel para compilar o arquivo ".c" de acordo com a opção selecionada com "make menuconfig".

	- Compilar o código de forma paralela:
		- Incluir Makefile do kernel.
		- Compilar código.
		- Instalar módulos no rootfs.

Obs: Módulos (carregados depois do boot) aparecem no comando "lsmod". Já módulos "builtins", só é possível saber se realmente está rodando olhando em '/sys/module/NOME-MODULO'.


Obs: Em /proc/devices é possível ver qual o major number um módulo alocou dinamicamente.

Obs: Em /proc/iomen é possível visualizar se um módulo alocou uma regiao da memória física corretamente

