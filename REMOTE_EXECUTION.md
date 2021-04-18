# Running SR700 Artisan Server remotely

As SR700 Server runs using Python's "Pyro" tooling, it is possible to communicate over TCP/IP with a remote server.
You can, for example, run this server on a small Raspberry Pi Zero W connected to your SR700, while running Artisan on a more powerful laptop.

In order to provide a remote connection for artisan, you must:

* launch `Start_SR700_Artisan_Server` with the `--network_mode public` flag
* have the SR700_Artisan_Server on the same network subnet as the machine running Artisan (as by default, the Pyro Proxy searches out a Nameserver with a broadcast that assumes it will find it on the same subnet)
* install the SR700_Artisan_Server code on the Artisan host as well as the Server host that is providing a connection

Note that the configuration you import into Artisan tells artisan to look on the Path for functions such as Get_Artisan_Temps, which is provided by this package. This is why it must be installed on both machines to work (and be visible/callable by Artisan)
