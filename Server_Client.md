


![server-workstation](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/e4790612-c01b-418d-98ae-f95005a593cf)




1. One server (no GUI) running the following services:
    - DHCP (one scope serving the local internal network)  isc-dhcp-server
    - DNS (resolve internal resources, a redirector is used for external resources) bind
    - HTTP+ mariadb (internal website running GLPI)
    - **Required**
        1. Weekly backup the configuration files for each service into one single compressed archive
        2. The server is remotely manageable (SSH)
    - **Optional**
        1. Backups are placed on a partition located on  separate disk, this partition must be mounted for the backup, then unmounted


The server's IP address is set to 192.168.1.53 with a subnet mask of 255.255.255.0. It connects to the network through the gateway at 192.168.1.1.

![ip](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/853752d7-46c8-44d5-89c5-1ffd152f8b1d)

### SSH
===========================================================================

![ssh](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/9dcde1fb-09c0-4c40-bc98-34a9a76d5010)
![ssh-server](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/def46831-8478-4ee7-9e12-8dfb80b1c155)



### DHCP
===========================================================================


Configuration:
Configuring DHCP Server
Install ISC DHCP Server:
```
sudo apt install isc-dhcp-server 
```
Configure DHCP Server:

Edit the DHCP configuration file.
```
 sudo nano /etc/dhcp/dhcpd.conf
```

![autho](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/1a1d8300-cd46-41cd-978b-a5113179632a)


 we designate the INTERFACESv4 variable to correspond with our server's network interface, which is eth0.
 
 ![interface](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/38f56588-0556-4205-8736-5edaa7d4de2d)

now lets check dhcp on the server 

![dhcp status](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/6ada5d87-a1d1-43c1-a5e0-b432570ab64f)

lets now the workstation will request ip from dhcp server and get ip between 192.168.1.10-192.168.1.20

![dhcpst1](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/60c59420-40fa-4828-859b-3bf040293b33)


![statudhcp2](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/21569b73-3a73-4e0e-8f21-964f16531b35)
![workstationssh](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/58f528b4-4161-4cd1-9dee-03c0937c326a)
![workstation](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/b26d2890-6738-4c59-bc9c-b6d0464b6eec)

 

### DNS
===========================================================================

![forward](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/6b9641aa-b6a4-4a31-acc3-c8e543500781)

![reverse](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/da7384f9-f953-43f2-8a0b-bec4bf45e793)
![mymy](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/f2105c3a-aa78-4198-b87a-5f2638b1fa28)
![dns](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/9e0ce8f6-2474-45e0-8428-4ed57a912f3b)

![apche2run](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/9d79b628-8a97-40a5-8cce-65383f777a2d)
![apache2](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/9c1028d6-9f68-4bc7-ace9-b68734808ec6)



### HTTP+ mariadb 
===========================================================================


![sql](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/8da31a86-7ff3-4ffc-9f0e-4473f14ad063)

![mariadb](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/1e9241d8-10e1-4232-95d4-8356a927f8d3)

![database_glpi](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/1a499366-a307-48c1-9b1b-1aae6521f7f0)

![glpiusr](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/020b92e3-d1eb-4bf1-9967-3049677e8cd1)


======================================================================================================================================================





2. One workstation running a desktop environment and the following apps:
    - LibreOffice
    - Gimp
    - Mullvad browser
    - **Required** 
        1. This workstation uses automatic addressing
        2. The /home folder is located on a separate partition, same disk 
    - **Optional**
        1. Propose and implement a solution to remotely help a user

