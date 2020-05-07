Name:		tl-expected-devel
Summary:	An implementation of std::expected with functional extensions
Version:	1.0.0
Release:	2
Source0:	https://github.com/TartanLlama/expected/archive/v%{version}/expected-%{version}.tar.gz
Source1:	https://github.com/TartanLlama/tl-cmake/archive/284c6a3f0f61823cc3871b0f193e8df699e2c4ce.tar.gz
Patch0:		expected-1.0.0-no-download.patch
License:	CC0 1.0 Universal
Url:		https://tl.tartanllama.xyz/
Group:		Development/C
BuildRequires:	cmake
BuildRequires:	ninja

%description
An implementation of std::expected with functional extensions

%prep
%autosetup -p1 -n expected-%{version} -a 1
cd cmake
rmdir tl-cmake; mv ../tl-cmake-* tl-cmake
cd ..

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
