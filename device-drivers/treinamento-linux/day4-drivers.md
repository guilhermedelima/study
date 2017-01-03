DRIVERS
-------

Todas as informações de hardware não devem estar escritas no driver. Ele deve ser configurável. Componentes para desenvolvimento de drivers no linux:
	- Framework para interface com o usuário.
	- Infraestrutura de barramento (Registra o dispositivo e instancia o driver).


FRAMEWORK
---------

Define padrão para dispositivos do mesmo tipo (O driver não se preocupa com a interface com o usuário - syscalls).
	* Obs: Se não existir framework para a categoria do dispositivo, é necessário implementar ou fazer isso no driver mesmo.
	* Ex: IO, Input, TTY, Block (Os frameworks disponibilizam device number), Network.
	* Obs: /sys/class
	* Obs: Código do framework e dos drivers especificos estão na pasta drivers/CLASS-NAME/


GPIO-LIB
--------

Abstrai acesso ao Hardware para o driver.
Driver das controladoras de cada chip (grupo) de GPIOs registram os pinos na gpio-lib.

--> OBS: CONTROLADORA É UMA DRIVER QUE ESCREVE/LE DIRETO NO BARRAMENTO DO DISPOSITIVO.


BUS PLATAFORM
-------------

Os dispositivos são registrados no Bus Plataform, que é responsável por instanciar / "deletar" (probe / remove) um módulo responsável pelo dispositivo em questão. Para barramentos como i2c, spi, os drivers da controladora do barramento também se registram no bus plataform. O dispositivo pode se registrar no Bus Plataform de duas formas:
	- Diretamento no ccódigo de inicialização da placa. Ex: "arch/arm/mach-imx/mach-im6q.c".
	- Device tree.
		- Para saber a documentação de um nó do device tree, é necessário ver o valor da propriedade compatible e procurar este valor no diretório Documentation/devecetree/bindings
		Obs: X86 nao usa device tree, pois usa o barramento PCI e ACPI para descobrir 


Obs: Quando o processador escreve direto no registrador do Hardware (porta serial / Direfente de barramento i2c, spi, etc), você precisa escrever um plataform driver.
