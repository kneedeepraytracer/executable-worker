#pragma once

#include "kdrt/renderer/vector3.h"

namespace kdrt::worker {
    class Worker {
    public:
        Worker();
        void hello();

    private:
        renderer::Vector3 v;
    };
}
