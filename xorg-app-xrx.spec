Summary:	xrx application
Summary(pl.UTF-8):	Aplikacja xrx
Name:		xorg-app-xrx
Version:	1.0.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xrx-%{version}.tar.bz2
# Source0-md5:	5f65e24f8a225e255beb2059e33d6b37
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-proto-xproxymanagementprotocol-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xrx application.

%description -l pl.UTF-8
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
	DESTDIR=$RPM_BUILD_ROOT

# not needed for plugins
rm -f $RPM_BUILD_ROOT%{_libdir}/libxrx*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xrx
%attr(755,root,root) %{_libdir}/libxrx.so.*.*.*
%attr(755,root,root) %{_libdir}/libxrx.so
%attr(755,root,root) %{_libdir}/libxrxnest.so.*.*.*
%attr(755,root,root) %{_libdir}/libxrxnest.so
%{_mandir}/man1/libxrx.1x*
%{_mandir}/man1/xrx.1x*
