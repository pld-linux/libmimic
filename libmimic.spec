Summary:	Mimic v2.x (ML20) video encoding/decoding library
Summary(pl.UTF-8):	Biblioteka kodująca/dekodująca obraz Mimic v2.x
Name:		libmimic
Version:	1.0.4
Release:	3
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/farsight/%{name}-%{version}.tar.gz
# Source0-md5:	94f0dbb1d3c253201553a4069555fb84
Patch0:		link.patch
URL:		http://farsight.sourceforge.net/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmimic is an open source video encoding/decoding library for Mimic
v2.x-encoded content (fourCC: ML20), which is the encoding used by MSN
Messenger for webcam conversations.

%description -l pl.UTF-8
libmimic to mająca otwarte źródła biblioteka do kodowania/dekodowania
obrazu w formacie Mimic v2.x (fourCC: ML20), który jest używany przez
MSN Messendera do rozmów przez kamery internetowe.

%package devel
Summary:	Header files for libmimic library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libmimic
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.0

%description devel
Header files for libmimic library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libmimic.

%package static
Summary:	Static libmimic library
Summary(pl.UTF-8):	Statyczna biblioteka libmimic
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmimic library.

%description static -l pl.UTF-8
Statyczna biblioteka libmimic.

%prep
%setup -q
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libmimic.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmimic.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/api/html/*
%attr(755,root,root) %{_libdir}/libmimic.so
%{_includedir}/mimic.h
%{_pkgconfigdir}/libmimic.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmimic.a
