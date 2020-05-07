Name:		tl-expected-devel
Summary:	An implementation of std::expected with functional extensions
Version:	1.0.0
Release:	1
Source0:	https://github.com/TartanLlama/expected/archive/v%{version}/expected-%{version}.tar.gz
License:	CC0 1.0 Universal
Url:		https://tl.tartanllama.xyz/
Group:		Development/C
BuildArch:	noarch
BuildRequires:	cmake
BuildRequires:	ninja

%description
An implementation of std::expected with functional extensions

%prep
%autosetup -p1 -n expected-%{version}
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%check
build/tests

%files
%{_includedir}/tl
%{_datadir}/cmake/tl-expected
