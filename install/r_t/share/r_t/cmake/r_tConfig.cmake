# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_r_t_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED r_t_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(r_t_FOUND FALSE)
  elseif(NOT r_t_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(r_t_FOUND FALSE)
  endif()
  return()
endif()
set(_r_t_CONFIG_INCLUDED TRUE)

# output package information
if(NOT r_t_FIND_QUIETLY)
  message(STATUS "Found r_t: 0.0.0 (${r_t_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'r_t' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${r_t_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(r_t_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${r_t_DIR}/${_extra}")
endforeach()
