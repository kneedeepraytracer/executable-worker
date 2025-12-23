#!/usr/bin/env python3

### IMPORTS ###
import os

from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout, CMakeToolchain, CMakeDeps

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class LibraryRenderer(ConanFile):
    name = "kdrtworker"
    version = "0.0.1"
    #package_type = "library"

    license = "BSD-2-Clause"
    author = "Daniel Williams <dwilliams@port8080.net>"
    url = "https://github.com/kneedeepraytracer/executable-worker"
    description = "A raytracing worker"
    topics = ("raytracing")

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    #generators = "CMakeToolchain", "CMakeDeps"

    #exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def requirements(self):
        self.requires("fmt/11.2.0")
        self.requires("spdlog/1.15.3")
        # Note: This currently only exists in my local Artifactory instance.
        #       For someone else to get this, they'll have to build the library
        #       via Conan manually and have it available in their local Conan cache.
        self.requires("libkdrtrenderer/0.0.4")

    def build_requirements(self):
        self.test_requires("gtest/1.17.0")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    # def package(self):
    #     cmake = CMake(self)
    #     cmake.install()
    #
    # def package_info(self):
    #     self.cpp_info.libs = ["kdrtworker"]
