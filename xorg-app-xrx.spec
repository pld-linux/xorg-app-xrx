Summary:	X Remote eXecution using WWW browser
Summary(pl.UTF-8):	X Remote eXecution - zdalne wywoływanie aplikacji przy użyciu przeglądarki WWW
Name:		xorg-app-xrx
Version:	1.0.2
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xrx-%{version}.tar.bz2
# Source0-md5:	c0928bdc816e89a876405d317005ce29
Patch0:		%{name}-ac.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
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
The remote execution (RX) service specifies a MIME format for invoking
applications remotely, for example via a World Wide Web browser. This
RX format specifies a syntax for listing network services required by
the application, for example an X display server. The requesting Web
browser must identify specific instances of the services in the request
to invoke the application.

The distribution contains a helper program (xrx) and a Mozilla family
browser plug-in (libxrx) that demonstrate this protocol.

%description -l pl.UTF-8
Usługa RX (Remote eXecution) określa format MIME do zdalnego
wywoływania aplikacji, na przykład poprzez przeglądarkę WWW. Format RX
określa składnię definiowania usług sieciowych wymaganych przez
aplikację, na przykład serwera X. Przeglądarka wysyłająca żądania musi
podać w żądaniu określone instancje usługi w celu wywołania aplikacji.

Ten pakiet zawiera program pomocniczy (xrx) oraz wtyczkę przeglądarki
z rodziny Mozilli (libxrx) demonstrujące działanie tego protokołu.

%prep
%setup -q -n xrx-%{version}
%patch0 -p1

%build
%{__libtoolize}
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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xrx
%attr(755,root,root) %{_libdir}/libxrx.so
%attr(755,root,root) %{_libdir}/libxrxnest.so
%{_mandir}/man1/libxrx.1x*
%{_mandir}/man1/xrx.1x*
