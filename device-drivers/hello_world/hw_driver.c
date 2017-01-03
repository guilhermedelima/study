#include <linux/kernel.h>
#include <linux/module.h>

#define MODULE_NAME "hello world driver"

static int __init hw_driver_init( void )
{
	pr_info( "%s: Module initialized\n", MODULE_NAME );
	return 0;
}

static void __exit hw_driver_exit( void )
{
	pr_info( "%s: Module finilized\n", MODULE_NAME );
}

module_init( hw_driver_init );
module_exit( hw_driver_exit );

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Guilherme de Lima <guilhermedelima@gmail.com>");
MODULE_DESCRIPTION("Hello world kernel module");
MODULE_VERSION("1.0");
