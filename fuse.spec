Summary:	Free Unix Spectrum Emulator
Summary(pl):	"Wolny" uniksowy emulator ZX Spectrum
Name:		fuse
Version:	0.5.0
Release:	2
License:	GPL
Group:		Applications/Emulators
Source0:	http://www.srcf.ucam.org/~pak21/spectrum/%{name}-%{version}.tar.gz
URL:		http://www.srcf.ucam.org/~pak21/spectrum/fuse.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	perl
%ifarch %{ix86} alpha ppc
BuildRequires:	svgalib-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fuse is Free Unix Spectrum Emulator.
What Fuse does have:

* Working 48K/128K/+2/+2A Speccy emulation, running at true Speccy
  speed on any computer you're likely to try it on (it runs at full
  speed on a SparcStation 4 unless you do too much graphics intensive
  stuff).
* Support for loading from .tzx files.
* Sound emulation.

%description -l pl
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum.
Jego w³a¶ciwo¶ci to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Mo¿liwo¶æ ³adowania programów z plików .tzx.
* D¼wiêk.

%package common
Summary:	Free Unix Spectrum Emulator (common files)
Summary(pl):	"Wolny" uniksowy emulator ZX Spectrum (pliki wspólne)
Group:		Applications/Emulators

%description common
fuse is Free Unix Spectrum Emulator.
What Fuse does have:

* Working 48K/128K/+2/+2A Speccy emulation, running at true Speccy
  speed on any computer you're likely to try it on (it runs at full
  speed on a SparcStation 4 unless you do too much graphics intensive
  stuff).
* Support for loading from .tzx files.
* Sound.

This package contains common files for X11 and svga version.

%description common -l pl
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum.
Jego w³a¶ciwo¶ci to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Mo¿liwo¶æ ³adowania programów z plików .tzx.
* D¼wiêk.
* Emulacja kilku drukarek przeznaczonych dla ZX Spectrum.

W tym pakiecie znajduj± siê wspólne pliki dla wersji X11 i svga.

%package svga
Summary:	Free Unix Spectrum Emulator (svga version)
Summary(pl):	"Wolny" uniksowy emulator ZX Spectrum (wersja na svgalib)
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}

%description svga
fuse is Free Unix Spectrum Emulator.
What Fuse does have:

* Working 48K/128K/+2/+2A Speccy emulation, running at true Speccy
  speed on any computer you're likely to try it on (it runs at full
  speed on a SparcStation 4 unless you do too much graphics intensive
  stuff).
* Support for loading from .tzx files.
* Sound.

This package contains files for svga version.

%description svga -l pl
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum.
Jego w³a¶ciwo¶ci to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Mo¿liwo¶æ ³adowania programów z plików .tzx.
* D¼wiêk.

W tym pakiecie znajduj± siê pliki dla wersji korzystaj±cej z svgalib. 

%package X11
Summary:	Free Unix Spectrum Emulator (X11 version)
Summary(pl):	"Wolny" uniksowy emulator ZX Spectrum (wersja na XWindow)
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}

%description X11
fuse is Free Unix Spectrum Emulator.
What Fuse does have:

* Working 48K/128K/+2/+2A Speccy emulation, running at true Speccy
  speed on any computer you're likely to try it on (it runs at full
  speed on a SparcStation 4 unless you do too much graphics intensive
  stuff).
* Support for loading from .tzx files.
* Sound.

This package contains files for X11 version.

%description X11 -l pl
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum.
Jego w³a¶ciwo¶ci to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Mo¿liwo¶æ ³adowania programów z plików .tzx.
* D¼wiêk.

W tym pakiecie znajduj± siê pliki dla wersji X11.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
# version for X11
%configure  \
	--with-x \
	--with-glib \
	--without-svgalib \
	--without-fb
%{__make} clean
%{__make}
cp -f ./fuse ./fuse-x11

#version for svga
%ifarch %{ix86} alpha ppc
%{__make} clean
%configure \
	--without-x \
	--without-glib \
	--without-fb \
	--with-svgalib
%{__make}
cp -f ./fuse ./fuse-svga
%endif

%install
rm -rf $RPM_BUILD_ROOT
%define _xbindir /usr/X11R6/bin
%{__make} install DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_xbindir}

install fuse-svga $RPM_BUILD_ROOT%{_bindir}
install fuse-x11 $RPM_BUILD_ROOT%{_xbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%doc README THANKS AUTHORS keysyms.dat keysyms.pl hacking/* 
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_bindir}/tzxlist
%{_datadir}/%{name}/*
%{_mandir}/man1/*

%ifarch %{ix86} alpha ppc
%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fuse-svga
%endif

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_xbindir}/fuse-x11
