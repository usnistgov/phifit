cmake_minimum_required(VERSION 3.0)

project(PHIFIT)

# Set the standard for C++ to c++11
set(CMAKE_CXX_STANDARD 11)

# Specify the Eigen root directory that will be used for all projects
include_directories("${CMAKE_SOURCE_DIR}/externals/CoolProp/externals/Eigen")

# Add CoolProp dependency
set(COOLPROP_STATIC_LIBRARY true CACHE BOOL "Use CoolProp")
add_subdirectory("${CMAKE_SOURCE_DIR}/externals/CoolProp" "CoolProp")

# Add NISTfit dependency
set(NISTFIT_STATIC_LIBRARY true CACHE BOOL "Use NISTfit")
add_subdirectory("${CMAKE_SOURCE_DIR}/externals/NISTfit" "NISTfit")

# Add root as include directory
include_directories("${CMAKE_SOURCE_DIR}/include")

# Get all the source files for the tests (everything in test directory)
file(GLOB_RECURSE APP_SOURCES "${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp")

if (PHIFIT_MAIN)
    # Add fitter code
    add_executable(Main ${APP_SOURCES} "${CMAKE_CURRENT_SOURCE_DIR}/src/main.cxx")

    # Link it to its dependent libraries
    target_link_libraries (Main CoolProp NISTfit)
elseif (PHIFIT_TEST)
    # Get all the source files for the tests (everything in test directory)
    file(GLOB_RECURSE TEST_SOURCES "${CMAKE_CURRENT_SOURCE_DIR}/test/*.cpp")

    # Add the code
    add_executable(TestRunner ${TEST_SOURCES} ${APP_SOURCES})

    # Link it to its dependent libraries
    target_link_libraries (TestRunner CoolProp NISTfit)

    # Add fitter code
    add_executable(Main ${APP_SOURCES} "${CMAKE_CURRENT_SOURCE_DIR}/src/main.cxx")

    # Link it to its dependent libraries
    target_link_libraries (Main CoolProp NISTfit)

    # Add root as include directory
    include_directories("${CMAKE_SOURCE_DIR}")
elseif (PHIFIT_PYBIND11)
    # ----------------------------
    # Build pybind11 python module
    # ----------------------------
    
    add_subdirectory("${CMAKE_SOURCE_DIR}/externals/CoolProp/externals/pybind11")
    add_definitions(-DPYBIND11)
    pybind11_add_module(MixtureCoefficientFitter ${APP_SOURCES} "${CMAKE_SOURCE_DIR}/externals/CoolProp/src/pybind11_interface.cxx")
    target_link_libraries (MixtureCoefficientFitter PUBLIC CoolProp PUBLIC NISTfit)
else()
    message(FATAL_ERROR "Must select a module: PHIFIT_MAIN, PHIFIT_TEST, PHIFIT_PYBIND11")
endif()

