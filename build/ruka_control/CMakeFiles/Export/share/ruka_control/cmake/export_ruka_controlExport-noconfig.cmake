#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "ruka_control::ruka_control" for configuration ""
set_property(TARGET ruka_control::ruka_control APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(ruka_control::ruka_control PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libruka_control.so"
  IMPORTED_SONAME_NOCONFIG "libruka_control.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS ruka_control::ruka_control )
list(APPEND _IMPORT_CHECK_FILES_FOR_ruka_control::ruka_control "${_IMPORT_PREFIX}/lib/libruka_control.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
