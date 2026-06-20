#
# Conditional build:
%bcond_with	svga	# svgalib UI
%bcond_without	fb	# framebuffer UI
%bcond_without	gtk3	# GTK+ 3 UI
%bcond_without	sdl	# SDL UI
%bcond_without	sdl2	# SDL2 UI
%bcond_with	libao	# libao instead of alsa
%bcond_without	pulseaudio	# pulseaudio
#
%define		libspectrum_ver	1.6.2
Summary:	Free Unix Spectrum Emulator
Summary(pl.UTF-8):	Darmowy uniksowy emulator ZX Spectrum
Name:		fuse
Version:	1.9.0
Release:	1
License:	GPL v2+
Group:		Applications/Emulators
Source0:	https://downloads.sourceforge.net/fuse-emulator/%{name}-%{version}.tar.gz
# Source0-md5:	f2e85959219c15b3577b1385fd086799
Source1:	ti_m397.rom
# Source1-md5:	8c61b20e1f7666ff80ad7f48bb2b10c0
Patch0:		pal_tv2x_bool.patch
Patch1:		https://downloads.sourceforge.net/fdd3000e/v_0.2.1/fuse-1.7.0-fdd3000-0.2.1.diff
# Patch1-md5:	e487fac131519a33446341006bf4cb5d
Patch2:		pal_tv2x_null.patch
URL:		https://fuse-emulator.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.4
%{?with_sdl2:BuildRequires:	SDL2-devel}
%{!?with_libao:BuildRequires:	alsa-lib-devel}
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 1:2.20.0
%{?with_fb:BuildRequires:	gpm-devel}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0}
%{?with_libao:BuildRequires:	libao-devel}
BuildRequires:	libpng-devel
BuildRequires:	libspectrum-devel >= %{libspectrum_ver}
BuildRequires:	libtool >= 2:2
BuildRequires:	libxml2-devel >= 1:2.6.0
BuildRequires:	perl-base
BuildRequires:	pkgconfig
%{?with_pulseadio:BuildRequires:	pulseaudio-devel}
BuildRequires:	rpmbuild(macros) >= 2.043
BuildRequires:	sed >= 4.0
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fuse is Free Unix Spectrum Emulator. What Fuse does have:

* Working 48K/128K/+2/+2A Speccy emulation, running at true Speccy
  speed on any computer you're likely to try it on (it runs at full
  speed on a SparcStation 4 unless you do too much graphics intensive
  stuff).
* Support for loading from .tzx files.
* Sound emulation.
* Emulation of several printers for ZX Spectrum.

%description -l pl.UTF-8
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum. Jego
właściwości to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Możliwość ładowania programów z plików .tzx.
* Dźwięk.
* Emulacja kilku drukarek przeznaczonych dla ZX Spectrum.

%package common
Summary:	Free Unix Spectrum Emulator (common files)
Summary(pl.UTF-8):	Darmowy uniksowy emulator ZX Spectrum (pliki wspólne)
Group:		Applications/Emulators
# actually -common doesn't require these libraries, but all the frontends do
Requires:	glib2 >= 1:2.20.0
Requires:	libspectrum >= %{libspectrum_ver}
Requires:	libxml2-devel >= 1:2.6.0

%description common
fuse is Free Unix Spectrum Emulator. What Fuse does have:

* Working 48K/128K/+2/+2A Speccy emulation, running at true Speccy
  speed on any computer you're likely to try it on (it runs at full
  speed on a SparcStation 4 unless you do too much graphics intensive
  stuff).
* Support for loading from .tzx files.
* Sound emulation.
* Emulation of several printers for ZX Spectrum.

This package contains common files for all versions.

%description common -l pl.UTF-8
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum. Jego
właściwości to:

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
fuse is Free Unix Spectrum Emulator. What Fuse does have:

* Working 48K/128K/+2/+2A Speccy emulation, running at true Speccy
  speed on any computer you're likely to try it on (it runs at full
  speed on a SparcStation 4 unless you do too much graphics intensive
  stuff).
* Support for loading from .tzx files.
* Sound emulation.
* Emulation of several printers for ZX Spectrum.

This package contains files for framebuffer version.

%description fb -l pl.UTF-8
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum. Jego
właściwości to:

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
fuse is Free Unix Spectrum Emulator. What Fuse does have:

* Working 48K/128K/+2/+2A Speccy emulation, running at true Speccy
  speed on any computer you're likely to try it on (it runs at full
  speed on a SparcStation 4 unless you do too much graphics intensive
  stuff).
* Support for loading from .tzx files.
* Sound emulation.
* Emulation of several printers for ZX Spectrum.

This package contains files for SDL version.

%description sdl -l pl.UTF-8
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum. Jego
właściwości to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Możliwość ładowania programów z plików .tzx.
* Dźwięk.
* Emulacja kilku drukarek przeznaczonych dla ZX Spectrum.

W tym pakiecie znajdują się pliki dla wersji korzystającej z SDL.

%package sdl2
Summary:	Free Unix Spectrum Emulator (SDL2 version)
Summary(pl.UTF-8):	Darmowy uniksowy emulator ZX Spectrum (wersja na SDL2)
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}-%{release}
Requires:	SDL2 >= 2.0

%description sdl2
fuse is Free Unix Spectrum Emulator. What Fuse does have:

* Working 48K/128K/+2/+2A Speccy emulation, running at true Speccy
  speed on any computer you're likely to try it on (it runs at full
  speed on a SparcStation 4 unless you do too much graphics intensive
  stuff).
* Support for loading from .tzx files.
* Sound emulation.
* Emulation of several printers for ZX Spectrum.

This package contains files for SDL2 version.

