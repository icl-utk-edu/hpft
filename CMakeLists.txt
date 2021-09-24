cmake_minimum_required( VERSION 3.0 FATAL_ERROR )

project( hpft VERSION 0.1.0 LANGUAGES C )

if (CMAKE_VERSION VERSION_LESS "3.1")
  if (CMAKE_C_COMPILER_ID STREQUAL "GNU")
    set (CMAKE_C_FLAGS "-std=gnu99 ${CMAKE_C_FLAGS}")
  endif ( CMAKE_C_COMPILER_ID )
else ( )
  set ( CMAKE_C_STANDARD 99 )
endif ( )

# don't need MPI C++ bindings, now deprecated anyways
set( MPI_CXX_SKIP_MPICXX ON )
set( MPI_FIND_COMPONENTS C )
find_package( MPI REQUIRED )

if (HPFT_USE_FFTE)
  find_package( FFTE )
endif ()

if (HPFT_USE_FFTW)
  find_package( FFTW )
endif ()

if (HPFT_USE_HEFFTE)
  find_package( HEFFTE )
endif ()

if (HPFT_USE_P3DFFT3)
  find_package( P3DFFT3 )
endif ()

# current Git branch
EXECUTE_PROCESS(
  COMMAND git rev-parse --abbrev-ref HEAD
  WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  OUTPUT_VARIABLE GIT_BRANCH
  OUTPUT_STRIP_TRAILING_WHITESPACE
)
set(HPFT_BRANCH ${GIT_BRANCH})

# Git hash
EXECUTE_PROCESS(
  COMMAND git log -1 --format=%h
  WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  OUTPUT_VARIABLE GIT_COMMIT_HASH
  OUTPUT_STRIP_TRAILING_WHITESPACE
)
set(HPFT_COMMIT ${GIT_COMMIT_HASH})

add_executable( hpft include/hpft.h src/hpft.c )
target_link_libraries( hpft MPI::MPI_C )

configure_file( include/hpftconfig.hin ${CMAKE_CURRENT_SOURCE_DIR}/include/hpftconfig.h @ONLY NEWLINE_STYLE LF )

install(TARGETS hpft RUNTIME DESTINATION bin)
