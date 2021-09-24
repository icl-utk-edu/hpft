# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Hpft(CMakePackage):
    """High Performance Fourier Transform benchmark."""

    homepage = "https://www.hpft.org/"
    url      = "https://github.com/icl-utk-edu/hpft"

    maintainers = ['G-ragghianti', 'luszczek']

    version('0.1.0', '0123456789abcdef0123456789abcdef')

    depends_on('ffte', when='+ffte')
    depends_on('fftw', when='+fftw')
    depends_on('hipfft', when='+hip')
    depends_on('rocfft', when='+rocm')
    depends_on('spfft', when='+spfft')
    depends_on('swfft', when='+swfft')

    variant('heffte', default=False)
    variant('p3dfft3', default=False)
    variant('accfft', default=False)

    variant('clfft', default=False)
    variant('ffte', default=False)
    variant('ffts', default=False)
    variant('fftw', default=False)
    variant('spfft', default=False)
    variant('swfft', default=False)

    variant('amdfftw', default=False)
    variant('cray-fftw', default=False)
    variant('fujitsu-fftw', default=False)

    variant('hip', default=False)
    variant('cuda', default=False)
    variant('rocm', default=False)

    variant('onlycomplex', default=False)

    def cmake_args(self):
        args = []
        for vrnt, nargs in (
            ("+ffte", ["-DHPFT_USE_FFTE"]),
            ("+fftw", ["-DHPFT_USE_FFTW"]),
            ("+heffte", ["-DHPFT_USE_HEFFTE"]),
            ("+p3dfft3", ["-DHPFT_USE_P3DFFT3"]),
        ):
            if vrnt in self.spec:
                args.extend(nargs)
        return args
