#include <iostream>

#include "network_library.h"


int main()
{
    network_library::NetworkClient client("127.0.0.1", 65432);
    client.send("suh dude");
    std::string reply = client.receive();
    while (reply.empty()) {
        reply = client.receive();
    }
    std::cout << reply << std::endl;
    return 0;
}
