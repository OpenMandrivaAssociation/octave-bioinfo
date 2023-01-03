Summary:	Bioinformatics manipulation in Octave
Name:		octave-bioinfo
Version:	0.2.1
Release:	1
Source0:	https://github.com/schloegl/octmat-bioinfo/archive/refs/tags/v%{version}/bioinfo-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/bioinfo/
BuildArch:	noarch

BuildRequires:	octave-devel >= 3.0.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Bioinformatics manipulation in Octave.

This package is part of unmantained Octave-Forge collection.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -n bioinfo-%{version}

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

