Name:           libgdata
Version:        0.5.0
Release:        2%{?dist}
Summary:        Library for the GData protocol

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://live.gnome.org/libgdata
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.5/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  glib2-devel libsoup-devel libxml2-devel gtk-doc intltool

%description
libgdata is a GLib-based library for accessing online service APIs using the
GData protocol --- most notably, Google's services. It provides APIs to access
the common Google services, and has full asynchronous support.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Requires:       gtk-doc


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure --disable-static 
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang gdata


%clean
rm -rf $RPM_BUILD_ROOT

%check
# Only the general test can be run without network access
cd gdata/tests
./general

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -f gdata.lang
%defattr(-,root,root,-)
%doc COPYING.LIB NEWS README AUTHORS
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gtk-doc/html/gdata/

%changelog
* Thu Jan 28 2010 Bastien Nocera <bnocera@redhat.com> 0.5.0-2
- Fix Source URL
Related: rhbz#543948

* Tue Sep 22 2009 Bastien Nocera <bnocera@redhat.com> 0.5.0-1
- Update to 0.5.0

* Tue Aug 11 2009 Bastien Nocera <bnocera@redhat.com> 0.4.0-3
- Fix source URL

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Bastien Nocera <bnocera@redhat.com> 0.4.0-1
- Update to 0.4.0

* Tue May 26 2009 Bastien Nocera <bnocera@redhat.com> 0.3.0-1
- Update to 0.3.0

* Sat Apr 25 2009 Bastien Nocera <bnocera@redhat.com> 0.2.0-1
- Update to 0.2.0

* Mon Apr 06 2009 - Bastien Nocera <bnocera@redhat.com> - 0.1.1-2
- Add check, snippet from Jason Tibbitts

* Wed Apr 01 2009 - Bastien Nocera <bnocera@redhat.com> - 0.1.1-1
- Update to 0.1.1

* Wed Apr 01 2009 - Bastien Nocera <bnocera@redhat.com> - 0.1.0-1
- First package

