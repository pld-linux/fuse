Summary:	Free Unix Spectrum Emulator
Summary(pl):	"Wolny" uniksowy emulator ZX Spectrum
Name:		fuse
Version:	0.5.1
Release:	2
License:	GPL
Group:		Applications/Emulators
Source0:	http://www.srcf.ucam.org/~pak21/spectrum/%{name}-%{version}.tar.gz
Patch0:		%{name}-typo.patch
Patch1:     %{name}-tmx.patch
URL:		http://www.srcf.ucam.org/~pak21/spectrum/fuse.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:  gtk+-devel
BuildRequires:	libspectrum-devel
BuildRequires:	perl
BuildRequires:  libxml2-devel
%ifarch %{ix86} alpha ppc
BuildRequires:	svgalib-devel
%endif
BuildRequires:	XFree86-devel
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
Jego w�a�ciwo�ci to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Mo�liwo�� �adowania program�w z plik�w .tzx.
* D�wi�k.

%package common
Summary:	Free Unix Spectrum Emulator (common files)
Summary(pl):	"Wolny" uniksowy emulator ZX Spectrum (pliki wsp�lne)
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
Jego w�a�ciwo�ci to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Mo�liwo�� �adowania program�w z plik�w .tzx.
* D�wi�k.
* Emulacja kilku drukarek przeznaczonych dla ZX Spectrum.

W tym pakiecie znajduj� si� wsp�lne pliki dla wersji X11 i svga.

%package fb
Summary:	Free Unix Spectrum Emulator (framebuffer version)
Summary(pl):	"Wolny" uniksowy emulator ZX Spectrum (wersja na framebuffer)
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
Jego w�a�ciwo�ci to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Mo�liwo�� �adowania program�w z plik�w .tzx.
* D�wi�k.

W tym pakiecie znajduj� si� pliki dla wersji korzystaj�cej z framebuffera. 

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
Jego w�a�ciwo�ci to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Mo�liwo�� �adowania program�w z plik�w .tzx.
* D�wi�k.

W tym pakiecie znajduj� si� pliki dla wersji korzystaj�cej z svgalib. 

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
Jego w�a�ciwo�ci to:

* Emulacja ZX Spectrum 48K/128K/+2/+2A.
* Mo�liwo�� �adowania program�w z plik�w .tzx.
* D�wi�k.

W tym pakiecie znajduj� si� pliki dla wersji X11.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

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
	--with-glib \
	--without-fb \
	--with-svgalib
%{__make} CFLAGS="-I/usr/include/glib-1.2 -I/usr/lib/glib/include %{rpmcflags}"
cp -f ./fuse ./fuse-svga
%endif

%{__make} clean
%configure \
	--without-x \
	--with-glib \
	--with-fb \
	--without-svgalib
%{__make} CFLAGS="-I/usr/include/glib-1.2 -I/usr/lib/glib/include %{rpmcflags}"
cp -f ./fuse ./fuse-fb

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%ifarch %{ix86} alpha ppc
install fuse-svga $RPM_BUILD_ROOT%{_bindir}
%endif
install fuse-x11 $RPM_BUILD_ROOT%{_bindir}
install fuse-fb  $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%doc README THANKS AUTHORS keysyms.dat keysyms.pl hacking/* 
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man1/*

%files fb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fuse-fb

%ifarch %{ix86} alpha ppc
%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fuse-svga
%endif

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fuse-x11
