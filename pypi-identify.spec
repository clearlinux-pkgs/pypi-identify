#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-identify
Version  : 2.5.6
Release  : 48
URL      : https://files.pythonhosted.org/packages/44/72/097d62a473327d9474003762bea3e17ebf992483f8896b7cf4a5cf8f256b/identify-2.5.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/44/72/097d62a473327d9474003762bea3e17ebf992483f8896b7cf4a5cf8f256b/identify-2.5.6.tar.gz
Summary  : File identification library for Python
Group    : Development/Tools
License  : MIT MPL-2.0
Requires: pypi-identify-bin = %{version}-%{release}
Requires: pypi-identify-license = %{version}-%{release}
Requires: pypi-identify-python = %{version}-%{release}
Requires: pypi-identify-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
identify
========
[![Build Status](https://dev.azure.com/asottile/asottile/_apis/build/status/pre-commit.identify?branchName=main)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=67&branchName=main)
[![Azure DevOps coverage](https://img.shields.io/azure-devops/coverage/asottile/asottile/67/main.svg)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=67&branchName=main)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/pre-commit/identify/main.svg)](https://results.pre-commit.ci/latest/github/pre-commit/identify/main)
[![PyPI version](https://badge.fury.io/py/identify.svg)](https://pypi.python.org/pypi/identify)

%package bin
Summary: bin components for the pypi-identify package.
Group: Binaries
Requires: pypi-identify-license = %{version}-%{release}

%description bin
bin components for the pypi-identify package.


%package license
Summary: license components for the pypi-identify package.
Group: Default

%description license
license components for the pypi-identify package.


%package python
Summary: python components for the pypi-identify package.
Group: Default
Requires: pypi-identify-python3 = %{version}-%{release}

%description python
python components for the pypi-identify package.


%package python3
Summary: python3 components for the pypi-identify package.
Group: Default
Requires: python3-core
Provides: pypi(identify)

%description python3
python3 components for the pypi-identify package.


%prep
%setup -q -n identify-2.5.6
cd %{_builddir}/identify-2.5.6
pushd ..
cp -a identify-2.5.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664830047
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-identify
cp %{_builddir}/identify-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-identify/428ea02ecbdb18e260e938e24a83f8d96b7def89 || :
cp %{_builddir}/identify-%{version}/identify/vendor/licenses.py %{buildroot}/usr/share/package-licenses/pypi-identify/c120f330fdc22f119d76f90e375c5ee6cd7bca67 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/identify-cli

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-identify/428ea02ecbdb18e260e938e24a83f8d96b7def89
/usr/share/package-licenses/pypi-identify/c120f330fdc22f119d76f90e375c5ee6cd7bca67

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
