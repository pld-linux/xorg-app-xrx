Summary:	xrx application
Summary(pl):	Aplikacja xrx
Name:		xorg-app-xrx
Version:	0.99.2
Release:	0.1
License:	MIT
Group:		X11/Application
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC2/app/xrx-%{version}.tar.bz2
# Source0-md5:	9c68169dfc89af3b3d2d3fb30d5c8156
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-proto-xproxymanagementprotocol-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xrx application.

%description -l pl
Aplikacja xrx.

%prep
%setup -q -n xrx-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	appmandir=%{_mandir}/man1

# not needed for plugins
rm -f $RPM_BUILD_ROOT%{_libdir}/libxrx*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libxrx.so.*.*.*
%attr(755,root,root) %{_libdir}/libxrx.so
%attr(755,root,root) %{_libdir}/libxrxnest.so.*.*.*
%attr(755,root,root) %{_libdir}/libxrxnest.so
%{_mandir}/man1/*.1x*
