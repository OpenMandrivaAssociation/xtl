%define devname %mklibname xtl -d

Name: xtl
Version: 0.7.6
Release: 1
Source0: https://github.com/xtensor-stack/xtl/archive/refs/tags/%{version}.tar.gz
Summary: Basic tools (containers, algorithms) used by other quantstack packages
URL: https://github.com/xtl/xtl
License: BSD-3-Clause
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildArch: noarch

%description
Basic tools (containers, algorithms) used by other quantstack packages

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C++

%description -n %{devname}
Development files (Headers etc.) for %{name}:

Basic tools (containers, algorithms) used by other quantstack packages

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{devname}
%{_includedir}/*
%{_datadir}/pkgconfig/*
%{_datadir}/cmake/*
