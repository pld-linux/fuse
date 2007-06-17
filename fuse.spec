#
# Conditional build:
%bcond_without	svga	# do not build svgalib version
%bcond_without	x	# do not build X11 version
%bcond_without	fb	# do not build framebuffer version
%bcond_without	sdl	# do not build SDL version
#
Summary:	Free Unix Spectrum Emulator
Summary(pl.UTF-8):	Darmowy uniksowy emulator ZX Spectrum
Name:		fuse
Version:	0.8.0.1
Release:	2
License:	GPL
Group:		Applications/Emulators
Source0:	ftp://ftp.worldofspectrum.org/pub/sinclair/emulators/unix/%{name}-%{version}.tar.gz
# Source0-md5:	34f85578c64d94ebf0cca309f837d502
Patch0:		%{name}-missing.patch
Patch1:		%{name}-update.patch
Patch2:		%{name}-keyboard.patch
URL:		http://fuse-emulator.sourceforge.net/
%{?with_sdl:BuildRequires:	SDL-devel >= 1.2.4}
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
%{?with_x:BuildRequires:	gtk+2-devel >= 1:2.0.0}
BuildRequires:	lib765-devel
BuildRequires:	libjsw-devel
BuildRequires:	libao-devel
BuildRequires:	libpng-devel
BuildRequires:	libspectrum-devel >= 0.3.0
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	perl
BuildRequires:	pkgconfig
%{?with_svga:BuildRequires:	svgalib-devel}
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

%description -l pl.UTF-8
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum.
Jego właściwości to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Możliwość ładowania programów z plików .tzx.
* Dźwięk.

%package common
Summary:	Free Unix Spectrum Emulator (common files)
Summary(pl.UTF-8):	Darmowy uniksowy emulator ZX Spectrum (pliki wspólne)
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

This package contains common files for all versions.

%description common -l pl.UTF-8
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum.
Jego właściwości to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Możliwość ładowania programów z plików .tzx.
* Dźwięk.
* Emulacja kilku drukarek przeznaczonych dla ZX Spectrum.

W tym pakiecie znajdują się wspólne pliki dla wszystkich wersji.

%package fb
Summary:	Free Unix Spectrum Emulator (framebuffer version)
Summary(pl.UTF-8):	Darmowy uniksowy emulator ZX Spectrum (wersja na framebuffer)
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}-%{release}

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

%description fb -l pl.UTF-8
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum.
Jego właściwości to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Możliwość ładowania programów z plików .tzx.
* Dźwięk.

W tym pakiecie znajdują się pliki dla wersji korzystającej z
framebuffera.

%package sdl
Summary:	Free Unix Spectrum Emulator (SDL version)
Summary(pl.UTF-8):	Darmowy uniksowy emulator ZX Spectrum (wersja na SDL)
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}-%{release}
Requires:	SDL >= 1.2.4

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

%description sdl -l pl.UTF-8
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum.
Jego właściwości to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Możliwość ładowania programów z plików .tzx.
* Dźwięk.

W tym pakiecie znajdują się pliki dla wersji korzystającej z SDL.

%package svga
Summary:	Free Unix Spectrum Emulator (svga version)
Summary(pl.UTF-8):	Darmowy uniksowy emulator ZX Spectrum (wersja na svgalib)
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}-%{release}

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

%description svga -l pl.UTF-8
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum.
Jego właściwości to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Możliwość ładowania programów z plików .tzx.
* Dźwięk.

W tym pakiecie znajdują się pliki dla wersji korzystającej z svgalib.

%package X11
Summary:	Free Unix Spectrum Emulator (X11 version)
Summary(pl.UTF-8):	Darmowy uniksowy emulator ZX Spectrum (wersja na XWindow)
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}-%{release}

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

%description X11 -l pl.UTF-8
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum.
Jego właściwości to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Możliwość ładowania programów z plików .tzx.
* Dźwięk.

W tym pakiecie znajdują się pliki dla wersji X11.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}

# X11
%if %{with x}
%configure  \
	--disable-ui-joystick \
	--with-joystick \
	--with-gtk
%{__make} clean
%{__make}
cp -f ./fuse ./fuse-x11
%endif

# SDL
%if %{with sdl}
%configure \
	--disable-ui-joystick \
	--with-joystick \
	--with-sdl
%{__make} clean
%{__make}
cp -f ./fuse ./fuse-sdl
%endif

# svga
%if %{with svga}
%configure \
	--disable-ui-joystick \
	--with-joystick \
	--with-svgalib
%{__make} clean
%{__make}
cp -f ./fuse ./fuse-svga
%endif

# framebuffer
%if %{with fb}
%configure \
	--with-joystick \
	--with-fb
%{__make} clean
%{__make}
cp -f ./fuse ./fuse-fb
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{?with_svga:install fuse-svga	$RPM_BUILD_ROOT%{_bindir}}
%{?with_x:install fuse-x11		$RPM_BUILD_ROOT%{_bindir}}
%{?with_fb:install fuse-fb		$RPM_BUILD_ROOT%{_bindir}}
%{?with_sdl:install fuse-sdl	$RPM_BUILD_ROOT%{_bindir}}

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%doc README THANKS AUTHORS keysyms.dat keysyms.pl hacking/*
%{_datadir}/%{name}
%{_mandir}/man1/*

%if %{with fb}
%files fb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fuse-fb
%endif

%if %{with sdl}
%files sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fuse-sdl
%endif

%if %{with svga}
%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fuse-svga
%endif

%if %{with x}
%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fuse-x11
%endif
