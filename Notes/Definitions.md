# Definitions

| Terms | Meanings | 
|---------|---|
| Sockets    | End point of a two way communication link between two programs running on the network, establish named contact points for exchange of infom|
| IPC     | Inter Process Communication refers to managing of shared data by the processes|
| ISP     | Organisation that lets you use and connect to the internet |
| Server  | A computer system that provides other systems in the network with functionalities and resources |
| Client  | A computer system that, as part of its operation, relies on sending a request to another computer system (server) and accesses its services and functionalities|
| Client-Server Model/Application| Structure that partitions tasks and workloads between providers of resources/services and the users/requesters of those resources/services|
| Berkely/BSD Sockets| It is an API that allows the connection of the internet communication to the program |
| Unix domain sockets | Used for communication between processes on the same host |
| Protocols | A network protocol is an established set of rules that determine how data is transmitted between different devices in the same network. Essentially, it allows connected devices to communicate with each other, regardless of any differences in their internal processes, structure or design|
| TCP | Transmission COntrol Protocol complements with the Internet Protocol and facilitates communication between two connected systems over the internet. TCP numbers each packet and reassembles them prior to handing them off to the application/server recipient |
| UDP | User Datagram Protocol is a communications protocol that is primarily used for establishing low-latency and loss-tolerating connections between applications on the internet. It speeds up transmissions by enabling the transfer of data before an agreement is provided by the receiving party.
| Packet Loss | Packet loss occurs when one or more packets of data travelling across a computer network fail to reach their destination. Packet loss is either caused by errors in data transmission, typically across wireless networks, or network congestion|
| Port | A port is a logical construct (or logical connection place) assigned to network processes so that they can be identified within the system|
| Listening Socket | Conceptually, the listening socket creates a new socket (the “child” socket), and establishes the connection on it. The listening socket is then free to resume listening on the same port, while the child socket has an established connection with the client that is independent from its parent. This results in no read/write operations by the listening socket.|
| Echo | It consists of a server which sends back whatever text the client sent. Used to check if connections have been succesfully established.|
| Address family | (AF)An address family is normally comprised of a number of protocols, one per socket type. Each protocol is characterized by an abstract socket type.|
| Host | A host is any computer connected to a network. The host is a versatile, multifunction computer; clients and servers are just programs that run on a host.|
| IPv4| IPv4 stands for Internet Protocol version 4. It is the underlying technology that makes it possible for us to connect our devices to the web. Whenever a device accesses the Internet, it is assigned a unique, numerical IP address such as 99.48. 227.227.|
| Loopback (interface) | The loopback device is a special, virtual network interface that your computer uses to communicate with itself. It is used mainly for diagnostics and troubleshooting, and to connect to servers running on the local machine.|
| DNS | DNS stands for Domain Name System. The main function of DNS is to translate domain names into IP Addresses, which computers can understand.|
| Configuration | A configuration of a system refers to the arrangement of each of its functional units, according to their nature, number and chief characteristics.|
| State | The state of a socket determines which network operations will succeed, which operations will block, and which operations with will fail (the socket state even determines the error code). Sockets have a finite number of states|
| Blocking calls | A "blocking" call "blocks" the program that calls it until it completes. Your program has to wait for it to do (whatever) before the next statement runs.|

