# TODO: Fix issue with the WORDS_BIGENDIAN macro of autoconf-2.63
# fuse built using autotools is unusable because of it.
#
# Conditional build:
%bcond_with	svga	# do not build svgalib version
%bcond_without	fb	# do not build framebuffer version
%bcond_without	gtk	# do not build gtk version
%bcond_with	gtk3	# do not build gtk3 version
%bcond_without	sdl	# do not build SDL version
#
Summary:	Free Unix Spectrum Emulator
Summary(pl.UTF-8):	Darmowy uniksowy emulator ZX Spectrum
Name:		fuse
Version:	1.1.0
Release:	1
License:	GPL v2+
Group:		Applications/Emulators
Source0:	http://download.sourceforge.net/fuse-emulator/%{name}-%{version}.tar.gz
# Source0-md5:	df79d24647e56e4ba2bf7a5f26aa5ccd
Patch0:		%{name}-includes.patch
URL:		http://fuse-emulator.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.4
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
%{?with_gtk:BuildRequires:	gtk+2-devel >= 1:2.0.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel}
%{?with_fb:BuildRequires:	gpm-devel}
BuildRequires:	libjsw-devel
BuildRequires:	libpng-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libspectrum-devel >= 1.1.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	perl-base
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
* Emulation of several printers for ZX Spectrum.

%description -l pl.UTF-8
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum.
Jego właściwości to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Możliwość ładowania programów z plików .tzx.
* Dźwięk.
* Emulacja kilku drukarek przeznaczonych dla ZX Spectrum.

%package common
Summary:	Free Unix Spectrum Emulator (common files)
Summary(pl.UTF-8):	Darmowy uniksowy emulator ZX Spectrum (pliki wspólne)
Group:		Applications/Emulators
Requires:	libspectrum >= 0.4.0

%description common
fuse is Free Unix Spectrum Emulator.
What Fuse does have:

* Working 48K/128K/+2/+2A Speccy emulation, running at true Speccy
  speed on any computer you're likely to try it on (it runs at full
  speed on a SparcStation 4 unless you do too much graphics intensive
  stuff).
* Support for loading from .tzx files.
* Sound emulation.
* Emulation of several printers for ZX Spectrum.

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
* Sound emulation.
* Emulation of several printers for ZX Spectrum.

This package contains files for framebuffer version.

%description fb -l pl.UTF-8
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum.
Jego właściwości to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Możliwość ładowania programów z plików .tzx.
* Dźwięk.
* Emulacja kilku drukarek przeznaczonych dla ZX Spectrum.

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
* Sound emulation.
* Emulation of several printers for ZX Spectrum.

This package contains files for SDL version.

%description sdl -l pl.UTF-8
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum.
Jego właściwości to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Możliwość ładowania programów z plików .tzx.
* Dźwięk.
* Emulacja kilku drukarek przeznaczonych dla ZX Spectrum.

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
* Sound emulation.
* Emulation of several printers for ZX Spectrum.

This package contains files for svga version.

%description svga -l pl.UTF-8
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum.
Jego właściwości to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Możliwość ładowania programów z plików .tzx.
* Dźwięk.
* Emulacja kilku drukarek przeznaczonych dla ZX Spectrum.

W tym pakiecie znajdują się pliki dla wersji korzystającej z svgalib.

%package gtk
Summary:	Free Unix Spectrum Emulator (X11 version)
Summary(pl.UTF-8):	Darmowy uniksowy emulator ZX Spectrum (wersja na XWindow)
Group:		Applications/Emulators
Obsoletes:	fuse-X11
Requires:	%{name}-common = %{version}-%{release}

%description gtk
fuse is Free Unix Spectrum Emulator.
What Fuse does have:

* Working 48K/128K/+2/+2A Speccy emulation, running at true Speccy
  speed on any computer you're likely to try it on (it runs at full
  speed on a SparcStation 4 unless you do too much graphics intensive
  stuff).
* Support for loading from .tzx files.
* Sound emulation.
* Emulation of several printers for ZX Spectrum.

This package contains files for gtk version.

%description gtk -l pl.UTF-8
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum.
Jego właściwości to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Możliwość ładowania programów z plików .tzx.
* Dźwięk.
* Emulacja kilku drukarek przeznaczonych dla ZX Spectrum.

W tym pakiecie znajdują się pliki dla wersji gtk.

%package gtk3
Summary:	Free Unix Spectrum Emulator (X11 version)
Summary(pl.UTF-8):	Darmowy uniksowy emulator ZX Spectrum (wersja na XWindow)
Group:		Applications/Emulators
Obsoletes:	fuse-X11
Requires:	%{name}-common = %{version}-%{release}

%description gtk3
fuse is Free Unix Spectrum Emulator.
What Fuse does have:

* Working 48K/128K/+2/+2A Speccy emulation, running at true Speccy
  speed on any computer you're likely to try it on (it runs at full
  speed on a SparcStation 4 unless you do too much graphics intensive
  stuff).
* Support for loading from .tzx files.
* Sound emulation.
* Emulation of several printers for ZX Spectrum.

This package contains files for gtk3 version.

%description gtk3 -l pl.UTF-8
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum.
Jego właściwości to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Możliwość ładowania programów z plików .tzx.
* Dźwięk.
* Emulacja kilku drukarek przeznaczonych dla ZX Spectrum.

W tym pakiecie znajdują się pliki dla wersji gtk3.

%prep
%setup -q

%build
#%{__libtoolize}
#%{__aclocal}
#%{__autoheader}
#%{__autoconf}
#%{__automake}

# SDL
%if %{with sdl}
%configure \
	--enable-ui-joystick \
	--with-sdl
%{__make} clean
%{__make}
cp -f fuse fuse-sdl
%endif

# svga
%if %{with svga}
%configure \
	--enable-ui-joystick \
	--with-svgalib
%{__make} clean
%{__make}
cp -f fuse fuse-svga
%endif

# framebuffer
%if %{with fb}
%configure \
	--with-joystick \
	--with-fb
%{__make} clean
%{__make}
cp -f fuse fuse-fb
%endif

# These two must be the last, because they install menu_data.ui
# gtk
%if %{with gtk}
%configure  \
	--disable-ui-joystick \
	--with-joystick \
	--with-gtk
%{__make} clean
%{__make}
cp -f fuse fuse-gtk
%endif

# gtk3
%if %{with gtk3}
%configure  \
	--disable-ui-joystick \
	--with-joystick \
	--enable-gtk3
%{__make} clean
%{__make}
cp -f fuse fuse-gtk3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{?with_svga:install fuse-svga	$RPM_BUILD_ROOT%{_bindir}}
%{?with_gtk:install fuse-gtk	$RPM_BUILD_ROOT%{_bindir}}
%{?with_gtk3:install fuse-gtk3	$RPM_BUILD_ROOT%{_bindir}}
%{?with_fb:install fuse-fb	$RPM_BUILD_ROOT%{_bindir}}
%{?with_sdl:install fuse-sdl	$RPM_BUILD_ROOT%{_bindir}}

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%doc README THANKS AUTHORS keysyms.dat keysyms.pl hacking/ChangeLog hacking/*.txt
%{_datadir}/%{name}
%{_mandir}/man1/fuse.1*

%if %{with fb}
%files fb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fuse-fb
%endif

%if %{with gtk}
%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fuse-gtk
%endif

%if %{with gtk3}
%files gtk3
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fuse-gtk3
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
