#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libcmis
Version  : 0.5.1
Release  : 2
URL      : https://dev-www.libreoffice.org/src/libcmis-0.5.1.tar.gz
Source0  : https://dev-www.libreoffice.org/src/libcmis-0.5.1.tar.gz
Summary  : CMIS protocol client library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1 MPL-1.1
Requires: libcmis-bin
Requires: libcmis-lib
Requires: libcmis-license
Requires: libcmis-man
BuildRequires : boost-dev
BuildRequires : cppcheck
BuildRequires : pkgconfig(cppunit)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libxml-2.0)

%description
No detailed description available

%package bin
Summary: bin components for the libcmis package.
Group: Binaries
Requires: libcmis-license
Requires: libcmis-man

%description bin
bin components for the libcmis package.


%package dev
Summary: dev components for the libcmis package.
Group: Development
Requires: libcmis-lib
Requires: libcmis-bin
Provides: libcmis-devel

%description dev
dev components for the libcmis package.


%package lib
Summary: lib components for the libcmis package.
Group: Libraries
Requires: libcmis-license

%description lib
lib components for the libcmis package.


%package license
Summary: license components for the libcmis package.
Group: Default

%description license
license components for the libcmis package.


%package man
Summary: man components for the libcmis package.
Group: Default

%description man
man components for the libcmis package.


%prep
%setup -q -n libcmis-0.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534626099
%configure --disable-static --without-man --disable-werror
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1534626099
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/libcmis
cp COPYING.GPL %{buildroot}/usr/share/doc/libcmis/COPYING.GPL
cp COPYING.LGPL %{buildroot}/usr/share/doc/libcmis/COPYING.LGPL
cp COPYING.MPL %{buildroot}/usr/share/doc/libcmis/COPYING.MPL
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cmis-client

%files dev
%defattr(-,root,root,-)
/usr/include/libcmis-0.5/libcmis/allowable-actions.hxx
/usr/include/libcmis-0.5/libcmis/document.hxx
/usr/include/libcmis-0.5/libcmis/exception.hxx
/usr/include/libcmis-0.5/libcmis/folder.hxx
/usr/include/libcmis-0.5/libcmis/libcmis.hxx
/usr/include/libcmis-0.5/libcmis/oauth2-data.hxx
/usr/include/libcmis-0.5/libcmis/object-type.hxx
/usr/include/libcmis-0.5/libcmis/object.hxx
/usr/include/libcmis-0.5/libcmis/property-type.hxx
/usr/include/libcmis-0.5/libcmis/property.hxx
/usr/include/libcmis-0.5/libcmis/rendition.hxx
/usr/include/libcmis-0.5/libcmis/repository.hxx
/usr/include/libcmis-0.5/libcmis/session-factory.hxx
/usr/include/libcmis-0.5/libcmis/session.hxx
/usr/include/libcmis-0.5/libcmis/xml-utils.hxx
/usr/include/libcmis-0.5/libcmis/xmlserializable.hxx
/usr/include/libcmis-c-0.5/libcmis-c/allowable-actions.h
/usr/include/libcmis-c-0.5/libcmis-c/document.h
/usr/include/libcmis-c-0.5/libcmis-c/error.h
/usr/include/libcmis-c-0.5/libcmis-c/folder.h
/usr/include/libcmis-c-0.5/libcmis-c/libcmis-c.h
/usr/include/libcmis-c-0.5/libcmis-c/oauth2-data.h
/usr/include/libcmis-c-0.5/libcmis-c/object-type.h
/usr/include/libcmis-c-0.5/libcmis-c/object.h
/usr/include/libcmis-c-0.5/libcmis-c/property-type.h
/usr/include/libcmis-c-0.5/libcmis-c/property.h
/usr/include/libcmis-c-0.5/libcmis-c/rendition.h
/usr/include/libcmis-c-0.5/libcmis-c/repository.h
/usr/include/libcmis-c-0.5/libcmis-c/session-factory.h
/usr/include/libcmis-c-0.5/libcmis-c/session.h
/usr/include/libcmis-c-0.5/libcmis-c/types.h
/usr/include/libcmis-c-0.5/libcmis-c/vectors.h
/usr/lib64/libcmis-0.5.so
/usr/lib64/libcmis-c-0.5.so
/usr/lib64/pkgconfig/libcmis-0.5.pc
/usr/lib64/pkgconfig/libcmis-c-0.5.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcmis-0.5.so.5
/usr/lib64/libcmis-0.5.so.5.0.0
/usr/lib64/libcmis-c-0.5.so.5
/usr/lib64/libcmis-c-0.5.so.5.0.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/libcmis/COPYING.GPL
/usr/share/doc/libcmis/COPYING.LGPL
/usr/share/doc/libcmis/COPYING.MPL

%files man
%defattr(-,root,root,-)
/usr/share/man/manx/cmis-client.xml
