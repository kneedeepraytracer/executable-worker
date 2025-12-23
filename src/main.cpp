#include <cstdlib>
#include <iostream>

#include <spdlog/spdlog.h>

#include "worker.h"

int main(int argc, char *argv[]) {
    spdlog::info("argc == {}", argc);

    kdrt::worker::Worker w = kdrt::worker::Worker();
    w.hello();
}