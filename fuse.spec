# Conditional build:
# _without_svga - don't build svgalib version
# _without_x11 - don't build X11 version
# _without_fb - don't build framebuffer version
# _without_sdl - don't build SDL version

Summary:	Free Unix Spectrum Emulator
Summary(pl):	Darmowy uniksowy emulator ZX Spectrum
Name:		fuse
Version:	0.6.0
Release:	1
License:	GPL
Group:		Applications/Emulators
Source0:	http://www.srcf.ucam.org/~pak21/spectrum/%{name}-%{version}.tar.gz
# Source0-md5:	6e8b1f31296b498332ab871dbdc378c6
URL:		http://www.srcf.ucam.org/~pak21/spectrum/fuse.html
BuildRequires:	autoconf
BuildRequires:	automake
%{!?_without_x11:BuildRequires:	gtk+-devel}
BuildRequires:	lib765-devel
BuildRequires:	libpng-devel
BuildRequires:	libspectrum-devel >= 0.1.1
BuildRequires:	libxml2-devel
BuildRequires:	perl
%{!?_without_sdl:BuildRequires:	SDL-devel}
%ifarch %{ix86} alpha ppc
%{!?_without_svga:BuildRequires:	svgalib-devel}
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
Summary(pl):	Darmowy uniksowy emulator ZX Spectrum (pliki wspólne)
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

%if %{!?_without_fb:1}0
%package fb
Summary:	Free Unix Spectrum Emulator (framebuffer version)
Summary(pl):	Darmowy uniksowy emulator ZX Spectrum (wersja na framebuffer)
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}

%description fb
fuse is Free Unix Spectrum Emulator.
What Fuse does have:

* Working 48K/128K/+2/+2A Speccy emulation, running at true Speccy
  speed on any computer you're likely to try it on (it runs at full
  speed on a SparcStation 4 unless you do too much graphics intensive
  stuff).
* Support for loading from .tzx files.
* Sound.

This package contains files for framebuffer version.

%description fb -l pl
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum.
Jego w³a¶ciwo¶ci to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Mo¿liwo¶æ ³adowania programów z plików .tzx.
* D¼wiêk.

W tym pakiecie znajduj± siê pliki dla wersji korzystaj±cej z framebuffera. 
%endif

%if %{!?_without_sdl:1}0
%package sdl
Summary:	Free Unix Spectrum Emulator (SDL version)
Summary(pl):	Darmowy uniksowy emulator ZX Spectrum (wersja na SDL)
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}

%description sdl
fuse is Free Unix Spectrum Emulator.
What Fuse does have:

* Working 48K/128K/+2/+2A Speccy emulation, running at true Speccy
  speed on any computer you're likely to try it on (it runs at full
  speed on a SparcStation 4 unless you do too much graphics intensive
  stuff).
* Support for loading from .tzx files.
* Sound.

This package contains files for SDL version.

%description sdl -l pl
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum.
Jego w³a¶ciwo¶ci to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Mo¿liwo¶æ ³adowania programów z plików .tzx.
* D¼wiêk.

W tym pakiecie znajduj± siê pliki dla wersji korzystaj±cej z SDL. 

%endif

%if %{!?_without_svga:1}0
%package svga
Summary:	Free Unix Spectrum Emulator (svga version)
Summary(pl):	Darmowy uniksowy emulator ZX Spectrum (wersja na svgalib)
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

%endif

%if %{!?_without_x11:1}0
%package X11
Summary:	Free Unix Spectrum Emulator (X11 version)
Summary(pl):	Darmowy uniksowy emulator ZX Spectrum (wersja na XWindow)
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

%endif

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}

# X11
%if %{!?_without_x11:1}0
%configure  \
	--with-gtk
%{__make} clean
%{__make}
cp -f ./fuse ./fuse-x11
%endif

# SDL
%if %{!?_without_sdl:1}0
%configure \
	--with-sdl
%{__make} clean
%{__make}
cp -f ./fuse ./fuse-sdl
%endif

# svga
%ifarch %{ix86} alpha ppc
%if %{!?_without_svga:1}0
%configure \
	--with-svgalib
%{__make} clean
%{__make}
cp -f ./fuse ./fuse-svga
%endif
%endif

# framebuffer
%if %{!?_without_fb:1}0
%configure \
	--with-fb
%{__make} clean
%{__make}
cp -f ./fuse ./fuse-fb
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%ifarch %{ix86} alpha ppc
%{!?_without_svga:install fuse-svga	$RPM_BUILD_ROOT%{_bindir}}
%endif
%{!?_without_x11:install fuse-x11	$RPM_BUILD_ROOT%{_bindir}}
%{!?_without_fb:install  fuse-fb	$RPM_BUILD_ROOT%{_bindir}}
%{!?_without_sdl:install fuse-sdl	$RPM_BUILD_ROOT%{_bindir}}

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%doc README THANKS AUTHORS keysyms.dat keysyms.pl hacking/* 
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man1/*

%if %{!?_without_fb:1}0
%files fb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fuse-fb
%endif

%if %{!?_without_sdl:1}0
%files sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fuse-sdl
%endif

%ifarch %{ix86} alpha ppc
%if %{!?_without_svga:1}0
%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fuse-svga
%endif
%endif

%if %{!?_without_x11:1}0
%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fuse-x11
%endif
