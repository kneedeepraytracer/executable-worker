cmake_minimum_required(VERSION 3.23)

project(kdrtworker CXX)

find_package(fmt REQUIRED)
find_package(spdlog REQUIRED)
find_package(libkdrtrenderer REQUIRED)

set(CMAKE_SKIP_RPATH TRUE)

set(KDRTWORKER_SOURCES
    src/worker.cpp
)

add_library(kdrtworkerlib ${KDRTWORKER_SOURCES})

target_link_libraries(kdrtworkerlib fmt::fmt)
target_link_libraries(kdrtworkerlib spdlog::spdlog)
target_link_libraries(kdrtworkerlib libkdrtrenderer::libkdrtrenderer)

add_executable(kdrtworkerexec src/main.cpp)

target_link_libraries(kdrtworkerexec PUBLIC kdrtworkerlib)

if(NOT BUILD_TESTING STREQUAL OFF)
    enable_testing()
    include(CTest)

    if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
        target_compile_options(kdrtworkerlib PRIVATE -coverage)
        target_link_options(kdrtworkerlib PRIVATE -coverage)
    endif()

    if(CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
        target_compile_options(kdrtworkerlib PRIVATE -fprofile-instr-generate -fcoverage-mapping)
        target_link_options(kdrtworkerlib PRIVATE -fprofile-instr-generate -fcoverage-mapping)
    endif()

    add_subdirectory(tests)
endif()
