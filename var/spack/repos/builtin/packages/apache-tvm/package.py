# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class ApacheTvm(CMakePackage, CudaPackage):
    """"Apache TVM is an open source machine learning compiler framework for
    CPUs, GPUs, and machine learning accelerators. It aims to enable machine
    learning engineers to optimize and run computations efficiently on any
    hardware backend."""

    homepage = "https://tvm.apache.org/"
    url = "https://dlcdn.apache.org/tvm/tvm-v0.16.0/apache-tvm-src-v0.16.0.tar.gz"

    license("Apache-2.0", checked_by="alex391")

    version("0.16.0", sha256="55e2629c39248ef3b1ee280e34a960182bd17bea7ae0d0fa132bbdaaf5aba1ac")

    variant("llvm", default=True, description="Build with llvm for CPU codegen")

    depends_on("cmake@3.18:", type="build")
    depends_on("python")
    depends_on("llvm@4.0:", type="build", when="+llvm")

    def cmake_args(self):
        args = []
        define = self.define
        if self.spec.satisfies("+cuda"):
           args.append(define("USE_CUDA", True))
        if self.spec.satisfies("+llvm"):
           args.append(define("USE_LLVM", True))
        return args
