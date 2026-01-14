cmake_minimum_required(VERSION 3.16)

project(simplest LANGUAGES C)

add_executable(simplest main.c)

include(GNUInstallDirs)
install(TARGETS simplest
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
