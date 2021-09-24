# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Ffte(Package):
    """Fastest Fourier Trnasform in the East."""

    homepage = "http://www.ffte.jp/"
    url = "http://www.ffte.jp/ffte-7.0.tgz"

    maintainers = ['luszczek']

    # FIXME: Add proper versions and checksums here.
    version('0.7.0', sha256='078d5f84a5f2479ca5c4a3bd777ad761fe98addf1642a045bac6602a0cae3da0')
    version('0.6.0', sha256='fc82595a8f8323b2796cc5eeb1cc9f7e50ca9e511a14365cc3984da6b7a9b8b4')
    version('0.5.0', sha256='1f46ca16badc3aca0ad13ca91a6a67829a57b403501cdc821b80cfa62b2a89c2')
    version('0.4.0', sha256='61680f73c48659ac45aec60ef5a725547f763bb9017edbd3f44a6a9ad0fda62f')
    version('0.3.0', sha256='dbaab8204a16072c8d572efa3733e9946a9be0d1a051fc19e2d9253be23247ff')
    version('0.2.0', sha256='f5cf1d1f880288e359f4d517191980ffca4420f817ecaa2d754ca5c5421271e3')
    version('0.1.0', sha256='35171e3324019018c25575b2807a6513fa85badad040f30f238fff03d4b4d1ab')

    variant('mpi', default=False)
    variant('cuda', default=False)
    variant('spiral', default=False)

    def install(self, spec, prefix):
        make()
        make('install')
