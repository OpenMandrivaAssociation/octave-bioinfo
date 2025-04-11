%global octpkg bioinfo

# NOTE: use commit if the last release is too old
%global	snapshot 20210728
%global	commit a74ca57046d1b9d998f31164eb551b700b4024c2

Summary:	Bioinformatics manipulation in Octave
Name:		octave-bioinfo
Version:	0.2.2
Release:	3
#Source0:	https://github.com/schloegl/octmat-bioinfo/archive/v%{version}/bioinfo-%{version}.tar.gz
Source0:	https://github.com/schloegl/octmat-bioinfo/archive/%{?commit:master}%{!?commit:v%{version}}/%{name}-%{?commit:master}%{!?commit:%{version}}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://github.com/schloegl/octmat-bioinfo
BuildArch:	noarch

BuildRequires:	octave-devel >= 3.0.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Bioinformatics manipulation in Octave.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1  -S gendiff  -n octmat-bioinfo-%{?commit:master}%{!?commit:%{version}}

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

