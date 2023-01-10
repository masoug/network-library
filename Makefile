all: network_library.cpp main.cpp
	g++ -o network_library_demo network_library.cpp main.cpp -I.