%description sdl2 -l pl.UTF-8
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum. Jego
właściwości to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Możliwość ładowania programów z plików .tzx.
* Dźwięk.
* Emulacja kilku drukarek przeznaczonych dla ZX Spectrum.

W tym pakiecie znajdują się pliki dla wersji korzystającej z SDL2.

%package svga
Summary:	Free Unix Spectrum Emulator (svga version)
Summary(pl.UTF-8):	Darmowy uniksowy emulator ZX Spectrum (wersja na svgalib)
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}-%{release}

%description svga
fuse is Free Unix Spectrum Emulator. What Fuse does have:

* Working 48K/128K/+2/+2A Speccy emulation, running at true Speccy
  speed on any computer you're likely to try it on (it runs at full
  speed on a SparcStation 4 unless you do too much graphics intensive
  stuff).
* Support for loading from .tzx files.
* Sound emulation.
* Emulation of several printers for ZX Spectrum.

This package contains files for svga version.

%description svga -l pl.UTF-8
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum. Jego
właściwości to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Możliwość ładowania programów z plików .tzx.
* Dźwięk.
* Emulacja kilku drukarek przeznaczonych dla ZX Spectrum.

W tym pakiecie znajdują się pliki dla wersji korzystającej z svgalib.

%package gtk3
Summary:	Free Unix Spectrum Emulator (GTK+ 3 version)
Summary(pl.UTF-8):	Darmowy uniksowy emulator ZX Spectrum (wersja GTK+ 3)
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	fuse-X11 < 1.7.0
Obsoletes:	fuse-gtk < 1.8.0

%description gtk3
fuse is Free Unix Spectrum Emulator. What Fuse does have:

* Working 48K/128K/+2/+2A Speccy emulation, running at true Speccy
  speed on any computer you're likely to try it on (it runs at full
  speed on a SparcStation 4 unless you do too much graphics intensive
  stuff).
* Support for loading from .tzx files.
* Sound emulation.
* Emulation of several printers for ZX Spectrum.

This package contains files for GTK+ 3 version.

%description gtk3 -l pl.UTF-8
fuse (Free Unix Spectrum Emulator) jest emulatorem ZX Spectrum. Jego
właściwości to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Możliwość ładowania programów z plików .tzx.
* Dźwięk.
* Emulacja kilku drukarek przeznaczonych dla ZX Spectrum.

W tym pakiecie znajdują się pliki dla wersji GTK+ 3.

%package -n bash-completion-fuse
Summary:	Bash completion for FUSE emulator commands
Summary(pl.UTF-8):	Bashowe dopełnianie składni poleceń emulatora FUSE
Group:		Applications/Shells
Requires:	%{name}-common = %{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-fuse
Bash completion for FUSE emulator commands.

%description -n bash-completion-fuse -l pl.UTF-8
Bashowe dopełnianie składni poleceń emulatora FUSE.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

# PLD uses per-backend fuse program instead of just "fuse"
%{__sed} -i -e '/^complete /s/ fuse$/ fuse-fb fuse-gtk3 fuse-sdl fuse-svga/' data/shell-completion/bash/fuse
%{__rm} -f settings.c settings.h options.h ui/gtk3/menu_data.ui

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}

%define	common_opts \\\
	--disable-silent-rules \\\
	--with-bash-completion-dir=%{bash_compdir} \\\
	%{nil}
# SDL
%if %{with sdl}
mkdir build-sdl
cd build-sdl
%define configuredir ..
%configure \
	%{common_opts} \
	--program-suffix=-sdl \
	--with-sdl
%{__make}
cd ..
%endif

# SDL2
%if %{with sdl2}
mkdir build-sdl2
cd build-sdl2
%define configuredir ..
%configure \
	%{common_opts} \
	--program-suffix=-sdl2 \
	--with-sdl2
%{__make}
cd ..
%endif

# svga
%if %{with svga}
mkdir build-svga
cd build-svga
%define configuredir ..
%configure \
	%{common_opts} \
	--program-suffix=-svga \
	--with-svgalib
%{__make}
cd ..
%endif

# framebuffer
%if %{with fb}
mkdir build-fb
cd build-fb
%define configuredir ..
%configure \
	%{common_opts} \
	--program-suffix=-fb \
%if %{with libao}
	--with-audio-driver=libao \
%endif
%if %{with pulseaudio}
	--with-audio-driver=pulseaudio \
%endif
	--with-fb
%{__make}
cd ..
%endif

# gtk3
%if %{with gtk3}
mkdir build-gtk3
cd build-gtk3
%define configuredir ..
%configure  \
	%{common_opts} \
	--enable-gtk3 \
	--program-suffix=-gtk3 \
%if %{with libao}
	--with-audio-driver=libao \
%endif
%if %{with pulseaudio}
	--with-audio-driver=pulseaudio \
%endif
	--with-gtk
%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with sdl}
%{__make} -C build-sdl install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with sdl2}
%{__make} -C build-sdl2 install \
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

%if %{with gtk3}
%{__make} -C build-gtk3 install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%doc README THANKS AUTHORS ChangeLog keysyms.dat keysyms.pl hacking/*.txt
%{_datadir}/%{name}

%if %{with fb}
%files fb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fuse-fb
%{_mandir}/man1/fuse-fb.1*
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

%if %{with sdl2}
%files sdl2
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fuse-sdl2
%{_mandir}/man1/fuse-sdl2.1*
%endif

%if %{with svga}
%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fuse-svga
%{_mandir}/man1/fuse-svga.1*
%endif

%files -n bash-completion-fuse
%defattr(644,root,root,755)
%{bash_compdir}/fuse
