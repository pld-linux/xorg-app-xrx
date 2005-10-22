Summary:	xrx application
Summary(pl):	Aplikacja xrx
Name:		xorg-app-xrx
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Application
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/app/xrx-%{version}.tar.bz2
# Source0-md5:	83d2c47879b2f4d2b5624d4bb03465ee
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-xtrans-devel
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
