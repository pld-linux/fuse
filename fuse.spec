# TODO: Fix issue with the WORDS_BIGENDIAN macro of autoconf-2.63
# fuse built using autotools is unusable because of it.
#
# Conditional build:
%bcond_with	svga	# svgalib version
%bcond_without	fb	# framebuffer version
%bcond_without	gtk	# GTK+ 2 version
%bcond_without	gtk3	# GTK+ 3 version
%bcond_without	sdl	# SDL version
#
Summary:	Free Unix Spectrum Emulator
Summary(pl.UTF-8):	Darmowy uniksowy emulator ZX Spectrum
Name:		fuse
Version:	1.2.2
Release:	1
License:	GPL v2+
Group:		Applications/Emulators
Source0:	http://downloads.sourceforge.net/fuse-emulator/%{name}-%{version}.tar.gz
# Source0-md5:	3968c9358485622d5934b7f8b06a388a
Source1:	ti_m397.rom
# Source1-md5:	8c61b20e1f7666ff80ad7f48bb2b10c0
Patch0:		fuse-1.1.1-2.patch
URL:		http://fuse-emulator.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.4
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.20.0
%{?with_gtk:BuildRequires:	gtk+2-devel >= 2:2.18.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel}
%{?with_fb:BuildRequires:	gpm-devel}
BuildRequires:	libjsw-devel
BuildRequires:	libpng-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libspectrum-devel >= 1.2.0
BuildRequires:	libtool >= 2:2
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	perl-base
BuildRequires:	pkgconfig
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
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
Requires:	glib2 >= 1:2.20.0
Requires:	libspectrum >= 0.4.0
Suggests:	fdd3000e

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
Summary:	Free Unix Spectrum Emulator (GTK+ 2 version)
Summary(pl.UTF-8):	Darmowy uniksowy emulator ZX Spectrum (wersja GTK+ 2)
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}-%{release}
Requires:	gtk+2 >= 2:2.18.0
Obsoletes:	fuse-X11

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

This package contains files for GTK+ 2 version.

%description gtk -l pl.UTF-8
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum.
Jego właściwości to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Możliwość ładowania programów z plików .tzx.
* Dźwięk.
* Emulacja kilku drukarek przeznaczonych dla ZX Spectrum.

W tym pakiecie znajdują się pliki dla wersji GTK+ 2.

%package gtk3
Summary:	Free Unix Spectrum Emulator (GTK+ 3 version)
Summary(pl.UTF-8):	Darmowy uniksowy emulator ZX Spectrum (wersja GTK+ 3)
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	fuse-X11

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

This package contains files for GTK+ 3 version.

%description gtk3 -l pl.UTF-8
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum.
Jego właściwości to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Możliwość ładowania programów z plików .tzx.
* Dźwięk.
* Emulacja kilku drukarek przeznaczonych dla ZX Spectrum.

W tym pakiecie znajdują się pliki dla wersji GTK+ 3.

%prep
%setup -q

%build
#%patch0 -p1
#%{__libtoolize}
#%{__aclocal}
#%{__autoheader}
#%{__autoconf}
#%{__automake}

# SDL
%if %{with sdl}
mkdir build-sdl
cd build-sdl
../%configure \
	--with-sdl \
	--program-suffix=-sdl
%{__make}
cd ..
%endif

# svga
%if %{with svga}
mkdir build-svga
cd build-svga
../%configure \
	--with-svgalib \
	--program-suffix=-svga
%{__make}
cd ..
%endif

# framebuffer
%if %{with fb}
mkdir build-fb
cd build-fb
../%configure \
	--with-fb \
	--program-suffix=-fb
%{__make}
cd ..
%endif

# gtk
%if %{with gtk}
mkdir build-gtk
cd build-gtk
../%configure  \
	--with-gtk \
	--program-suffix=-gtk
%{__make}
cd ..
%endif

# gtk3
%if %{with gtk3}
mkdir build-gtk3
cd build-gtk3
../%configure  \
	--with-gtk \
	--enable-gtk3 \
	--program-suffix=-gtk3
%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with sdl}
%{__make} -C build-sdl install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with svga}
%{__make} -C build-svga install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with fb}
%{__make} -C build-fb install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with gtk}
%{__make} -C build-gtk install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with gtk3}
%{__make} -C build-gtk3 install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%doc README THANKS AUTHORS keysyms.dat keysyms.pl hacking/*.txt
%{_datadir}/%{name}

%if %{with fb}
%files fb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fuse-fb
%{_mandir}/man1/fuse-fb.1*
%endif

%if %{with gtk}
%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fuse-gtk
%{_mandir}/man1/fuse-gtk.1*
%endif

%if %{with gtk3}
%files gtk3
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fuse-gtk3
%{_mandir}/man1/fuse-gtk3.1*
%endif

%if %{with sdl}
%files sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fuse-sdl
%{_mandir}/man1/fuse-sdl.1*
%endif

%if %{with svga}
%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fuse-svga
%{_mandir}/man1/fuse-svga.1*
%endif
