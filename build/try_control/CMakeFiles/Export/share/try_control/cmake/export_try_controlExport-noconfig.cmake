#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "try_control::try_control" for configuration ""
set_property(TARGET try_control::try_control APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(try_control::try_control PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libtry_control.so"
  IMPORTED_SONAME_NOCONFIG "libtry_control.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS try_control::try_control )
list(APPEND _IMPORT_CHECK_FILES_FOR_try_control::try_control "${_IMPORT_PREFIX}/lib/libtry_control.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
